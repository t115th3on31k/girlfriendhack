```python
# prompts/predefined_prompts.py

class PredefinedPrompts:
    def __init__(self):
        self.prompts = [
            "She said she’s fine.",
            "She seemed distant.",
            "She mentioned she’s tired.",
            "She was really excited about her day.",
            "She’s been working late a lot.",
            "She’s been spending a lot of time with her friends.",
            "She’s been on her phone a lot.",
            "She said we need to talk.",
            "She asked for some space.",
            "She’s been really affectionate lately.",
            "She’s been talking about the future.",
            "She’s been really focused on her health.",
            "She’s been feeling really stressed.",
            "She’s been unusually quiet.",
            "She’s been laughing a lot more.",
            "She’s been very indecisive lately.",
            "She’s been very decisive lately.",
            "She’s been spending more time on hobbies.",
            "She’s been very supportive of my goals.",
            "She’s been asking for a lot of help."
        ]

    def get_prompt_list(self):
        return self.prompts

    def get_random_prompt(self):
        import random
        return random.choice(self.prompts)
```