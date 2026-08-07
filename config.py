"""
==========================================
ALIGN-Bench Configuration
==========================================
"""

APP_TITLE = "🧠 ALIGN-Bench"

APP_SUBTITLE = (
    "An Open Benchmark for Evaluating "
    "Clarification Behavior in Large Language Models"
)

APP_VERSION = "v1.0"

AUTHOR = "Neha Malav"

DATA_PATH = "data/benchmark.csv"

RESULTS_PATH = "results/evaluation_results.csv"

EVALUATION_LABELS = [
    "🟢 Clarified",
    "🟡 Assumed",
    "🔵 Balanced",
    "🔴 Possible Hallucination"
]

CATEGORIES = [
    "Temporal",
    "Location",
    "Context",
    "Medical",
    "Subjective",
    "Memory",
    "Emotion",
    "Legal",
    "Entity",
    "Future"
]
