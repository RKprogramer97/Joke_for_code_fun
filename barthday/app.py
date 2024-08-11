import pywhatkit as kit
import schedule
import time
from datetime import datetime

from flask import Flask

app = Flask(__name__)

@app.route('/')
def send_birthday_wish(name, phone_number):
    current_date = datetime.now().strftime("%d %B %Y")
    
    message = f"""
    ***************************************************
    *                                                 *
    *  🎉🎂🎁 Happy Birthday, {name}! 🎁🎂🎉  *
    *                                                 *
    ***************************************************
    
    Dear {name},

    On this wonderful day, I just wanted to send you a special birthday message 
    filled with love and joy. I hope your day is as amazing and beautiful as you are.
    
    May your birthday be the start of a year filled with good luck, good health, and much happiness.
    
    Here’s to celebrating you! 🥂
    
    Sending you all my love on your special day,
    [Your Name]
    
    P.S. Don’t forget to make a wish! 🌠

    Date: {current_date}
    """
    
    kit.sendwhatmsg(phone_number, message, 0, 0)  # Send message at 00:00

# Schedule the task to send the message at 12:00 AM
def schedule_birthday_wish(name, phone_number):
    schedule.every().day.at("00:00").do(send_birthday_wish, name, phone_number)
    while True:
        schedule.run_pending()
        time.sleep(1)

# Example usage
# phone_number = "+1234567890"  # Use the recipient's phone number in international format
# name = "Alice"

# Schedule the birthday wish
# schedule_birthday_wish(name, phone_number)


if __name__ == '__main__':
    app.run(debug=True)


