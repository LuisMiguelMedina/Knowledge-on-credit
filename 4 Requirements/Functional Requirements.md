
# 1 Introduction 

## 1.1 References 

This document is loosely based on the IEEE Std 830-1998 Recommended Practice for Software Requirements Specifications.  

# 2 Overall Description 

## 2.1 Product functions 

The Knowledge on Credit will present information to the user in the form of quick interactive lectures and provide feedback on the answers the user enters. It will also allow the user to take notes on the lectures and share them with a community.  


## 2.2 User characteristics 

The user is our focal Persona: Ernesto Bocadillo. The main need of the user is the quality of the learning experience and information presented. He wants to learn on a mobile application with different types of tests and take text and diagram notes, he also wants to share his notes with a community, all that within a 20m time frame.  


## 2.4 Assumptions and dependencies 

- **Assumption 1**: The user should be able to do all this scenarios within a 20min range

# 3 Specific requirements  
 
## 3.1 External Interfaces 
- Log in Interface 
- Study plan interface 
- Lesson interface  
- Quiz interface
  - True or false question
  - Multiple choice question
  - Relate concepts
  - Complete sentence
- Rubric view
  
## 3.2 Functional Requirements

### 3.2.1 Authentication and Registration

1. The system shall allow the user to register an account with unique credentials within 5 seconds
2. The system shall notify the user if the account was successfully created within 10 seconds after entering their credentials.
3. The system shall notify the user if the account was not successfully created and indicate the reason within 10 seconds after entering their credentials and.
4. The system shall allow the user to log-in to their account.
5. The system shall notify the user if their login was successful within 10 seconds after the credentials are entered.
6. The system shall notify the user if their login failed and indicate the reason within 10 seconds after the credentials were entered.
