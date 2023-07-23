# DiningCourtMessenger
This project monitors Purdue's dining hall menu in order to provide customer alerts for specific food items.
## The Problem
Purdue's dining court menus list hundreds of items daily and scanning all of them to decide where to eat is tiresome. I made this notification system to alert the user of common food items they want to eat, so they know which dining court to go to instantly.
## How It Works
I deployed this program on an Azure Function App in order to run it daily, since they have a built in timer-trigger (cronjob). It retrieves the updated menu items from an API provided by Purdue and stores them in a SQL database. Then, another Function App queries the database with the user's inputted food items, and it sends a notification if there are any matches.
## Why I Made This
Learning Python is fun and I wanted to make something useful
## Helpful Resources
(for reference)
* [Azure Function App timer triggers](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-timer?tabs=python-v2%2Cin-process&pivots=programming-language-python)
* [Python's SMTP module](https://docs.python.org/3/library/smtplib.html)
