import streamlit as st
import pandas as pd
import plotly.express as px

from evaluator import evaluate_response, recommendation
from metrics import get_dashboard_metrics
from utils import (
    load_benchmark,
    load_results,
    save_evaluation,
    create_project_folders,
)

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="ALIGN-Bench",
    page_icon="🧠",
    layout="wide"
)

create_project_folders()

benchmark = load_benchmark()

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.title("🧠 ALIGN-Bench")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📝 Evaluate",
        "📊 Dashboard",
        "📂 Dataset",
        "ℹ️ About"
    ]
)

# -------------------------------------------------
# HOME PAGE
# -------------------------------------------------

if page == "🏠 Home":

    st.title("🧠 ALIGN-Bench")

    st.markdown("""
### An Open Benchmark for Evaluating AI Alignment

ALIGN-Bench evaluates whether AI systems
ask clarification questions,
avoid unsupported assumptions,
and respond responsibly.
""")

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Benchmark Questions",
            len(benchmark)
        )

    with col2:
        st.metric(
            "Categories",
            benchmark["category"].nunique()
        )

    with col3:
        st.metric(
            "Version",
            "1.0"
        )

    st.divider()

    st.subheader("Benchmark Categories")

    for cat in sorted(
        benchmark["category"].unique()
    ):
        st.write("•", cat)

    st.divider()

    st.info(
        "Research Goal: Evaluate whether language models ask clarifying questions before answering ambiguous prompts."
    )

    st.divider()

    st.subheader("Quick Start")

    st.markdown("""
1. Open **Evaluate**
2. Choose a category
3. Paste an AI response
4. View evaluation
5. Explore Dashboard
""")
