import sys
import time
import ACI
import os

conn = ACI.create(ACI.Client, 8675, "127.0.0.1")
time.sleep(2)

from mcrcon import MCRcon

connected = False
mcr = MCRcon("35.225.173.218", "MinecraftIsFun")
while not connected:
    try:
        mcr.connect()
        connected = True
    except Exception:
        print("Unable to Connect To Server. Trying again in 5 seconds.")
    time.sleep(5);

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
    conn["minecraft"]["PlayerList"] = resp

    if conn["minecraft"]["stop"] == "True":
        conn["minecraft"]["stop"] = "False"
        mcr.command("/stop")

    commandToExecute = conn["minecraft"]["command"]
    if commandToExecute != "" and commandToExecute != None:
        mcr.command(commandToExecute)
        conn["minecraft"]["command"] = ""

    conn["minecraft"]["log"] = os.popen('tail -n 20 /home/blightfall/server/logs/latest.log').read()

    conn["minecraft"]["dayTime"] = mcr.command("/time query daytime")
    conn["minecraft"]["numberOfDays"] = mcr.command("/time query day")
    conn["minecraft"]["worldAge"] = mcr.command("/time query gametime")

    
    time.sleep(1)
