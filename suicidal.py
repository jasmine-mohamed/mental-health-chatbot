from typing import List

crisis_words: List[str]=[
    "suicide",
    "suicidal",
    "die",
    "I want to die",
    "I don't want to live anymore",
    "I'm thinking of killing myself",
    "I'm suicidal",
    "I want to end it all",
    "No reason to go on",
    "Tired of living",
    "Would be better off dead",
    "Wish I never existed",
    "I'm done with everything",
    "I want to cut myself",
    "I'm hurting myself",
    "I need to feel pain",
    "I just cut again",
    "Bleeding makes it better",
    "I deserve pain",
    "I can’t stop hurting myself",
    "There's no hope",
    "Nothing matters",
    "I'm completely empty",
    "I feel dead inside",
    "I'm broken",
    "I can't take it anymore",
    "I'm at my breaking point",
    "I can't breathe",
    "My heart is racing",
    "I'm freaking out",
    "Everything is closing in",
    "I feel like I'm dying",
    "Nobody cares",
    "I'm all alone",
    "No one would notice if I disappeared",
    "I’m invisible",
    "I need a drink to forget",
    "I took something to feel numb",
    "Only pills help",
    "I'm high again and I don't care"
]

help_message = (
    "I'm really sorry you're feeling this way. You're not alone, and there are people who care about you and want to help.\n\n"
    "If you're in crisis or need someone to talk to immediately, please consider reaching out to one of the following resources in Egypt:\n\n"
    "📞 *Ministry of Health Mental Health Hotline (24/7)*: 080-088-80700\n"
    "📞 *General Suicide Prevention Line*: 0220816831 or 0220816830\n"
    "📱 *Instagram-based peer support*: @Shezlong or @EmpowerMentalHealth\n\n"
    "🧠 You can also speak to a trusted friend, family member, teacher, or doctor.\n\n"
    "You're stronger than you think. Help is here for you, and things can get better. Please don’t hesitate to reach out. 💙"
)


def contains_crisis_keywords(text:str) -> bool:
    text_lower=text.lower()
    return any(keyword in text_lower for keyword in crisis_words )
