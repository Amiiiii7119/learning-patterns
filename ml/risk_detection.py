def calculate_risk(row):
    risk_score = 0

    if row["failures"] > 0:
        risk_score += 2
    if row["absences"] > 10:
        risk_score += 2
    if row["studytime"] <= 2:
        risk_score += 1
    if row["G2"] < 10:
        risk_score += 2
    if row["Dalc"] + row["Walc"] >= 6:
        risk_score += 1

    if risk_score >= 5:
        return "High Risk"
    elif risk_score >= 3:
        return "Medium Risk"
    else:
        return "Low Risk"
