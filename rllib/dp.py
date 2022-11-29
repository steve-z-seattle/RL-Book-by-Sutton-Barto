# define the DP algorithm

import numpy as np

class dp:
    @classmethod
    def _v2q(self, mdp, V, gamma=1.0):
        Q = mdp.R + gamma * np.einsum('sta,t->sa', mdp.P, V)
        return Q


    @classmethod
    def compute_v_π(self, mdp, V, gamma=1.0):
        Q = self._v2q(mdp, V, gamma)
        return np.einsum('sa,sa->s', mdp.Π, Q)


    @classmethod
    def compute_v_star(self, mdp, V, gamma=1.0):
        Q = self._v2q(mdp, V, gamma)
        return np.max(Q, axis=1)


    @classmethod
    def compute_q_π(self, mdp, Q, gamma=1.0):
        V = np.einsum('sa,sa->s', mdp.Π, Q)
        return self._v2q(mdp, V, gamma)


    @classmethod
    def compute_q_star(self, mdp, Q, gamma=1.0):
        V = np.max(Q, axis=1)
        return self._v2q(mdp, V, gamma)
