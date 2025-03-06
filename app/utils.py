def load_job_description(file_path):
    """Loads a job description from a text file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
