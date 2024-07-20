```python
# feedback/user_reviews.py

class UserReview:
    def __init__(self, action_id, user_rating, user_comment):
        self.action_id = action_id
        self.user_rating = user_rating
        self.user_comment = user_comment

    def to_dict(self):
        return {
            'action_id': self.action_id,
            'user_rating': self.user_rating,
            'user_comment': self.user_comment
        }


class UserReviewsDatabase:
    def __init__(self):
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def get_reviews_for_action(self, action_id):
        return [review.to_dict() for review in self.reviews if review.action_id == action_id]

    def get_average_rating_for_action(self, action_id):
        ratings = [review.user_rating for review in self.reviews if review.action_id == action_id]
        return sum(ratings) / len(ratings) if ratings else 0


# Example usage:
# user_reviews_db = UserReviewsDatabase()
# user_reviews_db.add_review(UserReview(action_id=1, user_rating=5, user_comment="It worked wonders!"))
# user_reviews_db.add_review(UserReview(action_id=1, user_rating=4, user_comment="Pretty good suggestion."))
# average_rating = user_reviews_db.get_average_rating_for_action(action_id=1)
# print(f"Average Rating for Action 1: {average_rating}")
# reviews_for_action = user_reviews_db.get_reviews_for_action(action_id=1)
# print(f"Reviews for Action 1: {reviews_for_action}")
```