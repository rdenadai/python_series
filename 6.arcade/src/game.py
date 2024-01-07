import arcade

from .constants import (
    CHARACTERS,
    CHARACTERS_ATTACK_TIMER,
    CHARACTERS_LIFE_HIT,
    CHARACTERS_MOVES,
    PLAYERS_INITIAL_POSITION,
    SCREEN_HEIGHT,
    SCREEN_TITLE,
    SCREEN_WIDTH,
    SOUNDS,
)
from .level.forest import ForestLevel
from .sprite import Character


class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.game_over = False

        # Our Scene Object
        self.scene = None
        # Our physics engine
        self.physics_engine = None

        # Since this is a fighting game
        self.player1 = None
        self.player2 = None

        self.level = None
        self.screen_boundary = {"left": None, "right": None}
        self.general_sound = {"on": True, "player": None}

        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        self.level = ForestLevel()

        self.scene = arcade.Scene.from_tilemap(self.level.tile_map)

        # Sounds
        self.audio_sword = arcade.sound.load_sound(SOUNDS["sword"])
        self.audio_background = arcade.sound.load_sound(SOUNDS["background"])

        # Lateral Walls
        self.screen_boundary["left"] = arcade.SpriteSolidColor(1, SCREEN_HEIGHT * 2, arcade.color.BLACK)
        self.screen_boundary["left"].center_x = 1
        self.screen_boundary["left"].center_y = 0
        self.scene.add_sprite("boundary_left", self.screen_boundary["left"])
        self.screen_boundary["right"] = arcade.SpriteSolidColor(1, SCREEN_HEIGHT * 2, arcade.color.BLACK)
        self.screen_boundary["right"].center_x = SCREEN_WIDTH - 1
        self.screen_boundary["right"].center_y = 0
        self.scene.add_sprite("boundary_right", self.screen_boundary["right"])

        # -- Player 1 --
        self.player1 = Character(
            movement_speed=CHARACTERS["dark_knight"]["movement_speed"],
            image_width=CHARACTERS["dark_knight"]["image_width"],
            image_height=CHARACTERS["dark_knight"]["image_height"],
        )
        self.player1.center_x = 140
        self.player1.center_y = 130
        self.player1.load_assets({k: v for k, v in CHARACTERS["dark_knight"].items() if k in CHARACTERS_MOVES})
        self.scene.add_sprite("player1", self.player1)

        # -- Player 2 --
        self.player2 = Character(
            movement_speed=CHARACTERS["martial_hero"]["movement_speed"],
            image_width=CHARACTERS["martial_hero"]["image_width"],
            image_height=CHARACTERS["martial_hero"]["image_height"],
        )
        self.player2.going_left = True
        self.player2.center_x = SCREEN_WIDTH - 140
        self.player2.center_y = 130
        self.player2.load_assets({k: v for k, v in CHARACTERS["martial_hero"].items() if k in CHARACTERS_MOVES})
        self.scene.add_sprite("player2", self.player2)

        for i in range(1, 10):
            self.scene.add_sprite_list_before(f"back{i}", "player1")
            self.scene.add_sprite_list_before(f"back{i}", "player2")
            self.scene.add_sprite_list_before(f"back{i}", "boundary_left")
            self.scene.add_sprite_list_before(f"back{i}", "boundary_right")

        # Create the 'physics engine'
        self.physics_engine = arcade.PymunkPhysicsEngine(
            damping=1.0,
            gravity=(0, -1500.0),
            maximum_incline_on_ground=0.1,
        )
        self.physics_engine.add_sprite(
            self.player1,
            moment=arcade.PymunkPhysicsEngine.MOMENT_INF,
            mass=2.0,
            friction=1.0,
            elasticity=0.0,
            collision_type="player",
            max_horizontal_velocity=300,
            max_vertical_velocity=1600,
        )
        self.physics_engine.add_sprite(
            self.player2,
            moment=arcade.PymunkPhysicsEngine.MOMENT_INF,
            mass=2.0,
            friction=1.0,
            elasticity=0.0,
            collision_type="player",
            max_horizontal_velocity=300,
            max_vertical_velocity=1600,
        )

        self.physics_engine.add_sprite(
            self.screen_boundary["left"],
            collision_type="boundary_left",
            body_type=arcade.PymunkPhysicsEngine.STATIC,
            friction=1.25,
            elasticity=0.0,
        )
        self.physics_engine.add_sprite(
            self.screen_boundary["right"],
            collision_type="boundary_right",
            body_type=arcade.PymunkPhysicsEngine.STATIC,
            friction=1.25,
            elasticity=0.0,
        )
        self.physics_engine.add_sprite_list(
            self.scene.name_mapping["ground1"],
            collision_type="wall",
            body_type=arcade.PymunkPhysicsEngine.STATIC,
            friction=1.25,
            elasticity=0.0,
        )

        self.general_sound["player"] = arcade.sound.play_sound(self.audio_background, looping=True, volume=0.1)

    def on_draw(self):
        # This command has to happen before we start drawing
        arcade.start_render()

        self.clear()

        # Draw scene and use nearest approximation pixel render
        self.scene.draw(filter=self.ctx.NEAREST)

        # Draw our life on the screen, scrolling it with the viewport
        color = arcade.csscolor.DARK_RED
        arcade.draw_text(self.player1.life, 50, SCREEN_HEIGHT - 100, color, 20, bold=True)
        arcade.draw_text(self.player2.life, SCREEN_WIDTH - 75, SCREEN_HEIGHT - 100, color, 20, bold=True)

        if self.game_over:
            player_win = "Player 2" if self.player1.life <= 0 else "Player 1"
            color = arcade.csscolor.YELLOW
            arcade.draw_text(f"{player_win} WIN", (SCREEN_WIDTH // 2) - 250, SCREEN_HEIGHT // 1.5, color, 50, bold=True)
            return
        # Show player hit_box
        # x, y = self.player1.position
        # arcade.draw_polygon_outline(
        #     [(point_x + x, point_y + y) for point_x, point_y in self.player1.hit_box], color=arcade.csscolor.YELLOW
        # )
        # x, y = self.player2.position
        # arcade.draw_polygon_outline(
        #     [(point_x + x, point_y + y) for point_x, point_y in self.player2.hit_box], color=arcade.csscolor.YELLOW
        # )

    def on_update(self, delta_time):
        """Movement and game logic"""

        if self.game_over:
            return

        # Update physics engine
        self.physics_engine.step(delta_time)

        # Update assets
        scene_objects = ["player1", "player2"]
        self.scene.update_animation(delta_time, scene_objects)

        self.update_player_on_update(delta_time, self.player1, self.player2)
        self.update_player_on_update(delta_time, self.player2, self.player1)

        self.end_game()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
        if key == arcade.key.ENTER and self.game_over:
            self.reset_game()
        if key == arcade.key.SPACE:
            self.general_sound["on"] = not self.general_sound["on"]
            if self.general_sound["on"]:
                self.general_sound["player"].play()
            else:
                self.general_sound["player"].pause()

        self.update_player_on_key_press(self.player1, key, arcade.key.S, arcade.key.W, arcade.key.A, arcade.key.D)
        self.update_player_on_key_press(self.player2, key, arcade.key.K, arcade.key.I, arcade.key.J, arcade.key.L)

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""
        self.update_player_on_key_release(self.player1, key, arcade.key.S, arcade.key.A, arcade.key.D)
        self.update_player_on_key_release(self.player2, key, arcade.key.K, arcade.key.J, arcade.key.L)

    def update_player_on_update(self, delta_time, player, other_player):
        is_on_ground = self.physics_engine.is_on_ground(player)
        if player.is_walking and player.going_left:
            force = (-player.movement_speed, 0) if is_on_ground else (-900, 0)
            self.physics_engine.apply_force(player, force)
            self.physics_engine.set_friction(player, 0.25)
        elif player.is_walking and not player.going_left:
            force = (player.movement_speed, 0) if is_on_ground else (900, 0)
            self.physics_engine.apply_force(player, force)
            self.physics_engine.set_friction(player, 0.25)
        else:
            self.physics_engine.set_friction(player, 1.25)

        if is_on_ground and player.is_attacking:
            if arcade.check_for_collision(player, other_player) and player.attack_timer == CHARACTERS_ATTACK_TIMER:
                other_player.life -= CHARACTERS_LIFE_HIT
            player.attack_timer -= delta_time
            if player.attack_timer < 0:
                player.is_attacking = False
                player.attack_timer = CHARACTERS_ATTACK_TIMER
                player.update_state()

        if is_on_ground and player.is_jumping:
            player.is_jumping = False
            player.is_on_ground = True
            player.update_state()

        player.update()

    def update_player_on_key_press(self, player, pressed_key, attack_key, jump_key, left_key, right_key):
        is_on_ground = self.physics_engine.is_on_ground(player)
        if (
            pressed_key == attack_key
            and is_on_ground
            and not player.is_jumping
            and not player.is_attacking
            and player.attack_timer == CHARACTERS_ATTACK_TIMER
        ):
            player.is_attacking = True
            arcade.sound.play_sound(self.audio_sword, volume=0.5)
        elif pressed_key == jump_key and is_on_ground and not player.is_jumping:
            player.is_jumping = True
            player.is_on_ground = False
            self.physics_engine.apply_impulse(player, (0, 1350))
        elif pressed_key == left_key and not player.is_walking:
            player.is_walking = True
            player.going_left = True
        elif pressed_key == right_key and not player.is_walking:
            player.is_walking = True
            player.going_left = False
        player.update_state()

    def update_player_on_key_release(self, player, released_key, attack_key, left_key, right_key):
        if released_key == left_key or released_key == right_key:
            player.is_walking = False
        player.update_state()

    def end_game(self):
        if self.player1.life <= 0 or self.player2.life <= 0:
            self.game_over = True

    def reset_game(self):
        self.game_over = False

        self.player1.reset()
        player1_position = PLAYERS_INITIAL_POSITION["player1"]
        self.player1.position = player1_position
        self.player1.center_x = player1_position[0]
        self.player1.center_y = player1_position[1]

        self.player2.reset()
        player2_position = PLAYERS_INITIAL_POSITION["player2"]
        self.player2.going_left = True
        self.player1.position = player2_position
        self.player2.center_x = player2_position[0]
        self.player2.center_y = player2_position[1]
