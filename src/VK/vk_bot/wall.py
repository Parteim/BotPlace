from src.VK.vk_bot.Base import BaseVkBot


class WallBot(BaseVkBot):
    def __init__(self, ):
        super(WallBot, self).__init__()

    def get_posts(self, group, count=100):
        posts = super().get(
            'wall.get',
            domain=group,
            count=count,
            offset=0,

        )
        return posts


bot = WallBot()

print(bot.get_posts('hotpricesneakers'))