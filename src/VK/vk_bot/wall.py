from src.VK.vk_bot.Base import BaseVkBot, VkBotInstance


class WallBot(BaseVkBot):
    def __init__(self, bot):
        super(WallBot, self).__init__(bot)

    def get_posts(self, group, count_of_posts=100):
        posts = []
        offset = 0
        count = 100

        if count_of_posts <= 100:
            count = count_of_posts

            response = super().get(
                'wall.get',
                domain=group,
                count=count,
                offset=offset,

            )
            posts.extend(response.json()['response']['items'])
        else:
            offset = 100
            while count_of_posts > 0:

                response = super().get(
                    'wall.get',
                    domain=group,
                    count=count,
                    offset=offset,

                )

                count_of_posts -= 100

                if count_of_posts > 100:
                    offset += 100
                else:
                    count = count_of_posts
                    offset += count_of_posts

                posts.extend(response.json()['response']['items'])

        return posts

