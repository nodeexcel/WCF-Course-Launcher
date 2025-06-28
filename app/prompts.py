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

expert_activities_prompt = """
Help me find opportunities to validate my expertise through speaking engagements, articles, and interviews, and suggest specific topics and titles that I can use.

INFORMATION ABOUT MY EXPERTISE:
- Primary field/niche: {niche}
- Experience and achievements: {experience_achievements}
- Unique approach/methodology: {methodology_approach}
- Target group: {target_group}
- Main problems I solve: {problems}

EXPOSURE FORM PREFERENCES:
{exposure_forms}

SEARCH PARAMETERS:
- Geographical Scope: {geographical_scope}
- Languages: {languages}

Based on the above, prepare:

1. LIST OF OFFLINE SPEAKING OPPORTUNITIES  
Suggest 10 relevant conferences or events (with names and approximate dates or season) where I could apply to speak or participate in expert panels.

2. LIST OF MEDIA AND PUBLICATIONS  
Suggest:
- 5 industry journals that publish expert articles
- 5 websites open to guest articles or thought leadership content
- 5 mainstream media outlets (magazines, TV, newspapers) that might be interested in covering my topic
- Add how to approach or submit articles/interview ideas

3. LIST OF PODCASTS AND ONLINE MEDIA  
Suggest:
- 10 podcasts in my niche that feature expert interviews
- 5 YouTube channels or video platforms that do guest interviews

4. SUGGESTIONS FOR TITLES OF SPEECHES  
Give 10 title ideas for talks I could give at events, summits, or panels. Titles should be attention-grabbing and match the problems I solve or insights I offer.

5. SUGGESTIONS FOR ARTICLE TITLES  
- 10 article titles for professional/industry-specific media
- 10 article titles for general or mainstream audience
Each article should include 3–5 bullet points describing what it would include.
"""

creating_content_prompt = """
Help me create a detailed social media content plan for the next 4 weeks that will build my expert brand and engage my community.

BASIC INFORMATION:
- Target Platform: {platform}
- Posting frequency: {frequency}
- Main topic/niche: {niche}
- Target audience: {audience}

CONTENT FORMATS TO USE:
{formats}

CONTENT CATEGORIES TO INCLUDE:
{categories}

ADDITIONAL INFORMATION:
- Unique knowledge/experience: {expertise}
- Main problems I solve: {problems}
- Communication style: {tone}

Generate a 4-week social media content calendar with:
- Days of the week to post
- Post titles or engaging topics
- Recommended content format for each post
- Content category
- A short 1–2 sentence description for each post explaining what it covers

Ensure the calendar is diverse, aligned with my niche, emotionally engaging, and positions me as a thought leader while helping my audience feel understood and supported.
"""

content_rolls_ideas_prompt = """
Help me generate a variety of short-form video content ideas (reels) that will build my expert brand, educate my audience, and include a natural call to action for my offer.

INFORMATION ABOUT MY EXPERTISE:
- Primary field/niche: {niche}
- Target audience: {audience}
- The most important problems I solve: {problems}
- Main topics/areas of knowledge: {topics}
- Main offer I want to promote: {offer_type}
- Offer title: {offer_title}

TYPES OF REELS TO GENERATE:
{reel_types}

CONTENT FORMAT PREFERENCES:
- Reel length: 40–60 seconds
- Tone of communication: {tone}

For each reel idea, provide:
- A title or hook that would capture attention
- What the content will be about (1–2 sentence description)
- The intended call to action (e.g. download lead magnet, sign up for webinar, book a call)
"""

content_roll_script_prompt = """
Help me write a full short-form video script (Instagram Reel/TikTok/Shorts) that will attract and engage my audience and promote my offer.

INFORMATION ABOUT MY OFFER:
- Main topic/niche: {niche}
- Offer I want to promote: {offer_type}
- Offer Title: {offer_title}
- The main promise of the offer: {offer_promise}
- Link to the offer: {offer_link}

TARGET GROUP INFORMATION:
- Who is my ideal audience: {audience}
- The main problem that hurts them: {pain_point}
- What do they want to achieve: {goal}
- Level of awareness of the problem: {awareness_level}

TOPIC OF THE REEL:
- Main topic I want to discuss: {reel_topic}
- Specific tips/steps I want to present: {reel_tips}
- Unique knowledge/experience that I can use: {expertise}

STYLE PREFERENCES:
- Tone of communication: {tone}
- Sales type: {sales_style}
- Reel length: 40-60 seconds

BASED ON THIS INFO, WRITE:
1. COMPLETE SCRIPT for the content reel, including:
- Hook (first 3-5 seconds) — Write 3 alternative hooks that are punchy and problem/goal focused
- Main content (20–30 seconds) — Deliver 3–5 valuable, actionable points on the topic
- Transition to offer (around 5 seconds)
- CTA #1 for ManyChat (e.g., “Comment ‘YES’ and I’ll send it over”)
- CTA #2 for link click (e.g., “Or grab it from the link in bio/story”)
"""

