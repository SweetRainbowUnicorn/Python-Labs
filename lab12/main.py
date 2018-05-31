import re


if __name__ == "__main__":

    pattern = "([1-8][0-9]|90)(\.[0-9]{2,3}){3}.*(GET|POST).*200"
    amount = 0
    with open("log.txt") as file:
        for line in file:
            if re.match(pattern, line):
                amount += 1
                print(line)

    print("\nMatched requests: %d" % amount)
