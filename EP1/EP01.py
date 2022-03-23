#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import random
#Escreva seu nome e numero USP
INFO = {10336581:"Gabriel Brogota Lobo Durante"}

class Point():
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

def generate_points(n):
    points = []
    for index in range(n):
        points.append(Point(
            x=random.uniform(-1, 1),
            y=random.uniform(-1, 1)
        ))

    return points

def test_point(point):
    mod = point.x**2 + point.y**2

    return 1 if mod < 1 else 0

def get_proportion(points):
    n = len(points)

    sum = 0
    for point in points:
        sum += test_point(point)
    
    return (1/n)*sum

def estima_pi(Seed = None):

    random.seed(Seed)
    #random.random() gera um numero com distribuicao uniforme em (0,1)
    """
    Esta funcao deve retornar a sua estimativa para o valor de PI
    Escreva o seu codigo nas proximas linhas
    """
    
    # Params
    maxN = 50000 # Máximo de iterações
    area = 2**2 # Aŕea total. Com pontos no intervalo [-1, 1], possui lado = 2
    precision = 0.0005 # Precisão de 0.05%

    points = generate_points(1)
    lastProportion = get_proportion(points) * area

    n = 100
    shouldCalculate = True
    while(shouldCalculate and n <= maxN):
        points = generate_points(n)
        p = get_proportion(points)

        currentProportion = p*area
        if abs((math.pi - currentProportion)/math.pi) < precision :
            shouldCalculate = False
            print(f"O valor foi obtido com precisão {abs((lastProportion - currentProportion)/lastProportion)*100}% para n={n}")

        lastProportion = currentProportion
        n += 1

    return lastProportion

print(estima_pi())