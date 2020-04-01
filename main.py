import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# from keras.preprocessing import sequence
# import tensorflow as tf
# from keras.models import Sequential
# from keras.layers import Dense
# from keras.layers import LSTM
#
# from keras.optimizers import Adam
# from keras.models import load_model
# from keras.callbacks import ModelCheckpoint

WINDOW_SIZE = 40

def main():
    data_file1 ='./data_separated/phoneDataStill8sec.txt'
    data_file2 ='./data_separated/phoneDataWalking7sec.txt'
    data_file3 ='./data_separated/phoneDataRunning4sec.txt'
    #data_mixed = './phoneData40sec.txt'
    data_mixed = './test_set100sec.txt'


    windows, diffs = make_data(data_mixed)

    classes = threash_classify(diffs)

    plt.rcParams.update({'font.size': 22})

    plt.figure(figsize=[18, 15])
    plt.plot(range(len(classes)), classes)
    one_channel = [val[1][WINDOW_SIZE-1] for val in windows[:]]
    plt.plot(range(len(classes)), one_channel, label='x')
    one_channel = [val[2][WINDOW_SIZE-1] for val in windows[:]]
    plt.plot(range(len(classes)), one_channel, label='y')
    one_channel = [val[3][WINDOW_SIZE-1] for val in windows[:]]
    plt.plot(range(len(classes)), one_channel, label='z')
    i = 0
    current_class = 0 # not a class, dummy
    start_index = 0
    found = [0, 0, 0]
    while i < len(classes):
        if current_class != classes[i]:
            if current_class == -1:
                plt.axvspan(start_index, i, facecolor='g', alpha=0.1, zorder=-100, label =  "_"*found[0] + "still")
                found[0] = 1
            if current_class == -2:
                plt.axvspan(start_index, i, facecolor='b', alpha=0.1, zorder=-100, label =  "_"*found[1] + "walk")
                found[1] = 1
            if current_class == -3:
                plt.axvspan(start_index, i, facecolor='r', alpha=0.1, zorder=-100, label =  "_"*found[2] + "run")
                found[2] = 1
            current_class = classes[i]
            start_index = i
        i += 1
    plt.legend()
    plt.savefig('raw.png')
    plt.show()

    plt.figure(figsize=[18, 15])
    plt.plot(range(len(classes)), classes)
    one_channel = [val[1] for val in diffs[:]]
    plt.plot(range(len(classes)), one_channel, label='x_diff')
    one_channel = [val[2] for val in diffs[:]]
    plt.plot(range(len(classes)), one_channel, label='y_diff')
    one_channel = [val[3] for val in diffs[:]]
    plt.plot(range(len(classes)), one_channel, label='z_diff')
    i = 0
    current_class = 0 # not a class, dummy
    start_index = 0
    found = [0, 0, 0]
    while i < len(classes):
        if current_class != classes[i]:
            if current_class == -1:
                plt.axvspan(start_index, i, facecolor='g', alpha=0.1, zorder=-100, label =  "_"*found[0] + "still")
                found[0] = 1
            if current_class == -2:
                plt.axvspan(start_index, i, facecolor='b', alpha=0.1, zorder=-100, label =  "_"*found[1] + "walk")
                found[1] = 1
            if current_class == -3:
                plt.axvspan(start_index, i, facecolor='r', alpha=0.1, zorder=-100, label =  "_"*found[2] + "run")
                found[2] = 1
            current_class = classes[i]
            start_index = i
        i += 1
    plt.legend()
    plt.savefig('windowed_diff.png')
    plt.show()

    data_files = [data_file1, data_file2, data_file3]
    for dat in data_files:
        windows, diffs = make_data(dat)

        classes = threash_classify(diffs)

        # model = Sequential()
        # model.add(LSTM(256, input_shape=(seq_len, 4)))
        # model.add(Dense(1, activation='sigmoid'))

def threash_classify(diffs_t):
    output = []
    for i in range(len(diffs_t)):
        if diffs_t[i][0] < 2.5 and diffs_t[i][1] < 2.5 and diffs_t[i][2] < 2.5:
            output.append(-1)
        elif diffs_t[i][0] < 15 and diffs_t[i][1] < 15 and diffs_t[i][2] < 15:
            output.append(-2)
        else:
            output.append(-3)
    return output

def make_data(data_file):
    with open(data_file) as file:
        ll = []
        for line in file:
            ll.append(line.strip().split())

    # data format: time, x, y, z
    acc = []
    for line in ll:
        if len(line) > 1 and line[1] == 'ACC':
            #only_acc.append(line)
            vals = [line[0]] + line[2:]
            acc.append([float(x) for x in vals])

    acc_t = list(zip(*acc))
    # print(len(acc))

    # plt.plot(acc_t[0], acc_t[1])
    # plt.plot(acc_t[0], acc_t[2])
    # plt.plot(acc_t[0], acc_t[3])
    # plt.show()

    # we simplify and only classify after window size steps, currently only looking back in time
    windows = []
    diffs = []
    for i in range(WINDOW_SIZE,len(acc)):
        window = list(zip(*acc[i-WINDOW_SIZE:i]))
        #print(window)
        diff = []
        mean = []
        for j in range(1,4):
            diff.append(max(window[j]) - min(window[j]))
            # diff += window[j]
        for j in range(WINDOW_SIZE):
            mean1 = (window[1][j] + window[2][j] + window[3][j])/3
            # print(mean1)
            mean.append(mean1)
        diff.append(max(mean) - min(mean))
        #print(diff)
        diffs.append(diff)
        windows.append(window)

    diffs_t = list(zip(*diffs))

    print(min(diffs_t[0]))
    print(max(diffs_t[0]))
    print(min(diffs_t[1]))
    print(max(diffs_t[1]))
    print(min(diffs_t[2]))
    print(max(diffs_t[2]))
    print(min(diffs_t[3]))
    print(max(diffs_t[3]))
    print()

    return windows, diffs

if __name__ == "__main__":
    main()
