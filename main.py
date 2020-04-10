import sys
import time
import ACI.ACI

conn = ACI.create(ACI.Client, 8675, "127.0.0.1")
time.sleep(2)

from mcrcon import MCRcon

mcr = MCRcon("35.225.173.218", "MinecraftIsFun")
mcr.connect()
print("ONLINE")
print(" ")

resp = mcr.command("/testforblock 1253 12 626 651")

while True:
    resp = mcr.command("/testforblock 1253 12 626 651")
    if resp[0] == "S":
        conn["OmegaMainframe"]["testLamp"] = "True"
        print(conn["OmegaMainframe"]["testLamp"])
        mcr.command("/setblock 1254 12 624 1")
        mcr.command("/say THE WORLD IS ENDING")
        time.sleep(5)
        mcr.command("/setblock 1254 12 624 152")
        time.sleep(1)
        print("Goodbye!")
        mcr.command("/stop")
    else:
        mcr.command("/setblock 1254 12 624 152")

    resp = mcr.command("/list")
    conn["Minecraft"]["PlayerList"] = resp

    if conn["Minecraft"]["stop"] == "True":
        conn["Minecraft"]["stop"] = "False"
        mcr.command("/stop")

    
    time.sleep(1)
