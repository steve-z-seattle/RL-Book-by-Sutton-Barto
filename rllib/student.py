# define the student MDP problem

import numpy as np

class student:
    # states
    S = ['class1', 'class2', 'class3', 'fb', 'sleeping']
    # actions
    A = ['facebook', 'quit', 'study', 'sleep', 'pub', 'other']
    # model P
    P = np.zeros((len(S), len(S), len(A)))
    # model R
    R = np.zeros((len(S), len(A)))
    # policy
    Π = np.zeros((len(S), len(A)))


    def init_model_P(self):
        self.P[self.S.index('class1'), self.S.index('class2'), self.A.index('study')] = 1
        self.P[self.S.index('class1'),self.S.index('fb'),self.A.index('facebook')] = 1

        self.P[self.S.index('class2'), self.S.index('class3'), self.A.index('study')] = 1
        self.P[self.S.index('class2'), self.S.index('sleeping'), self.A.index('sleep')] = 1

        self.P[self.S.index('class3'), self.S.index('sleeping'), self.A.index('study')] = 1
        self.P[self.S.index('class3'), self.S.index('class1'), self.A.index('pub')] = 0.2
        self.P[self.S.index('class3'), self.S.index('class2'), self.A.index('pub')] = 0.4
        self.P[self.S.index('class3'), self.S.index('class3'), self.A.index('pub')] = 0.4

        self.P[self.S.index('fb'), self.S.index('class1'), self.A.index('quit')] = 1
        self.P[self.S.index('fb'), self.S.index('fb'), self.A.index('facebook')] = 1

        self.P[self.S.index('sleeping'), self.S.index('sleeping'), self.A.index('other')] = 1


    def init_model_R(self):
        self.R[self.S.index('class1'), self.A.index('study')] = -2
        self.R[self.S.index('class1'), self.A.index('facebook')] = -1

        self.R[self.S.index('class2'), self.A.index('study')] = -2
        self.R[self.S.index('class2'), self.A.index('sleep')] = 0

        self.R[self.S.index('class3'), self.A.index('study')] = 10
        self.R[self.S.index('class3'), self.A.index('pub')] = 1

        self.R[self.S.index('fb'), self.A.index('quit')] = 0
        self.R[self.S.index('fb'), self.A.index('facebook')] = -1

        self.R[self.S.index('sleeping'), self.A.index('other')] = 0


    def init_Π(self):
        self.Π[self.S.index('class1'), self.A.index('study')] = 0.5
        self.Π[self.S.index('class1'), self.A.index('facebook')] = 0.5
        self.Π[self.S.index('class2'), self.A.index('study')] = 0.5
        self.Π[self.S.index('class2'), self.A.index('sleep')] = 0.5
        self.Π[self.S.index('class3'), self.A.index('pub')] = 0.5
        self.Π[self.S.index('class3'), self.A.index('study')] = 0.5
        self.Π[self.S.index('fb'), self.A.index('facebook')] = 0.5
        self.Π[self.S.index('fb'), self.A.index('quit')] = 0.5
        self.Π[self.S.index('sleeping'), self.A.index('other')] = 1


    def __init__(self):
        self.init_model_P()
        self.init_model_R()
        self.init_Π()
