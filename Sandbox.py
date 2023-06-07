import numpy as np


# 有限种群类，包含种群的参数以及种群的
# 大致目标，输入初始参数，给定N以后得到
class CFinitePopulation:
    a,b,c,d=0,0,0,0
    i,N = 0,100
    '''
    payoff matrix
       A  B
    A  a  b
    B  c  d
    '''

    # 状态转移矩阵是一个三对角矩阵
    # 用一个3*N的列表储存内容，N的大小不确定，先
    transMatrix = np.empty((0,3))

    def __init__(self, payoff:list, size:int,selectionIntensity:float):

        for j in range(self.N):
            # f,g 分别为a和b的适合度
            f = 1-w+w*(a(i-1)+b*(N-1)):
            g =
            p0 =
            p2 =
            p1 = 1-p0-p1

    #当输入参数以后，状态转移矩阵也可以确定了,避免重复计算

    def Fitness(self,type = 'A'):
        if type == 'A':
            f = 1 - w + w * (a * (i - 1) + b * (N - i)) / (N - 1)
        elif type == 'A':
            f = 1 - w + w * (c * i + d * (N - i - 1)) / (N - 1)
        return f

    def StateTransition(self,i:int,step:int):




    def DeathBirthProcess(self):



        if self.i == 0:
            return "A"
        elif self.i == self.N:
            return "B"
    f_i = 1 - w + w *[]