import streamlit as st
import requests

# Page config
st.set_page_config(page_title="GitHub Code Mentor", page_icon="🐙")

# Title
st.title("🐙 The Student GitHub & Portfolio Reviewer")

# Input field
username = st.text_input("GitHub Username:", placeholder="e.g., torvalds")

# Button
if st.button("Analyze Portfolio"):
    if username:
        with st.spinner(f"Analyzing {username}'s repositories..."):
            try:
                # Call FastAPI backend
                response = requests.post(
                    f"https://github-reviewer-api-rdxz.onrender.com/review",
                    json={"username": username}   # ✅ send as JSON (correct way)
                )

                if response.status_code == 200:
                    data = response.json()

                    st.success("Analysis Complete!")

                    # Show extracted data
                    st.subheader("📊 Extracted GitHub Data")
                    st.json(data.get("extracted_data"))

                    # Show mentor feedback
                    st.subheader("💡 Mentor Feedback")
                    st.write(data.get("mentor_feedback"))

                else:
                    st.error(f"Backend Error: {response.status_code}")

            except Exception as e:
                st.error("Could not connect to the backend.")
                st.exception(e)
    else:
        st.warning("Please enter a GitHub username.")