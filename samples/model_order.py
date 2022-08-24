from typing import List
from src.sort.order import Order

class ModelOrder(Order[List]):

    def compare(one, two):
        avg =[0,0]
        for i in range(len(one)):
            avg[0] += one[i]/len(one)
            avg[1] += two[i]/len(two)
        if abs(avg[0]-avg[1]) < 1e-9:
            return 0
        if (avg[0]<avg[1]):
            return 1
        return -1

    def equals(one, two):
        for i in range(len(one)):
            if abs(one[i] - two[i]) > 1e-9:
                return False
        return True
