choosing_niche_prompt = """
Help me create a short, catchy sentence that defines my niche and the mission of my course.
My target group (who I help): {target_group}
Problem I'm Solving: {problem}
The benefit I offer: {benefit}

Based on this, create several versions of the sentence according to the format:
I help {target_group} solve the problem of {problem} so they can {benefit}
The versions should be understandable, specific and sound natural in everyday language.

Return the versions in a numbered list, with each version on a new line.
"""

market_research_prompt = """
I'm creating a digital product in the "{niche}" space. Please help me research the market.

Market research
Help me find 3 experts or companies that offer similar digital products to the ones I want to create – in {niche}.

I am interested in people/brands who:
– have online courses, e-books or consultations,
– are active on social media,
– have a similar target group.

For each of them, give me:
a) Name of the company or expert
b) Link to their website and most important social media channels
c) The name of the course/product and its price (if public)
d) The promise of the course – what exactly is promised to the participant (the final result)
e) Your observations – what distinguishes this person, what does their communication look like, is there anything that catches the eye?
"""

target_group_prompt = """
Help me create a profile of my ideal customer (target audience) for a digital product in the field of "{niche}".

Divide the profile into 6 parts:

1. Psychographic Profile
– What kind of life do they want to lead?
– What are their professional goals?
– What are their personal goals?
– What values do they hold?

2. Pain (Problems and Frustrations)
– What obstacles do they encounter in their professional or personal life?
– What problems keep them awake at night?
– What unmet expectations do they have for themselves?
– What do they think others expect from them that they don’t achieve?

3. Fear (Conscious and Unconscious)
– What are they afraid of?
– What danger are they not aware of?
– What dangers could await them in the future if they don’t change anything?

4. Success
– What is their life like when they are successful?
– What achievements do they desire?
– What are their biggest aspirations?

5. Failures
– What have they failed at in the past?
– What will their life and their family’s life be like if they don’t buy my course?
– What will they lose if they don’t choose my program?

6. Digital Behavior
– What social networking sites do they use?
– What forums and online groups do they belong to?
– What do they buy online and how much do they typically spend each month?
"""

course_topic_problem_prompt = """
Based on the customer profile "{niche}", prepare a list of 5 ideas for a course or other digital product.

For each product idea, provide:
– A short promise (what effect or result the course will give to the learner)
– What specific problem it solves for this audience
"""

generate_course_prompt = """
4 Ways to Generate an Online Course Idea
Help me generate ideas for online courses in four areas:
My profession is: {profession}
My passions are: {passions}
My personal transformation: {transformation}
Trends I follow: {trends}

Based on this, suggest me:
– 5 ideas for courses in the field of profession
– 5 ideas from the area of passion
– 5 ideas for personal transformation
– 5 ideas inspired by trends

For each idea, provide a course topic and a one-sentence promise to students.
""" 