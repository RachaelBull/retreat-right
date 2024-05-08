# Retreat Right

## Introduction

Welcome to Retreat Right. A travel blogging website based solely on my personal reviews and recomendations upon where I've travelled to and where I think that other people would like. Users can sign up, sign in, read already created blog posts, comment on posts and create and update their own profile.

This site is based around user authentication and user interactivity to create a feeling that the user is safe and in control whilst on this website.

[Visit the Website Here](https://retreat-right-89a95f86c8e5.herokuapp.com/)

[Visit this projects repository here](https://github.com/RachaelBull/retreat-right)

RESPONSIVE PIC TO GO HERE

LIST OF CONTENTS TO GO HERE

# UX

## User Stories

*First Time User:
- As a first time user, I would want to be displayed a visually attractive landing page that is descriptive.
- As a first time user, I would want to be shown a few posts on the landing page with catchy titles and excerpts to temp me to read more.
- As a first time user, I would want to be able to sign up for an account with Retreat Right.
- As a first time user, I would want the landing page and all pages to show clear nav links so that I can navigate around the website easily.

*Returning User:
- As a returning user, I would want to be able to log into my account easily using the nav links at the top of the page.
- As a returning user, I would want to open up posts and be able to read comments and comment on the posts.
- As a returning user, I would want to be able to create my own profile via the profile link and update it freely.

## User Stories Table

| id  |  Content | Label |
| ------ | ------ | ------ |
| [1](https://github.com/RachaelBull/retreat-right/issues/1) | As a Site User, I can click on a post so that the content will be displayed for me to read. | Must Have |
| [2](https://github.com/RachaelBull/retreat-right/issues/2) | As a Site User/Admin I can see the comments on the posts so that I can be involved in the conversations. | Must Have |
| [3](https://github.com/RachaelBull/retreat-right/issues/3) | As a User I can register for an account so that I can have access to the sites features. | Must Have |
| [4](https://github.com/RachaelBull/retreat-right/issues/4) | As a User/Admin I am able to comment on posts so that I can be involved in the conversations. | Must Have |
| [5](https://github.com/RachaelBull/retreat-right/issues/5) | As a User I am able to modify or delete my own comments so that I can make a decision upon what I would like to be involved in. | Should Have |
| [6](https://github.com/RachaelBull/retreat-right/issues/6) | As an Admin I can create, read, update and delete posts so that I can keep my site to my liking. | Should Have |
| [7](https://github.com/RachaelBull/retreat-right/issues/7) | As a User I can create drafts so that I can come back and finish my content at a later time | Must Have |
| [8](https://github.com/RachaelBull/retreat-right/issues/8) | As an Admin I can approve users comments so that I can keep track of the content being posted onto the site | Could Have |
| [9](https://github.com/RachaelBull/retreat-right/issues/9) | As a User I can like posts so that I can express my interest in the content | Could Have |
| [10](https://github.com/RachaelBull/retreat-right/issues/10) | As an Admin I can delete users so that I can manage who has accounts on the site | Could Have |
| [11](https://github.com/RachaelBull/retreat-right/issues/11) | As a User I can view posts from the homepage so that I can choose which one I would like to read. | Must Have |
| [12](https://github.com/RachaelBull/retreat-right/issues/12) | As a User, I am able to click on the about page link so that I can read about the website. | Must Have |
| [13](https://github.com/RachaelBull/retreat-right/issues/13) | As an Admin, I can create and update content on the About page to keep the content up to date and relevant. | Must Have |
| [14](https://github.com/RachaelBull/retreat-right/issues/14) | As a site owner, I can store contact requests from the form so that I can view them whenever desired. | Should Have |
| [15](https://github.com/RachaelBull/retreat-right/issues/15) | As a site viewer/user I can fill out the contact form so that I can get in direct contact with the site owner. | Must Have |
| [16](https://github.com/RachaelBull/retreat-right/issues/16) | As a site user, I can view my profile so that I can read and update my profile. | Could Have |

## Strategy

My aim is to bring in people that are serious and passionate about trying new things and wanting to see the world from other peoples views and angles. In order to do this I took a mental note that I would have to keep my target audience in mind at all times in order to achieve this goal.

My intended audience is:
- People of any age as my posts are adventurous, spontanious and diverse.
- Individuals that are passionate about travel and adventure.
- People who love to try new things and are keen on reading from other peoples experiences.

How I will draw in my audience:
- I will aim to try and captivate my audience by producing well written, well formatted, relevent and intruiging posts to create a feel as though the user was there with me.
- I will regularly update my posts to keep users entertained and to keep fresh content flowing through the website.

## Scope

This website will consist of the following features:

- A clear and attractive landing page
- Readable nav header links
- Further link promps over the landing page
- An option to register for an account
- An option to signi in to an account
- Allow the user to create and update their own personal profile
- Allow the user to comment on posts
- Allow the user to edit their comments
- Allow users to delete their comments
- Allow users to open and read posts
- Allow users to open and read the about page


## Wireframes and Design

WIREFRAMES WILL GO HERE

## Data Model Plans

DATA MODEL PLANS WILL GO HERE

# Data Models

Here I will explain in more depth what each model will do and is expected to do.

**User Model**

- The user model is an automatically generated default model from Django Authentication
- This model comes with user login authentication prompting the user to log in to their account or to sign up for an account
- The user model has a one to many relationship with the user post model. This is because the user can have many posts (in this websites case that would be me) but the post has only one author, the posts are authenticated to see if the user is logged in and has an account
- The user model will link anything such as comments, profiles, post etc to one user, so that only the content the user has inputted and provided may be shown/ avaible to edit to that user depending on the circumstance.

**Post Model**

- The post model is a one to many relationship with the user model and the post model as the user is able to have many post but each post has only one author
- The author field in this model is used as a Foreign Key that will be the main link to a user for authentication
- This model will give the creator (me in the website's case) fields to fill in from the admin panel in order to create a post. This consists of; A title field, a slug field, a content field, a ticket price field, a status field, an excerpt field, a created on field and an updated on field.

**Comment Model**

- The comment model has a many to many relationship regarding the post model but a many to one relationship in regards to the user model
- This model will use the post and author as the foreign keys for verification of a user to link the user to any comments they have made throughout the website
- The user has full ability to fill out the content of the body field provided to leave comments
- A time and a date will be automatically generated whenever the user leaves a comment to signify when the comment was left
- This model contains an approved field which essentially will send the users comment off to the admin panel for approval before it is left in the thread onto the post

**About Model**

- The about model acts as an additional information page about the user and the website itself
- The about model has fields that only the superuser can fill in and edit from the admin panel to keep the contents of this page to a high standard and free from outside customisation

**Profile Model**

- The profile has a one to one relationship with the use model as the user can only have one profile and that specific profile can only belong to one user
- The profile model consists of a name field, an email field, and a bio field which the user is able to create and update freely
- The contents updated by the user will stay filled in in the form in order for the user to come back to and read/update