import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Fallback responses when API is not available
FALLBACK_RESPONSES = {
    "greeting": "Hello! I'm here to provide mental health support and information. How are you feeling today?",
    "anxiety": "Anxiety is a common mental health concern. Some strategies that may help include deep breathing exercises, mindfulness meditation, regular exercise, and maintaining a consistent sleep schedule. It's important to talk to a mental health professional if anxiety is significantly impacting your daily life.",
    "depression": "Depression is a serious mental health condition that affects how you feel, think, and behave. Symptoms may include persistent sadness, loss of interest in activities, changes in appetite or sleep, and feelings of worthlessness. Professional help from a therapist or psychiatrist is crucial for effective treatment.",
    "stress": "Stress management techniques include regular exercise, deep breathing, progressive muscle relaxation, time management, setting boundaries, and practicing self-care. Finding what works best for you is key.",
    "sleep": "Good sleep hygiene includes maintaining a regular sleep schedule, creating a relaxing bedtime routine, avoiding screens before bed, keeping your bedroom cool and dark, and avoiding caffeine late in the day.",
    "loneliness": "Loneliness can be challenging. Consider reaching out to friends or family, joining clubs or groups with shared interests, volunteering, or seeking professional support. Remember that it's okay to ask for help.",
    "default": "I understand you're going through a difficult time. While I can provide general information, it's important to speak with a mental health professional for personalized support. Consider reaching out to a therapist, counselor, or your healthcare provider."
}

# Check if OpenAI is available
def is_openai_available():
    return bool(OPENAI_API_KEY)

# Get fallback response based on keywords
def get_fallback_response(query):
    query_lower = query.lower()
    
    if any(word in query_lower for word in ['anxiety', 'anxious', 'worry', 'nervous']):
        return FALLBACK_RESPONSES["anxiety"]
    elif any(word in query_lower for word in ['depression', 'depressed', 'sad', 'hopeless']):
        return FALLBACK_RESPONSES["depression"]
    elif any(word in query_lower for word in ['stress', 'stressed', 'overwhelmed']):
        return FALLBACK_RESPONSES["stress"]
    elif any(word in query_lower for word in ['sleep', 'insomnia', 'tired', 'rest']):
        return FALLBACK_RESPONSES["sleep"]
    elif any(word in query_lower for word in ['lonely', 'alone', 'isolated']):
        return FALLBACK_RESPONSES["loneliness"]
    elif any(word in query_lower for word in ['hello', 'hi', 'hey', 'how are you']):
        return FALLBACK_RESPONSES["greeting"]
    else:
        return FALLBACK_RESPONSES["default"]
