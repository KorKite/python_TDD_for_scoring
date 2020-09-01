import os, argparse

ps = argparse.ArgumentParser()
ps.add_argument("--data_path", type = str,
                help = "write data path")

args = ps.parse_args()


DATA_PATH = args.data_path
FILE_LIST = os.listdir(DATA_PATH)

if not FILE_LIST[0].endswith(".py"):
    FILE_LIST_COPY = FILE_LIST[:]
    FILE_LIST = []
    for temp in FILE_LIST_COPY:
        inside = os.path.join(DATA_PATH, temp)
        temp_list = os.listdir(inside)
        for file in temp_list:
            if file.endswith(".py"):
                FINAL_PATH = os.path.join(inside, file)
                FILE_LIST.append(FINAL_PATH)

else:
    FILE_LIST_COPY = FILE_LIST[:]
    FILE_LIST = []
    for temp in FILE_LIST_COPY:
        inside = os.path.join(DATA_PATH, temp)
        FILE_LIST.append(inside)
    

for PATH in FILE_LIST:
    print("##########",PATH,"############")
    os.system(f"python3 {PATH}")
    # os.system("30") #명령어를 입력해야 할 경우

    R = open(PATH, mode = "rt", encoding= "utf-8")
    print("\n------------CODE--------------")
    for line in R.readlines():
        print(line, end ="")
    R.close()
    print("\n------------------------------\n\n")
