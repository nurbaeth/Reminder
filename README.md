# Simple Reminder 

## Overview
Simple Reminder is a Python-based tool that allows users to set one-time and recurring reminders. It sends notifications via Telegram and runs continuously in the background.

## Features
- Set one-time reminders
- Set recurring daily reminders
- Sends notifications via Telegram
- Runs in the background and checks reminders every minute

## Installation   
1. Clone this repository: 
   ```bash
   git clone https://github.com/yourusername/simple-reminder.git 
   cd simple-reminder
   ```    
2. Install dependencies:      
   ```bash 
   pip install schedule requests   
   ```  
 
## Configuration
1. Open `simple_reminder.py` and replace `YOUR_BOT_TOKEN` with your actual Telegram bot token.
2. Replace `YOUR_CHAT_ID` with your Telegram chat ID.

## Usage
Run the script with:
```bash
python simple_reminder.py
```

The script will run in the background and send reminders to your Telegram.

## Example
Modify the script to add new reminders:
```python
schedule_reminder("14:30", "Take a break!", repeat=True)
schedule_reminder("16:00", "Meeting with team", repeat=False)
```

## License
This project is licensed under the MIT License.

