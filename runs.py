# Brandon Wood
# Random Walks Project 2017
# 12/4/17
import numpy as np
import math
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

class walk():
    def __init__(self):
        self.num_walkers = 2
        self.sick_prob = 1
        self.not_sick_prob = 0
        self.total = self.sick_prob + self.not_sick_prob

        self.positions = [random.randint(-self.num_walkers, self.num_walkers) for x in range(self.num_walkers)]
        self.sicknesses = [0 for x in range(self.num_walkers)]
        self.sicknesses[0] = 1
        self.middle_preference = 2

    def step(self):
        for i in range(self.num_walkers):
            if self.positions[i] <= 0:
                self.positions[i] += random.choice([self.middle_preference,-1])
            else:
                self.positions[i] += random.choice([1,-self.middle_preference])
        new_sicknesses = self.sicknesses
        for i in range(self.num_walkers):
            for j in range(self.num_walkers):
                if(self.positions[i] == self.positions[j]):
                    if self.sicknesses[i] == 0 and self.sicknesses[j] == 1:
                        if random.randint(0, self.total) <= self.sick_prob:
                            new_sicknesses[i] = 1
                    elif self.sicknesses[i] == 1 and self.sicknesses[j] == 0:
                        if random.randint(0, self.total) <= self.sick_prob:
                            new_sicknesses[j] = 1
        self.sicknesses = new_sicknesses

    def check_all_sick(self):
        for x in self.sicknesses:
            if x == 0:
                return False
        return True

    def walk(self):
        num_steps = 0
        while not self.check_all_sick():
            self.step()
            num_steps += 1
            if(num_steps == 10000):
                return 200
        return num_steps

    def simulate(self):
        self.results = []
        for central_tendency in range(2, 10):
            for not_sick_prob in range(100):
                # Reinit
                self.positions = [random.randint(-self.num_walkers, self.num_walkers) for x in range(self.num_walkers)]
                self.sicknesses = [0 for x in range(self.num_walkers)]
                self.sicknesses[0] = 1

                self.middle_preference = central_tendency
                self.not_sick_prob = not_sick_prob
                self.results.append(self.walk())
        print(self.results)

    def draw(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection = '3d')
        X = []
        Y = []
        for x in range(100):
            for i in range(2, 10):
                X.append(i)
        for y in range(2, 10):
            for j in range(100):
                Y.append(j)
        Z = self.results
        ax.scatter(X, Y, Z, marker = 'o')
        ax.set_xlabel('Central Tendency')
        ax.set_ylabel('Likeness of Staying healthy')
        ax.set_zlabel('Number of Steps')
        ax.set_title('Steps Needed to Infect another Walker from Central Affinity and Health')
        plt.show()
w = walk()
w.simulate()
w.draw()
