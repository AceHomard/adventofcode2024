import pandas as pd


def main():
    data = pd.read_csv("input.csv")
    data_sort1, data_sort2 = data['col1'], data['col2']
    counts = data_sort2.value_counts()
    result = 0
    for value in data_sort1:
        result += value * counts.get(value, 0)
    print(result)

if __name__ == '__main__':
    main()
