from discordbot.module import Module
import discord
import datetime


class Core(Module):
    name = 'core'
    uptime = None
    msg = []

    def bot(self):
        self.config['init'] = datetime.datetime.now()

        if 'core' in self.container.config['global']:
            self.config = self.container.config['global']['core']

        if 'website' in self.config:
            self.msg.append(self.config['website'])

        self.msg.append('Uptime: {}')

        if 'description' in self.config and type(self.config['description']) is list:
            self.msg.append('\n'.join(self.config['description']))

    async def on_message(self, message: discord.Message):
        if self.is_my(message):
            return False

        if self.has_command('info', message):
            self.uptime = self.__uptime()

            await self.container.client.send_message(
                message.channel,
                '\n'.join(self.msg).format(self.uptime)
            )

    def __uptime(self):
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
