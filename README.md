# Discord Bot

Bot help you to make more social your server. This Bot have a large functional and games.
Also, this bot have MVC pattern structure in which you can figure out and understand how it works.

## What Mean Directories
- data — keep .csv and .txt files. We store phrases to generate phrase responses
         for various aspects of the game aspects and communication
- src — contains the main logic of the program, which I will describe in more detail below.
- cogs — classes to organize a collection of commands, listeners and some states. 
- data — classes to connect and interact with a database.
- functions — classes control in mvc. Some help functionality. 
- modules — classes to describe user model and additional functional to discord.


## How To Use It
run cristi.py


## Contacts 
- Tg — GTai_IT
- Discord — gtai


## Functional roles
- administators — have all privileges
- moderstos — have control in chat, voice chat, opportunities change all stats
- users — standart functional

## Administrators:
- .load_all — load all cogs
- .load [name] — load name cog
- .unload [name] — unload name cog
- .reload [name] — reload name cog
- .git_update — update to new version
- .all_add_money [money] — add/substract money to all users
- .all_set_money [money] — set money to all users

## Moderators:
- .add_money [name] [money] — add/substract money to user
- .add_rate [name] [money] — add/substract rating to user
- .add_req_help [name] [count] — add/substract request help to user
- .add_done_help [name] [count] — add/substract done help to user
- .add_count_projects [name] [count] — add/substract count projects to user
- .set_req_help [name] [count] — set request help to user
- .set_done_help [name] [count] — set done help to user 
- .set_count_projects [name] [count] — set count projects to user
- .get_info [name] — get all info (main stats) about user
- .duel_info [name] — get duel info about user
- .duel_top [name] — top 5 users in table with all_games, win_games, win rate (%)
- .top_rate [name] — top 5 users in table with main stats
- .set_user_date [user] [date] — set user date to user

## Users:
- /рейтинг — user's rating 
- /монеты — users' money
- /дней_на_сервере — users' current years, month and days on server
- /инфо — main stats about user