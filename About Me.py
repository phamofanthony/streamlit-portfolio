import streamlit as st

st.set_page_config(
    layout='centered',
    page_title="Anthony's Portfolio",
    page_icon="👋"
)

st.title("Anthony Pham's Portfolio")

bio, experience, skills_certificates, education_awards, resume = st.tabs(['Bio', 'Experience', 'Skills/Certificates', 'Education/Awards', 'Resume'])

with bio:
    st.write("Howdy! I am a former software engineer with a deep passion for learning and problem-solving. I am currently pursuing my masters at the University of Arkansas, focusing on cybersecurity.")
    st.write("Throughout my academic and professional journey, I've cultivated a strong foundation in software engineering. This background has equipped me with a solid understanding of how to develop robust applications. However, my passion for learning and tackling new challenges has led me to cybersecurity, where I'm eager to learn how to create secure systems and defend against threats.")
    st.write("Although I'm still figuring out what field of cybersecurity I'd like to focus on, I'm particularly interested in a DevSecOps role, which I believe perfectly combines my software development skills with the security skills I'm acquiring. This role aligns with my goal of integrating security practices into the development process to build resilient and secure applications.")
    st.write("In my free time, I enjoy playing volleyball, spending time with friends and family, cooking and trying new foods, and in general just seeking new thrills in life. Oh, and I'm also obsessed with the majestic Texas-based gas staton chain that is known as Buc-ee's.")

with experience:
    st.header("Experience")
    st.subheader("Nuqleous Retail Analytics - Software Development Intern")
    st.write("Started on the operations team and expanded dataloading processes in SQL/C#, created monitoring scripts in SQL, created analytics metrics in MicroStrategy, and worked bi-weekly on-call weekends. \n \n Then shifted to the data engineering side, where I further automated the many manual processes I had done in the operations team. Developed a slackbot in Python that accessed several API's and databases to report monitoring statistics.")
    st.markdown('#')

with skills_certificates:
    st.header("Skills")
    st.subheader("Front-End: ")
    st.write("Telerik, Blazor, ReactJS, HTML, CSS, NPM, Yarn")
    st.subheader("Back-End: ")
    st.write("Django, .NET, NodeJS, SQL Server, Exasol, Snowflake, PostgreSQL, NoSQL")
    st.subheader("Languages")
    st.write("Python, C#, C++, C, Java, Kotlin, JavaScript, SQL")
    st.subheader("Tools")
    st.write("Azure, Airflow, Git, Visual Studio, DbVisualizer, Postman, Fiddler Everywhere, MicroStrategy, Microsoft Office")
    st.header("Certificates")
    st.write("Currently studying for Comptia Network+")

with education_awards:
    st.header("Awards")
    st.subheader("Cybercorps Scholarship for Service")
    st.write("")
    st.subheader("Outstanding Computer Science Senior")
    st.write("")
    st.subheader("First-Ranked Senior Scholar")
    st.write("")
    st.subheader("Honor's College Fellowship")
    st.write("")
    st.subheader("Governor's Distinguished Scholarship")
    st.write("")