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
    train_output = np.zeros([Train, 3])
    train_cpu = np.zeros([Train, 1])
    train_memory = np.zeros([Train, 1])
    train_storage = np.zeros([Train, 1])

    testRandom = np.random.rand(Test,4) * 100
    test_df = pd.DataFrame(testRandom, columns=['CPU', 'MEMORY', 'STORAGE', 'RATING']).round(0)
    test_cpu = np.zeros([Test, 1])
    test_memory = np.zeros([Test, 1])
    test_storage = np.zeros([Test, 1])

    print("\n" + bcolors.OKGREEN + "Training 데이터 생성" + bcolors.ENDC)
    for i in range(Train):
        print(bcolors.OKBLUE + "Training " + str(i+1) + "번째 데이터 ({}/{})".format(i+1,Train))
        print(bcolors.HEADER +  "\n CPU: {}\n MEMORY: {}\n STORAGE: {}\n RATING: {}".format(
            train_df.loc[i]['CPU'], train_df.loc[i]['MEMORY'], train_df.loc[i]['STORAGE'],train_df.loc[i]['RATING']
        ) + bcolors.ENDC)

        print("\nINPUT OUTPUT CPU")
        cpu = input()
        print("\nINPUT OUTPUT MEMORY")
        memory = input()
        print("\nINPUT OUTPUT STORAGE")
        storage = input()

        train_cpu[i] = cpu
        train_memory[i] = memory
        train_storage[i] = storage

    train_df['OUTPUT_cpu'] = train_cpu
    train_df['OUTPUT_memory'] = train_memory
    train_df['OUTPUT_storage'] = train_storage
    print(train_df)

    print(bcolors.OKBLUE + "SAVING TRAINING DATA . . ." + bcolors.ENDC)
    print("\nINPUT OUTPUT FILE" + bcolors.WARNING + " NAME" + bcolors.ENDC + " FOR Training DATA")
    name = input()
    if ".csv" in name:
        train_df.to_csv(name)
    else:
        train_df.to_csv(name + '.csv')

    print("\n" + bcolors.OKGREEN + "Test 데이터 생성" + bcolors.ENDC)
    for i in range(Test):
        print(bcolors.OKBLUE +"Test " + str(i+1) + "번째 데이터 ({}/{})".format(i+1,Test) + bcolors.ENDC)
        print(bcolors.HEADER + "\n CPU: {}\n MEMORY: {}\n STORAGE: {}\n RATING: {}".format(
            test_df.loc[i]['CPU'], test_df.loc[i]['MEMORY'], test_df.loc[i]['STORAGE'],test_df.loc[i]['RATING']
        ) + bcolors.ENDC)

        print("\nINPUT OUTPUT CPU")
        cpu = input()
        print("\nINPUT OUTPUT MEMORY")
        memory = input()
        print("\nINPUT OUTPUT STORAGE")
        storage = input()

        test_cpu[i] = cpu
        test_memory[i] = memory
        test_storage[i] = storage

    test_df['OUTPUT_cpu'] = test_cpu
    test_df['OUTPUT_memory'] = test_memory
    test_df['OUTPUT_storage'] = test_storage

    print(test_df)
    print(bcolors.OKBLUE + "SAVING TEST DATA . . ." + bcolors.ENDC)
    print("\nINPUT OUTPUT FILE"+ bcolors.WARNING +  " NAME" + bcolors.ENDC +" FOR TEST DATA")
    name = input()

    if ".csv" in name:
        test_df.to_csv(name)
    else:
        test_df.to_csv(name+'.csv')


if __name__ == '__main__':
    print("INPUT NUMBER OF DUMMY TRAINING DATA" +   bcolors.WARNING + " SIZE" + bcolors.ENDC)
    Train = input()
    print("INPUT NUMBER OF DUMMY TEST DATA"+   bcolors.WARNING + " SIZE" + bcolors.ENDC)
    Test = input()
    createDummy(Train,Test)
