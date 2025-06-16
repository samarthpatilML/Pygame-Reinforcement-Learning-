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
        pass
    
    
    
    def get-state(self, game):
        pass
    
    def remember(self, state, action, reward, next_state, done):
        pass