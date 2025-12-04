from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Message:
    role: str
    text: str
    label: Optional[str] = None
    risk: Optional[str] = None

@dataclass
class Conversation:
    messages: List[Message] = field(default_factory=list)

    def add_user(self, text, label, risk=None):
        self.messages.append(Message("user", text, label, risk))
    
    def add_bot(self, text):
        self.messages.append(Message("bot", text))

    def get_overall_sentiment(self):
        user_msgs = [m for m in self.messages if m.role == "user"]

        if not user_msgs:
            return "Neutral"

        # High-risk override
        if any(m.risk == "HIGH" for m in user_msgs):
            return "Negative (High Risk)"

        counts = {"Positive": 0, "Negative": 0, "Neutral": 0}

        for m in user_msgs:
            counts[m.label] += 1

        if counts["Negative"] > counts["Positive"]:
            return "Negative"
        elif counts["Positive"] > counts["Negative"]:
            return "Positive"
        else:
            return "Neutral"

    def get_mood_flow(self):
        """
        Returns chronological mood flow of user messages.
        Example: ['Neutral', 'Negative', 'Negative (High Risk)']
        """
        flow = []

        for m in self.messages:
            if m.role == "user":
                if m.risk == "HIGH":
                    flow.append("Negative (High Risk)")
                else:
                    flow.append(m.label)

        return flow

    def get_mood_summary(self):
        flow = self.get_mood_flow()

        if not flow:
            return "No mood data available."
        simplified = [flow[0]]
        for mood in flow[1:]:
            if mood != simplified[-1]:
                simplified.append(mood)
        if len(simplified) == 1:
            return f"Mood remained {simplified[0]} throughout the conversation."

        path = " to ".join(simplified)
        return f"Mood went from {path}."

    def print_analysis(self):
        print("\n" + "-"*60)
        print("FINAL CONVERSATION ANALYSIS")
        print("-"*60)

        for msg in self.messages:
            if msg.role == "user":
                print(f"User: '{msg.text}'")
                print(f"Sentiment: {msg.label}")
                if msg.risk == "HIGH":
                    print("Risk: HIGH (dangerous language)")

        overall = self.get_overall_sentiment()
        print(f"\nOverall sentiment: {overall}")
        print("-"*60)

    def print_mood_flow(self):
        flow = self.get_mood_flow()

        if not flow:
            print("\nMood Flow: No data\n")
            return

        print("\nMOOD FLOW:")
        print(" → ".join(flow))
