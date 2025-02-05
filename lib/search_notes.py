def search_notes(input_string, search_parameter):
    if len(input_string) == 0 or len(search_parameter) == 0:
        return None
    split_input_string = input_string.split('\n')
    
    result = [line for line in split_input_string if search_parameter in line]
    return result