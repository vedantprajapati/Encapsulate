# Goal

To create an application that allows users to:
- view their google calendar
- workout plan for the day
- create todo lists
    - simple ones
- manage their daily habit tracking
- visualize the habit tracking data

Create a react app?

Menu is a cli that looks kind of like notion ui/font etc


-----------------------------------------------
Epsilon - COMMAND_HERE(i.e calendar)
-----------------------------------------------






FRAME OF INFORMATION HERE







-------------------------------------------------

Lists of commands


- /h, /help
    - List commands
- /s, /start
    - register user with username/password
    <!--- LATER provide the ability to register with google sso? maybe -->
- /li,/login
    - username
    - password
- /lo, /logout
- /v, /view
    <!-- - LATER calendar (uses calendar api, not embed) not sure how much information it will require -->
    - todo
    - workout
    - weather
    - news COUNT(number of headlines/urls to view from google news world)
    - habit
    - history (view the user's past login history)
    - profile
- /a, /add
    - exercise NAME(STR) SETS(STR) REPS(STR)
    - routine NAME(STR)
    - routine EXERCISE_NAME
    - email NUMBER --ALIAS
    - todo
- /r,/remove
    - todo NAME
    - routine NAME
    - exercise NAME
    - habit NAME
    - email NUMBER/ALIAS
- /e, /edit
    - bm NAME 
        - --URL=URL
        - --NAME=NAME
    - email NUMBER/ALIAS
        - --URL=URL
        - --ALIAS=ALIAS
- /s,/set
    - home ADDRESS
    - name NAME
    - password PASS
    - mail NUMBER ALIAS URL
    - bm(bookmark) NAME/URL
- /o, /open (opens link in new tab)
    - maps
    - directions ADDRESS(REQUIRES HOME TO BE SET)
    - q(quercus)
    - gpt
    - bank
    - email NUMBER/ALIAS
    - bm(bookmark) NAME
    - yt 
    - drive
    - docs
    - sheets
    - cal
- /g. /google
    - new
        - cal
        - sheets
        - docs
    - drive/dr
    - cal
    - sheets
    - docs
    - colab
