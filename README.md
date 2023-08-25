# Book Recommendation System

## Introduction
 With an increasing amount of information on the internet and a considerable increase in the number of users, it is essential for companies to search, map, and offer relevant information based on the preferences of users. Aan important functional means of providing personalized service to users is Recommendation System. This system uses algorithms and data analysis techniques to suggest items,content, or services that should be of interest to customers based on their past choices or by analyzing the preferences of similar users. Companies like Netflix, Amazon, etc. use recommender systems to help their users to identify the correct product or content for them.

🎯 The main objective of this project is to create a Book recommendation system that best predicts user interests and recommend the suitable/appropriate books to them ,using various approaches.

## Problem statement
 In some industries, the use of recommender systems is crucial because, when implemented well, they can be extremely profitable and set themselves apart from their competitors. Online book selling websites nowadays are competing with each other by many means.One of the most effective strategies for increasing sales,enhancing customer experience and retaining customers is building an efficient Recommendation system. The book recommendation system must recommend books that are of interest to buyers. Popularity based approach and Collaborative filtering approach are used in this project to build book recommendation systems.

## Source
The dataset for this project has been taken from kaggle.
Here is link :-https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset

## Features

### Users
User-ID: A unique identification number for each user
Location:It contains city,state and country to which the user belongs ,separated by commas
Age:The age of the user

### Books
ISBN:International Standard Book Number unique to each edition of the book
Book-Title:Title of the book
Book-Author:Author of the book(incase of several authors only the first is provided)
Year-of-Publication:The year in which the particular edition of the book was published
Publisher:Name of the Book Publishing company
Image-URL-S: URL link to a small version of the book cover displayed on the Amazon website
Image-URL-M: URL link to Medium version image of the book cover displayed on the Amazon website
Image-URL-L: URL link to Large sized image of the book cover displayed on the Amazon website

### Ratings
User-ID:as mentioned above
ISBN:as mentioned above
Book-Rating: The rating given by the user (identified by User-ID) for the book (identified by ISBN). It is either explicit,expressed on a scale from 1-10 (higher values denoting higher appreciation), or implicit,expressed by 0.


## Project Overview
The approaches used in this project are:

Popularity Based recommendation system
It is a type of recommendation system that bases choices on factors like popularity and/or current trends. These systems determine which item (in this case,books) are in the trending list or are the most well-liked by users and then directly recommend them.

Weighted average rating approach
Country-wise approach
Author-wise approach
Collaborative Filitering Based recommendation system
The Collaborative Filtering approach first investigates the user’s behaviors, interests, and searches for similar users. It recommends items to users based on the ratings of similar users on various items and by predicting the missing ratings of the items .

Here Cosine Similarity is used for prediction.
## Conclusion

