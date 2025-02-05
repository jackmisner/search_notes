import os

def does_file_exist(filename):
    return os.path.exists(filename)

def get_file_contents(filename):
    if does_file_exist(filename):
        with open(filename) as f:
            data = f.readlines()
            return data
    else:
        return "This file cannot be found!"

# Function discards leading numbers, strips newlines and #TODO note for all lines in data.
# Takes input list, returns list
def cleanup_data(data):
    clean_data = [' '.join(line.strip('\n').strip(' #TODO').split(' ')[1:]) for line in data]
    return clean_data

# Function writes given list to file, each item on new numbered line.
# Takes input list, writes file, returns None
def write_file_contents(output_filename, data): 
    clean_data = cleanup_data(data)
    with open(output_filename, 'w') as f:
        counter = 1
        for item in clean_data:
            f.write(f"{counter}. {item}\n")
            counter += 1

def search_notes(input_filename, search_parameter):
    # Get file contents
    input_string = get_file_contents(input_filename)
    print(input_string)
    if len(input_string) == 0 or len(search_parameter) == 0:
        return None
    result = [line for line in input_string if search_parameter in line]
    return result
