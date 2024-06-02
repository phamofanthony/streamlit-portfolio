import streamlit as st

st.set_page_config(
    layout='centered',
    page_title="Portfolio",
    page_icon="👋"
)

st.title("Anthony Pham's Portfolio")

intro, experience, skills_certificates, education_awards, resume = st.tabs(['Intro', 'Experience', 'Skills/Certificates', 'Education/Awards', 'Resume'])

with intro:
    st.subheader("Howdy, and welcome to my portfolio! Feel free to learn about me from the tabs above and view my projects on the tabs to the left!")
    st.write("I am a former software engineer with a deep passion for learning and problem-solving. I am currently pursuing my masters at the University of Arkansas, focusing on cybersecurity.")
    st.write("Throughout my academic and professional journey, I've cultivated a strong foundation in software engineering. This background has equipped me with a solid understanding of how to develop robust applications. However, my passion for learning and tackling new challenges has led me to cybersecurity, where I'm eager to learn how to create secure systems and defend against threats.")
    st.write("Although I'm still figuring out what field of cybersecurity I'd like to focus on, I'm particularly interested in a DevSecOps role, which I believe perfectly combines my software development skills with the security skills I'm acquiring. This role aligns with my goal of integrating security practices into the development process to build resilient and secure applications.")
    st.write("In my free time, I enjoy playing volleyball, spending time with friends and family, cooking and trying new foods, and in general just seeking new thrills in life. Oh, and I'm also obsessed with the majestic Texas-based gas staton chain that is known as Buc-ee's.")
    volleyball_pic, bucees_pic = st.columns(2)
    with volleyball_pic:
        st.image('resources/AboutMe/VolleyballPicture.JPEG')
    with bucees_pic:
        st.image('resources/AboutMe/BuceesPicture.JPEG')

with experience:
    st.header("Experience")
    st.subheader("Nuqleous Retail Analytics - Software Development Intern")
    st.write("Started on the operations team and expanded dataloading processes in SQL/C#, created monitoring scripts in SQL, created analytics metrics in MicroStrategy, and worked bi-weekly on-call weekends. \n \n Then shifted to the data engineering side, where I further automated the many manual processes I had done in the operations team. Developed a slackbot in Python that accessed several API's and databases to report monitoring statistics.")
    st.markdown('#')

with skills_certificates:
    st.header("Skills")
    st.subheader("Front-End Development: ")
    st.write("Telerik, Blazor, ReactJS, HTML, CSS, NPM, Yarn")
    st.subheader("Back-End Development: ")
    st.write("Django, .NET, NodeJS, SQL Server, Exasol, Snowflake, PostgreSQL, NoSQL")
    st.subheader("Languages")
    st.write("Python, C#, C++, C, Java, Kotlin, JavaScript, SQL")
    st.subheader("Tools")
    st.write("Azure, Airflow, Git, Visual Studio, DbVisualizer, Postman, Fiddler Everywhere, MicroStrategy, Microsoft Office")
    st.header("Certificates")
    st.write("Currently studying for Comptia Network+")

with education_awards:
    st.header("Education")
    st.subheader("University of Arkansas - Graduate Degree")
    st.write("M.S. in Computer Science w/ Cybersecurity Certificate")
    st.write("Expected May 2026")
    st.subheader("University of Arkansas - Undergraduate Degree")
    st.write("B.S. in Computer Science w/ Minor in Mathematics")
    st.write("Graduated May 2024 w/ a 4.0 GPA")
    st.header("Awards")
    st.subheader("Cybercorps Scholarship for Service ")
    st.write("Award for high-achieving computer science students amounting to full tuition coverage, a \$37,000 annual stipend, and a \$6,000 stipend for professional development uses")
    st.write("Awarded 2024")
    st.subheader("Outstanding Computer Science Senior")
    st.write("Award given to one student per department each year, symbolizing excellence in academics, research, industry experience, and beyond ")
    st.write("Awarded 2024")
    st.subheader("First-Ranked Senior Scholar")
    st.write("Award given to students who achieve a 4.0 GPA in their undergraduate studies")
    st.write("Awarded 2024")
    st.subheader("Honor's College Fellowship")
    st.write("Award given for high-achieving students, amounting to $76,000 across four years of undergraduate education")
    st.write("Awarded 2020")
    st.subheader("Governor's Distinguished Scholarship")
    st.write("Award given for high-achieving students, amounting to $40,000 across four years of undergraduate education")
    st.write("Awarded 2020")

with resume:
    st.image('resources/AboutMe/Resume.jpg')