import pytest
from lib.search_notes import *

test_data = """
1. Review and update marketing strategy #TODO
2. Schedule team meeting for Q2 planning
3. Fix database connection issue #TODO
4. Prepare quarterly financial report
5. Develop new feature for mobile app 
6. Research competitor pricing strategies
7. Optimize server performance 
8. Write blog post about recent product launch
9. Clean up old project files 
10. Update customer support documentation
"""

# Test imput string isn't empty
def test_input_string_not_empty():
    assert search_notes('','#TODO') == None

# Test with content, without search parameter
def test_input_string_no_search_parameter():
    assert search_notes(test_data, '') == None

# Test with content and search parameter

def test_input_string_with_search_parameter():
    assert search_notes(test_data, '#TODO') == [
        "1. Review and update marketing strategy #TODO",
        "3. Fix database connection issue #TODO"
        ]