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

live_product_prompt = """
I want to create live digital products that meet the real needs of my target group.

Here's some context:

My niche:
{niche}

Problems I solve:
{problems_list}

🔹 My target group avatar:
{target_group_description}

Based on this, suggest at least 10 ideas for live digital products such as:
– 1:1 consultations
– mastermind
– online workshops or training (e.g. on Zoom)
– audit sessions
– virtual conferences

For each idea, provide:
1. Working title of the format (e.g. "Online Training: How to Run an Instagram That Attracts Clients in Industry X")
2. A brief description of how to deliver the product
3. What problem does it solve?
"""

evergreen_product_prompt = """
I want to create evergreen digital products that meet the real needs of my target group.

Here's some context:

My niche:
{niche}

Problems I solve:
{problems_list}

My target group avatar:
{target_group_description}

Based on this, suggest at least 10 ideas for evergreen digital products, such as:
– online course
– ebook
– video book
– course email
– subscription page
– VOD
– reports and analyses
– product audio
– workbooks and planners

For each idea, provide:
1. Working name of the format (e.g. "Online course: Increase sales in stationary business in 30 days")
2. A short description of what the product is about
3. What problem does it solve?
"""

product_ladder_prompt = """
Help me develop my 3-level product ladder which will include:

1. Lead magnet (free)
2. Mini product (low budget)
3. Main product (premium)

My niche:
{niche}

Problems I solve:
{problems_list}

My target group avatar:
{target_group_description}

I need ideas for lead magnets, both evergreen (e.g. e-books, checklists) and live events (e.g. webinars).

All elements of my product ladder should be logically linked to each other, where the lead magnet naturally leads to the next stage and attracts ideal customers.

For each level of the ladder (lead magnet, mini product, main product), suggest 3 ideas. For each idea, provide:
- Format (PDF, video, webinar, online course, etc.)
- Working name
- A short description with the benefits and the problem it solves
"""

course_structure_prompt = """
Help me create a detailed structure for my digital product:

BASIC INFORMATION:
- Product type: {product_type}
- Product Title: {product_title}
- Key promise/result for the customer: {key_promise}

CONTEXT:
- My niche: {niche}
- Main problem I'm solving: {main_problem}
- Who are the audience: {audience}
- What knowledge/skills do they already have: {current_skills}
- What knowledge/skills do I want to pass on to them: {target_skills}

Create a structure that contains:
1. 5-8 logical modules/chapters (less if the product is short)
2. 3-7 lessons/subchapters in each module (in the case of a video course, each lesson should last about 10-15 minutes)
3. For each module, specify:
- Module Title
- List of lessons with titles and short description (1-2 sentences) and lesson format (e.g. video, PDF, quiz, etc.)
4. Suggestions for practical exercises, tasks, and additional materials for each module

Additionally, suggest:
- Product introduction: what it should include
- Product conclusion: how to summarize and motivate users to take action
"""

subscription_product_structure_prompt = """
I want to create a content structure for my subscription site where I publish 1 new lesson per week for 3 months.

BASIC INFORMATION:
- Product Title: {product_title}
- Key promise/result for the customer: {key_promise}

CONTEXT:
- My niche: {niche}
- Main problem I'm solving: {main_problem}
- Who are the audience: {audience}
- What knowledge/skills do they already have: {current_skills}
- What knowledge/skills do I want to pass on to them: {target_skills}

The content is divided into 4 thematic pillars:
1. {pillar_1}
2. {pillar_2}
3. {pillar_3}
4. {pillar_4}

Publication scheme:
– Week 1 of each month = new lesson from pillar 1
– Week 2 = New lesson from Pillar 2
– Week 3 = New lesson from Pillar 3
– Week 4 = New lesson from Pillar 4

Create a publishing plan for 3 months (i.e. 12 weeks / 12 lessons).
For each lesson, provide:
- Title
- Short description (what the participant will gain from this lesson)
- The pillar to which the lesson belongs

Make sure that the lessons complement each other and create a logical and valuable development path, but are not too repetitive.

The general topics of my subscription program are: {general_topic}
"""

packaging_process_prompt = """
Help me create a unique, named process/system for my course that will serve as its main framework.

COURSE INFORMATION:
- Course Title: {course_title}
- Niche/topic: {niche}
- The main problem solved by the course: {main_problem}
- Target outcome for participants: {target_outcome}

PROCESS PREFERENCES:
- Preferred number of stages: {num_stages}
- Process name type: {process_name_type}

Based on the information above, create:

1. A catchy slogan (1 sentence) summarizing the main promise of the process
2. Unique name of the process/system
3. List of stages. For each stage, provide:
- Stage name (if using acronym, match the starting letter)
- A concise description (1 sentence) explaining what the stage involves
- The main result of this stage for the participant (what they gain after completing it)

4. Briefly explain why this sequence of steps is logical and effective for solving the user's problem and achieving the course goal.
"""

life_story_prompt = """
I want you to write me a short storytelling expert account using the hero's journey template. It should be:
– specific and based 100 percent on facts,
– short, concise, illustrative,
– emotional, but not over the top,
– end with a moral for the reader,
– showing one specific trait that helped me along the path of transformation.

Use the following personal facts as source:

Starting point – where I was before it all started:
{starting_point}

Problem – what bothered me the most:
{problem}

Breakthrough – what happened that made me decide to act:
{breakthrough}

The Path – what I did, how I developed, what was the biggest challenge:
{path}

Result – where I am today and what I have achieved:
{result}

Feature that helped me the most:
{key_trait}

Moral – what I would like the reader to take away from this:
{moral}

Write the story in the style of a personal post or “About Me” story:
– honest,
– written in simple, everyday language,
– suitable for video, social media post or website bio.
"""

expert_actions_prompt = """
Help me generate 10 article ideas that I could propose to industry portals, online magazines, or thematic blogs.

Each article must:
– Be interesting and valuable to my target audience
– Position me as an expert in my field
– Spark curiosity without giving away everything for free
– Include both strategy-level and practical insight

For each topic, provide:
- An engaging article title
- 1–2 sentence description of what the article will cover and who it is for

Here is some context about me and my brand:

Niche/theme of my brand:
{niche}

My target group:
{target_group}

Main problems I help solve:
{problems}

Outcomes I help clients achieve:
{outcomes}

Feel free to include strategic insights, how-to tips, trends, expert takes, or light case study ideas. 
Write in a tone that will catch the attention of an editor and the curiosity of a potential reader.
"""
