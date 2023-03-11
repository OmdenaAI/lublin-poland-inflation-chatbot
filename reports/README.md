# FINAL REPORT: Conversational AI Chatbot for People Affected by High Inflation and Increased Cost of Living

# A project by the Omdena Lublin Local Chapter.

<p align="center">
  <img width="40%" height="40%" src="images/logo.jpg">
</p>

# Executive Summary

'Conversational AI Chatbot for People Affected by High Inflation and Increased Cost of Living', a project by the Omdena Lublin Local Chapter led by chapter leader Bartosz Chojnacki, lasted over 6 weeks and saw the cooperation of an international team of AI engineers. These cooperated steadily to define the problem, collect question-answer pairs and financial information, pre-process and annotate the data, choose a suitable ML algorithm classification, and eventually deploy and publishing the chatbot in Streamlit. 

The project run smoothly and was completed successfully.

# Introduction

This challenge was created to develop a conversational AI chatbot. The main aim of our proposed solution was to assist people affected by high inflation and increased cost of living. 

The challenge, which united an international team of AI engineers for over 6 weeks, was led by chapter lead Bartosz Chojnacki. The common language for the chapter was English, and platforms such as GitHub and a dedicated Slack channed were used to coordinate and keep track of the engineers' work. 

As one of the main goals of Omdena is to promote continuous, high-quality education, thematic workshops organised by Chojnacki were delivered to the participants during the project.

## Problem statement

Inflation and high living costs have become a problem for the inhabitants of Poland. This problem is especially visible in the poorer parts of the country, such as the Lubelskie Voivodeship, and in the city of Lublin, the country's capital. 

Current inflation rates have raised at 18%, which is the highest rate in 26 years in Poland. Such a high level of inflation has caused job layoffs, and even the closure of entire enterprises. This is a very rare situation, as the country normally displays low unemployment rate.

Since not everyone in the country is coping with equally well in this situation, our project aimed at providing financial counselling to anyone who might be struggling.

## Project goal

The goal of this project was to create a virtual chatbot that is able to answer any user's questions about the possibility of saving money or depositing it safely, and to support our engineers' continuous learning in the field of NLP and conversational AI.

![An image from the Omdena chapter webpage](images/banner.png)

# Our solution

