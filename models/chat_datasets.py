import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

class ChatDataset(Dataset):
    def __init__(self, X_data, y_data):
        self.n_samples = len(X_data)
        self.x_data = X_data
        self.y_data = y_data

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return  self.n_samples