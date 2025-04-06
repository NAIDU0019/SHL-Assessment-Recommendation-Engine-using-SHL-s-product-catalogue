import streamlit as st
from core.recommender import SHLRecommender

st.set_page_config(page_title="SHL Assessment Recommendation Engine", layout="centered")

st.title("📊 SHL Assessment Recommendation Engine")
st.subheader("Get tailored SHL product recommendations based on job requirements")

job_description = st.text_area("Paste Job Description or Role Requirements")

if st.button("Generate Recommendation"):
    if not job_description.strip():
        st.warning("Please enter job requirements.")
    else:
        recommender = SHLRecommender("data/shl_products.json")
        recommendations = recommender.recommend(job_description, top_k=1)

        st.success("🎯 Recommendation Generated!")
        for rec in recommendations:
            st.markdown(f"### ✅ {rec['title']}")
            st.markdown(f"**Score:** {rec['score']}  \n{rec['description']}")
