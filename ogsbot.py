import discord
from asyncio import sleep
import asyncio
import discord
from discord.ext import commands
import random
import math
from keep_alive import keep_alive
import youtube_dl
import os


#opensource code copyed some codes

client = commands.AutoShardedBot(commands.when_mentioned_or('&'),help_command=None)


@client.event
async def on_ready():
    print('Ready.')

@client.command()
async def help_maths(ctx):
  await ctx.send("&math is the command 'add' , 'sub' , 'div' , 'sqrt' , 'mult' , (eg : &mathadd 2 6) warning '&'' is the preflex also an api based math answer ")


@client.command()
async def maths(ctx):
  await ctx.send(" ``` &mathadd number + number (eg : mathadd 2 3) result = 5 ||now|| math sub &mathsub number - number (eg : mathsub 2 3) result = -1 every math function works like that ``` ")


def add(n: float, n2: float):
    return n + n2


def sub(n: float, n2: float):
    return n - n2


def div(n: float, n2: float):
    return n / n2


def sqrt(n: float):
    return math.sqrt(n)
  

def mult(n: float, n2: float):
    return n * n2


@client.command()
async def mathadd(ctx, x: float, y: float):
    try:
        result = add(x, y)
        await ctx.send(result)

    except:
        pass


@client.command()
async def mathsub(ctx, x: float, y: float):
    try:
        result = sub(x, y)
        await ctx.send(result)

    except:
        pass


@client.command()
async def mathdiv(ctx, x: float, y: float):
    try:
        result = div(x, y)
        await ctx.send(result)

    except:
        pass


@client.command()
async def mathmult(ctx, x: float, y: float):
    try:
        result = mult(x, y)
        await ctx.send(result)

    except:
        pass


@client.command()
async def mathsqrt(ctx, x: float):
    try:
        result = sqrt(x)
        await ctx.send(result)

    except:
        pass

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@client.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.Do &place (the number u wanna place ur 1000iq move at.)")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.Do &place (the number u wanna place ur 1000iq move at.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")

@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " wins! seeeesh what a pro")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn ")
    else:
        await ctx.send("Please start a new game using the &tictactoe command.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <672029802118643723>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.or place where its not placed")

@client.command()
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " Server Information",
        description=description,
        color=discord.Color.dark_blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)
  
  #open source code snipe 

snipe_message_author = {}
snipe_message_content = {}

@client.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     await sleep(30)
     del snipe_message_author[message.channel.id]
     del snipe_message_content[message.channel.id]

@client.command(name = 'snipe')
async def snipe(ctx):
    channel = ctx.channel
    try: #This piece of code is run if the bot finds anything in the dictionary
        em = discord.Embed(name = f"Sniped message #{channel.name}", description = snipe_message_content[channel.id])
        em.set_footer(text = f"Message from {snipe_message_author[channel.id]}")
        await ctx.send(embed = em)
    except: #This piece of code is run if the bot doesn't find anything in the dictionary
        await ctx.send(f"No deleted message found or was an emblem or a file(30 second is time limit) #{channel.name}")


        
keep_alive()
client.run('Ur token')


