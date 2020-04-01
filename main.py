import numpy as np
import matplotlib.pyplot as plt

# from keras.preprocessing import sequence
# import tensorflow as tf
# from keras.models import Sequential
# from keras.layers import Dense
# from keras.layers import LSTM
#
# from keras.optimizers import Adam
# from keras.models import load_model
# from keras.callbacks import ModelCheckpoint

WINDOW_SIZE = 20

def main():
    data_file1 ='./data_separated/phoneDataStill8sec.txt'
    data_file2 ='./data_separated/phoneDataWalking7sec.txt'
    data_file3 ='./data_separated/phoneDataRunning4sec.txt'
    #data_mixed = './phoneData40sec.txt'
    data_mixed = './test_set100sec.txt'


    windows, diffs = make_data(data_mixed)
    print(diffs[0])

    classes = threash_classify(diffs)
    plt.plot(range(len(classes)), classes)
    one_channel = [val[1][WINDOW_SIZE-1] for val in windows[:]]
    plt.plot(range(len(classes)), one_channel, label='x')
    one_channel = [val[2][WINDOW_SIZE-1] for val in windows[:]]
    plt.plot(range(len(classes)), one_channel, label='y')
    one_channel = [val[3][WINDOW_SIZE-1] for val in windows[:]]
    plt.plot(range(len(classes)), one_channel, label='z')
    plt.legend()
    plt.show()

    plt.plot(range(len(classes)), classes)
    one_channel = [val[1] for val in diffs[:]]
    plt.plot(range(len(classes)), one_channel, label='x')
    one_channel = [val[2] for val in diffs[:]]
    plt.plot(range(len(classes)), one_channel, label='y')
    one_channel = [val[3] for val in diffs[:]]
    plt.plot(range(len(classes)), one_channel, label='z')
    plt.legend()
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
        if diffs_t[i][0] < 0.2 and diffs_t[i][1] < 0.2 and diffs_t[i][2] < 0.2:
            output.append(1)
        elif diffs_t[i][0] < 4.5 and diffs_t[i][1] < 4.5 and diffs_t[i][2] < 12:
            output.append(2)
        else:
            output.append(3)
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
