# Footy Stats CLI

Live site: [Footy Stats CLI](https://footy-stats-cli-7fb9beca2387.herokuapp.com/)

![Main image](documentation/imagery/images/main_image.png)

## About
Footy Stats CLI is a command line interface tool built using Python. It utilises 
the [football-data.org](https://www.football-data.org/) API. The aim of this application 
is to give value to the underlying API. Allowing end users to easily access, display 
and find the relevant information they need about a league, club or particular season. 

## How To: Program Instructions
The program itself is simple to use. It utilizes the keyboard to navigate,
select and display data. Breakdown of controls:

- **[UP/DOWN ARROW KEYS]**: Navigate menu items. Menu's are cyclical. Pressing down on the
last menu item will navigate to the first menu item. 
- **[ESC/Q]**: On menu screens, pressing either Q or ESC will navigate back to the previous 
menu screen. Allowing you to choose different criteria to display, e.g. different Leagues
or different Seasons
- **[ENTER]**: The Enter key is used to select a menu item. Once selected the program
will either show a menu screen or display data depending where you are in the program.
Enter can also be used when prompted, the app will ask the user to click Enter to progress.
- **[Q]**: Q, on its own, when viewing data from the main menu will navigate back to the main
manu. This option is used when the data displayed is paginated. 

## User Stories 

As a user, I want to be able to:

- Be guided through the program clearly.
- Feel comfortable with what I have to do next to use the program how I want.
- See the information I have asked for.
- Always have the option to navigate back if I need to.
- Seek help where appropiate.
- Know what it is I am viewing.
- Be prompted if I have done something wrong. 

## Design
I wanted the initial design for the application to intuitive to the user and easy
to navigate. The approach for the design was always "User First". To keep in mind
the problem that we were solving, easy access to football data. Menu's are navigated
using the keyboard. I didnt want any user input to navigate menus or to display the 
data. It needed to be easy to use. The application has a forward feeling to it. 
Always relying on keyboard entries to move around and navigate back and forth. 
When a user is viewing data they can use the keyboard to go back to the main menu.
With as little as two clicks on the main menu a user can select the data they 
want, see the data and go back to the main menu. The cycling menu feature saves 
time for a user they can quickly get from the last menu option to the first menu 
option with one click. 

- ### Inspiration
The idea behind how Footy Stats CLI should function and feel borrowed inspiration 
from the oldschool Teletext. Simply put, Teletext was the standard for displaying 
text and graphics on television sets. Its a nostalgic, childhood memory of checking
football scores on a saturday afternoon before the internet was made publicly 
available in Ireland. [More about Teletext](https://en.wikipedia.org/wiki/Teletext)

- ### Imagery 
The colors used in Footy Stats CLI are bright and visiually striking. The 
bright colors implemented in Footy Stats CLI were to mimic those found in Teletext,
seen below: 

![Teletext1](documentation/imagery/images/teletext1.png)
![Teletext2](documentation/imagery/images/teletext2.png)

- ### Wireframes
To get a better understanding of how the program would flow and fit together for 
the end user I created a wireframe using [Lucid Charts](https://www.lucidchart.com/pages/?)

![wireframe](documentation/imagery/images/Footy_Stats_CLI_wireframe.png)

- ## Research
I took notes when researching this project. Different potential projects for usings an 
API. The core idea was to always use an api and manipulate and display data to the end
user. The question was, what sort of data that would be. The links below show
some project planning and initial concepts. 

  - [Research](documentation/documents/Footy_Stats_Research.pdf)
  - [Initial Concept](documentation/documents/Footy_Stats_Initial_Concept.pdf)


## Features

- ### Iterable Menu 
All menu's are created with the help of python library [simple-term-menu](https://pypi.org/project/simple-term-menu/). 
It offers a cyclical scrolling which allows the user to navigate more quickly.

![Cyclical Menu](documentation/imagery/images/features/cyclical_menu.gif)

- ### Help & About Area
There is a help area on the start screen that provides a user with information on how to navigate the application.
It contains tips and tricks on how to best use the app. There is also an about area on the start screen. This screen 
provides information to the user about what type of data they can expect to see in the app. 

![Help and About Area](documentation/imagery/images/features/help_and_about.gif)

- ## Dynamic Menus
Menus are created using the [simple-term-menu](https://pypi.org/project/simple-term-menu/) this allows users to
select an option with their keyboard. No need for extra steps such as entering a value and clicking enter. This
leads to an enhanced user experience. 

![Dynamic Menus](documentation/imagery/images/features/cyclical_menu.gif)

- ## Saving User Selection
The menus displayed to the user are strategically placed. The League menu appears prior to the Seasons menu.
This allows the program to dynamically build the APIClient before making a request for data. It also allows the 
program to display the league and season to the user on the main menu screen. 

The same can be said for the Team menu. Before making a request for Team data, we ask the user to select their 
team of choice. The APIClient is then updated with the teams ID so we can make a request for data.

![Saving User Selection](documentation/imagery/images/features/Build_APIClient.gif)

- ## Back Navigation
A user always has the option to navigate back to the previous menu/screen. This helps the user either, navigate
back if they have selected the wrong option and choose a different selection. i.e A user can select the 2022/2023
season, view all the data and then navigate back to the Seasons menu and select a new season and view that data.
It allows the user to get everything they want, without leaving the program. The same can also be said for choosing
a different League option.

![Back Navigation](documentation/imagery/images/features/navigate_back.gif)

- ## Team Data
The program can display information about all teams that participated in that League during that season. It shows the 
Team, Year it was founded and the Stadium they play in. 

![Team Data](documentation/imagery/images/features/team_data.gif)

- ## League Table
The program can display information about the League Table for a particular season. It shows the Team, Matches Played,
Matches Won, Drawn Matches, Lost Matches, Total Points. 

![League Table](documentation/imagery/images/features/league_table.gif)

- ## Fixtures and Results
The program can display information about all of the Fixtures and Results for a League in a particular season. It shows 
the Date Played, Home Team, Away Team and the Score. 

![Fixtures and Results](documentation/imagery/images/features/fixtures_results.gif)

- ## Team Fixtures and Results
The program can go one step further and display an individual teams matches for a particular League and Season. It shows
the Date Played, Home Team, Away Team and the Score. 

![Team Fixtures and Results](documentation/imagery/images/features/team_fixture_results.gif)

- ## Top 10 Goalscorers
The program can display the Top 10 Goalscorers for a particular League and Season. It shows the Players Name, Players Team, 
Count of Matches and the Count of Goals Scored. 

![Top 10 Goalscorers](documentation/imagery/images/features/top_goalscorer.gif)

- ## Leagues and Seasons
The program displayes 5 Leagues and 5 Seasons. The Leagues shown are hardcoded. The only reason these leagues are hardcoded
is due to the restriction of the API Access Token the program uses. Seasons are automatically generated from the API. The 
program only shows the last 5 seasons due to the Access Token restrictions. There is a check before requesting the seasons 
for a league, if the season count is >= 5 then show 5 seasons. Else show the number of seasons available. 

![Leagues and Seasons](documentation/imagery/images/features/5_leagues.gif)

![Leagues and Seasons](documentation/imagery/images/features/5_seasons.gif)

- ## Input Handling
The program will only accept the keyboard input it asks for. If the user enters something other than what is asked for then 
the program displays a warning message saying "Sorry, thats not a valid action. Please try again" in red.

![Input Handling](documentation/imagery/images/features/input_handling.gif)



### Future Features

## Technologies

### Languages


### Other Tools


## Deployment


## Testing

## Credits

- ### Resources
 

- ### Media

- ### Helpful Links


- ### Acknowledgments 


## Bugs
