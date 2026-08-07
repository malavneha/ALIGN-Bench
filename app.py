import streamlit as st
import pandas as pd

from evaluator import evaluate_response

st.set_page_config(
    page_title="ALIGN-Bench",
    layout="wide"
)

st.title("ALIGN-Bench")

st.subheader(
    "Evaluate Clarification Behaviour in Large Language Models"
)

df = pd.read_csv("benchmark.csv")

question = st.selectbox(
    "Choose Question",
    df["question"]
)

response = st.text_area(
    "Paste AI Response"
)

if st.button("Evaluate"):

    ideal = df[df["question"] == question]["ideal_behavior"].values[0]

    label = evaluate_response(
        question,
        response,
        ideal
    )

    st.success(f"Evaluation: {label}")

    st.write("Ideal Behaviour")

    st.info(ideal)