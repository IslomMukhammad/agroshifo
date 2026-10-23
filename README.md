# 🌱 AgroShifo — AI-Powered Agronomist Telegram Bot

**AgroShifo** is an intelligent Telegram bot designed to assist farmers, gardeners, and agricultural specialists by identifying plant diseases, solving agricultural problems, and providing instant AI-driven consultations.

---

## ✨ Key Features

- 🤖 **AI Consultation:** Powered by artificial intelligence to provide expert advice on plant care, disease diagnosis, and pest control (`ai_api.py`, `ai_logic.py`).
- 💬 **Interactive Chat:** Seamless text-based interaction system for answering user queries in real time (`chat_hd.py`, `ai_hd.py`).
- 🔐 **Mandatory Subscription System:** Custom middleware that verifies whether users are subscribed to required channels before using the bot (`sub_middleware.py`, `subscibe_kb.py`).
- 🛠 **Admin Dashboard:** Dedicated administrative panel to monitor user statistics and manage bot operations (`admin_hd.py`, `admin_kb.py`).
- 🗄 **Database Management:** Reliable local storage of user profiles, daily usage dates, and AI request limits using SQLite (`users_db.py`, `users.db`).

---

## 📂 Project Structure

```text
agro-ai-bot/
├── admin/                  # Admin panel handlers and keyboards
│   ├── admin_hd.py
│   └── admin_kb.py
├── api/                    # External AI API integration
│   └── ai_api.py
├── components/             # Static texts and message templates
│   └── texts.py
├── database/               # SQLite database operations
│   └── users_db.py
├── handlers/               # User message and callback handlers
│   ├── ai_hd.py
│   ├── chat_hd.py
│   ├── privacy_hd.py
│   └── start_hd.py
├── keyboards/              # Reply and Inline keyboards
│   ├── main_kb.py
│   └── subscibe_kb.py
├── logic/                  # Core business logic and middlewares
│   ├── ai_logic.py
│   └── sub_middleware.py
├── bot.py                  # Main entry point to run the bot
├── config.py               # Configuration and secret keys
└── Pipfile                 # Pipenv dependency manifest

## Islom Mukhammad
```
