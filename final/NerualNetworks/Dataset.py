import random
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
import torch.nn as nn
from torch.utils.data import DataLoader
import os
import numpy as np
import torch
from PIL import Image


class dataset(torch.utils.data.Dataset):
    def __init__(self, dataPath=None):
        assert dataPath is not None, "The datapath is invalid"
        self.dataPath =dataPath
        with open(self.dataPath, 'r') as f:
            self.data = f.readlines()
            print()

    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):
        x, y, maxdata = self.data[item].split('#')
        maxdata = maxdata.strip('\n')
        x = torch.tensor(eval(x)).float()
        x = torch.unsqueeze(x, -1)
        y = torch.tensor(eval(y)).float()
        maxdata = torch.tensor(eval(maxdata)).float()
        maxdata = torch.unsqueeze(maxdata, -1)
        # x = x.view(x.shape[1], x.shape[0], x.shape[2])
        # y = y.view(y.shape[1], y.shape[0], y.shape[2])

        return x, y, maxdata



if __name__ == '__main__':
    data = dataset(r'Data/val.txt')
    print(data[0])