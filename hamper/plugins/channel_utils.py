from hamper.interfaces import Command, ChatCommandPlugin


class ChannelUtils(ChatCommandPlugin):

    name = 'channelutils'
    priority = 0

    class JoinCommand(Command):
        name = 'join'
        regex = r'^join (.*)$'

        short_desc = 'join #channel - Ask the bot to join a channel.'
        long_desc = None

        def command(self, bot, comm, groups):
            """Join a channel, and say you did."""
            chan = groups[0]
            if not chan.startswith('#'):
                chan = '#' + chan
            bot.join(chan)
            bot.reply(comm, 'OK, {0}.'.format(comm['user']))

    class LeaveCommand(Command):
        name = 'leave'
        regex = r'^leave( #?[-_a-zA-Z0-9]+)?$'

        short_desc = 'leave [#channel] - Ask the bot to leave.'
        long_desc = 'If channel is ommited, leave the current channel.'

        def command(self, bot, comm, groups):
            """Say goodbye and leave channel."""
            chan = groups[0]
            if chan:
                chan = chan.lstrip()  # Strip captured space
            else:
                chan = comm['channel']
            if not chan.startswith('#'):
                chan = '#' + chan
            comm['channel'] = chan  # Say Bye in the channel I'm leaving
            bot.reply(comm, 'Bye!')
            bot.leave(chan)


channel_utils = ChannelUtils()
