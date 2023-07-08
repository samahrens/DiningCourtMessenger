# DiningCourtMessenger
This project monitors Purdue's dining hall menu in order to provide customer alerts for specific food items. Aftering being deployed on Azure, it receives data from the dining hall API daily and updates it into an SQL database. Using SMTP, daily notifications are sent out based on the query sent to the database. You can customize the specific food items. I chose "chicken" and "kiwi"s!
## How to Run
All you need to run this program is your own Azure connection string to a [Function App](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-function-app-portal#create-a-function-app).
The program will run daily and send text messages to your phone number with updates.
