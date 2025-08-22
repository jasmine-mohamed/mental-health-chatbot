# Simple document chat with local responses
def query_documents(user_query: str) -> str:
    """Get a response based on the user's query using local knowledge."""
    query_lower = user_query.lower()
    
    # Mental health topic detection and responses
    if any(word in query_lower for word in ['anxiety', 'anxious', 'worry', 'nervous', 'panic']):
        return "Anxiety is a common mental health concern. Some strategies that may help include deep breathing exercises, mindfulness meditation, regular exercise, and maintaining a consistent sleep schedule. It's important to talk to a mental health professional if anxiety is significantly impacting your daily life."
    
    elif any(word in query_lower for word in ['depression', 'depressed', 'sad', 'hopeless', 'worthless', 'empty']):
        return "Depression is a serious mental health condition that affects how you feel, think, and behave. Symptoms may include persistent sadness, loss of interest in activities, changes in appetite or sleep, and feelings of worthlessness. Professional help from a therapist or psychiatrist is crucial for effective treatment."
    
    elif any(word in query_lower for word in ['stress', 'stressed', 'overwhelmed', 'pressure']):
        return "Stress management techniques include regular exercise, deep breathing, progressive muscle relaxation, time management, setting boundaries, and practicing self-care. Finding what works best for you is key."
    
    elif any(word in query_lower for word in ['sleep', 'insomnia', 'tired', 'rest', 'bed']):
        return "Good sleep hygiene includes maintaining a regular sleep schedule, creating a relaxing bedtime routine, avoiding screens before bed, keeping your bedroom cool and dark, and avoiding caffeine late in the day."
    
    elif any(word in query_lower for word in ['lonely', 'alone', 'isolated', 'friendless']):
        return "Loneliness can be challenging. Consider reaching out to friends or family, joining clubs or groups with shared interests, volunteering, or seeking professional support. Remember that it's okay to ask for help."
    
    elif any(word in query_lower for word in ['hello', 'hi', 'hey', 'how are you', 'start']):
        return "Hello! I'm here to provide mental health support and information. How are you feeling today? You can ask me about anxiety, depression, stress management, or any other mental health topics. Remember, I'm here to help, but I'm not a replacement for professional medical advice."
    
    elif any(word in query_lower for word in ['suicide', 'kill myself', 'end it all', 'want to die']):
        return "If you're having thoughts of suicide, please know that you're not alone and help is available. Please call 988 (Suicide & Crisis Lifeline) immediately, or go to your nearest emergency room. Your life has value and there are people who want to help you."
    
    elif any(word in query_lower for word in ['self harm', 'cutting', 'hurting myself']):
        return "Self-harm is a serious concern that indicates you're in emotional pain. Please reach out for professional help immediately. Consider calling a crisis hotline or speaking with a mental health professional. You deserve support and care."
    
    else:
        return "I understand you're going through a difficult time. While I can provide general information, it's important to speak with a mental health professional for personalized support. Consider reaching out to a therapist, counselor, or your healthcare provider. If you're in crisis, please call 988 for immediate support."
