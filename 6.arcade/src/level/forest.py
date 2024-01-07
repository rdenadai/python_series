import arcade

from ..constants import FOREST_MAP
from .level import Level


class ForestLevel(Level):
    def __init__(self):
        super().__init__()
        # Read in the tiled map
        self.tile_map = arcade.load_tilemap(FOREST_MAP, 1, self.layer_options)
