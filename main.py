import time
import schedule
import requests

# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, json=payload)

def remind(message):
    print(f"Reminder: {message}")
    send_telegram_message(f"Reminder: {message}")

def schedule_reminder(time_str, message, repeat=False):
    if repeat:
        schedule.every().day.at(time_str).do(remind, message=message)
    else:
        schedule.every().day.at(time_str).do(lambda: (remind(message), schedule.clear(time_str)))

if __name__ == "__main__":
    # Example reminders
    schedule_reminder("14:30", "Take a break!", repeat=True)
    schedule_reminder("16:00", "Meeting with team", repeat=False)
    
    while True:
        schedule.run_pending()
        time.sleep(60)
