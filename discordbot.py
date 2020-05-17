from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='*')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def Ar(ctx):
    await ctx.send('読んだか~い?')

@bot.command()
async def こんにちは(ctx):
    await ctx.send('こん～')

@bot.command()
async def よろしくお願いします!(ctx):
    await ctx.send('よろしくうううううう!!')

@bot.command()
async def よろしくお願いします(ctx):
    await ctx.send('よろしくううううううううぇええええええい!!!')

@bot.command()
async def 死ね(ctx):
    await ctx.send('は？そういうこといったらだめですよぉ!')

@bot.command()
async def こんばんは(ctx):
    await ctx.send('こんばんわんこ!!')
@bot.command()
async def おやすみ(ctx):
    await ctx.send('おやすみなさいませ')

@bot.command()
async def ちんちん(ctx):
    await ctx.send('ちんちん大好き!!')

@bot.command()
async def 森(ctx):
    await ctx.send('もりもり唐揚げ')

@bot.command()
async def メイ(ctx):
    await ctx.send('メイ大好き!!')

@bot.command()
async def おはよう(ctx):
    await ctx.send('おはよう!お腹すいた!金くれ!!')

@bot.command()
async def うんち(ctx):
    await ctx.send('きたない')

@bot.command()
async def Discord(ctx):
    await ctx.send('Discordは神!!!')

@bot.command()
async def うるさい(ctx):
    await ctx.send('は？Ar様になんてことを!!!')

bot.run(token)
