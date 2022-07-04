import discum
import random
import requests
bot = discum.Client(token='Your Token Here', log=False)

result = ["大吉", "中吉", "小吉", "吉", "末吉", "凶", "大凶"]

result2 = ["裏", "表"] # toinfrip

trigger = "au!" # Prefix
@bot.gateway.command
def botcmds(resp):
    if resp.event.message:
        message = resp.parsed.auto()
        if message['content'] == f'{trigger}おみくじ': # Send Massege Templates
            ttt = random.choice(result)
            bot.sendMessage(message['channel_id'], f'{ttt}')
        elif message['content'] == f'{trigger}コイントス': #Second Commands
            ttt = random.choice(result2)
            bot.sendMessage(message['channel_id'], f'{ttt}')
        elif message['content'] == f'{trigger}おすすめ': # File Send Commands Template
            URL = "https://www.mirrativ.com/api/live/catalog?id=2&cursor="
            Header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36", "accept-language": "ja,en-US;q=0.9,en;q=0.8"}
            resp = requests.get(URL, timeout=500000, headers=Header)
            f = open('output2.txt', 'a', encoding='UTF-8')
            f.write(resp.text)
            bot.sendFile(message['channel_id'], "output2.txt")
            f.truncate(0)
        else:
            if message['content'].startswith(f'{trigger}'):
                bot.sendMessage(message['channel_id'], 'その様なコマンドはありません、もう一度よくお確かめの上実行してください。') # if someone Attempt Commands.
            if message['author']['username'] == (f'Your bot name here'): # if bot acc is send message.
                print("botが何かに返信しました。")
            else:
                guildID = message['guild_id'] if 'guild_id' in message else None #because DMs are technically channels too
                channelID = message['channel_id']
                username = message['author']['username']
                discriminator = message['author']['discriminator']
                content = message['content']
                f = open('Chat.txt', 'a', encoding='UTF-8')
                f.write("guild {} channel {} | {}#{}: {}\n".format(guildID, channelID, username, discriminator, content)) # logging a chats.
                f.close
                print("> guild {} channel {} | {}#{} | Message: {}\nLogging a Chat in Chat.txt".format(guildID, channelID, username, discriminator, content))

bot.gateway.run()
