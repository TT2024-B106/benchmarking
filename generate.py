import os
import json
import random

from datetime import datetime

def trajectory(size: int) -> list[object]:
    """Generate trajectory as a collection of Points (features).

    size: The size of the trajectory.
    """
    features = []

    for i in range(size):
        feature = {"type": "Feature", "properties": {}}

        x = random.uniform(-99.0 + i, -100.0 + i)
        y = random.uniform(19.0, 20.0)
        feature["geometry"] = {"coordinates": [x, y], "type": "Point"}

        features.append(feature)

    return features

def geojson(features: int) -> object:
    """Generate geojson dict.

    features: The number of features (trajectories).
    """
    feature_collection = {
            "type": "FeatureCollection",
            "features": trajectory(features)
    }

    return feature_collection

def geojson_file(pairs: int, target_dir="generated", filename="") -> None:
    """
    Generate a geojson file with a given number of pair points.

    :param pairs: The number of pair points (tuples).
    :param target_dir str: The target directory where it will be saved.
    """
    # Create the directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)

    # Create the full path to the file
    if filename == "":
        nowstr = datetime.now().strftime("%y%m%d%H%M%S")
        filename = "t" + nowstr + "_p" + str(pairs) + ".json"
    elif filename[-5:] != ".json":
        filename += ".json"

    filepath = os.path.join(target_dir, filename)

    with open(filepath, "w") as file:
        json.dump(geojson(pairs), file)

def geojson_files(files: int, target_dir="generated") -> None:
    """
    Generate a number of geojson files that will create from 1 to `files`
    number of features for each file. I.e.: 1.json, 2.json, ..., `files`.json;
    where these numbers will represent the number of features that each file
    has.

    :param files: The number of files to be created.
    :param target_dir str: The target directory where it will be saved.
    """
    # Create directories if they do not exist
    nowstr = datetime.now().strftime("%y%m%d%H%M%S")
    dirpath = target_dir + "/" + nowstr
    os.makedirs(dirpath, exist_ok=True)

    for i in range(1, files+1):
        geojson_file(i, dirpath, str(i))
