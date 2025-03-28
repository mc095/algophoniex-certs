import streamlit as st
import os
import pandas as pd

# set the page title and header with smaller sizes using markdown, in lowercase, without boldness
st.markdown("### algophoenix hackathon certificate download")
st.markdown("##### enter your roll number to download your certificate")

# directory where certificates are stored
certificate_dir = "generated_certificates"

# input field for roll number
roll_number = st.text_input("roll number - [UPPER CASE PREFERRED] (e.g., 22A81A05Z7)", "").strip().upper()

# admin contact details in lowercase (except proper nouns)
admin_details = """
admin contact details:  
- Prasanna Kumar: +91 93926 93465  
- Mohan:  +91 80742 74880
"""

# search button
if st.button("search"):
    if roll_number:
        # path to the certificate file
        certificate_path = os.path.join(certificate_dir, f"{roll_number}.png")
        
        # check if the certificate exists
        if os.path.exists(certificate_path):
            st.success(f"certificate found for roll number: {roll_number}")
            
            # provide a download button for the certificate
            with open(certificate_path, "rb") as file:
                st.download_button(
                    label="download certificate",
                    data=file,
                    file_name=f"{roll_number}_certificate.png",
                    mime="image/png"
                )
        else:
            st.error(f"certificate not found for roll number: {roll_number}")
            st.markdown("please contact the admins for assistance.")
            st.markdown(admin_details, unsafe_allow_html=True)
    else:
        st.warning("please enter a valid roll number.")

# add a footer with additional information in lowercase
st.markdown("---")
st.markdown("algophoenix hackathon - held on 6th and 7th january 2025 at Sri Vasavi Engineering College (Autonomous).")
st.markdown("for more updates, visit our [website](https://bbscsvec.vercel.app/)")