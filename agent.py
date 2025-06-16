import torch
import random
import numpy as np
from game import SnakeGameAI, Direction, Point
from collections import deque

max_memory = 100_000
batch_size = 1000
LR = 0.001



class Agent:
    def __init__(self):
        self.n_games = 0
        self.epsilon = 0 # control exploration
        self.gamma = 0.9  # discount rate
        self.memory = deque(maxlen=max_memory)
        #self.model = None  # Placeholder for the neural network model
    
    
    
    def get-state(self, game):
        pass
    
    def remember(self, state, action, reward, next_state, done):
        pass
    
    
    def train_long_memory(self):
        pass
    
    
    def train_short_memory(self, state, action, reward, next_state, done):
        pass
    
    
    def get_action(self, state):
        pass

def train():
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    record = 0
    agent = Agent()
    game = SnakeGameAI()
    while True:
        # get old state
        state_old = agent.get_state(game)

        # get move
        action = agent.get_action(state_old)

        # perform move and get new state
        reward, done, score = game.play_step(final_move)
        state_new = agent.get_state(game)

        # train short memory
        agent.train_short_memory(state_old, action, reward, state_new, done)

        # remember
        agent.remember(state_old, action, reward, state_new, done)

        if done:
            # train long memory, plot result
            game.reset()
            agent.n_games += 1
            agent.train_long_memory()

            if score > record:
                record = score
                agent.model.save()

if __name__ == "__main__":
    train()    
        