"""
==========================================
ALIGN-Bench Metrics Engine
==========================================

Calculates dashboard statistics and
performance metrics.
"""

import pandas as pd


def get_total_evaluations(results):

    return len(results)


def get_models_tested(results):

    return results["Model"].nunique()


def get_categories_tested(results):

    return results["Category"].nunique()


def get_clarification_rate(results):

    if len(results) == 0:
        return 0

    clarified = len(
        results[
            results["Evaluation"] == "🟢 Clarified"
        ]
    )

    return round(
        clarified / len(results) * 100,
        2
    )


def get_assumption_rate(results):

    if len(results) == 0:
        return 0

    assumed = len(
        results[
            results["Evaluation"] == "🟡 Assumed"
        ]
    )

    return round(
        assumed / len(results) * 100,
        2
    )


def get_balanced_rate(results):

    if len(results) == 0:
        return 0

    balanced = len(
        results[
            results["Evaluation"] == "🔵 Balanced"
        ]
    )

    return round(
        balanced / len(results) * 100,
        2
    )


def get_hallucination_rate(results):

    if len(results) == 0:
        return 0

    hallucination = len(
        results[
            results["Evaluation"] == "🔴 Possible Hallucination"
        ]
    )

    return round(
        hallucination / len(results) * 100,
        2
    )


def get_dashboard_metrics(results):

    return {

        "total": get_total_evaluations(results),

        "models": get_models_tested(results),

        "categories": get_categories_tested(results),

        "clarification_rate": get_clarification_rate(results),

        "assumption_rate": get_assumption_rate(results),

        "balanced_rate": get_balanced_rate(results),

        "hallucination_rate": get_hallucination_rate(results)

    }
