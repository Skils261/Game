class Settings():
    '''Клас для хранения всех настроек игры'''

    def __init__(self):
        '''Инициализирует статические настройки игры'''
        # Параметры экрана
        self.screen_width = 1100
        self.screen_height = 600
        self.bg_color = (47, 79, 79)

        # Настройки корабля
        self.ship_limit = 3

        # Параметры снаряда
        self.bullet_width = 4
        self.bullet_height = 7
        self.bullet_color = (0, 0, 0)
        self.bullets_allowed = 5

        # Настройки пришельцев
        self.fleet_drop_speed = 5
        # fleet_direction = 1 означает движение вправо, а -1 влево
        self.fleet_direction = 1

        # Темп ускорения игры
        self.speedup_scale = 1.1
        # Темп роста стоимости пришельцев
        self.score_scale = 1.5

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        '''Инициализирует настройки, изменяющиеся в ходе игры'''
        self.ship_speed_factor = 2
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 0.5

        # fleet_direction = 1 означает движение вправо, а -1 влево
        self.fleet_direction = 1

        # Подсчет очков
        self.alien_points = 50


    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)