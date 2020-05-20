import discord
import asyncio
import os
client = discord.Client()

token = "NzEyMTE2MDU1MTQ5MTE3NDYw.XsSLCQ.xVn-CLTG9Glf9srj7WlIAZ_dQf8"

@client.event
async def on_ready():

    print("=========================")
    print("다음으로 로그인 합니다 : ")
    print(client.user.name)
    print("connection was successful")
    game = discord.Game("24시간온라인입니다")
    print("=========================")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == "야이좆밥아":
        await message.channel.send("왜이씹썅놈아!")

    if message.content == "야병신":
        await message.channel.send("왜병신")
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)



