import argparse


def cli_parser():
    parser = argparse.ArgumentParser(description='Task2')
    parser.add_argument('path_to_file', help='path_to_file')
    return parser.parse_args()


def parse_txt(file):
    nums = []
    with open(file, 'r') as f2:
        while True:
            line = f2.readline().strip()
            if line:
                nums.append(int(line.split('\n')[0]))
            if not line:
                break
    return nums


def task2(nums):
    nums.sort()
    mid = len(nums) // 2
    res = 0
    for n in nums:
        res += abs(n-nums[mid])
    return res



def main():
    namespace = cli_parser()
    massiv = parse_txt(namespace.path_to_file)
    result = task2(massiv)
    print(result)


if __name__ == '__main__':
    main()
