def compare_candidates(candidates):
    comparison = []

    for c in candidates:
        comparison.append({
            "name": c.name,
            "overall_score": c.overall_score,
            "confidence_score": c.confidence_score,
            "skills": c.get_skill_scores(),
            "status": c.status
        })

    return comparison