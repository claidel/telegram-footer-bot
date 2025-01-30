from telethon import TelegramClient, events
import logging
import asyncio

# Configuration du logging pour voir les détails
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Vos identifiants
api_id = 26773187
api_hash = "8e7bee094423bdab3c3fba3a33064022"
bot_token = '8024994242:AAESzFYndmg-Eo5Tdg3aJP06WZg4wsYAE0c'
CANAL_ID = -1002096587825

# Le footer à ajouter
FOOTER = """
------------------
📱 Rejoignez-nous:
• Telegram: t.me/votre_canal
• Twitter: twitter.com/votre_compte
• Instagram: instagram.com/votre_compte
"""

# Création du client
client = TelegramClient('bot_session_test', api_id, api_hash)

async def check_channel_access():
    try:
        channel = await client.get_entity(CANAL_ID)
        logger.info(f"✅ Accès réussi au canal: {channel.title}")
        return True
    except Exception as e:
        logger.error(f"❌ Erreur d'accès au canal: {str(e)}")
        return False

@client.on(events.NewMessage(chats=CANAL_ID))
async def add_footer(event):
    try:
        logger.info("📝 Nouveau message détecté dans le canal")
        if FOOTER not in event.message.message:
            new_message = event.message.message + "\n" + FOOTER
            await event.message.edit(new_message)
            logger.info("✅ Footer ajouté avec succès")
        else:
            logger.info("ℹ️ Le message contient déjà le footer")
    except Exception as e:
        logger.error(f"❌ Erreur lors de l'ajout du footer: {str(e)}")

async def main():
    try:
        await client.start(bot_token=bot_token)
        logger.info("✅ Bot connecté avec succès")
        
        me = await client.get_me()
        logger.info(f"Bot info: @{me.username}")
        
        if await check_channel_access():
            logger.info("🚀 Bot prêt à ajouter des footers")
            logger.info("📢 Envoyez un message dans le canal pour tester")
            await client.run_until_disconnected()
        else:
            logger.error("❌ Impossible d'accéder au canal, vérification nécessaire")
    except Exception as e:
        logger.error(f"❌ Erreur générale: {str(e)}")

if __name__ == '__main__':
    asyncio.run(main())