import pytest
import pastebin


def test_the_same_value():
    input_value = {
        'hired': {
            'be': {
                'to': {
                    'deserve': 'I'
                }
            }
        }
    }

    output_value = {
        'I': {
            'deserve': {
                'to': {
                    'be': 'hired'
                }
            }
        }
    }

    reverse_list_dict = pastebin.reverse_list(input_value)
    assert reverse_list_dict == output_value