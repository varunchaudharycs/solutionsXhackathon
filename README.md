# [SolutionsXHackathon]
## Virtual Bank Assistant- EVE
A banking friend that uses voice commands to perform banking operations

This assistant performs the following tasks:

  - Perform banking transactions according to the user command
  - Anamoly detection for fraud transactions
  - Blocking bank account due to suspicious activity
  - Other banking app operations as integrated functions
  
#### Components

Eve uses certain tools for implementation:

* [MySQL] = As database to store user bank information for retrieval and updation
* [Flask] = For Eve API deployment
* [Dialogue Flow] = For NLP, to extract entities and actions(https://bot.dialogflow.com/payment-bot)
* [Eve API] = As back-end, to fire queries 
* [Python] = Language of choice

!.[Work-flow](https://imgur.com/UzgH1pB)

#### Run-thru

!.[Eve in Bank of West](https://imgur.com/kQt3DzP)

1. User login to Bank of West website/app
2. Eve available to assist
3. User types/speaks command- "Send $50 to Bob"
4. Google Cloud service extracts entities and inference
5. Sends data to API deployed on Flask
6. The API fires back-end queries, balance amount checks and also performs anamoly detection for fraudulent transactions
- If transaction is fraudulent, asks the user for last 4 digits of bank account
- Incorrect user input blocks the account with a service message to visit the nearest branch

!.[Eve's About Us for Bank of West](https://imgur.com/8VZoLuF)

!.[Anamoly Fail](https://imgur.com/cX1cuKi)

!.[Anamoly Success](https://imgur.com/eavNVwO)

!.[Eve's Greeting](https://imgur.com/qPmiG9w)

!.[Handling missing data](https://imgur.com/SC0cxkv)

!.[SEND transaction](https://imgur.com/XX1kcEr)

#### TODO
1. Face authentication for on-the-fly transactions
2. Payment reminders