import tensorflow as tf
from model_goal import ModelGoal
from src.ia.tensorflow_s.sequential_space import SequentialSpace
from src.ia.tensorflow_s.models.multilayer.multilayer_dataset_parser import MultilayerDataParser
from src.ia.tensorflow_s.multilevel.multilevel_sequential_training import MultilevelSequentialTraining

inputs = [
    [ 0.1, 0.3, 0.4, 0.4 ],
    [ 0.8, 0.2, 0.2, 0.6 ],
    [ 0.2, 0.6, 0.4, 0.3 ],
    [ 0.3, 0.8, 0.7, 0.9 ],
    [ 0.1, 0.2, 0.3, 0.2 ],
    [ 0.4, 0.4, 0.9, 0.1 ],
    [ 0.1, 0.3, 0.2, 0.5 ],
    [ 0.5, 0.5, 0.3, 0.3 ],
    [ 0.7, 0.6, 0.2, 0.5 ],
    ]

outputs = [
    [ 0.25, 0.4  ],
    [ 0.5,  0.4  ],
    [ 0.5,  0.35 ],
    [ 0.55, 0.8  ],
    [ 0.15, 0.25 ],
    [ 0.4,  0.5  ],
    [ 0.4,  0.35 ],
    [ 0.5,  0.3  ],
    [ 0.65, 0.35 ],
    ]

args = {
    "inputs": 4,
    "outputs": 2,
    "hidden": [20, 20]
    }

compileArgs = {
    'optimizer': tf.keras.optimizers.Adamax(learning_rate=1e-3),
    'loss': tf.keras.losses.MeanSquaredError(),
    'metrics': [tf.keras.metrics.MeanSquaredError()]
}

fitArgs = {
    'epochs': 100,
    'batchSize': 32
}

iters = 10

goal = ModelGoal(inputs, outputs)

def sample4():
    layers = [
        tf.keras.layers.Dense(units=args['inputs'], input_shape=(args['inputs'],)), # input layer
        tf.keras.layers.Dense(units=20 ), # hidden layer 1
        tf.keras.layers.Dense(units=20 ), # hidden layer 2
        tf.keras.layers.Dense(units=args["outputs"]) # output layer
        ]
    space = SequentialSpace(layers)
    parser =  MultilayerDataParser(2)
    training = MultilevelSequentialTraining(goal, parser, compileArgs, fitArgs,iters)
    model = training.apply(space)
    print('> outputs: '+str(outputs))
    print("> predictions: "+str(model.apply(inputs)))
    

sample4()
