 # ClanBank

## Spending Tracker
Build an app that allows a user to track their spending.

### MVP
* The app should allow the user to create and edit merchants, e.g. Tesco, Amazon, ScotRail
* The app should allow the user to create and edit tags for their spending, e.g. groceries, entertainment, transport
* The user should be able to assign tags and merchants to a transaction, as well as an amount spent on each transaction.
* The app should display all the transactions a user has made in a single view, with each transaction's amount, merchant and tag, and a total for all transactions.

### Possible Extensions
* The user should be able to mark Merchants and Tags as deactivated. Users will not be able to choose deactivated merchants/tags when creating a transaction.
* Transactions should have a timestamp, and the user should be able to view transactions sorted by the time they took place.
* The user should be able to supply a budget, and the app should alert the user somehow when when they are nearing this budget or have gone over it.
* The user should be able to filter their view of transactions, for example, to view all transactions in a given month, or view all spending on groceries.

***
## To Run File:

1. Drop Database
```sh
dropdb -d spending_tracker 
```
2. Create Database

```sh
createdb -d spending_tracker
```
3. Connect Database

```sh
psql -spending_tracker -f spending_tracker.sql
```
4. Seed Database

```sh
python3 console.py 
```
5. Run Server

```sh
flask run 
```
***

### About:

I built the app with a SQL database with a one to many relationship between the transactions and the merchants and tags. The main functionality that I was proud to achieve with this project was to be able to filter by either merchants or tags.
The project really consolidated the 5 weeks of learning and made me realise how far I had come. I learned the importance of planning and time management.




## The Home Page:
![Home page](static/screenshots/home_page.png?raw=true "Home Page")

further work would see the home page updated with a different fact each day.

## Transaction List:
![Transactions](static/screenshots/transactions.png?raw=true "Transactions")



## Editing a Transaction:
![Edit Transaction](static/screenshots/edit_transaction.png?raw=true "Edit Transaction")

## User Profile:
![Profile Page](static/screenshots/profile.png?raw=true "Profile Page")





