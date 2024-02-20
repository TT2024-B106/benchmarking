import json
import random

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
