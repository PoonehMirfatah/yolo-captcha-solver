WEBSITE_CLASSES = [
    "Bicycle",
    "Bridge",
    "Bus",
    "Car",
    "Cross",
    "Hydrant",
    "Motorcycle",
    "Stair",
    "Tlight",
]

ALIASES = {
    "bicycle": "Bicycle",
    "bike": "Bicycle",
    "bridge": "Bridge",
    "bus": "Bus",
    "car": "Car",
    "cross": "Cross",
    "crosswalk": "Cross",
    "cross_walk": "Cross",
    "hydrant": "Hydrant",
    "fire_hydrant": "Hydrant",
    "motorcycle": "Motorcycle",
    "motorbike": "Motorcycle",
    "stair": "Stair",
    "stairs": "Stair",
    "tlight": "Tlight",
    "traffic_light": "Tlight",
    "trafficlight": "Tlight",
}


def normalize_key(name):
    return str(name).strip().lower().replace("-", "_").replace(" ", "_")


def map_class_name(name):
    key = normalize_key(name)

    if name in WEBSITE_CLASSES:
        return name

    return ALIASES.get(key, name)