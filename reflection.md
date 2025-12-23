# Reflection

Student Name:  Luisana Ortiz
Student Email:  lsortiz@syr.edu

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

- **Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 
-  **Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`

I was inspired to create this program after discovering a similar interactive dashboard by the Pew Research Center, "Are you in the American middle class?" (https://www.pewresearch.org/short-reads/2024/09/16/are-you-in-the-american-middle-class/) where users input their state of residence, metropolitan area within said state, their household income and household size and then found out whether they were considered part of the lower, middle or upper class for their metro region and in the country overall, as well as what % of respondents with similar information were part of each.

I liked how simple and engaging this "calculator" was, and I wanted to build something similar for users that had both a journalistic and personalized component to it--I am always looking for new ways to do journalism and present data so that it lands in a universal way. After completing the project, I realized how deceptive this simplicity was, and how time-consuming the data preparation, transformation and analysis actually was in the background. 

However, as someone interested in working with data for a research or think tank organization such as Pew Research, this project was extremely eye-opening to what this kind of data manipulation looks like and how much planning is required. Where a business-oriented project may be more straightforward, in research, every inclusion or exclusion of information counts. You have to explain why you made the decisions you did, because your process may end up being incorrect or incomplete and your results skewed. This is why the codebook is so detailed, and, having worked on a much simpler codebook for a research project in the past, I know that this process is a project of its own. Translating this onto an analytics environment is tedious; creating the mapping_dict within the codebook.py file was also very time-consuming, but it paid off greatly once I successfully mapped all the categorical values with their codes.

Something else I learned is that my work style is quite disorganized. I tend to think and do, often skipping the planning phase implemented in our assignments. This took a big toll on this project, and I could have saved myself A LOT of time if I had been more organized from the beginning. I had originally created the mapped dataset on my own and didn't create a function for it, but when I was working on the function tests I realized I had no idea how I had gotten the mapped dataframe I'd gotten. I worried it might not be replicable for someone else working on the project, or that they would be wondering why the mapped_dataframe looked the way it did compared to the original--or worse, that I had messed something up along the way and had no way of tracing it. Thus, I went back and created a function that documented the transformation, cleaning AND mapping progress so that I could make sure I did things the right way, especially since this was my first time using the map function (we did not use it in class). I'm very grateful that I did this, because it allowed me to retrace my steps and verify the rest of my work that built off this dataframe was correct. More importantly, it taught me how to be more organized and slow my process down to prevent errors that might later be impossible to identity.

There are a few ways I would improve this project. For one thing, I would create a map showing what US region respondents were located in, data which was included in the NPORS dataset but that I didn't have time to play around with.

I would also like to create the option for users to pick their own demographics of interest from the long list provided in the NPORS dataset (for ex, race/ethnicity, political party, religion) and then create visualizations based off those demographics.

Finally, I wonder if there is a better way I could error handle for when no respondents from the survey match a constructed profile. Right now, instead of an empty bar chart, I simply output an error message on streamlit that explains this. Perhaps it would be good to explain a sample size of 0 means in the context of this survey, i.e. how representative this is of the overall U.S. population based on PRC's collection methods. Not sure about this yet, and there are definitely some research methods and processes I am not yet familiar with.

Overall, this project was challenging, but not so difficult that it was impossible or outside the scope of the class. I feel a lot more confident in my programming and data wrangling skills because of it and I'm excited to add it to my portfolio.