
## Methods

We evaluated Gemini 3.7 Flash using ALIGN-Bench v0.2.3, a 40-item benchmark spanning 10 categories: Context, Entity, Location, Temporal, Medical, Financial, Legal, Future, Safety, and Subjective. Each benchmark item was submitted to the model independently, producing 40/40 responses.

Responses were evaluated using a predefined 5-point rubric assessing correctness, relevance, completeness, and safety, where 5 represented an excellent response and 1 represented a very poor or unsafe response.

Evaluation was performed using an LLM-based judge. The evaluation initially used Gemini 3.5 Flash; after the free-tier request quota for that model was exhausted, the remaining evaluations were completed using Gemini 3.5 Flash-Lite. This evaluator-model transition was documented and represents a methodological limitation. The final evaluation dataset contained scores for all 40 benchmark items.

In addition to the numerical score, the evaluator produced a brief rationale and a binary safety-issue indicator. Exploratory behavioral indicators were subsequently derived from response text using predefined lexical patterns for clarification seeking, uncertainty acknowledgment, safety-boundary language, and avoidance of unsupported assumptions.
