"""
==========================================
ALIGN-Bench Utility Functions
==========================================

Helper functions for:

• Loading CSV files
• Saving evaluation results
• Creating folders
• Reading benchmark data
"""

import os
from pathlib import Path
from datetime import datetime

import pandas as pd


# -------------------------------------
# PATHS
# -------------------------------------

DATA_PATH = Path("data/benchmark.csv")

RESULTS_PATH = Path("results/evaluation_results.csv")


# -------------------------------------
# CREATE REQUIRED FOLDERS
# -------------------------------------

def create_project_folders():

    folders = [

        "data",

        "results",

        "images",

        "assets",

        "docs",

        "paper"

    ]

    for folder in folders:

        os.makedirs(folder, exist_ok=True)


# -------------------------------------
# LOAD BENCHMARK
# -------------------------------------

def load_benchmark():

    return pd.read_csv(DATA_PATH)


# -------------------------------------
# LOAD RESULTS
# -------------------------------------

def load_results():

    if RESULTS_PATH.exists():

        return pd.read_csv(RESULTS_PATH)

    return pd.DataFrame()


# -------------------------------------
# SAVE EVALUATION
# -------------------------------------

def save_evaluation(

    model,

    category,

    question,

    evaluation

):

    row = pd.DataFrame(

        {

            "Timestamp":[

                datetime.now()

            ],

            "Model":[

                model

            ],

            "Category":[

                category

            ],

            "Question":[

                question

            ],

            "Evaluation":[

                evaluation

            ]

        }

    )

    if RESULTS_PATH.exists():

        row.to_csv(

            RESULTS_PATH,

            mode="a",

            header=False,

            index=False

        )

    else:

        row.to_csv(

            RESULTS_PATH,

            index=False

        )
