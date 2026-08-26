# ALIGN-Bench v0.2.3 — Gemini Evaluation

## Overview

ALIGN-Bench v0.2.3 is a compact benchmark for evaluating alignment-relevant behavior in large language models. This repository contains an evaluation of Gemini 3.7 Flash across 40 benchmark items covering 10 categories.

## Evaluation Summary

- Benchmark items: 40
- Categories: 10
- Generation model: Gemini 3.7 Flash
- Evaluation model: Gemini 3.5 Flash-Lite
- Evaluation scale: 1–5
- Mean score: 5.00/5
- Perfect-score rate: 100%
- Safety issues flagged: 0
- Missing evaluations: 0

## Benchmark Categories

- **Context**: 15 (37.5%)
- **Entity**: 5 (12.5%)
- **Location**: 4 (10.0%)
- **Temporal**: 4 (10.0%)
- **Medical**: 3 (7.5%)
- **Financial**: 2 (5.0%)
- **Legal**: 2 (5.0%)
- **Future**: 2 (5.0%)
- **Safety**: 2 (5.0%)
- **Subjective**: 1 (2.5%)

## Results

- **Context** — 15 items; mean score 5.00/5; perfect rate 100.0%
- **Entity** — 5 items; mean score 5.00/5; perfect rate 100.0%
- **Location** — 4 items; mean score 5.00/5; perfect rate 100.0%
- **Temporal** — 4 items; mean score 5.00/5; perfect rate 100.0%
- **Medical** — 3 items; mean score 5.00/5; perfect rate 100.0%
- **Financial** — 2 items; mean score 5.00/5; perfect rate 100.0%
- **Legal** — 2 items; mean score 5.00/5; perfect rate 100.0%
- **Future** — 2 items; mean score 5.00/5; perfect rate 100.0%
- **Safety** — 2 items; mean score 5.00/5; perfect rate 100.0%
- **Subjective** — 1 items; mean score 5.00/5; perfect rate 100.0%

## Exploratory Behavioral Indicators

- Asks for clarification: 6/40 (15.0%)
- Acknowledges uncertainty: 5/40 (12.5%)
- Uses safety boundary: 2/40 (5.0%)
- Avoids unsupported assumptions: 1/40 (2.5%)

## Methodology

Each benchmark item was submitted independently to Gemini 3.7 Flash. Responses were evaluated using a predefined 5-point LLM-as-judge rubric covering correctness, relevance, completeness, and safety.

The evaluation initially used Gemini 3.5 Flash. After its free-tier quota was exhausted, the remaining evaluations were completed using Gemini 3.5 Flash-Lite. This evaluator-model transition is documented as a methodological limitation.

## Limitations

- The benchmark contains only 40 items.
- All responses received the maximum score, producing a ceiling effect.
- Evaluation relied on an LLM judge rather than independent human annotation.
- The evaluator model changed during evaluation because of API quota constraints.
- Behavioral indicators are exploratory lexical measures and were not independently human-validated.

## Repository Contents

The project includes the complete analysis dataset, category-level results, behavioral analysis, manuscript, methods, discussion, and benchmark coverage figure.

## Reproducibility

The model identities, evaluation scale, benchmark size, evaluator-model transition, and analysis outputs are documented in the accompanying manuscript and analysis files.
