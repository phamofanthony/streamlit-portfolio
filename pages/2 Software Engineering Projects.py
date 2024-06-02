import streamlit as st

st.set_page_config(
    layout='centered',
    page_title="Portfolio",
    page_icon="👋"
)

st.markdown("## Software Engineering Projects")

capstone_proj, pacman, foodmap, navigation, bridge_crossing = st.tabs(['Capstone Matching', 'AI Pacman', 'FoodMap', 'Campus Navigation', 'Bridge Crossing Simulation'])

with capstone_proj:
    st.video('resources/SWEProjects/capstone.mp4')
    st.markdown("""
        For my final Capstone project, I worked with a team to develop a web application that streamlines the Capstone project matching process between students and sponsors. Previously, the process required numerous different portals for all the parties, presentations from the instructor, lengthy forms to fill out for students, and tens of hours of work from instructors. This web app combined all those processes into one portal, automating many of the former manual processes and allowing all the parties a straightforawrd view of what's relevant to them.
        \n **Skills:** Python, Django, HTML/CSS, OR-Tools
        """)

with pacman:
    st.video('resources/SWEProjects/pacman.mp4')
    st.markdown("""
        In my artifical intelligence class, we created an application in Python that automatically solved Pacman mazes using a variety of searching algorithms, including BFS, DFS, UCS, and A*. Depending on the algorithm, the simulation provided a score that rated how efficient the path was.
        \n **Skills:** Python, Pygame, Searching algorithms
        """)

with foodmap:
    _, container, _ = st.columns(spec=3, gap='small')
    with container:
        st.video('resources/SWEProjects/foodmap.mp4')
    st.markdown("""
        In my mobile application development class, my group created a network app based around food. In essence, users can friend each other and view on a map where all their friends ate at and detailed reviews including a star rating, description, and images of the food. It was developed specifically for Android utilizing design methodologies like MVVM and Android Room. Information was all stored in the cloud via Firebase Firestore and we had secure user authentication via Firebase Authentication.
        \n **Skills:** Kotlin, XAML, Firebase FireStore, NoSQL, Firebase Authentication, Android development, Android Studio
        """)

with navigation:
    st.image('resources/SWEProjects/campusnavigation.jpg')
    st.markdown("""
        In my algorithms course, I created this application to map out directions around campus based on various searching and sorting algorithms. Depending on the algorithm used, it would display the path on a map along with the length of that path.
        \n **Skills:** C++, Searching algorithms, Sorting algorithms, Optimization
        """)

with bridge_crossing:
    st.video('resources/SWEProjects/bridgecrossing.mp4')
    st.markdown("""
        In my operating systems class, I created a multithreaded bridge crossing simulation. A large number of vehicles would arrive at a bridge (each modeled by a thread) and according to a set list of traffic rules, the vehicles could only cross in a certain order. This project taught me key multithreading concepts like mutexes and semaphores.
        \n **Skills:** C, Pthreads, Multithreaded development, Unix
        """)