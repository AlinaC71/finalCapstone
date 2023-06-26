# finalCapstone
This is a folder containing two Capstone project files for the HyperionDev DfE Data Science course.

Table of Contents
      <li>Introduction
            <li>Projects
                  <ol>1. Semantic Similarity (NLP) project
                  <ul>
                        <li> Research-based task nlp_1.pdf, nlp_2.pdf
                        <li> Practical task: watch_next.py and movies.txt
                        <li> Usage
                   </ul>     
                      2. Variables and Control Structures project: 
                  <ul>
                        <li> Practical task: finance_calculators.py
                        <li> Usage
<br/><br/>
<br/><br/>

## Introduction

This folder contains Capstone projects completed during the HyperionDev Data Science course. The Semantic Similarity (NLP) project section illustrates an understanding of Natural Language Processing (NLP) and its applications. It is divided into two sections: a research-based task and a practical task. The first part is descriptive and focuses on natural language processing applications, such as text classification and sentiment analysis. The second one consists of watch_next.py Python file that focuses on building a system that can recommend what to watch next based on the word vector similarity of the description of the movies.  

## 1. Semantic Similarity (NLP) project ( files nlp_1.pdf, nlp_2.pdf, watch_next.py and movies.txt files)

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
<br><br>
<br><br>
**Research-based tasks: nlp_1.pdf, nlp_2.pdf**

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
<ul>
<li>Read in the movies.txt file. Each separate line is a description of a different movie.
<li>Your task is to create a function to return which movies a user would watch next if they have watched Planet Hulk with the description “Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.”

To fulfill the task requirements I used spaCy, the free, open-source library for NLP in Python written in Cython. 
spaCy is designed to make it easy to build systems for information extraction or general-purpose natural language processing. 
SpaCy is able to compare two objects and make a prediction of how similar they are. The similarity is shown as a floating decimal from 0
to 1, where 0 indicates ‘most dissimilar’ and the strength of the similarity increases all the way up to 1. 

**Usage**
In order to use the semantic.py and watch_next.py programsyou need to have the SpaCy library installed as well as the specific language models. Please follow the instructions to add SpaCy and english language models.

Type the following commands in the command line to install spaCy:

pip3 install spacy

To check spacy is installed correctly type "import spacy" the following into the Python console :
If you receive no error, this means that spaCy was installed correctly!

SpaCy uses language models to process different languages. SpaCy's models can be installed as Python packages, meaning that they are a component of your application, just like any other module. Models can be installed from a download URL or a local directory, manually or via pip. Their data can be located anywhere on your file system. To download the English "small" model, type the command below in your terminal.

python -m spacy download en_core_web_sm

Please also install a more advanced language model 'en_core_web_md' which is able to find similarities and differences better than the previous ‘en_core_web_sm’ model. This model can be installed typing the line below in your command prompt (terminal):

python -m spacy download en_core_web_md
<br/><br/>
<br/><br/>
## 2.  Variables and Control Structures project: finance_calculators.py

In this Capstone Project I have created a program that allows the user to access two different financial calculators: an investment calculator and a home loan repayment calculator (I imported and used the math module for the calculations)

The task required me to write the code that will do the following: 
<ol type="1">
<li>The user should be allowed to choose which calculation they want to do.
      The first output that the user sees when the program runs should look like this :
      <ul>
      <li>investment - to calculate the amount of interest you'll earn on your investment
      <li>bond - to calculate the amount you'll have to pay on a home loan
      Enter either 'investment' or 'bond' from the menu above to proceed:
      </ul> 
<li>How the user capitalises their selection should not affect how the program proceeds. i.e. ‘Bond’, ‘bond’, ‘BOND’ or ‘investment’, ‘Investment’, ‘INVESTMENT’, etc., should all be recognised as valid entries. If the user doesn’t type in a valid input, show an appropriate error message.


![fin1](https://github.com/AlinaC71/finalCapstone/assets/107502531/02965094-b8f5-4568-8f7e-bc3406508fc0)


<li>If the user selects ‘investment’, do the following:
    <ul>
    <li>Ask the user to input:
    <li>The amount of money that they are depositing.
    <li>The interest rate (as a percentage). Only the number of the interest rate should be entered — don’t worry about having to deal with the
    added ‘%’, e.g. The user should enter 8 and not 8%.
    <li>The number of years they plan on investing.
    <li>Then ask the user to input if they want “simple” or “compound” interest, and store this in a variable called interest. Depending on
    whether or not they typed “simple” or “compound”, output the appropriate amount that they will get back after the given period,
    at the specified interest rate. 
    </ul>
Interest formula:
  The total amount when simple interest is applied : 𝐴 = 𝑃(1 + 𝑟 × 𝑡)<br>
  The Python equivalent is very similar: A = P*(1 + r*t)<br>
  The total amount when compound interest is applied:𝐴 = 𝑃((1 + 𝑟) to the power of 𝑡)<br>
  The Python equivalent is slightly different: A = P * math.pow((1+r),t)<br>
  
In the formulae above:
    <ul>
    <li>‘r’ is the interest entered above divided by 100, e.g. if 8% is entered, then r is 0.08.
    <li>‘P’ is the amount that the user deposits.
    <li>‘t’ is the number of years that the money is being invested.
    <li>‘A’ is the total amount once the interest has been applied.
    <li>Print the answer.</ul>

![fin2](https://github.com/AlinaC71/finalCapstone/assets/107502531/20cb5a2b-d868-4f08-a975-74b53d9ad721)



<li>If the user selects ‘bond’, do the following:
    <ul>
    <li>Ask the user to input:
    <li>The present value of the house. e.g. 100000
    <li>The interest rate. e.g. 7
    <li>The number of months they plan to take to repay the bond. e.g. 120
    </ul>
Bond repayment formula:
The amount that a person will have to be repaid on a home loan each month is calculated as follows: 𝑟𝑒𝑝𝑎𝑦𝑚𝑒𝑛𝑡 = 𝑖 × 𝑃 divided by (1− (1+𝑖)) to the power of −𝑛.
The Python equivalent is slightly different: repayment = (i * P)/(1 - (1 + i)**(-n))

In the formula above:
    <ul>
    <li>‘P’ is the present value of the house.
    <li>‘i’ is the monthly interest rate, calculated by dividing the annual interest rate by 12. Remember to divide the interest entered by
    <li>the user by 100 e.g. (8 / 100) before dividing by 12.
    <li>‘n’ is the number of months over which the bond will be repaid.
    Calculate how much money the user will have to repay each month and output the answer.

![fin3](https://github.com/AlinaC71/finalCapstone/assets/107502531/0030117b-7ed2-4f38-90f5-26a16d78d2a2)

**Usage**

In order to use the finance_calculator.py you need the math module to perform the mathematical calculation for interest and bond. 
math is a built-in module in the Python 3 standard library that provides standard mathematical constants and functions, used to perform various mathematical calculations, such as numeric, trigonometric, logarithmic, and exponential calculations.
The program imports the module in the first line of code using the syntax "import math" 






