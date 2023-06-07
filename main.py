import numpy as np
import random


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# 在一个类中定义参数
class Sandbox:
    # payoff matrix
    #   A B
    # A a b
    # A c d

    a, b, c, d = 0, 0, 0, 0
    # size
    N = 100
    # num of A
    A_num = 0
    B_num = N - A_num
    # rounds
    # selection intensity
    w = 1

    # Markov process
    def process(self):
        # step1: kill a random identity
        index = random.randint(0, self.N)
        if index < self.A_num:
            # kill an A
            self.A_num -= 1
        else:
            self.B_num -= 1

def fitness():
    f = 1 - w + w * (a(i - 1) + b(N - i)) / (n - 1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    p = np.ones([100, 100], int)
    # TFT = 1, ALLD = 0
    # initial p
    for i in range(100):
        for j in range(100):
            p[i][j] = random.randint(0, 1)
    print(p)
    # payoff matrix
    #   A B
    # A a b
    # A c d
    # set payoff
    a, b, c, d = 1, 2, 3, 4

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
