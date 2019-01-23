"""
Made by Max Fedorchuck as a test task for applying to the:
Data Science - NLP computer linguistic school (Kyiv, Projector, 2019)

Code style was stolen from Google-oriented open-source project guide:
(http://google.github.io/styleguide/pyguide.html)

First couple versions of this programm in folder "/version history"
"""


def check_layout(message):
    """Check layout of the input message.

    Args:
      message: String with characters for building the structure like asciitree.
    Raises:
      ValueError: If very first or very last character in the message is not correct.
      ValueError: If amount of the 'opening' brackets not equal to amount of the 'closing' brackets.
    Returns:
      Input message if layout is correct for ascii tree building.
    """
    if message[0] != '(' or message[-1] != ')':
        raise ValueError('Input message with corrupted first or last symbol')
    elif message.count('(') != message.count(')'):
        raise ValueError('Input message with incorrect number of brackets')
    else:
        print('Layout is ok', end='\n\n')

        return message


def find_last_branch(message_structure):
    """Add the last branch index to the each field in dictionary with a tree structure.

    Args:
        message_structure: dictionary with order position as a key value and list with
        word and it`s depth index as a value:
        message_structure = {
        key(int value): [word(str), depth index(int)]
        ...
        }
    Returns:
        message_structure: dictionary with last branch indexes for correct printing
        the ascii-like tree.
    """
    word_depth = list(message_structure.values())
    depth_list = [d[1] for d in word_depth]

    for key in message_structure:
        depth = message_structure[key][1]
        if depth > 1 and depth <= min(depth_list[key - 1:]):
            message_structure[key] = (message_structure[key][0], message_structure[key][1], 1)
        else:
            message_structure[key] = (message_structure[key][0], message_structure[key][1], 0)

    return message_structure


def build_structure(message):
    """Build tree structures using characters from a string.

    Args:
        message: String with characters for building the structure like asciitree algorithm builds.
    Returns:
        structure_with_depth: dictionary with parameters for printing the ascii-like tree.
    """
    word = ''
    full_depth = -1
    space_depth = 0
    dictionary = {}
    struct_set = [' ', '(', ')']

    for i, symbol in enumerate(message):
        if symbol not in struct_set:
            word += symbol

        elif symbol == ' ':
            if word:
                dictionary[len(dictionary) + 1] = word, full_depth + space_depth

            word = ''
            space_depth = 1


        elif symbol == '(':
            if word:
                dictionary[len(dictionary) + 1] = word, full_depth + space_depth

            word = ''
            space_depth = 0
            full_depth += 1

        elif symbol == ')':
            if word:
                dictionary[len(dictionary) + 1] = word, full_depth + space_depth

            word = ''
            space_depth = 0
            full_depth -= 1

    structure_with_depth = find_last_branch(dictionary)

    return structure_with_depth


def print_structure(tree_structure):
    """Print into the console structure according to the given parameters.

    Args:
        tree_structure: dictionary with parameters for printing the ascii-like tree.
    Prints:
        tree structure row by row
    Returns:
        None
    """
    for word_params in tree_structure.values():
        depth = word_params[1]
        spacelist = ['    ', '|   ', '+-- ']
        if word_params[-1] != 0:
            spacelist[1] = '    '

        if depth < 3 and depth > 0:
            spaces = ''.join(spacelist[-depth:])
        elif depth >= 3:
            spaces = ''.join(spacelist[1] + spacelist[0] * (depth - 2) + spacelist[2])
        else:
            spaces = ''

        print(spaces + word_params[0])
