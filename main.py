def flatten(input_list, obtained_result = []):
    result = obtained_result
    for item in input_list:
        if isinstance(item, list):
            flatten(item,result)
        else:
            result.append(item)
    return result

def reverse(input_list):
    result = []
    for item in reversed(input_list):
        if isinstance(item, list):
            result.append(item[::-1])
        else:
            result.append(item)
    return result
