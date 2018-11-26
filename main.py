import discord
import os
import random

client = discord.Client()

@client.event
async def on_ready():
    print("E mo so’ cazzi, è arrivato lo Spammone")
    print(client.user)

@client.event
async def on_message(message):
    if message.author == client.user:
      return
    elif message.content.startswith("!comandi"):
        await client.send_message(message.channel, "Comandi Spammoni:\n!buongiorno - per un buongiorno speciale\n!8ball seguito da una domanda a cui si possa avere una risposta SI o NO - risposte affidabili\n!prova")
  
    elif message.content.startswith("!buongiorno"):
        await client.send_message(message.channel, random.choice(["Buongiorno un bel cazzo","Il buongiorno si vede dal mattino e infatti, io sto caricando letame...poi trasporto il letame...poi spargo il letame...praticamente una giornata di merda!","Io ve lo direi anche buongiorno, ma per averne la certezza dovrei aspettare questa sera","La giornata di oggi è stata cancellata. Puoi tornare a letto!","Ci sono due tipi di persone al mondo: quelli che si alzano presto alla mattina e quelli che vorrebbero sparargli.","Ed anche oggi come una gazzella mi alzo e so che dovrò correre più veloce della pipì se non me la voglio fare sotto.","I primi cinque giorni dopo il weekend sono i più duri da affrontare","E anche oggi si dorme domani...","L’uomo o la donna dei tuoi sogni esiste, devi solo dormire di più.","Certe mattine ti svegli con una voglia incredibile di ricominciare. A dormire","È un giorno nuovo: se devi fare qualcosa, mettici impegno; se non devi fare nulla, mettici stile.","Vivo con la speranza che qualche giorno i miei genitori mi dicano: in realtà noi siamo ricchi, ma volevamo insegnarti il senso dell’umiltà."]))
  
    elif message.content.startswith("!8ball"):
        await client.send_message(message.channel, random.choice(["Spero di no :8ball:","Ti piacerebbe :rofl: :8ball:","Se avessi tutte le risposte avrei già vinto al Superenalotto e sarei in una spiaggia tropicale a bere un cocktail alla faccia tua :tropical_drink: :8ball:","È desisamente così :8ball:","È difficile risponderti, prova di nuovo :8ball:","Meglio non risponderti adesso :8ball:","Non ci contare :8ball:","Le mie fonti dicono di no :8ball:","Sì :thumbsup: :8ball:","Assolutamente no :thumbsdown: :8ball:","Ci sono più probabilità che un aeroplano ti cada in testa :rofl: :8ball:","Le prospettive sono buone :8ball:","Ci puoi contare :8ball:","Vola basso e schiva i sassi, non avere obiettivi troppo alti :8ball:",]))
    elif message.content.startswith("!prova"):
      await client.add ({files: ["Trio.gif"]})

token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
