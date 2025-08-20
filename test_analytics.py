# test_analytics.py

from chatbot_app.modules import analytics

# Simulate fake data
analytics.log_interaction(
    user_input="What is AI?",
    bot_response="AI stands for Artificial Intelligence.",
    sentiment="neutral"
)

analytics.log_interaction(
    user_input="I love this bot!",
    bot_response="Thank you!",
    sentiment="positive"
)

analytics.log_interaction(
    user_input="You're not helpful.",
    bot_response="I'm sorry to hear that. I'll try to improve.",
    sentiment="negative"
)

# Show dashboard
import streamlit as st
analytics.display_dashboard()
