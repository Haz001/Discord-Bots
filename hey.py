try:#tries to import Requred d.scripts
    import asyncio
    import discord
    import os
    import time
    import random as rn
    from datetime import *
    import sys
    import display as disp
    from df import *
    import platform
except Exception as e:
    print ("Error moduals not installed\n"+str(e))
    input()
    exit()

class d:
    scr = None
class var:
    oc = 0
class pingc:
    uniqueid = "ID is not this"
    old = None
    old2 = None
    pis = False

d.scr = disp.disp()
d.scr.draw()
vr.prefix = "-"
d.scr.draw()
d.scr.info.Prefix = vr.prefix
client = discord.Client()
lids = ["Bot_Number_2"]
lhcs = [4545656465.3]
file = open("ver",'r')
vers = file.read();
vr.lst_day = 0;
cnt=0

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    d.scr.name = client.user.name
    d.scr.draw()
    print(client.user.id)
    print('Online')
    print(await client.change_presence(game=discord.Game(name='Hello World 2 (the better hello world)')))
    await client.send_message(client.get_channel('489502051919724557'),"Hey, just came online. Time to say Hi to everyone.\n```yml\nOS: "+str(platform.system())+"\n```")

@client.event
async def on_message(message):#this is way to long. Need to steal from RogueSensei again.
    try:
        if str(message.content)[0] == "-":
            d.scr.addmsg(str(message.author)+": "+message.content.replace("\n","\\n"))

        if str(message.content)[0] == "-":
            d.scr.addmsg(str(message.author)+": "+message.content.replace("\n","\\n"))
        if pingc.pis and pingc.uniqueid in message.content:
            t = datetime.utcnow()-pingc.old
            t2 = datetime.utcnow()-pingc.old2
            if ("basic" in message.content):
                await client.edit_message(message,"Ping Requested:\n```yml\nLatency: "+str(t).split(":")[2]+"s```")
            else:
                await client.edit_message(message,message.content.replace("\nID-Tag: "+pingc.uniqueid,"")+"\nSend-Latency: "+str(t2).split(":")[2]+"s\nTotal-Latency: "+str(t).split(":")[2]+"s\nID-Tag: "+pingc.uniqueid+"```")
            pingc.pis = False
        if fn.prehey(message):
            await client.send_message(message.channel,rn.choice(vr.cmdc1))
        if fn.precom(message,"vsauce"):
            await client.send_message(message.channel,"Hey Vsauce, Michal here!")
        elif fn.precom(message,"icon"):
            await client.send_message(message.channel,embed=fn.img_embed("https://cdn.discordapp.com/avatars/435477852465397760/b751673b138232148561faa1f78f92bc.png"))
        elif fn.precom(message,"meme"):
            await client.send_message(message.channel,embed=fn.meme_send())
        elif fn.precom(message,"ping"):
            pingc.pis = True
            pingc.old = message.timestamp
            pingc.uniqueid = str(hex(rn.randint(1000,9999)))
            pingc.old2 = datetime.utcnow()
            if("-d" in message.content):
                t = datetime.utcnow()-message.timestamp
                await client.send_message(message.channel,"Ping Request:\n```yml\nUser: "+message.author.name+";\nSize: "+str(len(message.content))+";\nRecieved-Latency: "+str(t).split(":")[2]+"s\nID-Tag: "+pingc.uniqueid)
            else:
                await client.send_message(message.channel, "basic"+pingc.uniqueid)
        elif fn.precom(message,"Hey! Listen") or fn.precom(message,"hey! listen") or fn.precom(message,"hey listen") or fn.precom(message,"Hey Listen"):
            await client.send_message(message.channel,"OMFG Its Navi Run!!!")
            time.sleep(5)
        elif "<@445009498927661079>" in message.content:
            await client.send_message(message.channel,"Hey!")
        elif fn.precom(message,"invite"):
            await client.send_message(message.channel,"https://discordapp.com/oauth2/authorize?client_id=435477852465397760&scope=bot&permissions=523328")
        elif fn.precom(message,"merry christmas") or fn.precom(message,"merry xmas"):
            await client.send_message(message.channel,"Merry Christmas!")
        elif fn.precom(message,"react"):
            if("-h" in message.content):
                await client.send_message(message.channel,"```yml\nreact <name>\n<name> = cool, cry, fight, happy, high, mad, plz, really, sad, sleep, suprised and what```")
            with open(react.get(str(message.content)), 'rb') as f:
                await client.send_file(message.channel, f)
        elif fn.precom(message,"help"):
            await client.send_message(message.channel,"Hey!(Navi)\n```yml\n Help:\nPrefix        -> '"+vr.prefix+"'\nhey/hi/yo/ect -> Replies\nvsauce        -> quotes him\nicon          -> uploads avatar\nmeme          -> uploads meme\nping          -> check response time\nping -d       -> for debug response message that includes more info\nonline        -> checks if hey bot is online or not\nlb            -> leaderboard is printed (lag may occure)\nreact <name>  -> uploads reaction of choice \nstats         -> prints the stats;\nforce-error   -> forces an error```")
        elif fn.precom(message,"online"):
            await client.send_message(message.channel,"Nope. I am offline right now. As you can clearly see.\n```yml\nStatus: Offline```")
        elif fn.precom(message,"github"):
            await client.send_message(message.channel,"I'm closed source!\nhttps://github.com/Haz001/Discord-Bots")
        elif fn.precom(message,"stats"):
            await client.send_message(message.channel,"Hey!(Navi)\n```yml\nMeme-count: "+str((meme.length))+"\nOfflines: "+str(var.oc)+"\nVersion: "+vers+"\nCoolness: i\n*i is an imaginary number, you can't get any cooler than that (√(-1) = i).```")
        elif fn.precom(message,"lb"):

            tmpx = str()
            for tmp in range(len(lids)):
                tmpx += str("\n"+str(lids[tmp])+": "+str(lhcs[tmp]))
            await client.send_message(message.channel,"```yml\nLeaderboard:\n"+tmpx+"```")
        elif fn.precom(message,"update"):

            await client.send_message(message.channel,"Hey(Navi) bot getting update!!! Yeah! OMG, what am I going to get!")
            try:
                if(platform.system() == 'Linux'):
                    os.system("python3 hey.py")
                elif(platform.system() == 'Windows'):
                    os.system("py hey.py")
                else:
                    await client.send_message(message.channel,"I was never built to run on a "+str(platform.system()))
                await client.send_message(message.channel,"Error in code")
            except:
                print("error")
                await client.send_message(message.channel,"Failed to start")
        elif fn.precom(message,"display-update"):
            await client.send_message(message.channel,"Updating")
            d.scr = disp.disp()
            await client.send_message(message.channel,"Updated")
        elif fn.precom(message,"force-error"):
            await client.send_message(message.channel,"ʎǝH")
            int("ʎǝH")

        for tmp in range(len(vr.cmdc1)):
            if (vr.cmdc1[tmp] in message.content.lower().split(" ")):
                if message.author.name in lids:
                    lhcs[lids.index(message.author.name)] += 1;
                    if(lhcs[lids.index(message.author.name)] % 10)==0:
                        await client.send_message(message.channel,"Level Up!\n:arrow_up:"+message.author.name+" > "+str(lhcs[lids.index(message.author.name)] /10))
                else:
                    lids.append(message.author.name);
                    lhcs.append(1);



    except Exception as e:
        await client.send_message(client.get_channel('438028465921589250'),"I F*CKED UP:\n```py\n"+str(e)+"```\nTo report the error go to: https://discord.gg/djFFREv")
        el = open("error.log",'a')
        el.write("\n"+str(e)+"\n")
        el.close()
        disp.info.add_error(str(e))
    print("draw")
    d.scr.draw()

def runbot():
    try:
        while True:
            loop = asyncio.get_event_loop()
            try:
                loop.run_until_complete(client.run(fn.gt(0)))
            except Exception as e:
                d.scr.addmsg(str(e).replace("\n","\\n"))
                d.scr.addmsg('Attempting to reboot in 30 seconds')
                loop=None
                time.sleep(30)
    except:
        os.system("python3 hey.py")
runbot()
#     while True:
#         loop = asyncio.get_event_loop()
#         while True:
#             loop.run_until_complete(client.run(fn.gt(0)))
#         d.scr.info.Status = "Restarting Loop"
#         d.scr.draw()
#         var.oc += 1
# try:
#     runbot()
# except Exception as e:
#     el = open("error.log",'a')
#     el.write("\n"+str(e)+"\n")
#     el.close()
#     if(platform.system() == 'Linux'):
#         os.system("python3 hey.py")
#     elif(platform.system() == 'Windows'):
#         os.system("py hey.py")
