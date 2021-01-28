import json
import os
from time import sleep
from discord_webhook import DiscordWebhook, DiscordEmbed
import platform
import subprocess
osN = platform.system()
import asyncio
def getconfig(name):
    with open(name,"r") as f:
        return json.loads(f.read())

config = getconfig("config.json")

async def sendmsg(config,ip):
    webhook = DiscordWebhook(url=config["webhookurl"], username="Owoki")
    embed = DiscordEmbed(title='Mr.Server', description=config["downmsg"] + "\n"+ ip, color=0xff0000)
    webhook.add_embed(embed)
    response = webhook.execute()
def run(bash):
    return os.popen(bash).read()

while True:
    for i in range(0,len(config["serverips"])):
        loop = asyncio.get_event_loop()
        if osN == "Linux":
            w = "W"
            n = "c"
        else:
            w = "w"
            n = "n"
        bash = "ping -"+w+" 1 -"+n+" 1 "+config["serverips"][i]
        output = run(bash)
        if "name" in output  or not "from" in output:
            loop.run_until_complete(sendmsg(config,config["serverips"][i]))
            print("[-] Server is down !!!! :",config["serverips"][i])
        else:
            print("[+] Server is up :",config["serverips"][i])
        
    sleep(int(config["looptime"]))




