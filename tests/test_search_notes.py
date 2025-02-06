import pytest
from lib.search_notes import *

input_file = 'lib/data.txt'
output_file = 'lib/todo.txt'

# Test imput string isn't empty
def test_input_string_not_empty():
    assert search_notes('lib/empty_data.txt','#TODO') == None

# Test with content, without search parameter
def test_input_string_no_search_parameter():
    assert search_notes(input_file, '') == None

# Test with content and search parameter

def test_input_string_with_search_parameter():
    assert search_notes(input_file, '#TODO') == [
        "1. Review and update marketing strategy #TODO\n",
        "3. Fix database connection issue #TODO\n", 
        "5. Develop new feature for mobile app #TODO\n",
        "7. Optimize server performance #TODO\n"
        ]
    
def test_cleanup_data():
    assert cleanup_data(["3. Fix database connection issue #TODO\n"]) == ["Fix database connection issue"]

# Write file contents
# File is created
def test_file_created():
    write_file_contents(output_file, search_notes(input_file, '#TODO'))
    assert does_file_exist(output_file) == True
