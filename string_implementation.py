class String(object):
    def __init__(self):
        pass

    def generate_string(self):
        user_input = []
        length = int(input("length: "))
        for i in range(length):
            char_input = input("type in a char: ")
            while len(char_input) != 1 and type(char_input) != type(str):
                char_input = input("invalid input. please type in a char: ")
            user_input.append(char_input)
        # ','.join(array)
        joined_string = ''.join(user_input)
        return joined_string

    @staticmethod
    def split_string_to_array_of_char(string):
        string_array = []
        for char in string:
            string_array.append(char)
        return string_array

    @staticmethod
    def combine_string(string1, string2):
        return string1 + string2

    @staticmethod
    def reverse_string(string):
        print(string.split(','))

    @staticmethod
    def split_sentence(string, seperator):
        return string.split(seperator)


def main():
    new_string = String()
    string_generated = new_string.generate_string()
    print(f'generated string: {string_generated}\n')
    string1 = "hello,"
    string2 = "word"
    combined_string = String.combine_string(string1, string2)
    print(f'combined string: {combined_string}\n')
    sentence = "This is a sentence."
    sentence = String.split_sentence(sentence, ' ')
    print(f'sentence: {sentence}\n')
    sentence = "This,is,a,sentence"
    sentence = String.split_sentence(sentence, ',')
    print(f'sentence: {sentence}\n')
    string_array = String.split_string_to_array_of_char(string1)
    print(f'string array: {string_array}')



if __name__ == "__main__":
    main()
