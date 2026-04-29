def get_feedback():
    feedback_map = {
        "1": "good",
        "2": "ok",
        "3": "bad"
    }

    user_input = input("Feedback? (1=good, 2=ok, 3=bad): ").strip()

    feedback = feedback_map.get(user_input, "unknown")

    print(f"Recorded feedback: {feedback}")

    return feedback