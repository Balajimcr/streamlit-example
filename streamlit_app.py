import streamlit as st

# Set page title and favicon
st.set_page_config(page_title="Marriage Compatibility Test", page_icon=":heart:")

# Define questions
questions = [
    "I feel loved and cared for by my partner.",
    "I feel comfortable sharing my thoughts and feelings with my partner.",
    "I trust my partner and feel secure in our relationship.",
    "My partner and I have similar values and goals in life."
]

# Define answer options
answer_options = ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]

# Define dictionary to store answers
answers = {}

# Display each question and collect answers
for i, question in enumerate(questions):
    st.write(f"**{i+1}. {question}**")
    selected_option = st.radio("", answer_options)
    answers[question] = selected_option

# Display submitted answers
if st.button("Submit"):
    st.write("Here are your submitted answers:")
    for question, answer in answers.items():
        st.write(f"- {question}: {answer}")
