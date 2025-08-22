import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import random

load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

# Warm, empathetic responses when API is not available
FALLBACK_RESPONSES = {
    "greeting": [
        "Hi there! 💙 I'm so glad you reached out. How are you really feeling today? I'm here to listen and support you.",
        "Hello! 💙 It's wonderful that you're here. What's on your mind today? I'm ready to listen.",
        "Hey there! 💙 I'm so happy you decided to chat. How are you doing right now?",
        "Hi! 💙 Thanks for reaching out. I'm here to listen and support you. What would you like to talk about?"
    ],
    "anxiety": [
        "I can hear how overwhelming this anxiety feels right now. It's completely normal to feel this way, and you're not alone. 💙\n\nSome gentle things that might help:\n• Take a few slow, deep breaths with me\n• Try some gentle stretching or a short walk\n• Write down what's worrying you\n• Talk to someone you trust\n\nRemember, it's okay to ask for help. If this anxiety is really affecting your daily life, talking to a mental health professional can make such a difference. You deserve support!",
        "Anxiety can feel like a storm inside, and I want you to know that storms pass. 💙\n\nRight now, try:\n• Placing one hand on your chest, one on your belly\n• Breathe in for 4 counts, hold for 4, out for 6\n• Name 5 things you can see around you\n• Remember: this feeling won't last forever\n\nYou're doing amazing just by being here and asking for help. That takes real courage."
    ],
    "depression": [
        "I'm so sorry you're going through this. Depression can feel like carrying a heavy weight, and it's not your fault. 💙\n\nYou're incredibly brave for reaching out. Some things that might help:\n• Be gentle with yourself - you don't have to be 'productive' right now\n• Try to maintain small routines, even just getting out of bed\n• Reach out to friends or family, even if it's hard\n• Consider talking to a therapist or counselor\n\nYou matter, and your feelings are valid. Professional help can be life-changing - you deserve to feel better.",
        "Depression is like wearing dark glasses - it colors everything you see. But those glasses can come off. 💙\n\nToday, try one small thing:\n• Maybe just sit outside for 5 minutes\n• Or text a friend 'hi'\n• Or make your favorite comfort food\n\nEvery tiny step counts. You're not broken - you're healing. And healing takes time and patience."
    ],
    "stress": [
        "Oh, I can feel how overwhelmed you are right now. Stress can be absolutely exhausting, and it's okay to acknowledge that. 💙\n\nLet's take this one step at a time:\n• What's one small thing you can do for yourself today?\n• Maybe try some deep breathing or gentle movement\n• Set some boundaries - you can't pour from an empty cup\n• Remember to be kind to yourself\n\nYou're doing the best you can, and that's enough. Sometimes the most important thing is just getting through the day.",
        "Stress is like carrying too many grocery bags - eventually something's going to drop. 💙\n\nRight now, let's lighten your load:\n• What can you say 'no' to today?\n• Can you ask someone for help?\n• Maybe take a 10-minute break to just breathe?\n\nYou don't have to carry everything alone. It's okay to put some bags down."
    ],
    "sleep": [
        "I know how frustrating it is when sleep won't come. Those long nights can feel endless, and it's so hard to function when you're exhausted. 💙\n\nSome gentle things to try:\n• Create a cozy bedtime routine - maybe some soft music or a warm drink\n• Keep your room cool and dark\n• Try to avoid screens an hour before bed\n• If you can't sleep, don't force it - get up and do something calming\n\nSleep struggles are really common, and they can make everything else feel harder. You're not alone in this.",
        "Sleep is like a shy friend - the more you chase it, the more it runs away. 💙\n\nInstead of chasing, try:\n• Reading something boring (seriously, it works!)\n• Progressive muscle relaxation\n• A warm bath or shower\n• Writing down your thoughts to clear your mind\n\nRemember: even if you don't sleep well tonight, your body will catch up. You're stronger than you think."
    ],
    "loneliness": [
        "I can feel how isolating this loneliness is. It's such a heavy feeling, and it's completely valid. 💙\n\nYou're not alone in feeling alone. Some gentle suggestions:\n• Reach out to someone you trust, even if it feels scary\n• Join a group or class for something you're interested in\n• Consider volunteering - helping others can help us feel connected\n• Remember that it's okay to ask for help\n\nLoneliness is really hard, and you don't have to go through it alone. Professional support can be incredibly helpful too.",
        "Loneliness is like being in a crowded room but feeling invisible. But you're not invisible to me. 💙\n\nToday, try:\n• Sending a 'thinking of you' text to someone\n• Joining an online community about something you love\n• Calling a family member just to chat\n• Remembering that this feeling won't last forever\n\nConnection is like a muscle - the more you use it, the stronger it gets."
    ],
    "name": [
        "Nice to meet you, Jasmine! 💙 That's such a beautiful name. I'm here to listen and support you. What would you like to talk about today?",
        "Hi Jasmine! 💙 I love that name - it reminds me of flowers and sunshine. I'm so glad you're here. How are you feeling right now?",
        "Jasmine! 💙 What a lovely name to meet. I'm here to be your listening ear and support. What's on your mind today?"
    ],
    "confusion": [
        "I know it can be frustrating when things don't make sense. 💙 Let me try to help. Can you tell me more about what's confusing you? I'm here to listen and figure this out together.",
        "I want to make sure I understand you correctly. 💙 Sometimes I need a little more context to give you the best support. Can you explain what you mean?",
        "I'm here to help, but I want to make sure I'm understanding you right. 💙 Can you tell me more about what you're looking for?"
    ],
    "default": [
        "I can hear that you're going through something difficult, and I want you to know that your feelings matter. 💙\n\nWhile I'm here to listen and support you, sometimes we need more specialized help. Consider reaching out to a mental health professional - they have the training to help you navigate what you're experiencing.\n\nYou're not alone, and you deserve support. What's one small thing you can do to take care of yourself today?",
        "I'm here to listen and support you through whatever you're going through. 💙\n\nSometimes the best thing we can do is talk about what's on our minds. What would be most helpful for you right now? I'm ready to listen.",
        "I want you to know that whatever you're feeling is valid, and you don't have to go through it alone. 💙\n\nI'm here to listen and support you. What's on your heart today? Sometimes just talking about it can help."
    ]
}

