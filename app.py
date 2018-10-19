import math as m
import sys


class Rule(object):
    def __init__(result, body):
        self.result = result
        self.body = body

    def __str__(self):
        if (len(self.body) > 0):
            string = ""
            for i in range(len(self.body)-1):
                string = string + self.body[i] + " ∧ "
            string = string + self.body[len(self.body)-1]
            return string + " -> " + self.result
        else:
            return self.result


# Taking in inputs
if len(sys.argv) == 2:
    in_file = open(sys.argv[1], "r")
else:
    sys.exit("ERROR: Wrong number of arguments")

# Converting file into rules
i = 0
rules = []
print("My rules and facts are..\n")
for line in in_file:
    line = line.replace("(", "")
    line = line.replace(")", "")
    line = line.replace("[", "")
    line = line.replace("]", "")
    line = line.replace("\n", "")
    line = line.replace(" ", "")
    arr = line.split(",")
    rule = Rule(arr[0], arr[1:])
    rules.append(rule)
    i += 1
    print(rule)

