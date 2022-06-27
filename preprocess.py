
from datetime import date
from datetime import datetime
from sklearn.preprocessing import MinMaxScaler
import numpy as np


def preprocess_input(d) : 

    '''Preprocess user input
    Argument :
    d -- dictionary

    Returns : 
      a list of process output 
    '''

    features = []
    for key, val in d.items() :
            features.append(val)

    return features


