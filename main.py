import streamlit as st
from app.resume_parser import extract_text_from_pdf
from app.job_matcher import match_resume_to_job


st.title("ATS Resume Checker")
st.sidebar.header("Upload Resume and Job Description")

# File upload
uploaded_resume = st.sidebar.file_uploader("Upload Resume (PDF)", type="pdf")
uploaded_job_description = st.sidebar.text_area("Paste Job Description")

if st.sidebar.button("Analyze"):
    if uploaded_resume and uploaded_job_description:
        with st.spinner("Processing..."):
            # Parse the resume
            resume_text = extract_text_from_pdf(uploaded_resume)

            # Match with job description
            match_score, feedback = match_resume_to_job(
                resume_text, uploaded_job_description
                )

            # Display results
            st.subheader("Results")
            st.write(f"**Match Score:** {match_score}%")
            st.write("**Feedback:**")
            st.write(feedback)
    else:
        st.error("Please upload a resume and provide a job description!")
