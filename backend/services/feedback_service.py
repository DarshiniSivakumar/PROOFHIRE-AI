def generate_why_not_selected(candidate):
    scores = candidate.get_skill_scores()

    weak_areas = [k for k, v in scores.items() if v < 70]

    if weak_areas:
        return f"After careful review, we found areas for improvement in: {', '.join(weak_areas)}."

    return "While your application showed promise, we had many strong candidates."