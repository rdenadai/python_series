from arcade import AnimatedTimeBasedSprite, AnimationKeyframe, load_texture

from .constants import CHARACTERS_ATTACK_TIMER, CHARACTERS_LIFE, SPRITE_SCALING


def load_sprite(filename, tile_max_w, tile_w, tile_h):
    return [
        AnimationKeyframe(
            tile_id=tile_id,
            duration=128,
            texture=load_texture(
                file_name=filename,
                **{
                    "x": x,
                    "y": 0,
                    "width": tile_w,
                    "height": tile_h,
                },
            ),
        )
        for tile_id, x in enumerate((x_ for x_ in range(0, tile_max_w, tile_w)))
    ]


class Character(AnimatedTimeBasedSprite):
    def __init__(self, movement_speed, image_width, image_height):
        super().__init__(scale=SPRITE_SCALING, image_width=image_width, image_height=image_height)
        self.life = CHARACTERS_LIFE
        self.movement_speed = movement_speed
        self.going_left = False
        self.hit_box = None
        self.is_on_ground = True
        self.is_jumping = False
        self.is_walking = False
        self.is_attacking = False
        self.attack_timer = CHARACTERS_ATTACK_TIMER
        self.attack_hit_box = {
            "right": [
                (0, -50),
                (100, -50),
                (100, 50),
                (0, 50),
            ],
            "left": [
                (-100, -50),
                (0, -50),
                (0, 50),
                (-100, 50),
            ],
        }

    def load_assets(self, assets):
        for asset in ("idle", "walk", "jump", "attack", "idle_left", "walk_left", "jump_left", "attack_left"):
            if load := assets.get(asset, None):
                setattr(self, f"{asset}_animation", load_sprite(*load))
        self.idle()

    def reset(self):
        self.life = CHARACTERS_LIFE
        self.is_on_ground = True
        self.is_jumping = False
        self.is_walking = False
        self.is_attacking = False
        self.attack_timer = CHARACTERS_ATTACK_TIMER
        self.idle()

    def idle(self):
        self.cur_frame_idx = 0
        self.frames = self.idle_left_animation if self.going_left else self.idle_animation
        self.hit_box = self.frames[0].texture.hit_box_points

    def walk(self):
        self.cur_frame_idx = 0
        self.frames = self.walk_left_animation if self.going_left else self.walk_animation
        self.hit_box = self.frames[0].texture.hit_box_points

    def jump(self):
        self.cur_frame_idx = 0
        self.frames = self.jump_left_animation if self.going_left else self.jump_animation
        self.hit_box = self.frames[0].texture.hit_box_points

    def attack(self):
        self.cur_frame_idx = 0
        self.frames = self.attack_left_animation if self.going_left else self.attack_animation
        self.set_hit_box(self.attack_hit_box["left"] if self.going_left else self.attack_hit_box["right"])

    def update_state(self):
        if self.is_attacking and self.is_on_ground and not self.is_jumping:
            self.attack()
        elif self.is_on_ground and self.is_walking and not self.is_jumping:
            self.walk()
        elif not self.is_on_ground and self.is_jumping:
            self.jump()
        elif self.is_on_ground and not self.is_jumping and not self.is_walking:
            self.idle()
