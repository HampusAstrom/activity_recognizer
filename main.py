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
    #data_file1 ='./data_separated/phoneDataStill8sec.txt'
    #data_file2 ='./data_separated/phoneDataWalking7sec.txt'
    #data_file3 ='./data_separated/phoneDataRunning4sec.txt'
    #data_mixed = './phoneData40sec.txt'
    data_file1 = './data_fused/out_still.txt'
    data_file2 = './data_fused/out_walking.txt'
    data_file3 = './data_fused/out_running.txt'
    data_mixed = './data_fused/out_test_set100sec.txt'


    windows, diffs, vec = make_data2(data_mixed)

    print(len(vec))
    print(len(vec[0]))
    print(vec[0])
    print(diffs[0])

    classes = threash_classify(diffs)

    plt.figure(1)
    plt.suptitle('Raw vector')
    plt.subplot(3, 4, 1)
    one_channel = [val[0][WINDOW_SIZE-1] for val in windows[:]]
    plt.plot(range(len(classes)), one_channel)
    plt.title('pn')
    plt.subplot(3, 4, 2)
    one_channel = [val[1][WINDOW_SIZE-1] for val in windows[:]]
    plt.plot(range(len(classes)), one_channel)
    plt.title('pe')
    plt.subplot(3, 4, 3)
    one_channel = [val[2][WINDOW_SIZE-1] for val in windows[:]]
    plt.plot(range(len(classes)), one_channel)
    plt.title('pd')
    plt.subplot(3, 4, 4)
    plt.plot(range(len(classes)), classes)
    plt.title('class')

    plt.subplot(3, 4, 5)
    one_channel = [val[3][WINDOW_SIZE-1] for val in windows[:]]
    plt.plot(range(len(classes)), one_channel)
    plt.title('vn')
    plt.subplot(3, 4, 6)
    one_channel = [val[4][WINDOW_SIZE-1] for val in windows[:]]
    plt.plot(range(len(classes)), one_channel)
    plt.title('ve')
    plt.subplot(3, 4, 7)
    one_channel = [val[5][WINDOW_SIZE-1] for val in windows[:]]
    plt.plot(range(len(classes)), one_channel)
    plt.title('vd')

    plt.subplot(3, 4, 9)
    one_channel = [val[6][WINDOW_SIZE-1] for val in windows[:]]
    plt.plot(range(len(classes)), one_channel)
    plt.title('q1')
    plt.subplot(3, 4, 10)
    one_channel = [val[7][WINDOW_SIZE-1] for val in windows[:]]
    plt.plot(range(len(classes)), one_channel)
    plt.title('q2')
    plt.subplot(3, 4, 11)
    one_channel = [val[8][WINDOW_SIZE-1] for val in windows[:]]
    plt.plot(range(len(classes)), one_channel)
    plt.title('q3')
    plt.subplot(3, 4, 12)
    one_channel = [val[9][WINDOW_SIZE-1] for val in windows[:]]
    plt.plot(range(len(classes)), one_channel)
    plt.title('q4')
    #plt.show()

    plt.figure(2)
    plt.suptitle('Window differences')
    plt.subplot(3, 4, 1)
    one_channel = [val[0] for val in diffs[:]]
    plt.plot(range(len(classes)), one_channel)
    plt.title('pn')
    plt.subplot(3, 4, 2)
    one_channel = [val[1] for val in diffs[:]]
    plt.plot(range(len(classes)), one_channel)
    plt.title('pe')
    plt.subplot(3, 4, 3)
    one_channel = [val[2] for val in diffs[:]]
    plt.plot(range(len(classes)), one_channel)
    plt.title('pd')
    plt.subplot(3, 4, 4)
    plt.plot(range(len(classes)), classes)
    plt.title('class')

    plt.subplot(3, 4, 5)
    one_channel = [val[3] for val in diffs[:]]
    plt.plot(range(len(classes)), one_channel)
    plt.title('vn')
    plt.subplot(3, 4, 6)
    one_channel = [val[4] for val in diffs[:]]
    plt.plot(range(len(classes)), one_channel)
    plt.title('ve')
    plt.subplot(3, 4, 7)
    one_channel = [val[5] for val in diffs[:]]
    plt.plot(range(len(classes)), one_channel)
    plt.title('vd')

    plt.subplot(3, 4, 9)
    one_channel = [val[6] for val in diffs[:]]
    plt.plot(range(len(classes)), one_channel)
    plt.title('q1')
    plt.subplot(3, 4, 10)
    one_channel = [val[7] for val in diffs[:]]
    plt.plot(range(len(classes)), one_channel)
    plt.title('q2')
    plt.subplot(3, 4, 11)
    one_channel = [val[8] for val in diffs[:]]
    plt.plot(range(len(classes)), one_channel)
    plt.title('q3')
    plt.subplot(3, 4, 12)
    one_channel = [val[9] for val in diffs[:]]
    plt.plot(range(len(classes)), one_channel)
    plt.title('q4')
    plt.show()

    data_files = [data_file1, data_file2, data_file3]
    for dat in data_files:
        windows, diffs, vec = make_data2(dat)

        classes = threash_classify(diffs)

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

    # data format, ned and quaternion format: npos, epos, dpos, nvel, evel, dvel, q1, q2, q3, q4
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

def make_data2(data_file):
    with open(data_file) as file:
        ll = []
        for line in file:
            ll.append(line.strip().split(','))

    # data format: time, x, y, z
    vec = []
    for line in ll:
        if len(line) > 1:
            vals = line
            vec.append([float(x) for x in vals])

    vec_t = list(zip(*vec))
    print(len(vec[0]))

    # plt.plot(acc_t[0], acc_t[1])
    # plt.plot(acc_t[0], acc_t[2])
    # plt.plot(acc_t[0], acc_t[3])
    # plt.show()

    # we simplify and only classify after window size steps, currently only looking back in time
    windows = []
    diffs = []
    for i in range(WINDOW_SIZE,len(vec)):
        window = list(zip(*vec[i-WINDOW_SIZE:i]))
        #print(window)
        diff = []
        means1 = []
        means2 = []
        means3 = []
        for j in range(len(window)):
            diff.append(max(window[j]) - min(window[j]))
            # diff += window[j]
        for j in range(WINDOW_SIZE):
            mean1 = (window[0][j] + window[1][j] + window[2][j])/3 # mean pos variation
            mean2 = (window[3][j] + window[4][j] + window[5][j])/3 # mean vel variation
            mean3 = (window[6][j] + window[7][j] + window[8][j] + window[9][j])/4 # mean quaternion variation
            # print(mean1)
            means1.append(mean1)
            means2.append(mean2)
            means3.append(mean3)
        diff.append(max(means1) - min(means1))
        diff.append(max(means2) - min(means2))
        diff.append(max(means3) - min(means3))
        diffs.append(diff)
        windows.append(window)

    diffs_t = list(zip(*diffs))

    for i in range(len(diffs_t)):
        print('{} {}'.format(min(diffs_t[i]), max(diffs_t[i])))
    print()

    return windows, diffs, vec

if __name__ == "__main__":
    main()
