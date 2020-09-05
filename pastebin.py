'''
"""
Please use Python 3 to answer question
Welcome to answer with unit testing code if you can
 
After you finish coding, please push to your GitHub account and share the link with us.
"""
 
# Please write a function to reverse the following nested input value into output value
 
# Input:
input_value = {
  'hired': {
    'be': {
      'to': {
        'deserve': 'I'
      }
    }
  }
}
 
# Output:
output_value = {
  'I': {
    'deserve': {
      'to': {
         'be': 'hired'
      }
    }
  }
} 
'''
def input_value_list(input_value):
    sort_list = []
    for k, v in input_value.items():
        sort_list.append(k)
        if isinstance(v, dict):
            v_dict = eval(str(v))
            v_dict = input_value_list(v_dict)
            sort_list.extend(v_dict)
        else:
            sort_list.extend(v)
    return sort_list

def reverse_list(input_value=None, sort_list=None):
    if not sort_list:
        sort_list = input_value_list(input_value=input_value)
    else:
        sort_list = sort_list
    sort_list_len = len(sort_list)
    if sort_list_len > 1:
        if isinstance(sort_list, list):
            for i in range(sort_list_len):
                if i == 0:
                    reverse_dict ={
                        sort_list[i+1]: sort_list[i]
                    }
                    sort_list.pop(0)
                    sort_list.insert(0, reverse_dict)
                    sort_list.pop(1)
                    if len(sort_list) == 1:
                        break
                    reverse_list(sort_list=sort_list)
        return sort_list[0]

# def input_value_equal_output_value(input_value, output_value):
#     reverse_list_dict = reverse_list(input_value)
#     if reverse_list_dict == output_value:
#         return True

# if __name__ == "__main__":
#     input_value = {'hired': {'be': {'to': {'deserve': 'I'}}}}
#     output_value = {'I': {'deserve': {'to': {'be': 'hired'}}}}

#     print(input_value_equal_output_value(input_value, output_value))

    # reverse_list_dict = reverse_list(input_value)
    # print(reverse_list_dict == output_value)