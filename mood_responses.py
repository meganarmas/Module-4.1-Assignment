def mood_response(mood):
    responses = {
        'happy': "That is great to hear!",
        'sad': "Sorry to hear that - I hope your day gets better!",
        'sick': "I hope you feel better soon!",
        'anxious': "What is wrong?",
        'angry': "I am very sorry to hear that, do you want to talk about it?'",
        'sleepy': "Get some sleep and take it easy for the rest of the day.",
    }
    return responses.get(mood.lower(), "That mood is not in the dictionary.")