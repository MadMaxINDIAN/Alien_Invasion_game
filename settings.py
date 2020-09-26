class Settings:
    """a class to store all the setings. """
    def __init__(self):
        """initialise the game settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # SHIP SETTINGS
        self.ship_speed_factor = 1.5

        # BULLET SETTINGS.
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.final_power_of_bullet_keydown = 1
        self.initial_power_of_bullet_keydown = 0
        self.final_power_of_bullet_keyup = 0
        self.initial_power_of_bullet_keyup = 0
        self.bullets_allowed = 100

        # ALIEN SETTINGS.
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = -1
        self.health_of_alien = 1

