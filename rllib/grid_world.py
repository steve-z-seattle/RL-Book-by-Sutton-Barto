# define the student MDP problem

import numpy as np
from numpy import linalg as LA

class grid_world:
    # states
    S = list(range(16))
    # actions
    A = ['L', 'R', 'U', 'D']
    # model P
    P = np.zeros((len(S), len(S), len(A)))
    # model R
    R = np.zeros((len(S), len(A)))
    # policy
    Π = np.zeros((len(S), len(A)))

    def init_model_P(self):
        # TODO: simplify this:
        self.P[0,0,self.A.index('L')] = 1
        self.P[0,0,self.A.index('R')] = 1
        self.P[0,0,self.A.index('U')] = 1
        self.P[0,0,self.A.index('D')] = 1

        self.P[1,0,self.A.index('L')] = 1
        self.P[1,2,self.A.index('R')] = 1
        self.P[1,1,self.A.index('U')] = 1
        self.P[1,5,self.A.index('D')] = 1

        self.P[2,1,self.A.index('L')] = 1
        self.P[2,3,self.A.index('R')] = 1
        self.P[2,2,self.A.index('U')] = 1
        self.P[2,6,self.A.index('D')] = 1

        self.P[3,2,self.A.index('L')] = 1
        self.P[3,3,self.A.index('R')] = 1
        self.P[3,3,self.A.index('U')] = 1
        self.P[3,7,self.A.index('D')] = 1

        self.P[4,4,self.A.index('L')] = 1
        self.P[4,5,self.A.index('R')] = 1
        self.P[4,0,self.A.index('U')] = 1
        self.P[4,8,self.A.index('D')] = 1

        self.P[5,4,self.A.index('L')] = 1
        self.P[5,6,self.A.index('R')] = 1
        self.P[5,1,self.A.index('U')] = 1
        self.P[5,9,self.A.index('D')] = 1

        self.P[6,5,self.A.index('L')] = 1
        self.P[6,7,self.A.index('R')] = 1
        self.P[6,2,self.A.index('U')] = 1
        self.P[6,10,self.A.index('D')] = 1

        self.P[7,6,self.A.index('L')] = 1
        self.P[7,7,self.A.index('R')] = 1
        self.P[7,3,self.A.index('U')] = 1
        self.P[7,11,self.A.index('D')] = 1

        self.P[8,8,self.A.index('L')] = 1
        self.P[8,9,self.A.index('R')] = 1
        self.P[8,4,self.A.index('U')] = 1
        self.P[8,12,self.A.index('D')] = 1

        self.P[9,8,self.A.index('L')] = 1
        self.P[9,10,self.A.index('R')] = 1
        self.P[9,5,self.A.index('U')] = 1
        self.P[9,13,self.A.index('D')] = 1

        self.P[10,9,self.A.index('L')] = 1
        self.P[10,11,self.A.index('R')] = 1
        self.P[10,6,self.A.index('U')] = 1
        self.P[10,14,self.A.index('D')] = 1

        self.P[11,10,self.A.index('L')] = 1
        self.P[11,11,self.A.index('R')] = 1
        self.P[11,7,self.A.index('U')] = 1
        self.P[11,15,self.A.index('D')] = 1

        self.P[12,12,self.A.index('L')] = 1
        self.P[12,13,self.A.index('R')] = 1
        self.P[12,8,self.A.index('U')] = 1
        self.P[12,12,self.A.index('D')] = 1

        self.P[13,12,self.A.index('L')] = 1
        self.P[13,14,self.A.index('R')] = 1
        self.P[13,9,self.A.index('U')] = 1
        self.P[13,13,self.A.index('D')] = 1

        self.P[14,13,self.A.index('L')] = 1
        self.P[14,15,self.A.index('R')] = 1
        self.P[14,10,self.A.index('U')] = 1
        self.P[14,14,self.A.index('D')] = 1

        self.P[15,15,self.A.index('L')] = 1
        self.P[15,15,self.A.index('R')] = 1
        self.P[15,15,self.A.index('U')] = 1
        self.P[15,15,self.A.index('D')] = 1


    def init_model_R(self):
        for s, row in enumerate(self.R):
            for a in range(len(row)):
                if s == 0:
                    self.R[s,a] = 0
                elif s == 15:
                    self.R[s,a] = 0
                else:
                    self.R[s,a] = -1


    def init_Π(self):
        for s, row in enumerate(self.Π):
            for a in range(len(row)):
                self.Π[s, a] = 0.25


    def __init__(self):
        self.init_model_P()
        self.init_model_R()
        self.init_Π()
