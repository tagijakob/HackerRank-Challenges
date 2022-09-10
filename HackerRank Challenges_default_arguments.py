## Taguhi Hakobyan: Sept 9, Friday, 2022
## HackerRank Challenges Series

# Default Arguments
# In this challenge, the task is to debug the existing code to successfully execute all provided test files.
#
# This function should print the first  values returned by get_next() method of stream object provided as an argument.
# Each of these values should be printed in a separate line.
#
# Whenever the function is called without the stream argument,
# it should use an instance of EvenStream class defined in the code stubs below as the value of stream.

# Sample Input 0
# 3
# odd 2
# even 3
# odd 5

# Sample Output 0
# 1
# 3
# 0
# 2
# 4
# 1
# 3
# 5
# 7
# 9

class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=EvenStream()):
    stream.__init__()
    for i in range(n):
        print(stream.get_next())


queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())
