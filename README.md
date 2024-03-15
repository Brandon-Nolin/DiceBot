# A simple discord bot to roll dice


### Commands:
The bot contains two commands:

  - /roll: Rolls the specified dice and responds with the result.
  - /sync: Syncs the roll command so it can be seen in the discord app UI as a possible command. This command is only usable by the developer.


### Format of /roll:
The input of the /roll command is in the format "/roll [die] [mod]" where die refers to the amount and denomination of dice. For example, 3d20 would return the result of rolling 3 20 sided dice. The mod parameter refers to the modifier to add or subtract, which is a positive or negative number. 


### How to run:
To run this bot you will need to set up a discord bot through the discord developer portal and add it to the server(s) of your choice. Once properly set up, add a .env file to this programs folder including the TOKEN and DEV_ID variables. TOKEN being your bots token and DEV_ID being the discord id of the account you want to have access to the developer /sync command. Once everything is set up, you can run the bot_controller.py file and you will be able to use the two commands in your discord server.