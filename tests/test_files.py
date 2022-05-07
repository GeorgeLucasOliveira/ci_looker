import lkml
from pprint import pprint
import sys
import os

def test_descriptions_in_dimensions():
    files = changed_files()
    
    errors = []
    for file_path in files:
        if file_path.endswith('.view.lkml'):
            
            f = open(file_path)
            lookml = f.read()
            lkml_file = lkml.load(lookml)['views'][0]
            
            dimensions_with_errors = []
            if('dimensions' in lkml_file):
                for dimension in lkml_file['dimensions']:
                    if 'description' not in dimension or len(dimension['description']) != "":
                        dimensions_with_errors.append(dimension['name'])
              
            if('dimension_groups' in lkml_file):
                for dimension in lkml_file['dimension_groups']:
                    if 'description' not in dimension or len(dimension['description']) != "":
                        dimensions_with_errors.append(dimension['name'])
                    
            if dimensions_with_errors:
                errors.append({'file_path': file_path, 'dimensions': dimensions_with_errors})
                
    if len(errors) > 0:
        assert False, build_error_msg(errors, dimensions_with_errors)
                
def build_error_msg(errors, itens_errors):
    error_msg = ""
    error_msg += "\n ----------------------------- OUTPUT --------------------------\n"
    for error in errors:
        error_msg += f"file: {error['file_path']}"
        error_msg += "\n"
        for item in itens_errors:
            error_msg += f"  field: {item}"
            error_msg += "\n"
                
    return error_msg
    
def changed_files():
    #if ',' in os.getenv('CHANGED_FILES'):
        #files = os.getenv('CHANGED_FILES').strip('][').split(',')
    #else:
        #files = os.getenv('CHANGED_FILES').strip('][').split()
    files = ['views/view_name.view.lkml']
    return files


if __name__ == "__main__":
    test_descriptions_in_dimensions()