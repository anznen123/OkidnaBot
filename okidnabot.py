import discord
import os
client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("계승자 주머니 까는중...")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("1"): #명령어 입력시
        await message.channel.send("2") #명령어 입력시 출력할 메세지
        
access_token = os.environ["BOT_TOKEN"]
client.run(access.token)
