# day 7 advent of code 2024

def P1(f):
    validResults = []
    for equation in f:
        result, values = equation.split(":")
        validResults.append(CheckEquation(
            int(result), [int(v) for v in values.strip().split(" ")], ['+', '*']))
    return sum(validResults)

def P2(f):
    validResults = []
    for equation in f:
        result, values = equation.split(":")
        validResults.append(CheckEquation(
            int(result), [int(v) for v in values.strip().split(" ")], ['+', '*', '||']))
    return sum(validResults)

# Produces a list of all possible results of the combinations of operands and operators
def CheckEquation(result, operands, operators):
    results = []
    for operand in operands:
        if (results == []):
            results.append(operand)
            continue
        newResults = []
        for operator in operators:
            for i in range(len(results)):
                if (operator == '+'):
                    newResults.append(results[i]+operand)
                if (operator == '*'):
                    newResults.append(results[i]*operand)
                if (operator == '||'):
                    newResults.append(int(str(results[i])+str(operand)))
        results = newResults
    if result in results:
        return result
    return 0

f = open("resources\day07.txt", "r")
print(f"Day 7/1: {P1(f)}")
f.close()
f = open("resources\day07.txt", "r")
print(f"Day 7/2: {P2(f)}")
f.close()
