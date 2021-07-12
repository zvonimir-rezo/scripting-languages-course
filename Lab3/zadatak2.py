import sys


def calc(q, lines):
    m = []
    for line in lines:
        l = []
        splitted_line = line.split()
        float_list = sorted(list(map(float, splitted_line)))
        for i in range(1, 10):
            l.append(float_list[int(len(splitted_line) * (q*i)) - 1])
        m.append(l)
    return m


def main():
    end_str = "Hyp#Q10#Q20#Q30#Q40#Q50#Q60#Q70#Q80#Q90\n"
    with open(sys.argv[1], 'r') as file:
        m = calc(0.1, file.readlines())
    for i in range(len(m)):
        end_str += "{:0>3d}".format(i+1) + "#"
        end_str += "#".join("{0:.1f}".format(x) for x in m[i]) + "\n"
    print(end_str)


if __name__ == "__main__":
    main()