import os, argparse

ps = argparse.ArgumentParser()
ps.add_argument("--data_path", type = str,
                help = "write data path")

args = ps.parse_args()
DATA_PATH = args.data_path

FILE_LIST = os.listdir(DATA_PATH)

for file in FILE_LIST:
    file_path = os.path.join(DATA_PATH, file)
    print("##########",file,"############")
    os.system(f"python3 {file_path}")
    # os.system("30") #명령어를 입력해야 할 경우

    R = open(file_path, mode = "rt", encoding= "utf-8")
    print("\n------------CODE--------------")
    for line in R.readlines():
        print(line, end ="")
    R.close()
    print("\n------------------------------\n\n")
