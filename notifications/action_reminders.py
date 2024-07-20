```python
import datetime
from notifications.notification_manager import NotificationManager

class ActionReminder:
    def __init__(self, user_preferences):
        self.notification_manager = NotificationManager()
        self.user_preferences = user_preferences

    def set_action_reminders(self, action_suggestions):
        for action in action_suggestions:
            reminder_time = self.calculate_reminder_time(action)
            self.schedule_reminder(reminder_time, action)

    def calculate_reminder_time(self, action):
        # This function calculates the best time to remind the user based on their preferences
        # For simplicity, we'll just set a default reminder time for now
        current_time = datetime.datetime.now()
        reminder_offset = datetime.timedelta(minutes=30)  # Remind after 30 minutes
        return current_time + reminder_offset

    def schedule_reminder(self, reminder_time, action):
        # This function schedules the reminder using the NotificationManager
        reminder_message = f"Remember to {action['description']} for your partner."
        self.notification_manager.schedule_notification(reminder_time, reminder_message)

    def send_action_reminders(self):
        # This function sends out the reminders that are due
        due_reminders = self.notification_manager.get_due_reminders()
        for reminder in due_reminders:
            self.notification_manager.send_notification(reminder['message'])

# Example usage:
# user_preferences = load_user_preferences()  # This function would load the user's preferences
# action_suggestions = get_action_suggestions()  # This function would retrieve the suggested actions
# action_reminder = ActionReminder(user_preferences)
# action_reminder.set_action_reminders(action_suggestions)
# action_reminder.send_action_reminders()
```

Please note that this code assumes the existence of a `NotificationManager` class with methods `schedule_notification`, `get_due_reminders`, and `send_notification`, which handle the scheduling and sending of notifications. The `load_user_preferences` and `get_action_suggestions` functions are placeholders for the actual implementation that would retrieve user preferences and action suggestions, respectively.