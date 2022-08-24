from math import sqrt
from typing import List
from src.ia.train.training_goal import TrainingGoal
from src.ia.train.dataset import Dataset
from model_order import ModelOrder

class ModelGoal(TrainingGoal[List[List],List[List],List]):
    
    def __init__(self,inputs:List[List],outputs:List[List],name='ModelGoal') -> None:
        super().__init__(name, Dataset(inputs,outputs), ModelOrder)
    
    def getTrainingSet(self) -> Dataset[List[List],List[List]]:
        return self.dataset
    
    def evaluate(self,outputs: List[List], predictions: List[List]) -> List:
        result = []
        for i in range(len(outputs[0])):
            sum=0
            for j in range(len(outputs)):
                sum += (outputs[j][i] - predictions[j][i]) * (outputs[j][i] - predictions[j][i])
            result.append(sqrt(sum/len(outputs)))
        return result

    def init(self)->None:
        pass