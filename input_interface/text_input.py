```python
# input_interface/text_input.py

from interpretation_engine.nlp_processing import processUserInput

# Define a function to capture text input from the user
def capture_text_input():
    # Prompt the user to enter what their girlfriend has said
    input_text = input("Enter what your girlfriend has said: ")
    return input_text

# Define a function to handle the submission of text input
def submit_text_input():
    # Capture the user's text input
    user_input_text = capture_text_input()
    
    # Process the user input using the NLP processing function
    processUserInput(user_input_text)

# If this script is run as the main program, prompt for text input
if __name__ == "__main__":
    submit_text_input()
```