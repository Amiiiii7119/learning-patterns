from genai.explanations import generate_explanation

print(
    generate_explanation(
        "Disengaged Learner",
        "High Risk",
        "- Low study time\n- High absences\n- Declining grades"
    )
)
