import discord
import os
import json
client = discord.Client()

if os.path.isfile("main.json"):
    with open('main.json', encoding='utf-8') as f:
        db = json.load(f)
else:
    db = {}
    with open('main.json', 'w') as f:
        json.dump(db, f, indent=4)

@client.event
async def on_message(message):
    try:
        for var in db["commands"]:
            try:
                if message.content.startswith(var["befehl"]):
                    try:
                        msg = await message.channel.send(var["antwort"])
                        try:
                            if var["pin"] == "Befehl":
                                await message.pin()
                            elif var["pin"] == "Antwort":
                                await msg.pin()
                            elif var["pin"] == "Antwort, Befehl":
                                await msg.pin()
                                await message.pin()
                            else:
                                print("pin: Falsches/Fehlendes Argument. Verwende 'Befehl', 'Antwort' oder 'Antwort, Befehl'")
                        except:
                            None
                        try:
                            if var["unpin"] == "Befehl":
                                await message.unpin()
                            elif var["unpin"] == "Antwort":
                                await msg.unpin()
                            elif var["unpin"] == "Antwort, Befehl":
                                await msg.unpin()
                                await message.unpin()
                            else:
                                print("unpin: Falsches/Fehlendes Argument. Verwende 'Befehl', 'Antwort' oder 'Antwort, Befehl'")
                        except:
                            None
                        try:
                            if var["nachrichtLöschen"] == "Befehl":
                                await message.delete()
                            elif var["nachrichtLöschen"] == "Antwort":
                                await msg.delete()
                            elif var["nachrichtLöschen"] == "Antwort, Befehl":
                                await msg.delete()
                                await message.delete()
                            else:
                                print("nachrichtLöschen: Falsches/Fehlendes Argument. Verwende 'Befehl', 'Antwort' oder 'Antwort, Befehl'")
                        except:
                            None
                    except:
                        None
            except:
                None
    except:
        None

try:
    client.run(db["token"])
except:
    print("Fehler: Bitte füge den Token hinzu!")