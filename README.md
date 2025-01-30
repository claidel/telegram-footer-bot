# Bot Telegram avec Footer Automatique

Ce bot permet d'ajouter automatiquement un footer personnalisé à tous les messages publiés sur votre canal Telegram.

## Fonctionnalités

- Ajout automatique d'un footer personnalisable
- Détection des messages sans footer
- Support des liens vers vos réseaux sociaux

## Prérequis

- Python 3.7 ou supérieur
- Un compte Telegram
- Les identifiants API Telegram (api_id et api_hash)
- Un token de bot Telegram (si vous utilisez un bot)

## Installation

1. Clonez ce repository :
```bash
git clone https://github.com/claidel/telegram-footer-bot.git
cd telegram-footer-bot
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## Configuration

1. Obtenez vos identifiants API Telegram :
   - Rendez-vous sur https://my.telegram.org/auth
   - Créez une application
   - Notez votre `api_id` et `api_hash`

2. Si vous utilisez un bot :
   - Créez un bot via @BotFather sur Telegram
   - Notez le token du bot

3. Modifiez le fichier `telegram_bot.py` :
   - Remplacez `VOTRE_API_ID`, `VOTRE_API_HASH` et `VOTRE_BOT_TOKEN`
   - Personnalisez le `FOOTER` avec vos propres liens
   - Remplacez `VOTRE_CANAL_ID` par l'ID de votre canal

## Utilisation

Lancez le bot :
```bash
python telegram_bot.py
```

Le bot ajoutera automatiquement votre footer à chaque nouveau message publié sur votre canal.

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.

## Licence

Ce projet est sous licence MIT.