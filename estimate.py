from learn import isFloat

if __name__ == "__main__":
    try:
        f = open("log", "r")
    except:
        exit("no log file found, did you trained your model first ?");
    data = f.read().splitlines()
    if (len(data) is not 2):
        exit("wrong number of variable provided in log file")
    if not isFloat(data[0]) or not isFloat(data[1]):
        exit("wrong format found in log file")
    b = float(data[1])
    a = float(data[0])

    while True:
        x = input("Provide a value for x: ")
        if not isFloat(x):
            print("You must specify a valid value for x")
        else:
            print(str((a * float(x)) + b))
