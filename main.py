import discord
# import * - è un modo rapido per importare tutti i file della libreria.
from bot_logic import gen_pass,gen_emodji,flip_coin

# La variabile intents memorizza i privilegi del bot
intents = discord.Intents.default()
# Abilitazione del privilegio di lettura dei messaggi
intents.message_content = True
# Creare un bot nella variabile client e trasferirgli i privilegi
client = discord.Client(intents=intents)


# Una volta che il bot è pronto, stamperà il suo nome!
@client.event
async def on_ready():
    print('Abbiamo effettuato l accesso come {client.user}')


# Quando il bot riceve un messaggio, invia messaggi nello stesso canale!
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Ciao! Sono un bot!')

    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$emodji'):
        await message.channel.send(gen_emodji()) 
    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())        
    else:
        await message.channel.send("Non è possibile elaborare questo comando, mi dispiace!")

client.run("MTE2MDUxNzMzMDc5OTk3MjQwMw.GNuLJI.kuxNNf_ZjcoqJrdMNZcO9fKwU33xPF-e4SGQaQ")
