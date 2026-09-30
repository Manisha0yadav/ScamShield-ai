import re

def check_scam(text):
    text = text.lower()
    score = 0
    reasons = []

    if "offer" in text or "earn" in text:
        score += 30
        reasons.append("Shak wala shabd mila: offer/earn")
    if "90%" in text or "free" in text or "giveaway" in text:
        score += 30
        reasons.append("Lalach wala word: free/90%")
    if "lottery" in text or "winner" in text:
        score += 40
        reasons.append("Lottery scam pattern")
    if "bit.ly" in text or "t.me" in text:
        score += 20
        reasons.append("Suspicious short link")

    if score >= 60:
        level = "HIGH RISK - Scam Hai"
    elif score >= 30:
        level = "SUSPICIOUS"
    else:
        level = "LOW RISK - Safe Hai"

    return {"level": level, "score": score, "reasons": reasons}