import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None


def load_saved_artifacts():
    print("Loading saved artifacts...")

    global __data_columns
    global __locations

    import os
    base_path = os.path.dirname(__file__)  # gets server folder path

    with open(os.path.join(base_path, "columns.json"), "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    global __model
    with open(os.path.join(base_path, "model.pkl"), "rb") as f:
        __model = pickle.load(f)

    print("Loading done!")

def get_location_names():
    return __locations


def get_estimated_price(location, sqft, bath, bhk):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)