def get_fallback_response(query):
    query_lower = query.lower()
    
    # Check for name mentions
    if any(name in query_lower for name in ['jasmine', 'my name is', 'i am', 'call me']):
        return random.choice(FALLBACK_RESPONSES["name"])
    
    # Check for confusion or unclear input
    if any(word in query_lower for word in ['what', 'huh', 'confused', 'don\'t understand', 'unclear']):
        return random.choice(FALLBACK_RESPONSES["confusion"])
    
    # Check for specific mental health topics
    if any(word in query_lower for word in ['anxiety', 'anxious', 'worry', 'nervous', 'panic', 'scared']):
        return random.choice(FALLBACK_RESPONSES["anxiety"])
    elif any(word in query_lower for word in ['depression', 'depressed', 'sad', 'hopeless', 'worthless', 'empty', 'down']):
        return random.choice(FALLBACK_RESPONSES["depression"])
    elif any(word in query_lower for word in ['stress', 'stressed', 'overwhelmed', 'burnout', 'exhausted', 'tired']):
        return random.choice(FALLBACK_RESPONSES["stress"])
    elif any(word in query_lower for word in ['sleep', 'insomnia', 'tired', 'rest', 'bed', 'awake']):
        return random.choice(FALLBACK_RESPONSES["sleep"])
    elif any(word in query_lower for word in ['lonely', 'alone', 'isolated', 'disconnected', 'no friends']):
        return random.choice(FALLBACK_RESPONSES["loneliness"])
    elif any(word in query_lower for word in ['hello', 'hi', 'hey', 'how are you', 'good morning', 'good afternoon', 'greetings']):
        return random.choice(FALLBACK_RESPONSES["greeting"])
    else:
        return random.choice(FALLBACK_RESPONSES["default"])

#bykhazen session l kol user
session_memory_map={}

def get_response(session_id:str,user_query:str) ->str:
    if not OPENAI_API_KEY:
        return get_fallback_response(user_query)
    
    try:
        if session_id not in session_memory_map:
            llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.7)
            memory = ConversationBufferMemory()
            session_memory_map[session_id] = ConversationChain(llm=llm, memory=memory, verbose=False)
        
        conversation = session_memory_map[session_id]    
        return conversation.predict(input=user_query)
    except Exception as e:
        print(f"OpenAI API error: {e}")
        return get_fallback_response(user_query)