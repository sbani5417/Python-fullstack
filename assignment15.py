feedback={
    "positive":45,
    "Neutral":18,
    "Negative":7
    }
total_feedback=sum(feedback.values())
print("tOtal feedback:",total_feedback)
max_feedback_type=max(feedback,key=feedback.get)
print("Highest feedback type:",max_feedback_type)
