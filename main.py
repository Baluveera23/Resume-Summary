import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from Secret_code import Google_API_Key
import os
os.environ['Google_API_Key']= Google_API_Key

# Setup LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=Google_API_Key,
    temperature=0.7
)

# Prompt Template
prompt_template = PromptTemplate.from_template(
    """
    You are a professional resume writer. Write a compelling and concise 3–4 sentence resume summary.
    Tone: Professional and confident.
    Format: Plain text, no bullet points.
    Make sure to highlight:
    - Number of years of experience
    - Key skills relevant to the target job
    - Quantifiable achievements (if possible)

    Candidate Info:
    - Previous Job Title: {previous_title}
    - Years of Experience: {years_experience}
    - Key Skills: {skills}
    - Target Job Title: {target_job}

    Summary:
    """
)

# Streamlit UI
st.title("📝 AI Resume Summary Writer")


with st.form("resume_form"):
    previous_title = st.text_input("Previous Job Title")
    years_experience = st.text_input("Years of Experience")
    skills = st.text_input("Key Skills (comma-separated)")
    target_job = st.text_input("Target Job Title")
    submitted = st.form_submit_button("Generate Summary")
    

    if submitted:
        with st.spinner("Generating your resume summary..."):
            final_prompt = prompt_template.format(
                previous_title=previous_title,
                years_experience=years_experience,
                skills=skills,
                target_job=target_job,
            )
            response = llm.invoke(final_prompt)
            output = st.success("Hurrah, here's your professional summary:")
            st.write(response.content)
