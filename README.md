# Uberhack_backend

# CHILDREN STRESS DETECTION APPLICATION USING NATURAL LANGUAGE PROCESSING AND DEEP NEURAL NETWORKS 

CHILDREN STRESS DETECTION APPLICATION USING NATURAL LANGUAGE PROCESSING AND DEEP NEURAL NETWORKS 



## 1/ Introduction
We introduce Howde, a friendly chat-bot app which is designed to communicate with users, detecting negative thoughts and preventing it from elaborating. The app includes five main features: Howde friendly chatbot , Howde depressed diagnosis system, Howde the supporter, the Howde networking, Howde diary,. 

While using the application , users can interact with the Howde friendly chatbot which can give simple advice. Next, the Howde network allows customers to connect with other users . User’s data such as daily heart rate, past depression diagnostic session’s results together with their happy memories and achievements are recorded in the Howde diary to keep track of the user’s status. Furthermore, the app can detect negative thoughts using the Howde depression diagnosis system. In other words, it could measure users’ heartbeat as well as scan the conversation  to identify whether the users are in a bad mood and need support. By comparing with the information stored in the Howde diary, the app will evaluate the significance of the problem, and if more then 4 symptoms of depression are detected, the bot will automatically switch to Howde the supporter mode. In this mode, the bot will offer to converse with the user more frequently and remind them about their success, their happy memories in the past as well as revoke their interest in other habits . The bot will use the data from the diary to make the best decision. In the meantime, Howde will contact the user's parents or friends and inform them about the customer’s situation so that they can seek help and support them to learn about depression on their own; the app will also connect them with other users who have faced the same issues. The chat-bot is also capable of reminding users of everyday tasks and taking care of their health by continuously measuring their heart rate, sleep condition and giving advice


## 2/ The problem
Depression is a common illness worldwide and the amount of people who have to face it is predicted to increase rapidly. According to WHO, there are about 280 millions people suffering from depression. Depression can lead to declines in the work efficiency of affected people. They might find difficulty in performing daily activities. They may also feel tired all the time, suffer lack of sleep as well as negative changes in personality. This can further result in self-harm or violence towards those who may be perceived as the cause. In the worst scenario, depression can lead to suicide. Despite being a serious problem, more than 75% of people in low- and middle-income countries receive no treatment due to WHO. 

“There are barriers to effective care including a lack of resources, lack of trained health-care providers and social stigma associated with mental disorders. In countries of all income levels, people who experience depression are often not correctly diagnosed and may not receive proper treatment, and others who do not have the disorder are too often misdiagnosed and prescribed antidepressants,” said WHO.

### 2.1/ How will our product help:
Customers can interact with our friendly, intelligent chatbot at any time, anywhere. Our apps can effectively detect depression via various methods ( measuring heartbeat, recording daily sleep condition, identifying negative meaning context) , evaluate the situation and give the best decision based on the data stored in the Howde diary. The app could also seek help from the customers’ friends, parents as well as connect them with other users, especially psychologists and those who have suffered the same issue.
.
### 2.2/ Target users

We intend to help users of all ages, but focus on young customers. They are the group of people who are familiar with technologies and frequently use it, which will allow the app to reach its full potential. People in this range of age are also the most likely to have negative thoughts due to the stress caused by financial problems, work, unhealthy lifestyles as well as personal relationships. Users experiencing depression are more likely to neglect daily activities, pay less attention to their health, and rarely interact with others. They might also progress negative thoughts which may results in tragic consequence such as suicide. 

As you may have known, the Vietnamese school system requires students to study multiple subjects all at once and include regular exams to ensure that students have the basic knowledge. As a result, many schoolchildren are under a heavy burden of getting high scores in standardized tests. Nevertheless, some parents in my institution rely mainly on academic performance to judge kids’ future. This problem has caused many to undergo stress, which may lead to depression if not treated properly. This project will help identify those students and get help as soon as possible to ensure children’s both physical and mental well-being. This will create a healthy environment in schools and promote learning between peers (Studies have shown that children who are less stressed are more creative in terms of solving real-world situations.). Furthermore, both children and parents (and teacher) will have a mutual understanding, strengthening family’s relationship.

### 2.3 What’s new?

There are many free version of the app.

Howde is integrated with a network which allows users to communicate with others.

The app can also connect with therapists to make the best decisions.

## 3/ Current status

This project is currently an idea. There are, however, many other companies who have already been developing stress detection applications, but they often come with high prices and focus on a wide range of ages and types of people. Our product is free of charge and focuses on children in their teenage years. In the next few weeks, we will develop our first prototype and test it on schoolchildren across Ho Chi Minh city.   

