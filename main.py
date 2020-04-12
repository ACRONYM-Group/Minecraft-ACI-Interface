import sys
import time
import ACI

conn = ACI.create(ACI.Client, 8675, "127.0.0.1")
time.sleep(2)

from mcrcon import MCRcon

mcr = MCRcon("35.225.173.218", "MinecraftIsFun")
mcr.connect()
print("ONLINE")
print(" ")

resp = mcr.command("/testforblock 1253 12 626 651")

 def tail(f, lines=20):
    total_lines_wanted = lines

    BLOCK_SIZE = 1024
    f.seek(0, 2)
    block_end_byte = f.tell()
    lines_to_go = total_lines_wanted
    block_number = -1
    blocks = []
    while lines_to_go > 0 and block_end_byte > 0:
        if (block_end_byte - BLOCK_SIZE > 0):
            f.seek(block_number*BLOCK_SIZE, 2)
            blocks.append(f.read(BLOCK_SIZE))
        else:
            f.seek(0,0)
            blocks.append(f.read(block_end_byte))
        lines_found = blocks[-1].count(b'\n')
        lines_to_go -= lines_found
        block_end_byte -= BLOCK_SIZE
        block_number -= 1
    all_read_text = b''.join(reversed(blocks))
    return b'\n'.join(all_read_text.splitlines()[-total_lines_wanted:])

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
    if commandToExecute != "":
        mcr.command(commandToExecute)
        conn["minecraft"]["command"] = ""

    file = open("/home/blightfall/server/logs/latest.log")
    conn["minecraft"]["log"] = tail(file)
    file.close()

    
    time.sleep(1)
