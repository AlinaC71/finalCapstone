# finalCapstone

This is a folder containing two Capstone project files for the HyperionDev DfE Data Science course.
<br/><br/>
<br/><br/>
**1. Semantic Similarity (NLP) project** ( files nlp_1.pdf, nlp_2.pdf, watch_next.py and movies.txt files)
  Natural Language Processing (NLP) is currently one of the largest fields of research in artificial intelligence (AI).
<br/><br/>
<br/><br/>
![NLP Image source: Conversica ](https://miro.medium.com/v2/resize:fit:828/format:webp/1*_TV_ZLIhZpmX7HpMODwmiA.png)
<br/><br/>
<br/><br/>
NLP is a big part of AI because a large portion of NLP has to do with training computers or AI programs. These AI programs identify patterns and use probabilities to make informed decisions.
This is known as machine learning and is a massive field of research. Today it has many applications: in recommendation engines 
(items to buy, films to watch), in identifying images, helping driverless cars to act according to their environment etc.

The NLP Capstone project tasks were divided into two parts: research  and practical tasks.
<br/><br/>
<br/><br/>
**Research tasks: nlp_1.pdf, nlp_2.pdf**

The file nlp_1.pdf categorises which type of NLP application applies for each of the following use-cases:
- A model that allocates which mail folder an email should be sent to (work, friends, promotions, important), like Gmail’s inbox tabs.
- A model that helps decide what grade to award to an essay question (This can be used by a university professor who grades a lot of classes
or essay competitions.
- A model that provides assistive technology for doctors to provide their diagnosis. Remember, doctors ask questions, so the model will
use the patients’ answers to provide probable diagnoses for the doctor to weigh and make decisions.

The second task required me to read up on any innovative technology using NLP (by companies such as Google or IBM, for instance) and write a brief summary about the technology, what it achieves/does, and an overview of how it works (250 -500 words) in a file called nlp_2.pdf
<br/><br/>
<br/><br/>
**Practical task: watch_next.py and movies.txt**

The practical NLP task had the following requirements:
-Read in the movies.txt file. Each separate line is a description of a different movie.
-Your task is to create a function to return which movies a user would watch next if they have watched Planet Hulk with the description “Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.”

To fulfill the task requirements I used spaCy, the free, open-source library for NLP in Python written in Cython. 
spaCy is designed to make it easy to build systems for information extraction or general-purpose natural language processing. 
SpaCy is able to compare two objects and make a prediction of how similar they are. The similarity is shown as a floating decimal from 0
to 1, where 0 indicates ‘most dissimilar’ and the strength of the similarity increases all the way up to 1. 



2.  Variables and Control Structures project: finance_calculators.py

In this Capstone Project I have created a program that allows the user to access two different financial calculators: an investment calculator and a home loan repayment calculator (I imported and used the math module for the calculations)

The task required me to write the code that will do the following: 

1. The user should be allowed to choose which calculation they want to do.
The first output that the user sees when the program runs should look like this :
  investment - to calculate the amount of interest you'll earn on your investment
  bond - to calculate the amount you'll have to pay on a home loan
Enter either 'investment' or 'bond' from the menu above to proceed:

2. How the user capitalises their selection should not affect how the program proceeds. i.e. ‘Bond’, ‘bond’, ‘BOND’ or ‘investment’, ‘Investment’, ‘INVESTMENT’, etc., should all be recognised as valid entries. If the user doesn’t type in a valid input, show an appropriate error message.

3. If the user selects ‘investment’, do the following:
● Ask the user to input:
○ The amount of money that they are depositing.
○ The interest rate (as a percentage). Only the number of the interest rate should be entered — don’t worry about having to deal with the
added ‘%’, e.g. The user should enter 8 and not 8%.
○ The number of years they plan on investing.
○ Then ask the user to input if they want “simple” or “compound” interest, and store this in a variable called interest. Depending on
whether or not they typed “simple” or “compound”, output the appropriate amount that they will get back after the given period,
at the specified interest rate. 
Interest formula:
  The total amount when simple interest is applied : 𝐴 = 𝑃(1 + 𝑟 × 𝑡)
  The Python equivalent is very similar: A = P*(1 + r*t)
  The total amount when compound interest is applied:𝐴 = 𝑃((1 + 𝑟) to the power of 𝑡)
  The Python equivalent is slightly different: A = P * math.pow((1+r),t)
In the formulae above:
● ‘r’ is the interest entered above divided by 100, e.g. if 8% is entered, then r is 0.08.
● ‘P’ is the amount that the user deposits.
● ‘t’ is the number of years that the money is being invested.
● ‘A’ is the total amount once the interest has been applied.
○ Print the answer.

4. If the user selects ‘bond’, do the following:
● Ask the user to input:
○ The present value of the house. e.g. 100000
○ The interest rate. e.g. 7
○ The number of months they plan to take to repay the bond. e.g. 120
Bond repayment formula:
The amount that a person will have to be repaid on a home loan each month is calculated as follows: 𝑟𝑒𝑝𝑎𝑦𝑚𝑒𝑛𝑡 = 𝑖 × 𝑃 1− (1+𝑖) −𝑛
The Python equivalent is slightly different: repayment = (i * P)/(1 - (1 + i)**(-n))
In the formula above:
● ‘P’ is the present value of the house.
● ‘i’ is the monthly interest rate, calculated by dividing the annual interest rate by 12. Remember to divide the interest entered by
the user by 100 e.g. (8 / 100) before dividing by 12.
● ‘n’ is the number of months over which the bond will be repaid.
○ Calculate how much money the user will have to repay each month and output the answer.



