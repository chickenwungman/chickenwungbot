import discord
from discord.ext import commands

client = commands.Bot(command_prefix='?')


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Do "?help" for commands.'))
    print('Bot is ready.')


@client.command()
async def ping():
    await client.say('Pong!')


@client.command(pass_context=True)
@commands.has_role("Staff")
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Messages deleted.')


@client.command()
@commands.has_role("Staff")
async def say(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)


@client.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}".format(user.name), description="{}'s information.".format(user.name),color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await client.say(embed=embed)


@client.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server), description="Here's what I could find.",color=0x00ff00)
    embed.set_author(name="Discord is owned by Steven!")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=str(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=str(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await client.say(embed=embed)


@client.command(pass_context=True)
@commands.has_role("Staff")
async def kick(ctx, user: discord.Member):
    await client.say("{} has been kicked!".format(user.name))
    await client.kick(user)


@client.command(pass_context=True)
@commands.has_role("Staff")
async def ban(ctx, user: discord.Member):
    await client.say("{} has been banned!".format(user.name))
    await client.ban(user)


@client.command(pass_context=True)
@commands.has_role("Staff")
async def warn(ctx, user: discord.Member):
    await client.say("{} has been warned!".format(user.name))
    await client.warn(user)

client.run("")
