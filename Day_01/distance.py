import pandas as pd


def main():
    data = pd.read_csv("input.csv")
    data_sort1, data_sort2 = sorted(data['col1']), sorted(data['col2'])
    result = 0
    for i in data.index:
        result += abs(data_sort2[i] - data_sort1[i])
    print(result)

if __name__ == '__main__':
    main()
