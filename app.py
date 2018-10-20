import sys


class Rule(object):
    def __init__(self, result, body):
        self.result = result
        self.body = body
        self.searched = False
        if len(body) == 0:
            self.truth_value = True
        else:
            self.truth_value = False

    def __str__(self):
        if len(self.body) > 0:
            string = ""
            for i in range(len(self.body)-1):
                string = string + self.body[i] + " ∧ "
            string = string + self.body[len(self.body)-1]
            return string + " -> " + self.result
        else:
            return self.result


def backward_chaining(goals, rules):
    if len(goals) == 0:
        return True
    else:
        head = goals[0]
        goals = goals[1:]
        for r in rules:
            if r.result == head:
                # Copy goal elements into temp array
                temp = []
                for el in goals:
                    temp.append(el)
                temp.extend(r.body)

                if backward_chaining(temp, rules):
                    # Add to true values
                    return True
        return False


# Taking in inputs
if len(sys.argv) == 2:
    in_file = open(sys.argv[1], "r")
else:
    sys.exit("ERROR: Wrong number of arguments")

# Converting file into rules
rule_arr = []
print("My rules and facts are..")
for line in in_file:
    line = line.replace("(", "")
    line = line.replace(")", "")
    line = line.replace("[", "")
    line = line.replace("]", "")
    line = line.replace("\n", "")
    line = line.replace(" ", "")
    arr = line.split(",")
    rule = Rule(arr[0], arr[1:])
    rule_arr.append(rule)
    print(rule)


# Take input from user
while True:
    atom = str(input("Please enter an atom.\n"))
    if atom == "exit":
        exit(0)
    goal = [atom]
    print("I will search for " + str(goal[0]))
    res = backward_chaining(goal, rule_arr)
    if res:
        print(atom + " is a logical consequence of the set of rules.")
    else:
        print("Unable to reach " + atom)


