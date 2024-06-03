import streamlit as st

st.set_page_config(
    layout='centered',
    page_title="Portfolio",
    page_icon="👋"
)

st.title("Anthony Pham's Portfolio")
st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/phamofanthony) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/phamofanthony/) [![Email](https://img.shields.io/badge/Email-EA4335?style=flat&logo=gmail&logoColor=white)](mailto:phamofanthony@gmail.com)")

intro, experience, skills_certificates, education_awards, resume, hobbies = st.tabs(['Intro', 'Experience', 'Skills/Certificates', 'Education/Awards', 'Resume', 'Hobbies'])

with intro:
    st.markdown("### Howdy, welcome to my portfolio! Find out more about me from the tabs above and view my projects on the tabs to the left!")
    text, image = st.columns(spec=2, gap='small')
    with text:
        st.markdown("""
            I am a former software/data engineer with a deep passion for learning and problem-solving. I am currently pursuing my masters at the University of Arkansas, focusing on cybersecurity.
            \n Throughout my academic and professional journey, I've cultivated a strong foundation in software engineering. This background has equipped me with a solid understanding of how to develop robust applications. However, my passion for learning and tackling new challenges has led me to cybersecurity, where I'm eager to learn how to create secure systems and defend against threats.
            \n Although I'm still figuring out what field of cybersecurity I'd like to focus on, I'm particularly interested in a DevSecOps role, which I believe perfectly combines my software development skills with the security skills I'm acquiring. This role aligns with my goal of integrating security practices into the development process to build resilient and secure applications.
            """)
    with image:
        st.image('resources/AboutMe/SelfPicture.jpg')

with experience:
    st.markdown("""
        ## Experience
        \n ### Nuqleous Retail Analytics - Software Development Intern (May 2022 - May 2024)
        \n I spent two years at Nuqleous, where I worked across all four primary development teams: Product Development, ShelfIQ, Operations, and Data Engineering. With this wide breadth of experience, I was able to gain insight into the development processes of a variety of teams. During my whole two years, I worked on-call shifts every other week, amounting to approximately 52 on call weekends. 
        \n On the product development team, I worked primarily on developing new business intelligence metrics for users in MicroStrategy, updating our backend services (C#/.NET/Azure Functions) to be more robust, as well as helping maintain the operations of our ETL proccess that ran on a daily basis. On this team, one of my largest projects were to write a script to synchronize our dozens of customer schemas in the database to match table and view definitions.
        \n On the ShelfIQ team, I worked on adding additional functionality to the product by creating new \"actions\" (C#/.NET/Telerik) which are scripts that users can use to automate their planogram creation process. I also helped out in bugfixing for existing actions.
        \n On the operations team, I worked directly with customer tickets through a CRM. I handled customer issues ranging from failing reports in MicroStrategy to data issues in our database and ETL process (SQL/Python/C#/.NET). On top of fixing their issues, I also facilitated communications back to the customer. In my time on the team, I handled over 50 customer tickets.
        \n Lastly, on the data engineering team, where I worked on expanding the ETL processes, pulling in new data feeds and adding connectors to new retailers (Python/SQL). Some of my largest projects were creating two new connectors, a Slack-bot that periodically sent updates on the loading process throughout the day to a team-chat, and a Streamlit page that allowed us to quickly analyze SLA times for customers through querying the database.
        """)
with skills_certificates:
    st.markdown("""
        ### Skills
        \n **Front-End Development:** Telerik, Blazor, ReactJS, 
        \n **Back-End Development:** Django, .NET, NodeJS, SQL S
        \n **Languages:** Python, C#, C++, C, Java, Kotlin, Java
        \n **Tools:** Azure, Airflow, Git, Visual Studio, DbVisu
        \n ### Certificates
        \n Currently studying for Comptia Network+
        """)

with education_awards:
    st.markdown("""
        ## Education
        \n ### University of Arkansas - Graduate Degree
        \n M.S. in Computer Science w/ Cybersecurity Certificate
        \n Expected May 2026
        \n ### University of Arkansas - Undergraduate Degree
        \n B.S. in Computer Science w/ Minor in Mathematics
        \n Graduated May 2024 with a 4.0 GPA
        \n ## Awards
        \n ### CyberCorps Scholarship for Service 
        \n Award for high-achieving computer science students amounting to full tuition coverage, a \$37,000 annual stipend, and a \$6,000 stipend for professional development uses
        \n Awarded 2024
        \n ### Outstanding Computer Science Senior
        \n Award given to one student per major each year, symbolizing excellence in academics, research, industry experience, and beyond 
        \n Awarded 2024
        \n ### First-Ranked Senior Scholar
        \n Award given to students who achieve a 4.0 GPA in their undergraduate studies
        \n Awarded 2024
        \n ### Honor's College Fellowship
        \n Award given for high-achieving students, amounting to $76,000 across four years of undergraduate education
        \n Awarded 2020
        \n ### Governor's Distinguished Scholarship
        \n Award given for high-achieving students, amounting to $40,000 across four years of undergraduate education
        \n Awarded 2020
        """)

with resume:
    st.markdown("## Resume")
    with open("resources/AboutMe/Resume.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()
    st.download_button(label="Download Resume", data=pdf_bytes, file_name="Anthony Pham Resume.pdf", mime="application/octet-stream")
    st.image('resources/AboutMe/Resume.jpg')

with hobbies:
    st.markdown("""
        ## Hobbies
        \n In my free time, I enjoy playing volleyball, spending time with friends and family, cooking and trying new foods, and in general just seeking new thrills in life. With life being so short, I'm determined to make the most of it!
        \n I'm also active in the UVSA South space, a non-profit that unites all the Vietnamese Student Associations (VSA's) in Arkansas, Oklahoma, and Texas. Welcoming people of every background and ethnicity, UVSA South is geared towards empowering the next generation of leaders with the skills they need to succeed in their careers. In this space, I've staffed for several conferences that pull in 200+ attendees and currently, I am the logistics captain for Camp Legacy 9.
        \n Oh, I'm also obsessed with the majestic Texas-based gas staton chain called Buc-ee's.
        """)
    volleyball_pic, bucees_pic = st.columns(2)
    with volleyball_pic:
        st.image('resources/AboutMe/VolleyballPicture.JPEG')
    with bucees_pic:
        st.image('resources/AboutMe/BuceesPicture.JPEG')
    st.image('resources/AboutMe/SummitPicture.jpg')