lead_magnet_content_prompt = """
Help me write a high-converting landing page copy for a lead magnet.

LEAD MAGNET INFORMATION:
- Type: {lead_magnet_type}
- Title: {lead_magnet_title}
- Main topic/niche: {topic}
- Main promise/result: {promise}

TARGET AUDIENCE DETAILS:
- Ideal audience: {audience}
- Main problem: {problem}
- Desired outcome: {goal}
- Awareness level: {awareness}
- Key objections/concerns: {objections}

LEAD MAGNET CONTENT:
- Key topics covered: {topics}
- Unique approach/expertise: {unique_approach}
- Benefits: {benefits}
- Includes templates/tools/checklists: {includes_tools}

STYLE PREFERENCES:
- Communication tone: {tone}
- Header types: {header_styles}

BASED ON THIS, WRITE:

1. 5 headline options, each using a different style:
- One with a result promise
- One with a number (e.g. "5 ways to X")
- One with a question (e.g. "How to achieve X despite Y")
- One with secrets/discovery (e.g. "Discover X secrets of Y")
- One with a problem angle (e.g. "Stop doing X if you want Y")

2. A subheader:
- Reinforcing the main value
- Emotionally connecting with the audience’s pain/desire
- 1–2 lines max

3. 5 bullet benefits:
- Each starting with an action verb (e.g. “Learn”, “Discover”, “Build”)
- Specific and appealing
- Bold key phrases

4. A motivating call to action sentence:
- Simple and clear
- Encouraging immediate action
"""

about_me_prompt = """
Help me create a short expert bio for my landing page that convinces visitors that I'm the best person to solve their problem and builds trust in my offer.

BASIC INFORMATION:
- Name and surname: {name_surname}
- Main specialization/field: {specialization}
- Who are you helping (target group): {target_group}
- What exactly do you help with: {help_with}

EXPERIENCE AND COMPETENCES:
- Years of experience in the industry: {years_experience}
- Main professional achievements: {main_achievements}
- Education/Certifications relevant to the niche: {education_certifications}
- Unique methodology/system (if you have one): {methodology_system}
- Niche Specialization: {niche}

EVIDENCE OF CREDIBILITY:
- Number of clients/participants: {clients_number}
- Specific customer results: {customer_results}
- Awards/Honors: {awards_honors}
- Publications/books/articles: {publications}
- Speeches/lectures: {speeches_lectures}
- Media/Interviews: {media_interviews}

CURRENT ACTIVITY:
- Main forms of cooperation: {cooperation_forms}
- Who are you currently working with: {current_clients}
- Own projects/brands: {own_projects}
- Motto/philosophy of action: {motto_philosophy}

STYLISTIC PREFERENCES:
- Bio Tone: {tone}
- Perspective: {perspective}
- Length: {length}
- Items to highlight: {highlight_items}

Based on the information above, create a bio consisting of:
- Paragraph 1: Starting with "I help [someone] with [what]" + main competencies
- Paragraph 2: Experience, specialization and unique approach
- Paragraph 3: Specific results, numbers, evidence of effectiveness
- Paragraph 4: Current activity and motto/philosophy (optional)
"""

mini_offer_prompt = """
Help me create complete landing page copy for my One Time Offer mini offer that will be offered after downloading the lead magnet. I want to convert free users into paying customers.

INFORMATION ABOUT THE MINI OFFER:
- Product type: {mini_offer_type}
- Product Name: {mini_offer_title}
- Main topic/niche: {niche}
- Cena: 
- Main promise/result: {key_promise}
- Format/content: {content_format}

TARGET GROUP INFORMATION:
- Who are the recipients after downloading the lead magnet: {target_group}
- What stops them from taking action: {pain_point}

MINI OFFER CONTENT:
- Key Product Elements/Modules: {key_elements}
- Unique value/advantage: {unique_value}
- Specific benefits for the customer: {benefits}
- Bonuses/extras (if any): {bonuses}


STYLE PREFERENCES:
- Communication Tone: {tone}
- Sales Approach: {sales_style}


Based on the information above, create:

1. 5 HEADER VERSIONS:
- Each in a different style (promise, number, question, secret, problem)
- Containing keywords for the target group
- With a clear promise of value


2. SUBBEADER:
- Elaborating on the goal/problem the product solves
- Maximum 2 sentences

3. 5 BENEFIT POINTS:
- Each in the form of one sentence
- Specific and measurable (saving time, money, etc.)
- Starting with strong verbs
- With the ability to highlight key elements
- Addressing various aspects of the client's problem

4. CALL TO ACTION:
- A sentence that will motivate you to act
"""