import sys
import re
import urllib.request


def main():
    webpage = urllib.request.urlopen(sys.argv[1])
    mybytes = webpage.read()
    webpage_str = mybytes.decode('utf8')

    hrefs = re.findall('href="[^"]+"', webpage_str)
    emails = re.findall(r'[\w\.-]+@[\w\.-]+', webpage_str)

    links = []

    for i in hrefs:
        links.append(i[i.index("\"")+1:len(i)-1])

    print("Linkovi:")
    for l in links:
        if l.startswith("#") or l.startswith("javascript"):
            continue
        if l.startswith("/"):
            l = sys.argv[1]
        if sys.argv[1] in l:
            continue
        print(l)

    hosts = {}

    for link in links:
        if link.startswith("#") or link.startswith("javascript"):
            continue
        if link.startswith("/"):
            link = sys.argv[1]
        link = link.replace("http://", "")
        link = link.replace("https://", "")
        link = link.replace("www.", "")
        if "/" in link:
            link = link[:link.index("/")]
        if link in hosts:
            hosts[link] += 1
        else:
            hosts[link] = 1
    for k, v in hosts.items():
        print("Host: " + str(k) + " Broj referenciranja: " + str(v))

    print("Emailovi:")
    for e in emails:
        print(e)

    print("Linkova na slike ima:", str(len(re.findall(r'<img([\w\W]+?)/>', webpage_str))))



if __name__ == "__main__":
    main()