## 4/ Technology
In this project, we are planning to apply Artificial Intelligence (AI) to find the emotional state of the user. In particular, we will use a subfield of AI called Deep Learning which employs the use of deep neural networks (which are analogous to a human brain, where one unit - called activation -  corresponds to a neuron in the human brain.) 


<img src="./img/deep-neural-network.jpg" width="750" height="500" />



An illustration of a deep neural network. A deep neural network consists of an input layer,  multiple hidden layers, and an output layer.

Source: Kdnuggets.com

We will be using Python for the detection of stress. There are many frameworks that will be applied in the project, but the two most important ones that will be utilized here are Tensorflow and Pytorch. They are among the most well-known deep learning frameworks written in Python and have been applied in numerous fields such as medical imaging or self-driving cars. Other frameworks such as spaCy or Microsoft’s NLTK will be used to preprocess input data from end users. 

We are importing BERT (Bidirectional Encoder Representations from Transformers) library, specifically its components for fine-tuning BERT models for various NLP tasks. BERT is a popular pre-trained language model developed by Google that has shown remarkable performance on a wide range of NLP tasks. We are focusing on fine-tuning BERT for classification.

Comparing to BERT, we are using 2 more models Word2Vec + TF-IDF and TF-IDF.
* Doc2Vec and Word2Vec are two popular techniques in natural language processing (NLP) that are used to represent words and documents (sentences or paragraphs) as continuous vector representations in a high-dimensional space. They are both part of the family of methods known as word embedding techniques, which aim to capture semantic relationships and meanings of words and documents.
* TF-IDF (Term Frequency-Inverse Document Frequency) is a numerical representation technique used in natural language processing (NLP) and information retrieval to assess the importance of words in a document relative to a collection of documents (corpus). 

From these libraries, we will build our neural network and train them using the free online jupyter notebooks named Google Colab which also include free cloud GPU to speed up our training. We will also utilize some of the state-of-the-art pre-trained deep learning models like Transformers to get the best results. The data collected from users will then be fed to the algorithms so that they can learn directly from the customers and improve their predictions overtime.

### Overall model results
- Recall is the most important metric because we want to identify the stress posts accurately. However, we also want to prevent
misclassifying a lot of non-stress posts as stress post. 
- Although word2vec+tfidf with random forest has the highest recall, it also misclassified a lot of non-stress as stress 
(low precision). 
    - Some sentences may look non-stress, but they include words with high tfidf weights in stress posts (from train set),
    which may make them be classified as stress.
    
- BERT is the most stable model in this case, with a balanced FP and FN. 
- Both models can predict whether the text is stressful or non stressful and provide a confidence score

| Feature Extraction Model | Best Classification Model | Precision | Recall | F1-Score |
| :---------------- | :-------------  | :-------- |:-------| :------- |
| TF-IDF            | Logistic Regression         | 75.1%     | 75.7%  | 75.4%    |
| Word2Vec + TF-IDF | Random Forest   | 69.4%     | 84.8%  | 76.3%    |
| BERT              | Fine Tuning NN  | 80.8%     | 81.0%  | 80.9%    |

### BERT Prediction
<img src="https://github.com/gillian850413/Insight_Stress_Analysis/blob/master/img/bert_result.png" width="750" height="200" />

In addition, another programming language, Javascript, may be used to build the interface of our application, although in Python there are numerous graphical user interface frameworks like PyQT or Kivy.


## 5/ External Links
Additional resources and research studies can be found here
## 6/ Additional information
We commit to protect user privacy as all critical information is encrypted and will not be shared to third-party companies. 

News about depression: \
[Depression in fathers and children linked, regardless of genetic relatedness](https://www.sciencedaily.com/releases/2022/07/220706153059.htm) \
[Complex post-traumatic stress disorder](https://www.sciencedaily.com/releases/2022/07/220701113149.htm) \
[Researchers uncover brain waves related to social behavior](https://www.sciencedaily.com/releases/2022/06/220627100231.htm) \
[Losing a grandmother may trigger rise in depression for some of her survivors](https://www.sciencedaily.com/releases/2022/06/220615113247.htm)





## 7/ IDEAL OUTCOME
By competing in the Stemhacks, we hope our team will be able to reach out to those investors. We believe that our project can help alleviate depression in many students nowadays. Moreover, Stemhacks is a competition where we could find out more ideas which can develop ours better. It is also a competition where we can test whether our ideal and technology would be suitable before considering making it real. This project is likely to be charitable work rather than a profitable project. Therefore,through Stemhacks we hope this idea can soon be a solution to those problems.
