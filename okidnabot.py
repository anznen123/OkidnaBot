import discord
from bs4 import BeautifulSoup
from selenium import webdriver

client = discord.Client()

url = "https://archeage.xlgames.com/play/worldinfo/DAHUTA"

driver = webdriver.Chrome('./driver/chromedriver.exe')
driver.implicitly_wait(3) #버튼이 생성이 안되었을 때 기다려주는 시간(묵시적 대기)

# 페이지 가져오기
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html)

for anchor in soup.select('div.bond-info'):
        print(anchor.get_text())
        #line_break.replaceWith("\n")

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("히라마 서부에서 사냥")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("!채권"):
        await message.channel.send(anchor.get_text())

client.run('Njg2OTc2MzE1NzM5NzM0MDQw.XmfCjQ.kGHX_Dcd9PDvPAHMpnlabr63SZY')
