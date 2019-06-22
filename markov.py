import numpy as np
from utils import *


class MarkovModel():

    def __init__(self, mu, sigma, N):
        self.prob= getP(mu, sigma, N)
        self.N_states= N
        self.current_state= 0
        self.states= np.array(list(range(self.N_states)))

    def transition(self):
        self.current_state =  choose(self.states , self.prob)
        return self.draw()

    def draw(self):
        return np.random.uniform(self.current_state/ self.N_states, (self.current_state+1)/ self.N_states)


mm= MarkovModel(0.5, 0.2, 4)

X=[]
for i in range(500):
    X.append(mm.transition())


# import matplotlib.pyplot as plt
# import numpy as np
# plt.hist(X, bins=mm.N_states, normed= True)
# plt.show()