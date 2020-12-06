
operators = {
    "(": 20,
    "*": 5,
    "/": 5,
    "+": 6,
    "-": 6,
    "^": 4,
    ",": 17
}


class AlgoTreeNode:

    def __init__(self, op="", le=None, r=None):
        self.operator = op
        self.left = le
        self.right = r
        pass

    def __str__(self):
        le = self.left
        r = self.right

        if le is None:
            le = ""
        else:
            le = "(" + str(le)
        if r is None:
            r = ""
        else:
            r = str(r) + ")"

        return str(le) + " " + self.operator + " " + str(r)

    def printTree(self, i=1):
        print(str(self.left) + " " + self.operator + " " + str(self.right))

    def update(self, algo):
        existing = str(self.left) + " " + self.operator + " " + str(self.right)
        existing = existing.replace("( ", "(")
        existing = existing.replace(" )", ")")
        if algo[0] in operators and algo[0] != "(":
            if algo[0] != " ":
                algo = " " + algo
            new = existing + algo
        else:
            new = existing + ", " + algo

        return buildTree(new)


def pal(algo):
    algo = algo.split()
    output = []
    number = ""
    count = 0
    comma = 0

    for i in algo:
        if i in operators or i == ")":
            output.append(i)
            pass
        else:
            number = number + i
            count = 1
            pass

        if count == 1:
            if number[-1] == ",":
                number = number.replace(",", "")
                comma = 1
            if number[0] == "(":
                while number[0] == "(":
                    output.append("(")
                    number = number[1:]
            if number[-1] == ")":
                output.append(number.replace(")", ""))
                for i in number:
                    if i == ")":
                        output.append(")")
                count = 0

            if comma == 1:
                output.append(",")
                comma = 0
            if count == 1:
                output.append(number)
            number = ""
            count = 0

    return output
    pass


def algorithmParser(algo):
    stack = []
    output = []

    algo = pal(algo)

    for i in algo:
        # build postfix
        if i in operators and i != "(":
            stack.append(i)
            ind = len(stack) - 1
            while ind > 0:
                for y in range(0, len(stack)-1):
                    if operators[stack[y]] < operators[i]:
                        output.append(stack.pop(y))
                        ind = -1
                    else:
                        # output.append(stack.pop())
                        ind -= 1
            pass

        elif i == ")":
            p = ""
            while p != "(" and len(stack) > 0:
                p = stack.pop()
                if p != "(":
                    output.append(p)

            pass

        elif i == "(":
            stack.append(i)
            pass

        else:
            output.append(i)
        pass

    for i in range(0, len(stack)):
        output.append(stack.pop())

    return output
    pass


def buildexpr(algo):
    exp = []

    for i in range(0, len(algo)):
        if algo[i] in operators:
            right = exp.pop()
            left = exp.pop()
            exp.append(AlgoTreeNode(algo[i], left, right))
            pass
        else:
            exp.append(AlgoTreeNode(algo[i]))

    return exp
    pass


def buildTree(algo):
    return buildexpr(algorithmParser(algo))[0]


if __name__ == "__main__":
    al = "4 + (5 * 6 + 4 - 5) / 3"
    al2 = "(4 + 5) * 6 + 4 - 5 / 3"
    al3 = "4 + 5 * 6 + (4 - 5) / 3"
    al4 = "4 + 5 * 6 + 4 - 5 / 3"
    al5 = "4 * 4 * 4 * 4"
    buildTree(al).printTree()
    buildTree(al2).printTree()
    buildTree(al3).printTree()
    buildTree(al4).printTree()
    buildTree(al5).printTree()
    buildTree(al5).update("* 4 + 54 / 63 ^ 4").printTree()
