class Level:
    def __init__(self):
        # Layer specific options are defined based on Layer names in a dictionary
        # Doing this will make the SpriteList for the platforms layer
        # use spatial hashing for detection.
        self.layer_options = {
            "ground1": {
                "use_spatial_hash": True,
            },
        }
