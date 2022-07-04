import discum
import random
bot = discum.Client(token='Your Selfbot Token here', log=False)

omikujiresult = ["大吉", "中吉", "小吉", "吉", "末吉", "凶", "大凶"]

coinresult = ["裏", "表"]

trigger = "au!" # Selfbot Prefix
@bot.gateway.command
def bot(resp):
    if resp.event.message:
        message = resp.parsed.auto()
        if message['content'] == f'{trigger}おみくじ': # omikuji
            ttt = random.choice(omikujiresult)
            bot.sendMessage(message['channel_id'], f'{ttt}')
        elif message['content'] == f'{trigger}コイントス': # Coinfrip
            ttt = random.choice(coinresult)
            bot.sendMessage(message['channel_id'], f'{ttt}')
        else:
            if message['content'].startswith(f'{trigger}'):
                bot.sendMessage(message['channel_id'], 'その様なコマンドはありません、もう一度よくお確かめの上実行してください。') # Attempt Commands Meesages.
            else:
                guildID = message['guild_id'] if 'guild_id' in message else None #because DMs are technically channels too
                channelID = message['channel_id']
                username = message['author']['username']
                discriminator = message['author']['discriminator']
                content = message['content']
                f = open('Chat.txt', 'a', encoding='UTF-8')
                f.write("guild {} channel {} | {}#{}: {}\n".format(guildID, channelID, username, discriminator, content)) # Chat logging
                f.close
                print("> guild {} channel {} | {}#{} | Message: {}\nLogging a Chat in Chat.txt".format(guildID, channelID, username, discriminator, content))

bot.gateway.run()
