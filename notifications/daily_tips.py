```python
import random
from datetime import datetime
import json

# Assuming there is a function to send notifications to the user's device
from notifications.notification_sender import send_notification_to_user

# Shared dependency: userPreferences
from user_preferences import userPreferences

# Daily tips content
DAILY_TIPS = [
    "Remember to express gratitude for the little things your partner does.",
    "Surprise your partner with their favorite treat as a thoughtful gesture.",
    "Plan a spontaneous date night to break the routine and enjoy each other's company.",
    "Give your partner a sincere compliment about a trait you admire.",
    "Offer to take on a task your partner usually handles to give them a break.",
    "Write a love note and hide it somewhere for your partner to find.",
    "Spend quality time together without distractions, like phones or TV.",
    "Listen actively when your partner is sharing their thoughts or feelings.",
    "Show affection with a warm hug or a gentle touch to strengthen your bond.",
    "Take a moment to reminisce about a happy memory you share.",
    "Encourage your partner's dreams and support their goals.",
    "Be patient and understanding during disagreements, seeking to resolve conflicts amicably.",
    "Plan a future adventure together to create excitement and anticipation.",
    "Show interest in your partner's hobbies or activities, even if they're not your own.",
    "Practice forgiveness and let go of small annoyances for a happier relationship."
]

def get_daily_tip():
    # Select a random tip from the list
    tip_of_the_day = random.choice(DAILY_TIPS)
    return tip_of_the_day

def send_daily_tip():
    # Get the current date
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # Check if the user has enabled daily tips in their preferences
    if userPreferences.get('dailyTipsEnabled', False):
        # Get the daily tip
        tip = get_daily_tip()
        
        # Prepare the notification content
        notification_content = {
            "title": "Daily Love Tip",
            "body": tip,
            "date": current_date
        }
        
        # Convert the content to JSON format
        notification_json = json.dumps(notification_content)
        
        # Send the notification to the user
        send_notification_to_user(notification_json)

# Call the function to send the daily tip
send_daily_tip()
```