import os

SPRITE_SCALING = 2.5

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_TITLE = "Mythic Brawls"

FOREST_MAP = f"{os.getcwd()}/6.arcade/src/assets/stages/stage1_forest.tmx"

SOUNDS = {
    "sword": f"{os.getcwd()}/6.arcade/src/assets/sounds/sword.mp3",
    "background": f"{os.getcwd()}/6.arcade/src/assets/sounds/background.mp3",
}

PLAYERS_INITIAL_POSITION = {
    "player1": (140, 130),
    "player2": (SCREEN_HEIGHT - 140, 130),
}

CHARACTERS_LIFE = 10
CHARACTERS_LIFE_HIT = 1
CHARACTERS_ATTACK_TIMER = 0.5  # seconds

CHARACTERS_MOVES = ("idle", "idle_left", "walk", "walk_left", "jump", "jump_left", "attack", "attack_left")

CHARACTERS = {
    "dark_knight": {
        "movement_speed": 1500,
        "image_width": 170,
        "image_height": 170,
        "idle": (f"{os.getcwd()}/6.arcade/src/assets/DarkKnight/Sprites/Idle.png", 1700, 170, 170),
        "idle_left": (f"{os.getcwd()}/6.arcade/src/assets/DarkKnight/Sprites/IdleLeft.png", 1700, 170, 170),
        "walk": (f"{os.getcwd()}/6.arcade/src/assets/DarkKnight/Sprites/Walk.png", 1360, 170, 170),
        "walk_left": (f"{os.getcwd()}/6.arcade/src/assets/DarkKnight/Sprites/WalkLeft.png", 1360, 170, 170),
        "jump": (f"{os.getcwd()}/6.arcade/src/assets/DarkKnight/Sprites/Jump.png", 510, 170, 170),
        "jump_left": (f"{os.getcwd()}/6.arcade/src/assets/DarkKnight/Sprites/JumpLeft.png", 510, 170, 170),
        "attack": (f"{os.getcwd()}/6.arcade/src/assets/DarkKnight/Sprites/Attack1.png", 680, 170, 170),
        "attack_left": (f"{os.getcwd()}/6.arcade/src/assets/DarkKnight/Sprites/AttackLeft.png", 680, 170, 170),
    },
    "martial_hero": {
        "movement_speed": 2000,
        "image_width": 200,
        "image_height": 200,
        "idle": (f"{os.getcwd()}/6.arcade/src/assets/MartialHero/Sprites/Idle.png", 800, 200, 200),
        "idle_left": (f"{os.getcwd()}/6.arcade/src/assets/MartialHero/Sprites/IdleLeft.png", 800, 200, 200),
        "walk": (f"{os.getcwd()}/6.arcade/src/assets/MartialHero/Sprites/Walk.png", 1600, 200, 200),
        "walk_left": (f"{os.getcwd()}/6.arcade/src/assets/MartialHero/Sprites/WalkLeft.png", 1600, 200, 200),
        "jump": (f"{os.getcwd()}/6.arcade/src/assets/MartialHero/Sprites/Jump.png", 400, 200, 200),
        "jump_left": (f"{os.getcwd()}/6.arcade/src/assets/MartialHero/Sprites/JumpLeft.png", 400, 200, 200),
        "attack": (f"{os.getcwd()}/6.arcade/src/assets/MartialHero/Sprites/Attack1.png", 800, 200, 200),
        "attack_left": (f"{os.getcwd()}/6.arcade/src/assets/MartialHero/Sprites/AttackLeft.png", 800, 200, 200),
    },
    "medieval_warrior": {
        "movement_speed": 1000,
        "image_width": 135,
        "image_height": 135,
        "idle": (f"{os.getcwd()}/6.arcade/src/assets/MedievalWarrior/Sprites/Idle.png", 1350, 135, 135),
        "idle_left": (f"{os.getcwd()}/6.arcade/src/assets/MedievalWarrior/Sprites/IdleLeft.png", 1350, 135, 135),
        # "walk": (f"{os.getcwd()}/6.arcade/src/assets/DarkKnight/Sprites/Walk.png", 1360, 135, 135),
        # "walk_left": (f"{os.getcwd()}/6.arcade/src/assets/DarkKnight/Sprites/WalkLeft.png", 1360, 135, 135),
        # "jump": (f"{os.getcwd()}/6.arcade/src/assets/DarkKnight/Sprites/Jump.png", 510, 135, 135),
        # "jump_left": (f"{os.getcwd()}/6.arcade/src/assets/DarkKnight/Sprites/JumpLeft.png", 510, 135, 135),
    },
}
