from telethon import TelegramClient, events
from datetime import datetime

# Vos identifiants API Telegram (à obtenir sur https://my.telegram.org/auth)
api_id = "26773187"  # Remplacez par votre API_ID
api_hash = "8e7bee094423bdab3c3fba3a33064022"  # Remplacez par votre API_HASH
bot_token = '8024994242:AAESzFYndmg-Eo5Tdg3aJP06WZg4wsYAE0c'

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

@client.on(events.NewMessage(chats='-1002096587825'))
async def add_footer(event):
    # Vérifie si le message ne contient pas déjà le footer
    if FOOTER not in event.message.message:
        # Ajoute le footer au message
        new_message = event.message.message + "\n" + FOOTER
        
        # Modifie le message
        await event.message.edit(new_message)

def main():
    print("Bot démarré...")
    client.run_until_disconnected()

if __name__ == '__main__':
    main()
