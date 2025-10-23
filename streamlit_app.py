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
EMAIL = "manojbharath.bi@gmail.com"
CONTACT = "+918807474836"
SOCIAL_MEDIA = {
    "LinkedIn" : "https://www.linkedin.com/in/manojbharathj30/",
    "GitHub" : "https://github.com/manojbharath89",
    "Kaggle" : "https://www.kaggle.com/manojbharathj",
    "Medium" : "https://medium.com/@manojbharathk"
}
PROJECTS = {
    "🏆 Empowering Business with Effective Insights - Virtual Internship, TataiQ-Forage" : "https://www.novypro.com/project/online-retail-storedashboard-power-bi",
    "🏆 Operations & Revenue Analysis" : "https://app.powerbi.com/view?r=eyJrIjoiYmQwNjkyNjEtNGQxNC00MTdiLWIzZGMtYzgzNDg3YmMwNTc1IiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9",
    "🏆 EdTech Academy Analytics" : "https://app.powerbi.com/view?r=eyJrIjoiMmE3MDUxZTItNzUxYi00ZDU0LThiNzEtNjA1MmViMDFjMjIyIiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9"
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
- ✔️ 3 Plus Years experience in extracting actionable insights from data
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
st.write("**Logistics Analyst | Schneider Electric India**")
st.write("*February 2025 - Present*")
st.write(
    """
- ► Analyzed Logistics data to deliver actionable insights, resulting in a 15% increase in Sales forecasting accuracy and delivered predictive models for Production Planning.
- ► Automated and developed various Excel Dashboards with Tools that reduced 65% of the human working hours that helped making the process more efficient than it has been over the yesteryears.
    """
)

# --- JOB 2
st.write("\n")
st.write("**Business Intelligence Analyst | BLUEKODE SOLUTIONS**")
st.write("*January 2024 - January 2025*")
st.write(
    """
- ► Analyzed Superstore data to deliver actionable insights, resulting in a 15% increase in sales forecasting accuracy and 10% reduction in costs.
- ► Designed and developed interactive PowerBI and Python visual dashboards to provide real-time business insights, driving a 25% increase in ROI for the business.
    """
)


# --- JOB 3
st.write("\n")
st.write("**Data Analyst in Operations | MK Technologies**")
st.write("*January 2023 - December 2023*")
st.write(
    """
- ► Analyzing the operations data over the years and help the company in data-driven decision-making.
- ► Creating effective and interactive PowerBI dashboards that helps the company envisage the business forecast.
    """
)

# --- JOB 4
st.write("\n")
st.write("**Lead, Quality Assurance | Real Team Systems**")
st.write("*April 2021 - December 2022*")
st.write(
    """
- ► Analyzed employee performance data to identify areas for improvement.
- ► Created data visual dashboards to inform quality score improvement.
    """
)

# --- JOB 5
st.write("\n")
st.write("**Head of Operations | RndSoftech**")
st.write("*January 2018 - March 2021*")
st.write(
    """
- ► Analyzed and visualized performance data for clients using advanced Excel skills, providing actionable insights for strategic decisions.
- ► Developed and maintained detailed reports and dashboards to track KPIs and KPMs, identifying areas for improvement and optimizing processes.
    """
)

# --- JOB 6
st.write("\n")
st.write("**Senior Healthcare Documentation Analyst | AQuity Solutions India**")
st.write("*September 2014 - December 2017*")
st.write(
    """
- ► Analyzed patient records to predict medical conditions and identify trends
- ► Improved patient outcomes and disease management through data-driven insights
    """
)

# --- JOB 6
st.write("\n")
st.write("**Business Operations Analyst | Rndsoftech**")
st.write("*April 2009 - September 2014*")
st.write(
    """
- ► Analyzed client data to provide business forecasts using predictive analytics, identifying trends, patterns and correlations to inform strategic decisions.
- ► Developed Excel Dashboards to track KPIs and presented findings to Senior Management, ensuring data-driven decision-making across the organization.
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
