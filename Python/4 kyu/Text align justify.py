# Your task in this Kata is to emulate text justification in monospace font.
# You will be given a single-lined text and the expected justification width.
# The longest word will never be greater than this width.
#
# Here are the rules:
#
# - Use spaces to fill in the gaps between words.
# - Each line should contain as many words as possible.
# - Use '\n' to separate lines.
# - Last line should not terminate in '\n'
# - '\n' is not included in the length of a line.
# - Gaps between words can't differ by more than one space.
# - Lines should end with a word not a space.
# - Large gaps go first, then smaller ones ('Lorem--ipsum--dolor--sit-amet,' (2, 2, 2, 1 spaces)).
# - Last line should not be justified, use only one space between words.
# - Lines with one word do not need gaps ('somelongword\n').

def distribute_spaces(no_of_words, no_of_spaces):
    initial_spaces = no_of_spaces // (no_of_words - 1)  # minimum num of spaces
    additional_spaces = no_of_spaces % (no_of_words - 1)  # how many additional spaces are left
    x = no_of_words - 1
    distributed_spaces = []
    while x > 0:
        distributed_spaces.append(initial_spaces + (additional_spaces > 0))
        additional_spaces -= 1
        x -= 1
    distributed_spaces.append(0)
    return distributed_spaces


def justify(text, width):
    words = text.split(' ')
    result = ''
    line_words = []  # words in a given line
    char_count = 0  # characters in a given line
    while len(words) > 0:
        if char_count + len(line_words) + len(words[0]) <= width:  # word fits?
            line_words.append(words[0])
            char_count += len(words[0])
            words.pop(0)
        else:
            if len(line_words) > 1:
                distributed_spaces = distribute_spaces((len(line_words)), (width - char_count))
                for word in line_words:
                    result += word + (distributed_spaces[0] * ' ')
                    distributed_spaces.pop(0)
                result += '\n'
            else:
                result += line_words[0] + '\n'
            line_words = []
            char_count = 0
    if len(line_words) > 0:
        result += ' '.join(line_words)  # for remaining words on last line
    return result
