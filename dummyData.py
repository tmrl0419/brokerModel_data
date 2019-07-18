import numpy as np
import pandas as pd

np.set_printoptions(precision=2)


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def createDummy(Train, Test):
    np.random.seed(0)

    Train = int(Train)
    Test = int(Test)

    trainRandom = np.random.rand(Train,4) * 100
    train_df = pd.DataFrame(trainRandom, columns=['CPU', 'MEMORY', 'STORAGE', 'RATING']).round(0)
    train_df['OUTPUT'] = 0
    train_output = np.zeros([Train, 1])

    testRandom = np.random.rand(Test,4) * 100
    test_df = pd.DataFrame(testRandom, columns=['CPU', 'MEMORY', 'STORAGE', 'RATING']).round(0)
    test_df['OUTPUT'] = 0
    test_output = np.zeros([Test, 1])

    print("\n" + bcolors.OKGREEN + "Training 데이터 생성" + bcolors.ENDC)
    for i in range(Train):
        print(bcolors.HEADER + "Training " + str(i) + "번째 데이터 ({}/{})".format(i,Train))
        print("\n CPU: {}\n MEMORY: {}\n STORAGE: {}\n RATING: {}".format(
            train_df.loc[i]['CPU'], train_df.loc[i]['MEMORY'], train_df.loc[i]['STORAGE'],train_df.loc[i]['RATING']
        ) + bcolors.ENDC)

        print("\nINPUT OUTPUT FILE NUMBER")
        print("\n 0: NO CHANGE\n 1: CPU UP\n 2: CPU DOWN\n 3: MEMORY UP\n 4: MEMORY DOWN\n 5: STORAGE UP\n 6: STORAGE DOWN")
        print(bcolors.WARNING + bcolors.UNDERLINE+  "IF YOU WANT TO STOP PRESS 'C'" + bcolors.ENDC)
        mapping = input()
        if(mapping == 'C' or mapping =='c'):
            break
        train_output[i] = mapping

    train_df['OUTPUT'] = train_output
    print(train_df)

    print(bcolors.OKBLUE + "SAVING TRAINING DATA . . ." + bcolors.ENDC)
    print("\nINPUT OUTPUT FILE NAME FOR TRAINING DATA")
    name = input()
    if ".csv" in name:
        train_df.to_csv(name)
    else:
        train_df.to_csv(name + '.csv')

    print("\n" + bcolors.OKGREEN + "Test 데이터 생성" + bcolors.ENDC)
    for i in range(Test):
        print(bcolors.HEADER +"Test " + str(i) + "번째 데이터 ({}/{})".format(i,Test))
        print("\n CPU: {}\n MEMORY: {}\n STORAGE: {}\n RATING: {}".format(
            test_df.loc[i]['CPU'], test_df.loc[i]['MEMORY'], test_df.loc[i]['STORAGE'],test_df.loc[i]['RATING']
        ) + bcolors.ENDC)

        print("\nINPUT OUTPUT FILE NUMBER")
        print("\n 0: NO CHANGE\n 1: CPU UP\n 2: CPU DOWN\n 3: MEMORY UP\n 4: MEMORY DOWN\n 5: STORAGE UP\n 6: STORAGE DOWN")
        print(bcolors.WARNING + bcolors.UNDERLINE+  "IF YOU WANT TO STOP PRESS 'C'" + bcolors.ENDC)
        mapping = input()
        if(mapping == 'C' or mapping =='c'):
            break
        test_output[i] = mapping

    test_df['OUTPUT'] = test_output
    print(test_df)

    print(bcolors.OKBLUE + "SAVING TEST DATA . . ." + bcolors.ENDC)
    print("\nINPUT OUTPUT FILE NAME FOR TEST DATA")
    name = input()
    if ".csv" in name:
        test_df.to_csv(name)
    else:
        test_df.to_csv(name+'.csv')


if __name__ == '__main__':
    print("INPUT NUMBER OF DUMMY TRAINING DATA SIZE")
    Train = input()
    print("INPUT NUMBER OF DUMMY TEST DATA SIZE")
    Test = input()
    createDummy(Train,Test)
