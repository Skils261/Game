
class GameStats():
    '''Отслеживание статистики игры'''

    def __init__(self, ai_game):
        '''Инициализирует статистику'''
        self.settings = ai_game.settings
        self.reset_stats()

        # Флаг активности игры
        self.game_active = False

        # Рекордное значение счета
        self.high_score = 0

    def reset_stats(self):
        '''Инициализирует статистику, изменяющуюся в ходе игры'''
        # Количество жизней у корабля
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1


