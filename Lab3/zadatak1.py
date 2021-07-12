import sys

def main():
    try:
        resurs = sys.argv[1]
        adrese = {}
        p = sys.argv[2]
        with open(p, 'r') as file:
            lines = file.readlines()
            for line in lines:
                splitted_line = line.split()
                if resurs in splitted_line:
                    splitted_address = splitted_line[0].split('.')
                    prva_dva = ".".join(splitted_address[:2])
                    print(prva_dva)
                    if prva_dva not in adrese.keys():
                        adrese[prva_dva] = 1
                    else:
                        adrese[prva_dva] += 1
    except IndexError:
        print("Potrebno je za prvi argument unijeti resurs, a za drugi argument putanju do log datoteke.")
        exit(0)

    print("-------------------------")
    print("Broj pristupa stranici: " + resurs)
    print("  IP podmreza : Broj pristupa")
    print("-------------------------")

    sortirano = dict(sorted(adrese.items(), key=lambda x: x[1], reverse=True))
    for k, v in sortirano.items():
        if v > 1:
            print('%9s.*.* :%3d' % (k, v))

main()