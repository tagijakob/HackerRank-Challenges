## Taguhi Hakobyan
## HackerRank Challenges Series
# The Minion Game
# Game Rules

# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
# Vowels are defined as: "A","E","I","O","U"

# string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
# Sample Input: BANANA
# Sample Output: Stuart 12


# The Minion Game

def minion_game(string="BANANA"):
    """
    Creates all substrings of the string
    :param string: str 0 < len(string) < 10^6
    :return:
    """
    vowels = ["A","E","I","O","U"]
    # Note that number of substrings depends on where the element is located.
    # for the first element, total number of substrings would be len(string) - 0 (or the position of that letter)
    # Hence

    Kevin = sum([len(string) - x for x in range(len(string)) if string[x] in vowels])
    Stuart = sum([len(string) - x for x in range(len(string)) if string[x] not in vowels])

    if Kevin>Stuart:
        return print("Kevin "+str(Kevin))
    elif Kevin==Stuart:
        return print("Draw")
    else:
        return print("Stuart "+str(Stuart))

test1="BANANA"

if __name__ == '__main__':
    s = input()
    minion_game(s)