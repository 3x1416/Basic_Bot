import discord
import os
import random
from discord.ext import commands
from bot_logic import *
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def bye(ctx):
    await ctx.send("\U0001f642")

@bot.command()
async def contraseña(ctx):
    await ctx.send((gen_pass(10) ))

@bot.command()
async def moneda(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def emoji(ctx):
    await ctx.send(gen_emodji())
    
@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def mem(ctx):
    img = random.choice(os.listdir('images'))
    with open(f'images\{img}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)\
    
@bot.command()
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)

@bot.command()
async def fox(ctx):
    image_url = get_fox_image_url()
    await ctx.send(image_url)

bot.run("token ultra secreto")
