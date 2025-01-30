from telethon import TelegramClient, events
from datetime import datetime

# Vos identifiants API Telegram
api_id = "26773187"
api_hash = "8e7bee094423bdab3c3fba3a33064022"
bot_token = '8024994242:AAESzFYndmg-Eo5Tdg3aJP06WZg4wsYAE0c'

# L'ID de votre canal
CANAL_ID = -1002096587825

# Le footer que vous souhaitez ajouter
FOOTER = """
------------------
📱 Rejoignez-nous:
• Telegram: t.me/votre_canal
• Twitter: twitter.com/votre_compte
• Instagram: instagram.com/votre_compte
"""

# Création du client
client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Bot démarré! Je vais ajouter automatiquement le footer à vos messages.')

@client.on(events.NewMessage(chats=CANAL_ID))  # Utilisation directe de l'ID numérique
async def add_footer(event):
    try:
        # Vérifie si le message ne contient pas déjà le footer
        if FOOTER not in event.message.message:
            # Ajoute le footer au message
            new_message = event.message.message + "\n" + FOOTER
            
            # Modifie le message
            await event.message.edit(new_message)
            print(f"Footer ajouté avec succès au message")
    except Exception as e:
        print(f"Erreur lors de l'ajout du footer: {str(e)}")

async def check_channel_access():
    try:
        # Vérifie si le bot a accès au canal
        channel = await client.get_entity(CANAL_ID)
        print(f"Connexion réussie au canal: {channel.title}")
        return True
    except Exception as e:
        print(f"Erreur d'accès au canal: {str(e)}")
        return False

async def main():
    print("Bot en cours de démarrage...")
    
    # Vérifie l'accès au canal
    if await check_channel_access():
        print(f"Bot démarré et connecté au canal {CANAL_ID}")
        print("En attente de nouveaux messages...")
    else:
        print("Erreur: Impossible d'accéder au canal. Vérifiez que:")
        print("1. L'ID du canal est correct")
        print("2. Le bot est membre du canal")
        print("3. Le bot a les droits d'administrateur sur le canal")
        return
    
    # Maintient le bot en fonctionnement
    await client.run_until_disconnected()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())