def evaluate_response(question, response, ideal_behavior):
    """
    Simple rule-based evaluator
    """

    response = response.lower()

    if "which" in response or "what" in response or "could you" in response:
        return "Clarified"

    elif "don't know" in response or "cannot" in response:
        return "Balanced"

    else:
        return "Assumed"