from discordbot.module import Module
import discord
import datetime


class Core(Module):
    name = 'discordbot-core'

    def bot(self):
        self.config['init'] = datetime.datetime.now()

    async def on_message(self, message: discord.Message):
        if self.is_my(message):
            return False

        if self.has_command('info', message):
            msg = [
                self.config['info']['website'],
                'Uptime ' + self.uptime(),
                'Bot script: ' + self.config['info']['repository']
            ]

            await self.container.client.send_message(message.channel, '\n'.join(msg))

    def uptime(self):
        def plural(val):
            if val == 1:
                return ''
            else:
                return 's'

        diff = datetime.datetime.now() - self.config['init']

        hours = (diff.seconds // 3600) % 24
        minutes = (diff.seconds // 60) % 60
        seconds = diff.seconds % 60

        return '{} day{} {} hour{} {} minute{} {} second{}'.format(
            diff.days,
            plural(diff.days),
            hours,
            plural(hours),
            minutes,
            plural(minutes),
            seconds,
            plural(seconds),
        )
