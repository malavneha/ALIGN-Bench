import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
from pathlib import Path

from evaluator import evaluate_response
import os


# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------

st.set_page_config(
    page_title="ALIGN-Bench",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# -------------------------------------------------
# PATHS
# -------------------------------------------------

DATA_PATH = Path("data/benchmark.csv")
RESULTS_PATH = Path("results/evaluation_results.csv")


# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------

@st.cache_data
def load_dataset():
    return pd.read_csv(DATA_PATH)


benchmark = load_dataset()


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

    st.markdown(
        """
        ### An Open Benchmark for Evaluating AI Alignment Behavior in Large Language Models

        ALIGN-Bench is a research-oriented evaluation framework designed to assess
        how well Large Language Models (LLMs) respond to ambiguous, context-dependent,
        subjective, and safety-critical user queries.

        Instead of measuring only factual correctness, ALIGN-Bench evaluates whether
        AI systems ask appropriate clarifying questions, avoid unsupported assumptions,
        and respond responsibly.
        """
    )

    st.divider()

    # ---------- Statistics ----------
    total_questions = len(benchmark)
    total_categories = benchmark["category"].nunique()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Benchmark Questions",
            value=total_questions
        )

    with col2:
        st.metric(
            label="Categories",
            value=total_categories
        )

    with col3:
        st.metric(
            label="Project Version",
            value="v1.0"
        )

    st.divider()

    st.subheader("📂 Benchmark Categories")

    categories = benchmark["category"].unique()

    for cat in categories:
        st.write(f"• {cat}")

    st.divider()

    st.subheader("🎯 Research Objective")

    st.info(
        """
        Evaluate whether language models recognize ambiguity,
        request clarification when necessary,
        and avoid hallucinations or unsupported assumptions.
        """
    )

    st.divider()

    st.subheader("🚀 Quick Start")

    st.markdown(
        """
        1. Open **Evaluate** from the sidebar.
        2. Select an AI model.
        3. Choose a benchmark category.
        4. Paste the AI response.
        5. View the automatic evaluation.
        """
    )
# -------------------------------------------------
# EVALUATION PAGE
# -------------------------------------------------

elif page == "📝 Evaluate":

    st.title("📝 AI Response Evaluation")

    st.markdown(
        """
        Evaluate how a language model responds to benchmark questions.
        Select a category, choose a question, paste the AI response,
        and ALIGN-Bench will evaluate its behavior.
        """
    )

    st.divider()

    # -----------------------------
    # MODEL SELECTION
    # -----------------------------

    model = st.selectbox(
        "Select AI Model",
        [
            "ChatGPT",
            "Gemini",
            "Claude",
            "Llama",
            "Manual Evaluation"
        ]
    )

    # -----------------------------
    # CATEGORY
    # -----------------------------

    category = st.selectbox(
        "Benchmark Category",
        sorted(benchmark["category"].unique())
    )

    filtered = benchmark[
        benchmark["category"] == category
    ]

    # -----------------------------
    # QUESTION
    # -----------------------------

    question = st.selectbox(
        "Benchmark Question",
        filtered["question"]
    )

    row = filtered[
        filtered["question"] == question
    ].iloc[0]

    ideal_behavior = row["ideal_behavior"]

    st.info(f"🎯 Expected Behaviour: {ideal_behavior}")

    st.divider()

    response = st.text_area(
        "Paste AI Response",
        height=220,
        placeholder="Paste the AI response here..."
    )

    if st.button(
        "Evaluate Response",
        use_container_width=True
    ):

        if response.strip() == "":

            st.warning("Please paste an AI response.")

        else:

            result = evaluate_response(
                response
            )

            st.divider()

            st.subheader("Evaluation Result")

            if result == "🟢 Clarified":
                st.success(result)

            elif result == "🟡 Assumed":
                st.warning(result)

            elif result == "🔴 Possible Hallucination":
                st.error(result)

            else:
                st.info(result)

            st.divider()

            st.subheader("Recommendation")

            if result == "🟢 Clarified":

                st.success(
                    "Excellent. The model requested additional information before answering."
                )

            elif result == "🟡 Assumed":

                st.warning(
                    "The model answered without requesting the missing information. It should ask a clarifying question first."
                )

            elif result == "🔴 Possible Hallucination":

                st.error(
                    "The response may contain unsupported or fabricated information. Manual review is recommended."
                )

            else:

                st.info(
                    "The model appropriately acknowledged uncertainty or multiple perspectives."
                )

            st.divider()

            st.subheader("Evaluation Summary")

            summary = pd.DataFrame(
                {
                    "Field": [
                        "AI Model",
                        "Category",
                        "Question",
                        "Evaluation"
                    ],
                    "Value": [
                        model,
                        category,
                        question,
                        result
                    ]
                }
            )
            # ------------------------------------
# SAVE RESULT
# ------------------------------------

save_row = pd.DataFrame(
    {
        "Timestamp": [datetime.now()],
        "Model": [model],
        "Category": [category],
        "Question": [question],
        "Evaluation": [result]
    }
)

os.makedirs("results", exist_ok=True)

result_file = "results/evaluation_results.csv"

if os.path.exists(result_file):

    save_row.to_csv(
        result_file,
        mode="a",
        header=False,
        index=False
    )

else:

    save_row.to_csv(
        result_file,
        index=False
    )

st.success("✅ Evaluation saved successfully.")

            st.dataframe(
                summary,
                use_container_width=True,
                hide_index=True
            )
# -------------------------------------------------
# DASHBOARD
# -------------------------------------------------

elif page == "📊 Dashboard":

    st.title("📊 Evaluation Dashboard")

    result_file = "results/evaluation_results.csv"

    if not os.path.exists(result_file):

        st.warning(
            "No evaluations found. Evaluate some responses first."
        )

    else:

        results = pd.read_csv(result_file)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Total Evaluations",
                len(results)
            )

        with col2:
            st.metric(
                "Models Tested",
                results["Model"].nunique()
            )

        with col3:
            st.metric(
                "Categories",
                results["Category"].nunique()
            )

        st.divider()

        st.subheader("Evaluation Distribution")

        pie = px.pie(
            results,
            names="Evaluation",
            hole=0.45
        )

        st.plotly_chart(
            pie,
            use_container_width=True
        )

        st.divider()

        st.subheader("Category Distribution")

        category_chart = px.bar(
            results["Category"].value_counts().reset_index(),
            x="Category",
            y="count"
        )

        st.plotly_chart(
            category_chart,
            use_container_width=True
        )

        st.divider()

        st.subheader("Evaluation History")

        st.dataframe(
            results,
            use_container_width=True
        )

        st.download_button(
            "⬇ Download Results CSV",
            data=results.to_csv(index=False),
            file_name="evaluation_results.csv",
            mime="text/csv"
        )

            


