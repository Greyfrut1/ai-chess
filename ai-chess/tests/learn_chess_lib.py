import chess

import torch
import torch.nn as nn
import torch.optim as optim

import numpy as np
# init board
board = chess.Board("k7/8/8/8/8/8/8/6K1 w KQ - 0 1")

# if GPU is to be used
device = torch.device(
    "cuda" if torch.cuda.is_available() else
    "mps" if torch.backends.mps.is_available() else
    "cpu"
)

print(board)

map_position = {
    0: 0,
    "p": 1,
    "r": 2,
    "n": 3,
    "b": 4,
    "q": 5,
    "k": 6,
    "P": -1,
    "R": -2,
    "N": -3,
    "B": -4,
    "Q": -5,
    "K": -6
}

# board_tensor = torch.tensor(board.fen().split()).to(device)

def board_to_tensor(board):
    # Conver the board to a tensor representation
    board_fen = board.board_fen()
    board_slited = board_fen.split('/')
    board_tensor = torch.zeros((8, 8), dtype=torch.float32).to(device)
    for index, i in enumerate(board_slited):
        i_len = len(i)
        row_items = 0
        char_id = 0
        while i_len > 0:
            item = i[char_id]
            match item:
                case item if item in map_position:
                    board_tensor[index][row_items] = map_position[item]
                    row_items += 1
                case item if item.isnumeric():
                    num = int(item)
                    while num > 0:
                        board_tensor[index][row_items] = 0
                        row_items += 1
                        num = num - 1
                    

            i_len -= 1
            char_id += 1
    return board_tensor

state = board_to_tensor(board)

# class DQN(nn.Module):

#     def __init__(self, n_observations, n_actions):
#         super(DQN, self).__init__()
#         self.layer1 = nn.Linear(n_observations, 128)
#         self.layer2 = nn.Linear(128, 128)
#         self.layer3 = nn.Linear(128, n_actions)

#     def forward(self, x):
#         x = F.relu(self.layer1(x))
#         x = F.relu(self.layer2(x))
#         return self.layer3(x)

class Agent:
    def __init__(self, state_dim, action_dim):
        self.device(device)
        self.state_dim = state_dim
        self.action_dim = action_dim

        self.exploration_rate = 1
        self.exploration_rate_decay = 0.99975
        self.exploration_rate_min = 0.1
        self.curr_step = 0

    def act(self, state, legal_moves):
        # Explore
        global board
        
        if np.random.rand() < self.exploration_rate:
            action_idx = np.random.randint(board.legal_moves.count())

        # Exploit
        else:
            print("exploit")
        
        self.exploration_rate *= self.exploration_rate_decay
        self.exploration_rate = max(self.exploration_rate_min, self.exploration_rate)
        self.curr_step += 1
        return action_idx



    def cache(self, experience):
        """Add the experience to memory"""
        pass

    def recall(self):
        """Sample experiences from memory"""
        pass

    def learn(self):
        """Update online action value (Q) function with a batch of experiences"""
        pass

agent = Agent(state_dim=64, action_dim=4096)