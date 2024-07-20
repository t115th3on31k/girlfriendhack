```python
import json
from textblob import TextBlob
from interpretation_engine.nlp_processing import processUserInput

class EmotionDetection:
    def __init__(self):
        self.emotion_keywords = {
            "happy": ["happy", "excited", "joyful", "amused", "delighted"],
            "sad": ["sad", "down", "unhappy", "depressed", "mournful"],
            "angry": ["angry", "mad", "irritated", "frustrated", "annoyed"],
            "anxious": ["anxious", "nervous", "worried", "stressed", "tense"],
            "surprised": ["surprised", "shocked", "astonished", "amazed"],
            "affectionate": ["affectionate", "loving", "fond", "tender", "caring"]
        }

    def detect_emotion(self, input_text):
        processed_input = processUserInput(input_text)
        analysis = TextBlob(processed_input)
        polarity = analysis.sentiment.polarity
        subjectivity = analysis.sentiment.subjectivity

        # Determine the most likely emotion based on keywords and sentiment analysis
        detected_emotions = {}
        for emotion, keywords in self.emotion_keywords.items():
            for keyword in keywords:
                if keyword in processed_input.lower():
                    detected_emotions[emotion] = detected_emotions.get(emotion, 0) + 1

        # Consider sentiment polarity
        if polarity > 0.1:
            detected_emotions['happy'] = detected_emotions.get('happy', 0) + 1
        elif polarity < -0.1:
            detected_emotions['sad'] = detected_emotions.get('sad', 0) + 1

        # Consider sentiment subjectivity
        if subjectivity > 0.5:
            detected_emotions['anxious'] = detected_emotions.get('anxious', 0) + 1

        # Sort emotions based on detection count
        sorted_emotions = sorted(detected_emotions.items(), key=lambda item: item[1], reverse=True)
        primary_emotion = sorted_emotions[0][0] if sorted_emotions else 'neutral'

        return json.dumps({
            'primary_emotion': primary_emotion,
            'all_emotions': detected_emotions,
            'polarity': polarity,
            'subjectivity': subjectivity
        })

# Example usage:
# emotion_detector = EmotionDetection()
# user_input = "I had a long day at work and I'm feeling quite tired."
# emotion_data = emotion_detector.detect_emotion(user_input)
# print(emotion_data)
```