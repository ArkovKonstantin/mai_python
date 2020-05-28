import pytest
from testing_tools import morse


@pytest.mark.parametrize('input_data, expected', [
    ('-- .- ..', 'MAI'),
    ('.... . .-.. .-.. ---', 'HELLO'),
    ('-- . ... ... .- --. .', 'MESSAGE')
])
def test_decode(input_data, expected):
    assert morse.decode(input_data) == expected


if __name__ == '__main__':
    # print(morse.encode('MAI'))
    # morse_msg = '-- .- .. -....- ' \
    #             '.--. -.-- - .... --- -. -....- ' \
    #             '..--- ----- ..--- -----'
    # decoded_msg = morse.decode(morse_msg)
    # print(decoded_msg)
    pass
