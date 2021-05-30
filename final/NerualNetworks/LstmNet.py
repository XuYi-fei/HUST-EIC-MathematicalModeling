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

class OurNet(nn.Module):
    def __init__(self, batch):
        self.size = 30
        self.batch = batch
        super(OurNet, self).__init__()
        nn.Embedding
        self.FC1 = nn.Linear(1, 100, bias=True)
        # self.BN = nn.BatchNorm1d(num_features=10)
        self.h0 = torch.zeros(2, batch, 100)
        self.c0 = torch.zeros(2, batch, 100)
        self.hx = torch.zeros(batch, 100)
        self.cx = torch.zeros(batch, 100)
        self.net = nn.LSTM(input_size=100, hidden_size=100, num_layers=2, bias=True)
        self.cell = nn.LSTMCell(input_size=100, hidden_size=100, bias=True)
        self.cell2 = nn.LSTMCell(input_size=100, hidden_size=100, bias=True)
        self.FC2 = nn.Linear(7*100, 7)
        self.activation = torch.nn.Sigmoid()

    def forward(self, x, predict=7):
        hx, cx = self.hx, self.cx
        x = x.view(x.shape[0] * x.shape[1], 1)
        x = self.FC1(x)
        x = x.view(self.size, self.batch, -1)
        output = []
        # x, t = self.net(x, (self.h0, self.c0))
        for i in range(x.shape[0]):
            hx, cx = self.cell(x[i], (hx, cx))
            output.append(hx)
        output = torch.stack(output, dim=0)
        result = []
        for i in range(predict):
            hx, cx = self.cell2(output[-1], (hx, cx))
            result.append(hx)
        x = result[:]
        x = torch.stack(x, dim=0)
        x = x.transpose(1, 0)
        # x = x.transpose(1, 2)
        x = x.reshape(x.shape[0] , x.shape[1] * x.shape[2])
        x = self.FC2(x)
        x = self.activation(x)
        return x
