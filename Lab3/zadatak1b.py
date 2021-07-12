import sys


def extract_from_file(lines):
    values1 = []
    values2 = []
    empty_line = False
    for line in lines:
        if line == "\n":
            empty_line = True
            continue
        splitted_line = line.split()
        if empty_line:
            if len(splitted_line) == 2:
                if int(splitted_line[0]) < 1 or int(splitted_line[1]) < 1:
                    raise ValueError
                dim2 = (int(splitted_line[0]), int(splitted_line[1]))
            elif len(splitted_line) == 3:
                if int(splitted_line[0]) < 0 or int(splitted_line[0]) > dim2[0] - 1 or int(splitted_line[1]) < 0 or int(
                        splitted_line[1]) > dim2[1] - 1:
                    raise ValueError
                else:
                    values2.append(list(map(int, splitted_line)))
            else:
                raise ValueError
        else:
            if len(splitted_line) == 2:
                if int(splitted_line[0]) < 1 or int(splitted_line[1]) < 1:
                    raise ValueError
                dim1 = (int(splitted_line[0]), int(splitted_line[1]))
            elif len(splitted_line) == 3:
                values1.append(list(map(int, splitted_line)))
            else:
                raise ValueError
    return dim1, values1, dim2, values2


def from_file(path):
    with open(path, 'r') as file:
        return extract_from_file(file.readlines())


def add_to_dict(dim, values):
    d = dict()
    for i in range(dim[0]):
        row = []
        added = False
        for k in range(dim[1]):
            for j in values:
                if i == j[0] and k == j[1]:
                    row.append(j[2])
                    added = True
                    break
            if not added:
                row.append(0)
            added = False
        d[i] = row
    return d


def rez_str(m):
    end_str = str(len(m)) + " " + str(len(m[0])) + "\n"
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] != 0:
                end_str += str(i) + " " + str(j) + " " + str(float(m[i][j])) + "\n"
    return end_str + "\n"


def make_str(name, m):
    end_str = name + ":\n"
    for i in range(len(m)):
        for j in range(len(m[i])):
            end_str += " " + str(float(m[i][j]))
        end_str += "\n"
    return end_str


def multiply(d1, d2):
    result = []
    for i in range(len(d1)):
        l = []
        for j in range(len(d2[0])):
            l.append(0)
        result.append(l)

    for i in range(len(d1)):
        for j in range(len(d2[0])):
            for k in range(len(d2)):
                result[i][j] += d1[i][k] * d2[k][j]
    print(make_str("A", d1))
    print(make_str("B", d2))
    print(make_str("A*B", result))

    str_result = rez_str(result)

    return str_result


def main():
    dim1, values1, dim2, values2 = from_file(sys.argv[1])

    dict1 = add_to_dict(dim1, values1)
    dict2 = add_to_dict(dim2, values2)

    with open(sys.argv[2], 'w') as file:
        file.write(multiply(dict1, dict2))


if __name__ == "__main__":
    main()