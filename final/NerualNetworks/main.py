import random
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
import torch.nn as nn
from torch.utils.data import DataLoader
import os
import numpy as np
import torch
import matplotlib.pyplot as plt
from PIL import Image
from Dataset import dataset
from LstmNet import OurNet

def train_loop(train_dataloader, val_dataloader, model, loss_fn, optimizer, epoches, cuda):
    size = len(train_dataloader.dataset)
    losses = []
    t  = list(range(epoches))
    loss = 0
    for epoch in tqdm(range(epoches)):
        for batch, (X, y, maxData) in enumerate(train_dataloader):
            # Compute prediction and loss
            X = X.view(X.shape[1], X.shape[0], X.shape[2])
            if cuda:
                X = X.cuda()
                y = y.cuda()
                maxData = maxData.cuda()
            pred = model(X)
            loss = loss_fn(pred, y)

            # Backpropagation
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            if batch % 30 == 0:
                print("Epoch: ", epoch + 1, '/', epoches, end='\t')
                print(batch * X.shape[0], '/', len(train_dataloader) * X.shape[0], end='\t')
                loss, current = loss.item(), batch * len(X)
                # print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")
                print(f"loss: {loss:>7f}")

        if (epoch != 0 and epoch % 1 == 0) or epoch == epoches - 1:
            # model.save(str(epoch) + ".pth")
            if epoch % 10 == 0:
                torch.save(model, './work-dir' + str(epoch) + '.pth')
            size = len(val_dataloader.dataset)
            test_loss, correct = 0, 0

            with torch.no_grad():
                for X, y, maxData in val_dataloader:
                    X = X.view(X.shape[1], X.shape[0], X.shape[2])
                    if cuda:
                        X = X.cuda()
                        y = y.cuda()
                        maxData = maxData.cuda()
                    pred = model(X)
                    test_loss += loss_fn(pred, y).item()
                    pred *= maxData
                    y *= maxData
                    pred = torch.round(pred).long()
                    y = y.long()
                    for i in range(y.shape[0]):
                        # judgeLine = 10 if maxData[i] < 1000 else 0.01 * maxData[i]
                        correct += (torch.abs(pred[i] - y[i]) < 2 * y[i]).type(torch.float).sum().item()

                    # correct += (torch.abs(pred - y) < maxData).type(torch.float).sum().item()

            test_loss /= size
            correct /= size*7
            print(f"Test Error: \n Accuracy: {(100 * correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")
        losses.append(loss.item())

    plt.plot(t, losses)
    plt.title("Loss during training")
    plt.savefig('loss.png')
    torch.save(model, './work-dir/latest.pth')
    return

def test_loop(dataloader, model, loss_fn):
    size = len(dataloader.dataset)
    test_loss, correct = 0, 0

    with torch.no_grad():
        for X, y in dataloader:
            pred = model(X)
            test_loss += loss_fn(pred, y).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()

    test_loss /= size
    correct /= size
    print(f"Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")

    return

def train(cuda=False,resume=False, batch_size=10):
    cudaAvailable = torch.cuda.is_available()

    trainDataet = dataset("Data/train2.txt")
    valDataet = dataset("Data/val2.txt")
    trainDataLoader = DataLoader(dataset=trainDataet, batch_size=batch_size, drop_last=True)
    valDataLoader = DataLoader(dataset=valDataet, batch_size=batch_size, drop_last=True)
    if resume:
        model = torch.load('./work-dir/40.pth')
    else:
        model = OurNet(batch_size)
    if cudaAvailable:
        model = model.cuda()
        # device = torch.device("cuda:1" if torch.cuda.is_available() else "cpu")
        # model.to_device(device)

    loss_fn = nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.5, momentum=0.9, weight_decay=1e-5)
    optimizer = torch.optim.Adamax(model.parameters(), lr=0.1, weight_decay=1e-4)
    epoches = 1

    train_loop(trainDataLoader, valDataLoader, model, loss_fn, optimizer, epoches, cudaAvailable)

    return


if __name__ == "__main__":
    train(resume=False)








