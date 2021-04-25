# インストールした discord.py を読み込む
import discord
import random

# 自分のBotのアクセストークンに置き換えてください(テスト用トークン)
TOKEN = "DISCORD_BOT_TOKEN"
# 接続に必要なオブジェクトを生成
client = discord.Client()
# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name='!helpDDでヘルプを表示(1.40)'))
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    #条件に当てはまるメッセージかチェックし正しい場合は返す
    await client.change_presence(status=discord.Status.offline)
    def check(msg):
        return msg.author == message.author
    
    def is_num(a):
        try:
            int(a)
        except:
            return False
        return True

    def TDTM(txt):
        # 送られてきたd入りの文字列をダイスとして処理して文字列で返す
        l=list(txt)
        # a=num b=num2
        x=0
        txt=""
        m=""
        while len(l)>x:
            if l[x]=="d":
                # txtに保存されている数と後ろ部分の数からダイスを振る
                a=int(txt)
                x=x+1
                txt=""
                while len(l)>x and l[x].isdecimal()==True:
                    txt=txt+l[x]
                    x=x+1
                b=int(txt)
                x=x-1
                count=1
                random.seed()
                txt="("+str(int(random.random()*b)+1)
                while count<a:
                    random.seed()
                    txt=txt+"+"+str(int(random.random()*b)+1)
                    count=count+1
                txt=txt+")"
                m=m+txt
                txt=""
            elif l[x].isdecimal()==True:
                txt=txt+l[x]
            else:
                # 区切りとしてmに出力
                txt=txt+l[x]
                m=m+txt
                txt=""
            x=x+1
        return m

    def Skill(ver,num,bp):
        num=int(num)
        bp=int(bp)
        random.seed()
        rum1=int(random.random()*10)
        random.seed()
        rum2=int(random.random()*10)
        dc=[100-(rum1*10+rum2)]
        rum=100-(rum1*10+rum2)

        while len(dc)<=abs(int(bp)):
            random.seed()
            rum1=int(random.random()*10)
            dc.append(100-(rum1*10+rum2))
            if 0<=bp:
                if 100-(rum1*10+rum2)<=rum:
                    rum=100-(rum1*10+rum2)
            else:
                if 100-(rum1*10+rum2)>=rum:
                    rum=100-(rum1*10+rum2)

        if ver=="7":
            if num>=50:
                if 100==rum:
                    txt="(7)× ファンブル ×"
                elif rum==1:
                    txt="(7)☆ クリティカル ☆"
                elif rum<=num/5:
                    txt="(7)☆　エキスパート　☆"
                elif rum<=num/2:
                    txt="(7)○　ハード　○"
                elif rum<=num:
                    txt="(7)○ 成功 ○"
                elif rum>num:
                    txt="(7)△ 失敗 △"
            else:
                if 96<=rum:
                    txt="(7)× ファンブル ×"
                elif rum==1:
                    txt="(7)☆ クリティカル ☆"
                elif rum<=num/5:
                    txt="(7)☆　エキスパート　☆"
                elif rum<=num/2:
                    txt="(7)○　ハード　○"
                elif rum<=num:
                    txt="(7)○ 成功 ○"
                elif rum>num:
                    txt="(7)△ 失敗 △"
        elif ver=="6":
            if 96<=rum:
                txt="(6)× ファンブル ×"
            elif rum<=5:
                txt="(6)☆ クリティカル ☆"
            elif rum<=num:
                txt="(6)○ 成功 ○"
            elif rum>num:
                txt="(6)△ 失敗 △"
        else:
            if 96<=rum:
                txt="× ファンブル ×"
            elif rum<=5:
                txt="☆ クリティカル ☆"
            elif rum<=num/5:
                txt="☆　エキスパート　☆"
            elif rum<=num/2:
                txt="○　ハード　○"
            elif rum<=num:
                txt="○ 成功 ○"
            elif rum>num:
                txt="△ 失敗 △"
        
        txt=txt+" ("+str(num)+"=>"+str(rum)+str(dc)+")"
        return txt

    
    def Stsix(x):
        def ThreeDSix(x,a):
            txt=" "
            ct=0
            while ct<x:
                random.seed()
                num=int(random.random()*6)+1+int(random.random()*6)+1+int(random.random()*6)+1+a
                if len(str(num))<2:
                    txt+=" "+str(num)
                elif len(str(num))>1:
                    txt+=str(num)
                ct+=1
                if ct<x:
                    txt+=", "
            return txt
        
        def TwoDSix(x,a):
            txt=" "
            ct=0
            while ct<x:
                random.seed()
                num=int(random.random()*6)+1+int(random.random()*6)+1+a
                if len(str(num))<2:
                    txt+=" "+str(num)
                elif len(str(num))>1:
                    txt+=str(num)
                ct+=1
                if ct<x:
                    txt+=", "
            return txt
        
        x=int(x)
        txt="```"
        txt+="STR:"
        txt+=ThreeDSix(x,0)
        txt+="\nCON:"
        txt+=ThreeDSix(x,0)
        txt+="\nPOW:"
        txt+=ThreeDSix(x,0)
        txt+="\nDEX:"
        txt+=ThreeDSix(x,0)
        txt+="\nAPP:"
        txt+=ThreeDSix(x,0)
        txt+="\nSIZ:"
        txt+=TwoDSix(x,6)
        txt+="\nINT:"
        txt+=TwoDSix(x,6)
        txt+="\nEDU:"
        txt+=ThreeDSix(x,3)
        txt+="```"

        return txt

    def Stsev(x):
        def ThreeDSix(x,a):
            txt=" "
            ct=0
            while ct<x:
                random.seed()
                num=(int(random.random()*6)+1+int(random.random()*6)+1+int(random.random()*6)+1+a)*5
                if len(str(num))<3:
                    txt+=" "+str(num)
                elif len(str(num))>2:
                    txt+=str(num)
                ct+=1
                if ct<x:
                    txt+=", "
            return txt
        
        def TwoDSix(x,a):
            txt=" "
            ct=0
            while ct<x:
                random.seed()
                num=(int(random.random()*6)+1+int(random.random()*6)+1+a)*5
                if len(str(num))<3:
                    txt+=" "+str(num)
                elif len(str(num))>2:
                    txt+=str(num)
                ct+=1
                if ct<x:
                    txt+=", "
            return txt
        
        x=int(x)
        txt="```"
        txt+="STR:"
        txt+=ThreeDSix(x,0)
        txt+="\nCON:"
        txt+=ThreeDSix(x,0)
        txt+="\nPOW:"
        txt+=ThreeDSix(x,0)
        txt+="\nDEX:"
        txt+=ThreeDSix(x,0)
        txt+="\nAPP:"
        txt+=ThreeDSix(x,0)
        txt+="\nSIZ:"
        txt+=TwoDSix(x,6)
        txt+="\nINT:"
        txt+=TwoDSix(x,6)
        txt+="\nEDU:"
        txt+=TwoDSix(x,6)
        txt+="\nLUK:"
        txt+=ThreeDSix(x,0)
        txt+="```"
        
        return txt


    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
   
    if message.content.startswith('!r'):
        send_message=message.content.split(" ")
        if len(send_message)==1:
            number=int(random.random()*100)
            await message.channel.send(message.author.mention+str(number))
        else:
            txt=TDTM(send_message[1])
            await message.channel.send(message.author.mention+"{0}={1}".format(txt,eval(txt)))
        
    elif message.content.startswith('!sk'):
        send_message=message.content.split(" ")
        if len(send_message)>=3 and is_num(send_message[2])==True:
            await message.channel.send(message.author.mention+Skill(send_message[0].replace("!sk",""),send_message[1],send_message[2]))
        else:
            await message.channel.send(message.author.mention+Skill(send_message[0].replace("!sk",""),send_message[1],0))
    
    elif message.content.startswith('!st6'):
        send_message=message.content.split(" ")
        if len(send_message)<=1:
            await message.channel.send(message.author.mention+Stsix(1))
        else:
            await message.channel.send(message.author.mention+Stsix(send_message[1]))

    elif message.content.startswith('!st7'):
        send_message=message.content.split(" ")
        if len(send_message)<=1:
            await message.channel.send(message.author.mention+Stsev(1))
        else:
            await message.channel.send(message.author.mention+Stsev(send_message[1]))
    
    elif message.content=="!helpDD":

        hf=open('help.txt', 'r', encoding='UTF-8')
        mes=message.author.mention+"```"+hf.read()+"```"
        await message.channel.send(mes)

    await client.change_presence(status=discord.Status.online)




# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
