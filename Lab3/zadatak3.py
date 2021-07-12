import codecs
import sys
import os


def main():
    all_files = os.listdir(sys.argv[1])
    student_data = {}
    with codecs.open(sys.argv[1] + "/studenti.txt", 'r', 'utf-8') as file:
        for line in file.readlines():
            splitted_line = line.split()
            student_data[splitted_line[0]] = splitted_line[1] + ", " + splitted_line[2]
        print(student_data)
    student_results = {}
    student_results.update(student_data)
    for k in student_results:
        student_results[k] = [0.0,0.0,0.0]
    for filename in all_files:
        if "Lab_" not in filename:
            continue
        filename_splitted = filename.split("_")
        lab_name = filename_splitted[0][0] + filename_splitted[1][1]
        with open(sys.argv[1] + filename, 'r') as file:
            for line in file.readlines():
                splitted_line = line.split()
                if student_results[splitted_line[0]][int(lab_name[1])-1] != 0:
                    raise Warning("Prepisivanje podataka")
                student_results[splitted_line[0]][int(lab_name[1])-1] = float(splitted_line[1])

    print ("{:<10} {:<25} {:<5} {:<5} {:<5}".format('JMBAG','Prezime, Ime','L1','L2', 'L3'))
    for k, v in student_results.items():
        lab1, lab2, lab3 = v
        if lab1 == 0:
            lab1 = '-'
        if lab2 == 0:
            lab2 = '-'
        if lab3 == 0:
            lab3 = '-'
        name = student_data[k]
        print("{:<10} {:<25} {:<5} {:<5} {:<5}".format(k, name, lab1, lab2, lab3))


if __name__ == "__main__":
    main()