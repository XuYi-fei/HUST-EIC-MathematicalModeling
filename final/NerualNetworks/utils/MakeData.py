import pandas as pd
import os
import random

class MakeDataset():
    def __init__(self, known=30, predict=7, ratio=0.4, path=None):
        # ratio means the valid/(train + valid)
        assert path is not None, "The path is invalid"
        self.df = pd.read_excel(path)
        self.columns = self.df.columns
        self.knownLength = known
        self.ratio = ratio
        self.predictLength = predict
        self.data_length = len(self.df.values[0]) - 3
        # self.datasets: {known data: predict data}
        self.datasets = {}
        self.train_dataset = []
        self.val_dataset = []
        self.begin_index = self.data_length % (known + predict) + 3
        self.keys = []
        self.process()
        self.splitDataset()


    def process(self):
        # self.maxData = 0
        # self.minData = 0
        maxData = 0
        minData = 0
        for index, row in self.df.iterrows():
            data = list(row[self.begin_index:])
            while len(data) >= self.knownLength + self.predictLength:
                maxData = 1 if max(data[-(self.predictLength + self.knownLength):-self.predictLength]) * 1.5 == 0 else max(data[-(self.predictLength + self.knownLength):-self.predictLength]) * 1.5
                self.datasets[str(data[-(self.predictLength + self.knownLength):-self.predictLength])] = str([(data[-self.predictLength:]), maxData])
                # data = data[:-(self.predictLength+self.knownLength)]
                data = data[:-1]
        return

    def splitDataset(self):
        writer_train = open('../Data/train2.txt', 'w')
        writer_val = open('../Data/val2.txt', 'w')
        for index, (k,v) in enumerate(self.datasets.items()):
            k, v = eval(k), eval(v)
            k = str([i / v[1] for i in k])
            v[0] = str([i / v[1] for i in v[0]])
            if random.random() > self.ratio:
                writer_train.write(k)
                writer_train.write('#')
                writer_train.write(v[0])
                writer_train.write('#')
                writer_train.write(str(v[1]))
                writer_train.write('\n')
            else:
                writer_val.write(k)
                writer_val.write('#')
                writer_val.write(v[0])
                writer_val.write('#')
                writer_val.write(str(v[1]))
                writer_val.write('\n')

        writer_val.close()
        writer_train.close()

        return







if __name__ == '__main__':
    data = MakeDataset(path=r'D:\GitRepos\EIC\MathmaticalModeling\HUST-EIC-MathematicalModeling\final\NerualNetworks\Data\Preprocessed_original.xlsx')



