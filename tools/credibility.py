def credibility_score(text):
    if "world bank" in text.lower() or "iea" in text.lower():
        return 0.9
    return 0.6
