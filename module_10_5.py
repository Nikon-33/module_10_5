import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, "r", encoding='utf-8') as file:
        lines = file.read().split()
        all_data.append(lines)


if __name__ == '__main__':

    start1 = datetime.now()
    file_name = [f'./file {i}.txt' for i in range(1, 5)]
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, file_name)

    end1 = datetime.now()
    print(end1 - start1)

    start2 = datetime.now()
    for i in file_name:
        read_info(i)

    end2 = datetime.now()
    print(end2 - start2)
