from app.embeddings import generate_embeddings, calculate_similarity


def match_resume_to_job(resume_text, job_description):
    """Matches a resume with a job description and provides feedback."""
    # Generate embeddings
    resume_embedding = generate_embeddings(resume_text)
    job_embedding = generate_embeddings(job_description)

    # Calculate similarity
    match_score = calculate_similarity(resume_embedding, job_embedding)

    # Provide feedback
    feedback = analyze_differences(resume_text, job_description)

    return match_score, feedback


def analyze_differences(resume_text, job_description):
    """Analyzes differences between resume and job description for feedback."""
    feedback = []
    resume_words = set(resume_text.lower().split())
    job_words = set(job_description.lower().split())

    # Identify missing keywords
    missing_keywords = job_words - resume_words

    # Provide feedback for missing keywords
    if missing_keywords:
        feedback.append(
            "Your resume is missing the following keywords: "
            f"{', '.join(missing_keywords)}"
        )

    return " ".join(feedback)
