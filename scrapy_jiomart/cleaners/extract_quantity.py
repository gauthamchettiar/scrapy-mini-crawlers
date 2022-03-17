import json
import os
import re

# Doesn't work perfectly, may not work sometime.
# Purpose: 
# 1. Checks for any uncleaned file from 'scraped_data/jiomart'. 
# 2. Uses rules defined in 'cleaning_rules.json' to - 
#   a. filter out unwanted items and 
#   b. extract quantity and type from name
# 3. Stores cleaned files at 'cleaned_data/jiomart'.
# 4. Stores Error Data at 'error_data/jiomart', this data includes items
#   a. items for which there is no rules present (<file_name>-new_entry.json)
#   b. items for which riles were present but regex did not match (<file_name>-no_regex_rule.json)

class Extraction():
    def __init__(self):
        with open("scrapy_jiomart/cleaners/cleaning_rules.json", 'r') as crfile:
            self.cleaning_rules = json.load(crfile)
        self.scraped_data_folder = "scraped_data/jiomart"
        self.cleaned_data_folder = "cleaned_data/jiomart"
        self.error_data_folder = "error_data/jiomart"
    
    def get_all_files(self, dir_path):
        file_paths = []
        for dir_path,_,file_names in os.walk(dir_path):
            file_paths += [os.path.join(dir_path, file_name) for file_name in file_names]
        return file_paths
    
    def get_unprocessed_files(self):
        scraped_file_paths = self.get_all_files(self.scraped_data_folder)
        cleaned_file_paths = self.get_all_files(self.cleaned_data_folder)

        cleaned_file_names = [ os.path.basename(fname) for fname in cleaned_file_paths ]
        return [fname for fname in scraped_file_paths if os.path.basename(fname) not in cleaned_file_names ]

    def _get_output_path(self, input_path, append_tag=None):
        split_path = input_path.split(os.sep)
        split_name = split_path[-1].split('.')
        append_tag = '' if append_tag is None else '-'+append_tag

        return split_path[-2] + os.sep + split_name[0] + append_tag + '.' + split_name[1]

    def _should_include(self, item_name):
        for keyword in self.cleaning_rules["exclude_keywords"]:
            if keyword in item_name.lower():
                return False
        return True

    def _get_group_regex(self, item_name):
        for key, regexes in self.cleaning_rules["fetch_quantity_rules"].items():
            if len(set(key.lower().split(' ')).difference(set(item_name.lower().split(' ')))) == 0:
                return key, regexes
        return None, []

    def _get_quantity(self, item_name, regex_rules):
        for rules in regex_rules:
            matched = re.search(rules.get("regex"), item_name.lower())
            if matched is not None:
                if rules.get("quantity") is not None:
                    return {
                        "quantity" : rules.get("quantity"),
                        "type" : rules.get("type")
                    }
                return {
                    "quantity" : float(matched.group(1)),
                    "type" : rules.get("type")
                }
        return {}

    def extract(self, scraped_items):
        cleaned_items = []
        regex_mismatched_items = []
        ungrouped_items = []

        for item in scraped_items:
            if self._should_include(item["name"]):
                name, rules = self._get_group_regex(item["name"])
                if name is not None:
                    if (quantity := self._get_quantity(item["name"], rules)) != {}:
                        cleaned_items.append(item | quantity | {"group_name": name})
                    else:
                        regex_mismatched_items.append(item | {"group_name": name})
                else:
                    ungrouped_items.append(item)
        
        return cleaned_items, regex_mismatched_items, ungrouped_items

    def extract_file(self, input_file_path, cleaned_output_file_path, regex_mismatched_item_path=None, ungrouped_item_path=None):
        with open(input_file_path, 'r') as sfile:
            cleaned_items, regex_mismatched_items, ungrouped_items = self.extract(json.load(sfile))
            
            os.makedirs(os.path.split(cleaned_output_file_path)[0], exist_ok=True)
            with open(cleaned_output_file_path, 'w') as efile:
                json.dump(cleaned_items, efile)

            
            if regex_mismatched_item_path is not None and len(regex_mismatched_items) > 0:
                os.makedirs(os.path.split(regex_mismatched_item_path)[0], exist_ok=True)
                with open(regex_mismatched_item_path, 'w') as rfile:
                    json.dump(regex_mismatched_items, rfile)
            
            
            if ungrouped_item_path is not None and len(ungrouped_items) > 0:
                os.makedirs(os.path.split(ungrouped_item_path)[0], exist_ok=True)
                with open(ungrouped_item_path, 'w') as ufile:
                    json.dump(ungrouped_items, ufile)

    def extract_unprocessed(self):
        for input_file_path in self.get_unprocessed_files():
            cleaned_output_file_path = os.path.join(self.cleaned_data_folder, self._get_output_path(input_file_path))
            regex_mismatched_item_path = os.path.join(self.error_data_folder, self._get_output_path(input_file_path, append_tag='no_regex_rule'))
            ungrouped_item_path = os.path.join(self.error_data_folder, self._get_output_path(input_file_path, append_tag='new_entry'))
            
            self.extract_file(input_file_path, cleaned_output_file_path, regex_mismatched_item_path, ungrouped_item_path)

if __name__ == "__main__":
    ex = Extraction()
    ex.extract_unprocessed()