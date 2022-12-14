[![banner](https://media-exp1.licdn.com/dms/image/C561BAQFjPq3pi-mgZQ/company-background_10000/0/1540323628962?e=2159024400&v=beta&t=dELqmM_LCU2nVT1oJiLNqBY-xahFJ40mLOiIcOg5odw)](https://itrmachines.com)

<h1 align="center">Oceanai-py</h1>

> Wrapper library that allows a direct integration between the Ocean marketplace and artificial intelligence tools like tensorflow


With Oceanai-py, you can:

- **Create** artificial intelligence models: the current state of the library uses [Tensorflow](https://pypi.org/project/tensorflow/) for the implementation of the AI models, anything that you can do with [Tensorflow](https://pypi.org/project/tensorflow/)  you can also do it with **Oceanai-py** 


- **Buy** OCEAN marketplace datasets to use them on your models
- **Consume** OCEAN datatokens, to access the services of the Ocean environment.

Every function related to the OCEAN environment is fullfiled using [Ocean.py](https://github.com/oceanprotocol/ocean.py).
Ocean.py is part of the [Ocean Protocol](https://oceanprotocol.com) toolset.


This library is still in alpha state and you can expect running into problems.

- [📚 Prerequisites](#-prerequisites)
- [🏗 Installation](#-installation)
- [🏄 Quickstart](#-quickstart)
  - [Obtaining Ocean datasets](#obtaining-ocean-datasets)
  -  [📖 Learn More](#learn-more)
- [⬆️ Releases](#️-releases)
- [🏛 License](#-license)



## 📚 Prerequisites

- Python (recomended version 3.9) ([Install from here](https://www.python.org/downloads/))

## 🏗 Installation

```bash
#Is necesary to install tensorflow  and ocean-lib separately to avoid download errors.
pip install oceanai-py
pip install tensorflow
pip install --pre ocean-lib
```

## 🏄 Quickstart
The source code of this example is also included on the folder samples of the library

**index.py**
This file explains how to implement several types of AI models for the selected Ocean dataset

```py
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

def sample():
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
    

sample()
```

### Obtaining Ocean datasets

In here we will explain how to obtain OCEAN datasets using oceanai-lib. 

```py
from src.ocean.occean import Occean

d = {
   'network' : 'https://rinkeby.infura.io/v3/proyectid',
   'metadataCacheUri' : 'https://v4.aquarius.oceanprotocol.com',
   'providerUri' : 'https://v4.provider.rinkeby.oceanprotocol.com',
}

occean = Occean(d,"private key my account","private key accout buying from")

# create NFT token in the accoutn buying from
data_nft = occean.publishNFTToken('NFTToken1', 'NFT1')
##occean.createDatasetExmple()
# the account we are buying from create the datatoken 
datatoken = occean.createDataToken(data_nft,2)
#datatoken = occean.getDatatoken('token address') we can allso get the datatoken 
#creat exage id an the buy
exange_id = occean.getExchangeId(datatoken,1,3)
tx_result = occean.buy(datatoken,exange_id,1,2)
```

### 📖 Learn more

- [Ocean.py](https://github.com/oceanprotocol/ocean.py) - Library for accessing to the OCEAN services
- [Tensorflow.js](https://pypi.org/project/tensorflow/) - Tensorflow AI library.

## ⬆️ Releases

Coming soon.


## 🏛 License

```
Copyright ((C)) 2021 Intelligent Trading Machines

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
