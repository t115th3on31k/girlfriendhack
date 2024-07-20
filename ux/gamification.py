```python
# ux/gamification.py

class GamificationSystem:
    def __init__(self):
        self.user_points = 0
        self.badges = []
        self.actions_completed = 0

    def add_points(self, points):
        self.user_points += points
        self.check_for_badges()

    def check_for_badges(self):
        # Check the number of points and actions completed to award badges
        if self.user_points > 50 and 'Bronze Partner' not in self.badges:
            self.badges.append('Bronze Partner')
        if self.user_points > 100 and 'Silver Partner' not in self.badges:
            self.badges.append('Silver Partner')
        if self.user_points > 200 and 'Gold Partner' not in self.badges:
            self.badges.append('Gold Partner')
        if self.actions_completed > 10 and 'Active Listener' not in self.badges:
            self.badges.append('Active Listener')
        if self.actions_completed > 20 and 'Empathy Guru' not in self.badges:
            self.badges.append('Empathy Guru')

    def complete_action(self):
        self.actions_completed += 1
        self.add_points(10)  # Add points for completing an action

    def get_user_stats(self):
        return {
            'points': self.user_points,
            'badges': self.badges,
            'actions_completed': self.actions_completed
        }

    def display_badges(self):
        # This function would be used to update the UI with the badges earned
        # For example, it could update a user profile section with new badges
        pass

# Example usage:
# gamification = GamificationSystem()
# gamification.complete_action()
# user_stats = gamification.get_user_stats()
# print(user_stats)
```