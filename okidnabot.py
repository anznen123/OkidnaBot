import discord

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

client.run("Njg2OTc2MzE1NzM5NzM0MDQw.XmfCjQ.en6zZvqBh8-u-23lXiq9brnZ7Ek")