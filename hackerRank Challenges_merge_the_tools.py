## Taguhi Hakobyan: Sept 9, Friday, 2022
## HackerRank Challenges Series
## merge_the_tools

# Consider the following:
#
# A string, , of length  where .
# An integer, , where  is a factor of .
# We can split  into  substrings where each subtring, , consists of a contiguous block of  characters in . Then, use each  to create string  such that:
#
# The characters in  are a subsequence of the characters in .
# Any repeat occurrence of a character is removed from the string such that each character in  occurs exactly once. In other words, if the character at some index  in  occurs at a previous index  in , then do not include the character in string .
# Given  and , print  lines where each line  denotes string .

# Sample Input
# s = 'AABCAAADA'
# k = 3
#
# Sample Output
#
# AB
# CA
# AD


# Rules:

def merge_the_tools(string, k):
    # your code goes heref

    string_list = [string[start:start + k] for start in range(0, len(string), k)]

    def unique_string(str_item):
        t = ""
        for i in range(len(str_item)):
            if str_item[i] not in str_item[:i]:
                t += str_item[i]
        return t

    for str_item in string_list:
        print(unique_string(str_item))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