The team developed a financial chatbot based on the OpenAI ChatGPT-3 `curie` model fine-tuned on the [Financial Opinion Mining and Question Answering](https://sites.google.com/view/fiqa/home) dataset. The chatbot was later deployed as a Streamlit app.

##	The data

Given the peculiarity of the task that we wanted out chatbot to perform, we could not only rely on existing language models, and decided to collect financial data to use to fine-tune a language model of our choice later.

The collected data came from a variety of sources (mainly social media). It was done using well-known web-scraping tools such as beautifulsoup, lxml, and selenium. 

Sławomir Lisowski shared scraping scripts for all of these libraries with the team.

###	Data collection and EDA

The team scraped question & answer discussions on financial topics from social media such as Reddit, Quora, Facebook, and forums such as Ficoforum and Boglehead. The Reddit files were later discarded because they lacked the answers to the collected questions.

<p align="center">
  <img width="80%" height="80%" src="images/image(1).png">
</p>

<p align="center">
  <img width="50%" height="50%" src="images/image(3).png">
</p>

<p align="center">
  <img width="70%" height="70%" src="images/image(2).png">
</p>

###	Data pre-processing

We completed Data Cleaning with feature selection, drop null rows, drop rows outside of context, and outliers’ question and answer length. All these data sources have been merged into one file. To this file, one copy has been made and then has been applied all the steps for NLP pre-processing. We removed all the punctuation, links, emojis, numbers, and stop words. Then applied tokenization and lemmatization using the module nltk. We kept the original file with all the data merged. 

We analysed what would be the best approach for different models with processed and unprocessed data.

At a later stage, we nonetheless found issues with the dataset built from the data collected from social networks: many questions/answers were out of context, long sentences were often found instead of clear question-answer pairs. We therefore decided to go back to data collection. The team found a good finance Q&A dataset, the [Financial Opinion Mining and Question Answering challenge](https://sites.google.com/view/fiqa/home). This was well-structured and featured coherent Q&A pairs. Light pre-processing was performed to be able to use the data to fine-tune a language model for our chatbot.

##	The chatbot

<p align="center">
  <img width="70%" height="70%" src="images/streamlit.png">
</p>

###	Algorithm selection

In this task, the team explored the possibility to train/finetune existing transformers-based language models. The team were initially divided into two teams: one exploring Bert-based models, and the second team exploring GPT3 language models. 

The team eventually opted for the use of GPT-3 language models because all Transformer-based models tested by the team were text classification oriented, meaning that they require context in question-answering tasks. The  dataset we built for the project did not have the required structure and its transformation would have been unnecessarily time consuming.

The GPT-3 language models were thus the best option for our project. Those considered are the following:

<p align="center">
  <img width="70%" height="70%" src="images/models_table.png">
</p>

We started from fine-tuning the `ada` model because it has the lowest cost among all the models that we were considering. However, the results that we obtained were unsatisfactory. We therefore decided to rather work with `curie` as it is a very capable model which, compared to `davinci`, is faster and 10 times cheaper.

The Curie model was trained for 8 epochs on the Financial Q&A dataset. The resulting fine-tuned model, which we owe to Lamia Sekkai, was used within our chat-bot application. Below are two screenshots from preliminary performance tests that were run after 4 fine-tuning epochs.

<p align="center">
  <img width="70%" height="70%" src="images/testing.png">
</p>

<p align="center">
  <img width="70%" height="70%" src="images/testing2.png">
</p>

The same questions could not be answered by the non-fine-tuned `curie` model, as illustrated below:

<p align="center">
  <img width="70%" height="70%" src="images/testing3.png">
</p>

###	Publishing

Following the finalization of the chatbot algorithm, an interface was created on the [Streamlit](https://streamlit.io/) platform. 

Streamlit is an open-source app framework for Machine Learning and Data Science. It helps create and publish web apps in a short time. It is compatible with major Python libraries such as scikit-learn, Keras, PyTorch, SymPy(latex), NumPy, pandas, Matplotlib etc., and it does not require any front-end experience.

Streamlit was selected due to its multifunctionality and ease of usage. It also allows for the model to be hosted online and accessed by its users. For scalability, Flask was considered for integration with the Streamlit-hosted app.

The interface created by our engineers on Streamlit accepts an input from the chatbot user. This input is then sent through the model and an appropriate output is generated and subsequently displayed to the user.

The team decided to add the Omdena Lublin Local Chapter's logo to the application landing page, as well as the following disclaimer: 'The Content is for informational purposes only, you should not construe any such information or other material as legal, tax, investment, financial, or other advice.'. 

All publishing efforts were guided and coordinated by Vivienne Ordonez.

The chatbot is now publicly available at the following link: [https://omdena-lublin-financial-chatbot.streamlit.app/](https://omdena-lublin-financial-chatbot.streamlit.app/).

# Conclusions

[…]

____________________________________________________

This report was written and submitted by Caterina Bonan, Postdoctoral Researcher at the University of Cambridge, who takes full responsibility for any mistake or inaccuracy in it.

____________________________________________________

### Participants (in alphabetical order)

Rayan Kiswani
Abayomi Bello
Ahmed Salama
Aim Makarudze
Akash Biswas
Akanksha Sharma
Ananya Choudhary
Efrem Assefa
Bryan  Miranda
Enyinnaya Benjamin Uzuegbu
Mehmet Bertan Ulusoy
Bhaskar Abbireddy
Caterina Bonan
Tatenda Mukonoweshuro
Che-Yu Liu
Gowtham  CP
Derek Leckner
Rohit Nair
Fariz  Abdussalam
fathi mhiri
Rose Ann Fuentes
Priya  Gupta 
Garima Kapoor
Daniel Goddard Brookman
Shruti Gupta
Hanshika Gupta
Henok Ademtew
Peter Ibikunle
Irfan Pathan
Juan Castaneda
Jamie Handitye
John Cedric Angeles
Jean Denis
Jeshmitha Gunuganti
Nomin Khishigsuren
kang wang
Kartik Patil
Ketan  Mewara
Lydia Khelifa Chibout
Kirollos George
Udit Gagnani
Shivaani  Krishnakumar 
Surabhi Khandare
Lomash Yadav
Lamia Sekkai
Mahrukh Waqar
Mayank Garg
Megha Salimath
Mohamed Awnallah
Mukund shah
Yashwanth Kumar M V
Nabila Tajrin Bristy
Nadiera Mustapha
Navina Ganapathy Amuthan
Neethu Prabhakaran
Minh Huong Ngo
Rodgers Nyangani
David-Daniel Ojebiyi
Omkar Khade
PABAN GIRI
Vineeth Palani
Pritesh  Kuwar 
Pedro Velazquez
Prashanth Kumar Prashanthkumar
Priya Arora
Promodh  Fernando 
Lakshmi Raghavi Devalla
Raul Catacora
Ruan Donino
Shan Lin
Sadhana Savvaser
Samiksha Kolhe
Khushi Sanghrajka
Sayali Bachhav
Sandy Lauguico
Sharvi Endait
Shashank Rathi
Shashwath Punneshetty
Shivam Sunil Bhosale
Shubh Pathak
Siddhesh Pande
Surbhi Rohilla
Slawomir Lisowski
Soha Gad
Hetvi Soni
Sreejith Vidyadharan
Stephanie Creteur
Susan Claudia
Bisma Hilal
Thomas Gervais
Jia Yi Tan
Takashi Nishikawa
Tuyen Truong
Victor Ashioya
Vikas Patil
Vivienne May Ordonez
Weronika Limberger
