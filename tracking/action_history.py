```python
import json
from datetime import datetime

class ActionHistory:
    def __init__(self, file_path='action_history.json'):
        self.file_path = file_path
        self.load_history()

    def load_history(self):
        try:
            with open(self.file_path, 'r') as file:
                self.history = json.load(file)
        except FileNotFoundError:
            self.history = []

    def save_history(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.history, file, indent=4)

    def log_action(self, actionData):
        action_record = {
            'timestamp': datetime.now().isoformat(),
            'action': actionData['action'],
            'outcome': actionData['outcome'],
            'feedback': actionData.get('feedback', '')
        }
        self.history.append(action_record)
        self.save_history()

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history = []
        self.save_history()

# Example usage:
# action_history = ActionHistory()
# action_history.log_action({
#     'action': 'Cooked her favorite meal',
#     'outcome': 'She was very happy and appreciated the effort',
#     'feedback': 'Positive'
# })
# print(action_history.get_history())
```