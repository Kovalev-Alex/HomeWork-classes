def open_files(files: list):
    list_ = []
    for file in files:
        f = open(file, 'r')
        data = f.readlines()
        lines = len(data)
        list_.append([lines, file, data])
        f.close()
    return list_


def sort_list(list_):
    of = open_files(list_)
    count = len(of)
    for i in range(count-1):
        if of[i][0] > of[i + 1][0]:
            of[i], of[i + 1] = of[i + 1], of[i]
    return of


def write_file(list_):
    sl = sort_list(list_)
    with open('result.txt', 'w') as f:
        for item in sl:
            f.write(item[1])
            f.write('\n')
            f.write(str(item[0]))
            f.write('\n')
            f.write("".join(item[2]))
            f.write('\n')


write_file(['1.txt', '2.txt', '3.txt'])
