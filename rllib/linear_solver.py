# define the base class for MDP problems

import numpy as np
from numpy import linalg as LA

class linear_solver:
    @classmethod
    def value_linear_solver(self, mdp, gamma):
        p_s_sp = np.einsum('sa,sta->st', mdp.Π, mdp.P)
        r_s = np.einsum('sa,sa->s', mdp.Π, mdp.R)
        m = np.eye(len(r_s)) -  gamma*p_s_sp
        return LA.inv(m) @ r_s


    @classmethod
    def q_linear_solver(self, mdp, gamma):
        # TODO: remove reshape
        p_s_a = np.einsum('sta,tb->satb', mdp.P, mdp.Π)
        p_s_a = p_s_a.reshape(len(mdp.S), len(mdp.A),-1)
        p_s_a = p_s_a.reshape(-1, len(mdp.S)*len(mdp.A))

        m = np.eye(mdp.R.shape[0]*mdp.R.shape[1]) -  gamma*p_s_a
        invm = LA.inv(m)
        res = (invm @ mdp.R.reshape(-1)).reshape(len(mdp.S), len(mdp.A))
        return res
