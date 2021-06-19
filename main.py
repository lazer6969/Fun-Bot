import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix=">",help_command=None)

@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}#{client.user.discriminator} ({client.user.id})")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f">help on {len(client.guilds)} servers"))

@client.command()
async def ping(ctx):
    all_choices = ["200 ms", "144 ms", "69 ms", "169 ms", "229 ms", "120 ms"]
    victim = random.choice(all_choices)
    await ctx.send(f"My Current Ping Is -  {victim}")

@client.command()
async def help(ctx):
    await ctx.send (">ping , >howgay , >pp , >simp , >invite")

@client.command()
async def pp(ctx):
    all_choices = ["8============D", "8===D", "8======D", "8=D", "8==D", "8=====D", "8=====D", "8=======D", "8============D"]
    victim = random.choice(all_choices)
    await ctx.send(f"Calculated PP - {victim}")

@client.command()
async def howgay(ctx):
    all_choices = ["66% Gay", "1% Gay", "99% Gay", "12% Gay", "100% Gay", "4% Gay", "84% Gay", "69% Gay", "44% Gay", "2% Gay", "44% Gay", "87% Gay"]
    victim = random.choice(all_choices)
    await ctx.send(f"You Are {victim}")

@client.command()
async def simp(ctx):
    all_choices = ["66% Simp", "1% Simp", "99% Simp", "12% Simp", "100% Simp", "4% Simp", "84% Simp", "69% Simp", "44% Simp", "2% Simp", "44% Simp", "87% Simp"]
    victim = random.choice(all_choices)
    await ctx.send(f"You Are {victim}")

@client.command()
async def invite(ctx):
    await ctx.send ("Invite Me - [https://discord.com/api/oauth2/authorize?client_id=824997151426871317&permissions=2148005952&scope=bot]")

client.run("TOKEN_HERE")
