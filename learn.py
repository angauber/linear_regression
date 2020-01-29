import csv
import argparse
from sys import exit
from operator import sub
from numpy import linspace
from numpy import array as npArray
from matplotlib import pyplot

def isFloat(val):
    try:
        float(val)
        return True
    except:
        return False

def readFile(fileName):
    dataX = []
    dataY = []

    with open(fileName) as file:
        reader = csv.reader(file, delimiter=',')
        lineCount = 0
        for row in reader:
            if len(row) != 2:
                exit("error: expected two columns per row on line " + str(lineCount))
            if lineCount == 0:
                dataName = row
            else:
                if not isFloat(row[0]) or not isFloat(row[1]):
                    exit("error: unexpected digit on line " + str(lineCount))
                else:
                    dataX.append(float(row[0]))
                    dataY.append(float(row[1]))
            lineCount += 1
    return dict([('dataName', dataName), ('xSet', dataX), ('ySet', dataY)])

def writeLog(a, b):
    f = open("log", "w")
    f.write(str(b)+"\n"+str(a)+"\n")
    f.close()

def compute(data):
    m = len(data['xSet'])

    a = 0.0
    b = 0.0
    xArr = data['xSet']
    yArr = data['ySet']

    for e in range(args.epoch):
        try:
            computedY = [((a * x) + b) for x in xArr]
    
            cost = (1/ (2 * m)) * (sum([computedY[i] - yArr[i] for i in range(m)]) ** 2)

            bGrad = (1 / m) * sum([(computedY[i] - yArr[i]) for i in range(m)])
            aGrad = (1 / m) * sum([(xArr[i] * (computedY[i] - yArr[i])) for i in range(m)])
        
            b -= (0.01 * bGrad)
            a -= (args.rate * aGrad)
        except:
            exit("To large value encountered. exiting")
    if args.visualise:
        visualise(data, a, b)
    print("error: "+str(cost))
    print("y = "+str(a)+" x + "+str(b))
    writeLog(a, b)

def visualise(data, a, b):
    figure = pyplot.figure()

    ax = figure.subplots()
    ax.scatter(data['xSet'], data['ySet'])
    ax.set_xlabel(data['dataName'][0])
    ax.set_ylabel(data['dataName'][1])
    ax.set_title("point visualisation")

    x = linspace(npArray(data['xSet']).min(), npArray(data['xSet']).max(), 100)
    y = (a * x) + b
    ax.plot(x, y, '-r')

    pyplot.grid()
    pyplot.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset", help="your dataset file in csv format")
    parser.add_argument("-r", "--rate", type=float, default="0.0001", help="set the learning rate, defaul: 0.01")
    parser.add_argument("-e", "--epoch", type=int, default="1000", help="set the epoch number, default: 4")
    parser.add_argument("-v", "--visualise", action="store_true", help="get a visual feedback")
    global args

    args = parser.parse_args()
    data = readFile(args.dataset)
    compute(data)
