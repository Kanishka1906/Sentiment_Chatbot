from agent_builder import build_agent
from conversation import Conversation
from sentiment import analyze_sentiment
import os

def main():
    # Check API Key
    if not os.getenv("GROQ_API_KEY"):
        print("Environment variable not set")
        return

    client = build_agent()
    print("How can I Assist You??")
    convo = Conversation()
    print("\nType 'quit' to end conversation and see analysis\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ['quit','exit']:
            break
        
        #entire conversation sentiment
        label, risk = analyze_sentiment(user_input)
        convo.add_user(user_input, label, risk)


        # each user statement sentiment
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are a compassionate and experienced sentiment analysis bot designed to engage users in a meaningful conversation about their feelings and emotions. Your primary goal is to help users maintain a positive mood when they express happiness and to gently guide them toward a brighter perspective when they are feeling sad or destructive.Respond in MAXIMUM 2 short lines. No explanations. No paragraphs."},
                    {"role": "user", "content": user_input}
                ]
            )
            
            bot_reply = response.choices[0].message.content
            print(f"Bot: {bot_reply}\n")
            convo.add_bot(bot_reply)

        except Exception as e:
            print("Groq API Error (bot reply skipped):")
            print(e, "\n")
            convo.add_bot("[Groq unavailable this turn]")

    #final mood flow
    convo.print_analysis()
    convo.print_mood_flow()
    print("\n" + convo.get_mood_summary())



if __name__ == "__main__":
    main()
