# IndianVotingAssistant
A personalised helper for voters in Indian Elections for only viewing information relevant to them for casting a vote.

Most people who vote in India are not aware of anything related to the candidates they vote for. In recent years, assembly elections in India have turned into USA-like presidential elections where voters just vote for a political party instead of voting for a candidate. The aim of this project is to create a very easy way to use way to see personalized relevant information about all eligible candidates related only to matters that the voter cares about.

## Components
This is a complete FOSS project, which means that it includes the backend as well as the frontend for creation of this service. Although, we do not want to restrict the utility of this apptication to a certain form of product. Hence, we have created an independent REST API backend which can be used with any frontend. 

Hopefully, this backend API will be used to create chatbots, Android/iOS/KaiOS apps, websites, Alexa Skills etc. Consequently, any issues, pull requests etc. related to the backend API must have the label `api` and the issues, pull requests etc. related to any form of graphical frontend must have the `gui` label.

### API
The API is hosted on AWS Lambda. The code (and `README`) for the same can be found in the `api`.

### GUI
As of now (May 2021), there is no work done on the frontend. Please feel free to fork this repository, add a new folder for a new frontend, like `android`, `fb_messenger_bot`, `alexa` or `web`, to start building such a GUI for end-users to be able to fully utilize this program.
