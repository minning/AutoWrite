#coding:utf-8
#!/usr/bin/env python

__Author__ = 'Wei Song'


def readData(filename,is12Merge=False):
    """
    从文件读取篇章数据并建立初始矩阵
    """
    X, y = [], []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            lineList = []
            if "type" in line:
                xOneMatrix = []
                label = int(line[5:])-1
                if is12Merge==True:
                    if label==0 or label==1:
                        label = 0
                    elif label==2 or label==3:
                        label -= 1
                y.append(label)
            elif "#" not in line:
                    ls = line.split()
                    for item in ls:
                        lineList.append(int(item))
                    if lineList:
                        xOneMatrix.append(lineList)
            elif "#" in line:
               xOneMatrix = XPadding(xOneMatrix, max_npara, max_nsent)
               X.append(xOneMatrix)

    return X, y



def readBalancedData(filename,is12Merge=False):
    X, y = readData(filename,is12Merge=is12Merge)
    n_class = len(set(y))
    labeled_samples = [[] for i in range(n_class)]
    for index, label in enumerate(y):
        labeled_samples[label].append(X[index])

    label_count = [len(item) for item in labeled_samples]
    max_count = max(label_count)
    to_sample = [max_count-len(item) for item in labeled_samples]
    X_expanded, y_expanded = [], []
    for label, samplelist in enumerate(labeled_samples):
        newsamples = sampling(samplelist, to_sample[label])
        for sample in samplelist + newsamples:
            X_expanded.append(sample)
            y_expanded.append(label)

    return X_expanded, y_expanded


import random
def sampling(sample_list, n2sample):
    sampled = []
    for i in range(n2sample):
        index = random.randint(0,len(sample_list)-1)
        sampled.append(sample_list[index])
    return sampled

max_npara = 20
max_nsent = 10

def XPadding(X, n_row, n_col):
    """
    对初始矩阵进行裁剪或补充，使其满足要求的形状
    """
    X_new = []
    for x in X[0:min(len(X), n_row)]:
        newx = [0 for i in range(n_col)]
        for i in range(n_col):
            if i < len(x):
                newx[i] = x[i]
            else:
                newx[i] = 0
        X_new.append(newx)

    return X_new

if __name__ == "__main__":
    trainfile = 'StructMatrix.txt'
    testfile = 'TestStructMatrix.txt'
    X_train, y_train = readData(trainfile)
                #for index, X in enumerate(X_train):
    #    print X, y_train[index]
    print X_train[0]
    print y_train[0]










