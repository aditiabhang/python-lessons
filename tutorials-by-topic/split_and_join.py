def split_and_join(line):
    # write your code here
    line = line.split(" ")
    line = '-'.join(line)
    return line


print(split_and_join("python is very easy to understand"))


def mutate_string(string, position, character):
    modified_word = list(string)
    modified_word[position] = character
    modified_word = ''.join(modified_word)
    return modified_word

print(mutate_string('abracadabra', 4 , 'k'))


"""
ABCDCDC
CDC

"""


def count_substring(string, sub_string):
    count=0
    while(string.find(sub_string)!=-1):
        count=count+1
        i=string.find(sub_string)
        string=string[i+1:]
    return count

print(count_substring("ABCDCDC", "CDC"))    