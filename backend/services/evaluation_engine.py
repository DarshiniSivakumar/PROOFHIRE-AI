import random

def evaluate_submission(submission_text, task):
    """Mock AI evaluation engine - generates realistic scores and feedback"""

    base_score = random.uniform(60, 95)

    length_factor = min(len(submission_text) / 500, 1.2)
    adjusted_score = base_score * length_factor

    scores = {
        'problem_solving': min(100, adjusted_score + random.uniform(-10, 10)),
        'code_quality': min(100, adjusted_score + random.uniform(-10, 10)),
        'efficiency': min(100, adjusted_score + random.uniform(-15, 5)),
        'communication': min(100, adjusted_score + random.uniform(-5, 15)),
        'accuracy': min(100, adjusted_score + random.uniform(-10, 10)),
    }

    overall = sum(scores.values()) / len(scores)
    confidence = random.uniform(0.75, 0.95)

    if overall >= 85:
        feedback = f"Excellent work on this {task.task_type} task!"
    elif overall >= 70:
        feedback = f"Good attempt on this {task.task_type} task."
    else:
        feedback = f"Your {task.task_type} submission shows understanding of basics."

    return {
        'overall_score': round(overall, 1),
        'confidence': round(confidence, 2),
        'scores': {k: round(v, 1) for k, v in scores.items()},
        'feedback': feedback
    }