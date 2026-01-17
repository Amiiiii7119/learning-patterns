STUDENT_EXPLANATION_PROMPT = """
You are an educational analytics assistant.

A student has the following profile:
- Learning Cluster: {cluster}
- Risk Level: {risk}

Key indicators:
{features}

Explain in simple, teacher-friendly language:
1. Why the student falls into this learning pattern
2. Why the student has this risk level
3. What signals matter most

Avoid blaming language. Be factual and supportive.
"""

INTERVENTION_PROMPT = """
Based on the student's learning pattern and risk level:

- Learning Cluster: {cluster}
- Risk Level: {risk}

Suggest:
1. 2–3 practical teaching strategies
2. 1 short-term classroom action
3. 1 monitoring signal to track improvement

Keep suggestions realistic for a school classroom.
"""

COUNTERFACTUAL_PROMPT = """
A student has the following indicators:
{features}

If only ONE factor could be improved in the next month,
which change would reduce learning risk the most and why?

Answer in 3–4 lines, clearly explaining cause and effect.
"""
