import pygame


class Ship:
    """管理飞船的类"""
    def __init__(self, ai_game):
        """初始化飞船并设置初始位置"""
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图片并获取其外界矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 将每艘新飞船放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 在飞船的x属性中存储小数值
        self.x = float(self.rect.x)

        # 移动状态判断标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动状态标志调整飞船位置"""
        # 用更新飞船的x属性替换rect的x值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left:
            self.x -= self.settings.ship_speed

        # 根据self.x更新rect对象
        self.rect.x = self.x

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
