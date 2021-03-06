# The Crypto Investment Monitor

Access to the project: 

LIVE: Click [here]() to access the live website. <br>
REPO: Click [here]() to access the Github repository.

# Table of Contents
- Project Goal
- The Five Planes of UX design
    - Strategy
    - Scope 
    - Structure 
    - Skeleton
    - Surface 
- Database design
- Features
- Technologies & Tools
- Testing
- Deployment
- Credits
    - Content
    - Acknowledgments
    - Used websites 

# Project Goal
Monitoring your assets is always the best thing to do as a cryptocurrency investor. For this reason, this project aims to provide a comprehensive overview of the assets which the users' holds as well the transactions made by the user. The main focus will be the P/L (profit and lost) for each asset which the user is holding compared to the actual prices. 

# The Five Planes Of UX Design

## Strategy
The platform's concept is to provide a comprehensive overview of currently holding crypto assets. The user are able to set up a deposit and insert their transactions. The platform combines this to a overview, with current profit and loss calculated on real time prices. In the leaderboard section of the platform the top 10 users with most profits are listed. Other users can see the crypto's in which are investing and are able to make choices based on the best performing portfolio's. 

## Scope
The project itself is a crypto investment monitoring tool. The project consist out of different epics which work together as a whole. 

### Epics & Features 
#### <strong>Homescreen</strong>
This epic is the entry point of the website, from here the users can navigate to the login or register page as well to the leaderboard. 
#### Features 
- Presentation
- Button functionality


#### <strong>Login/Register</strong>
This epic enables users or potential users to make an account and login to the platform. The user will be connected to his own assets and transactions make the platform personalized for each user. Also, the options to register a deposit or a transaction can only be made when a user is logged on to his account. Lastly, a user must be able to delete his account with all underlying assets and transactions as well. 
#### Features 
- Presentation
- Login 
- Logout
- Register 
- Autorize 

#### <strong>Assets</strong> 
This epic consist out off different features which are connected to the assets management of the user. The user will be able to register their asset in USD. From their they can obtain other assets by doing transactions. Those assets will be visually presented by to the user as well the unrealized profits will be shown. Also a complete valuation will be shown to the user to make them able to monitor their assets closely with real-time information.  
#### Features 
- Presentation
- Deposit 
- Withdrawal
- Live valuation
- Profit and Loss 

#### <strong>Transactions</strong> 
The transactions are as well a backbone of the platform. As soon the users register their first asset in USD, they are able to register their transaction. Those transactions will be saved into the database and can be looked into. 
#### Features 
- Presentation
- Transaction validation 
- Add transaction

#### <strong>Leaderboard</strong>
The leaderboard is a open for everyone part of the platform. The aim of this page is to inform people about the most succesfull portfolio's. The overview show the top 10 succesfull portfolio's and give an overview which assets are included in the portfolio. 
#### Features 
- Presentation

#### <strong>Error handling</strong>
The error handling is part of defensive programming. In order to prevent the application to digest malicious data, some error handling measures are in place. Firstly, the unauthorized error, page not found error and also an internal service error. Those errors will be catched and the user will be redirected to the page, respectively. In case of an unknown exception or exception which has not their own page, the general error page will be shown. 
#### Features 
- Presentation 404
- Presentation 401
- Presentation 500
- Presentation general

### Nice to have 
One downside of the platform is the manual input used from the user to register their assets and transactions. It would be ideal to wire up the trading platform with the monitoring platform to automatically import the trades and assets from the user's account. But this is not in the scope of this project. 

# Structure 

The website will contain different pages as well for logged in users and not logged in users. The following tree map structure will further outline the intented structure for the website. 

- ( insert picture of treemap )

Furthermore, the portfolio is be compatible with all kind of devices. Small design changes can be expected such as omitting some data at smaller devices screens. But the main functionalities should be easy to use and understand on all devices. 

# Skeleton

The webapp consist out of the following views: 
- Welcome view
- Login view
- Register view
- Leaderboard view (while logged in)
- Leaderboard view (not logged in)
- Assets view
- Deposit/Withdrawal view
- Transactions view
- Add transaction view 
- Logout view
- 404 (page not found exception) error view 
- 401 (unauthorized exception) error view 
- 500 (internal server error ) error view 
- General error view

### Desktop design
### Tablet design
### Mobile design


https://dev.to/blankgodd/creating-a-blueprint-based-flask-app-199h



