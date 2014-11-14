#!/usr/bin/env python

import math, random

def main():
    points = read_in_points()
    c1 = [2, 3.5]
    c2 = [.5, 1]

    C1Points, C2Points = iterateKmeans(c1, c2, points)

def read_in_points():
    points = set()
    dataFile = open('data.csv', 'r')
    line = dataFile.readline()
    while (line):
        line_list = line.split(",")
        line_list[0] = float(line_list[0])
        line_list[1] = float(line_list[1])

        #add to list of points
        points.add((line_list[0], line_list[1]))
        line = dataFile.readline()
    dataFile.close()
    return points

def iterateKmeans(c1, c2, points):
    C1Points = set()
    C2Points = set()
    change = True
    while (change):
        C1PointsNew = set()
        C2PointsNew = set()
        for point in points:
            disC1 = dis(point, c1)
            disC2 = dis(point, c2)
            if (disC1 > disC2):
                C1PointsNew.add(point)
            else:
                C2PointsNew.add(point)
        change = (C1PointsNew == C1Points) and (C2PointsNew == C2Points)
        C1Points = C1PointsNew
        C2Points = C2PointsNew
    return C1Points, C2Points


def dis(point1, point2):
    dis1 = point1[0] - point2[0]
    dis2 = point1[1] - point2[1]
    return math.sqrt((dis1)**2 + (dis2)**2)
