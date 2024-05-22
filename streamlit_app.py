from pathlib import Path

import requests
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style" / "main.css"
resume_file = current_dir / "assets" / "Manoj Bharath_CV.pdf"
profile_pic = current_dir / "assets" / "Profile.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Resume | Manoj Bharath"
PAGE_ICON = "💼"
NAME = "Manoj Bharath"
DESCRIPTION = """
Data Analyst, assisting the organizations to develop and grow businesses with my key insights to help make data-driven decisions.
"""
EMAIL = "manojbharath.jci@gmail.com"
CONTACT = "+918807474836"
SOCIAL_MEDIA = {
    "LinkedIn" : "https://www.linkedin.com/in/manojbharathj30/",
    "GitHub" : "https://github.com/manojbharath89",
    "Kaggle" : "https://www.kaggle.com/manojbharathj",
    "Medium" : "https://medium.com/@manojbharathk"
}
PROJECTS = {
    "🏆 Empowering Business with Effective Insights - Virtual Internship, TataiQ-Forage" : "https://www.novypro.com/project/online-retail-storedashboard-power-bi",
    "🏆 HR Analytics" : "https://www.novypro.com/project/hr-analytics-power-bi-14",
    "🏆 Diabetic Patients Analysis" : "https://www.kaggle.com/code/manojbharathj/pima-diabetic-patients-analysis"
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=200)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📧", EMAIL)
    st.write("📞", CONTACT)

# --- SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write("---")
st.write(
    """
- ✔️ 2 Years experience in extracting actionable insights from data
- ✔️ Strong hands-on experience and knowledge in SQL, Python, Power BI and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)

# --- SKILLS ---
st.write("#")
st.subheader("Hard Skills")
st.write("---")
st.write(
    """
- 🗒️ Programming: Python (NumPy, Pandas, scikit-learn, Django, Tkinter, Streamlit), SQL
- 📊 Data Visualization: Power BI, Advanced Excel, Seaborn, Matplotlib, Plotly
- 🗄️ Databases: PostreSQL, Microsoft SQL Server, MySQL, SQLlite3
"""
)

# --- Projects & Accomplishments ---
st.write("\n")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

# --- EDUCATION ---
st.write("\n")
st.subheader("Education")
st.write("---")

# --- UG
st.write("**Bachelor of Science (Computer Science)**")
st.write("*June 2006 - April 2009*")
st.write("Bharathiar University, Coimbatore, Tamil Nadu, IN")
st.write(
    """
CGPA: 7.5/10
- *Java Programming, SQL, RDBMS, Data Structures & Algorithms, Artificial Intelligence*
    """
)

# --- WORK HISTORY ---
st.write("\n")
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("\n")
st.write("**Freelancer - Operations Analyst | MK Technologies**")
st.write("*January 2023 - Present*")
st.write(
    """
- ► Analyzing the operations data over the years and help the company in data-driven decision-making.
- ► Creating effective and interactive PowerBI dashboards that helps the company envisage the business forecast.
    """
)

# --- JOB 2
st.write("\n")
st.write("**Lead, Quality Assurance | Real Team Systems**")
st.write("*April 2021 - December 2022*")
st.write(
    """
- ► Edit the transcripts processed by the transcriptionists and deliver the accurate products to clients within specified TAT.
- ► Audit the edited transcripts and evaluate in order to reduce the errors in the future.
    """
)

# --- JOB 3
st.write("\n")
st.write("**Senior Editor | Rndsoftech**")
st.write("*January 2018 - March 2021*")
st.write(
    """
- ► Helped deliver the quality earnings call transcripts.
- ► Responsible for Quality Control, where I had to derive valuable insights using and visualizations on the performance and productivity across various departments of the company.
    """
)

# --- JOB 4
st.write("\n")
st.write("**Healthcare Documentation Specialist | AQuity Solutions India**")
st.write("*September 2014 - December 2017*")
st.write(
    """
- ► Helping deliver the error-free healthcare reports that hold the confidential patient records in U.S.
- ► Had ample amount of knowledge on various medical terminologies and the root cause of the various diseases that affect less the immune people.
    """
)

# --- JOB 5
st.write("\n")
st.write("**Editor | Rndsoftech**")
st.write("*April 2009 - September 2014*")
st.write(
    """
- ► Performed various methods on the business data using Microsoft Excel and helped the executives gain business insights.
- ► Served as a liaison between client, peers and business managers to solve the problems pertain to the projects.
    """
)


st.header(":mailbox: Get in touch with me!")

contact_form = """
<form action="https://formsubmit.co/manojbharath.jci@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your E-mail" required>
     <textarea name="message" placeholder="Your Message Here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use local CSS file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")
