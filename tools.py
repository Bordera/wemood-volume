def index_containing_substring(the_list, substring):
    for i, s in enumerate(the_list):
        if substring in s:
              return i
    return -1

def clean_extracted(list_to_clean):
    pre_list = []
    output_list = []
    for element in list_to_clean:
        pre_list= pre_list + element.split("\r")
    for element in pre_list:
        output_list.append(element.strip())
    return output_list

def extract_json(list_extractions, list_to_extract):
    word_dict = {}
    for word in list_extractions:
        index_word = index_containing_substring(list_to_extract, word)
        word_dict[word] = list_to_extract[index_word+1]
    return word_dict

def clean_text(input_string):
    split_output = input_string.replace("\n","PLACEHOLDER").replace(":","PLACEHOLDER").split("PLACEHOLDER")
    min_pos = index_containing_substring(split_output, "min")
    extract_list= split_output[min_pos:-1]
    clean_string = clean_extracted(extract_list)
    output_json = extract_json(["min","max","avg"], clean_string)
    return output_json
