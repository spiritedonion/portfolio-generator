def fill_template():
    # Prompt the user for their information
    full_name = input("Enter your full name: ").strip()
    profession = input("Enter your profession/field: ").strip()
    years_of_experience = input("Enter the number of years of experience: ").strip()
    location = input("Enter your current location: ").strip()
    key_interest_or_skill = input("Enter your key interest or skill: ").strip()
    goal_or_mission = input("Enter a brief description of your goal or mission: ").strip()

    project_title_1 = input("Enter the title of Project/Work 1: ").strip()
    project_description_1 = input("Enter a description of Project/Work 1: ").strip()
    role_1 = input("Enter your role in Project/Work 1: ").strip()
    skills_applied_1 = input("Enter the skills applied in Project/Work 1: ").strip()
    outcome_1 = input("Enter the outcome of Project/Work 1: ").strip()

    project_title_2 = input("Enter the title of Project/Work 2: ").strip()
    project_description_2 = input("Enter a description of Project/Work 2: ").strip()
    role_2 = input("Enter your role in Project/Work 2: ").strip()
    skills_applied_2 = input("Enter the skills applied in Project/Work 2: ").strip()
    outcome_2 = input("Enter the outcome of Project/Work 2: ").strip()

    skill_1 = input("Enter details for Skill 1: ").strip()
    skill_2 = input("Enter details for Skill 2: ").strip()
    skill_3 = input("Enter details for Skill 3: ").strip()
    skill_4 = input("Enter details for Skill 4: ").strip()
    skill_5 = input("Enter details for Skill 5: ").strip()
    skill_6 = input("Enter details for Skill 6: ").strip()

    degree_earned = input("Enter your degree earned and major: ").strip()
    additional_education = input("Enter any additional certifications or education: ").strip()

    email_address = input("Enter your email address: ").strip()
    linkedin_profile = input("Enter your LinkedIn profile URL: ").strip()

    # Fill in the template with the user's information
    template = f"""

{full_name}
About Me
Greetings! I am {full_name}, a seasoned {profession} professional with a rich tapestry of experience spanning over {years_of_experience} years. Nestled in the dynamic city of {location}, my professional journey revolves around a profound passion for {key_interest_or_skill}. My unwavering dedication is not merely a commitment but a strategic pursuit of excellence, aiming to elevate the industry through {goal_or_mission}.

My Work
[{project_title_1}]
Description: Embarking on {project_title_1}, I orchestrated a multidisciplinary team to navigate the intricate landscape of {project_description_1}. This endeavor encompassed {role_1}, demanding an innovative approach to {skills_applied_1}. Addressing challenges such as {outcome_1}, our collaborative efforts led to the seamless delivery of {outcome_1}.

Role: As the luminary orchestrator of this project, I assumed the mantle of {role_1}, steering the team through {outcome_1}. My approach, characterized by {skills_applied_1}, fostered an environment of creativity and efficiency.

Skills Applied: The project necessitated the mastery of {skills_applied_1}, where I expertly wielded {outcome_1} to sculpt a narrative of success. Notable was the deployment of {skills_applied_1} that set the project apart.

Outcome: The fruition of our labor surpassed expectations, culminating in {outcome_1}, solidifying my capacity to navigate complex projects, providing tangible proof of my ability to not only meet but exceed industry standards.

[{project_title_2}]
Description: Diving into another riveting chapter, {project_title_2} beckoned, demanding a nuanced understanding of {project_description_2}. This project became a canvas for innovation, as I navigated intricacies such as {role_2} to achieve {skills_applied_2}.

Role: My role extended beyond traditional boundaries, encompassing {skills_applied_2}. Collaborating seamlessly with {outcome_2}, my leadership ethos underscored the fusion of expertise, fostering an atmosphere of collective achievement.

Skills Applied: The project showcased my adeptness in {skills_applied_2}, deploying {outcome_2} to architect a solution that not only met but anticipated industry needs.

Outcome: {outcome_2}, solidifying my reputation as a strategist capable of steering projects toward success.

Skills
[{skill_1}]: My mastery of {skill_1} transcends conventional applications, as evidenced by {outcome_1}.
[{skill_2}]: Proficiency in {skill_2} has been a linchpin in sculpting success stories, where I seamlessly integrated this skill into the fabric of {outcome_2}.
[{skill_3}]: Adept at navigating complexities through {skill_3}, I have consistently demonstrated a prowess that not only solves challenges but transforms them into opportunities.
[{skill_4}]: Staying at the forefront of {skill_4}, I am an avid advocate of continuous learning, actively participating in {additional_education}.
[{skill_5}]: Noteworthy achievements in {skill_5} include {outcome_2}, showcasing a mastery that goes beyond conventional boundaries.
[{skill_6}]: My collaborative approach through {skill_6} has left an indelible mark on projects, fostering an ecosystem where diverse talents converge to create extraordinary outcomes.

Education
{degree_earned}
{additional_education}

Contact
Feel free to connect with me via email at {email_address}. For a more comprehensive view of my professional journey, please explore my LinkedIn profile at {linkedin_profile}. I welcome discussions, collaborations, and opportunities that align with my commitment to transformative excellence.
"""

    # Print the filled template
    print(template)


# Call the function to execute the program
fill_template()
