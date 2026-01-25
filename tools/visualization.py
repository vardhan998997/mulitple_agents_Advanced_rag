import matplotlib.pyplot as plt

def plot_confidence(claims):
    scores = [c["confidence"] for c in claims]
    plt.bar(range(len(scores)), scores)
    plt.xlabel("Claim Index")
    plt.ylabel("Confidence")
    plt.title("Confidence Scores")
    plt.show()
