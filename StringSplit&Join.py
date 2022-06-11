def split_and_join(line):
    lis=line.split(" ")
    s = '-'.join(lis)
    return s

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)