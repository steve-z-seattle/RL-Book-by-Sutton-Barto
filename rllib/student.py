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
        pp = 1
        self.P[0,1,self.A.index('study')] = 1*pp
        self.P[0,3,self.A.index('facebook')] = 1*pp

        self.P[1,2,self.A.index('study')] = 1*pp
        self.P[1,4,self.A.index('sleep')] = 1*pp

        self.P[2,4,self.A.index('study')] = 1*pp
        self.P[2,0,self.A.index('pub')] = 0.2*pp
        self.P[2,1,self.A.index('pub')] = 0.4*pp
        self.P[2,2,self.A.index('pub')] = 0.4*pp

        self.P[3,0,self.A.index('quit')] = 1*pp
        self.P[3,3,self.A.index('facebook')] = 1*pp

        self.P[4,4,self.A.index('other')] = 1


    def init_model_R(self):
        self.R[0,self.A.index('study')] = -2
        self.R[0,self.A.index('facebook')] = -1

        self.R[1,self.A.index('study')] = -2
        self.R[1,self.A.index('sleep')] = 0

        self.R[2,self.A.index('study')] = 10
        self.R[2,self.A.index('pub')] = 1

        self.R[3,self.A.index('quit')] = 0
        self.R[3,self.A.index('facebook')] = -1

        self.R[4,self.A.index('other')] = 0


    def init_Π(self):
        self.Π[0,self.A.index('study')] = 0.5
        self.Π[0,self.A.index('facebook')] = 0.5
        self.Π[1,self.A.index('study')] = 0.5
        self.Π[1,self.A.index('sleep')] = 0.5
        self.Π[2,self.A.index('pub')] = 0.5
        self.Π[2,self.A.index('study')] = 0.5
        self.Π[3,self.A.index('facebook')] = 0.5
        self.Π[3,self.A.index('quit')] = 0.5
        self.Π[4,self.A.index('other')] = 1


    def __init__(self):
        self.init_model_P()
        self.init_model_R()
        self.init_Π()
