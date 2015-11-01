import matplotlib.pyplot as plot
import numpy
import numpy.random as rand
from enum import Enum


class Entry:
    def __init__(self, x, y, type=None):
        self.x = x
        self.y = y
        self.type = type

    def get_coord(self):
        return (self.x, self.y)

    def init_multiple(Xs, Ys, type=None):
        entries = []
        for coord in zip(Xs, Ys):
            entries.append(Entry(coord[0], coord[1], type))
        return entries

    def getXs(entries):
        Xs = []
        for entry in entries:
            Xs.append(entry.x)
        return Xs

    def getYs(entries):
        Ys = []
        for entry in entries:
            Ys.append(entry.y)
        return Ys


class Type(Enum):
    A = 1
    B = 0

    def from_value(value):
        return Type.A if value > 0 else Type.B

class Perceptron:
    BEGINNING_OF_THE_LIST = 0
    NEUTRAL_WAGE = 1

    hypothesis = []

    def __init__(self, wages):
        self.hypothesis = wages

    def process(self, entry):
        data = [entry.x, entry.y]
        data.insert(self.BEGINNING_OF_THE_LIST, self.NEUTRAL_WAGE)
        return Type.from_value(numpy.dot(self.hypothesis, data))

    def learn(self, missclasified_entry):
        numpy.add(self.hypothesis + missclasified_entry.value * self.hypothesis)

def plotAll(A, B, P):
    fig = plot.figure()
    plot.scatter(Entry.getXs(A), Entry.getYs(A), color='red')
    plot.scatter(Entry.getXs(B), Entry.getYs(B), color='green')
    fig.show()
    plot.show()

x = numpy.linspace(0, 10)
groupA = Entry.init_multiple(x, rand.random(50),Type.A)
groupB = Entry.init_multiple(x, rand.random(50) + 5, Type.B)

p = Perceptron([1, 1, 1])

for entry in groupA + groupB:
    if p.process(entry) != entry.type:
        p.learn(entry)

print("aa")