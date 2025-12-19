# Chatbot with Sentiment Analysis

## Overview
This project is an interactive chatbot that analyzes emotional sentiment during conversation.
It maintains full chat history and produces an overall sentiment summary at the end of the session (Tier 1).
It also analyzes and displays sentiment for each individual user message (Tier 2).

## Features
- Conversation history tracking
- Per-message sentiment classification (Tier 2)
- Final conversation-level emotional summary (Tier 1)
- Mood transition summary
- Risk detection for harmful language
- Command-line chatbot interface
- Modular and structured codebase

## Tech Stack / Chosen Technologies
- **Language:** Python 3
- **Sentiment Analysis:** HuggingFace Transformers (DistilBERT)
- **Chatbot Engine:** Groq LLM API
- **Other Libraries:**
  - `torch` for model execution
  - `transformers` for NLP
  - `python-dotenv` for API key management

## How to Run

1. **Install dependencies**
    *pip install -r requirements.txt*
2. **Set up environment file**
Create a file named `.env` and add:
   *GROQ_API_KEY=your_api_key*

3. **Run the program**
    *python main.py*

4. **Exit**
Type `quit` to end the conversation and view the final sentiment analysis.

## Sentiment Logic
The chatbot uses a hybrid approach for sentiment detection:
- A transformer-based NLP model classifies each message
- Risk-related keywords detect harmful or dangerous language
- Stress terms adjust emotional labeling
- All messages are stored and later aggregated
- A final mood summary shows emotional movement

## Tier Implementation Status
- Tier 1 (Conversation-Level Sentiment): Implemented  
- Tier 2 (Statement-Level Sentiment): Implemented  
- Mood Trend Summary: Added  

## Note
API keys are not stored in the repository and must be supplied through environment variables.
The project is designed with secure coding and modular architecture in mind.

