from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command ()
@commands.has_permissions (administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    embed=discord.Embed (title=f'実行者:{ctx.author}', description=f"BANが成功しました:{member.mention}", color=0xff0000)
    embed.add_field (name=f"{member.id}", value=f"{ctx.author.created_at}", inline=False)
    await ctx.send (embed=embed)

@bot.command()
@commands.has_permissions (administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick (reason=reason)
    embed = discord.Embed (title=f'実行者:{ctx.author}', description=f"KICKが成功しました:{member.mention}",color=0xff0000)
    embed.add_field (name=f"{member.id}", value=f"{ctx.author.created_at}", inline=False)
    await ctx.send (embed=embed)
 
bot.run(token)
