## Behind the Scenes


## Diary 2

### SQL
We configured a SQL database digidiary.db which includes 2 tables:

We have a users table that stores session information for users: id which is a unique id that identifies users, username which represents a user's username, and a password hash that represents a user's password.


We have a second diary table that stores diary entry information with 6 fields: an id for each diary entry, user_id, a date variable that stores the date of the entry of the user, title which includes the titles of entries, content which contains whatever the user chose to write about their day, and mood which contains the mood of the day the user inputted.

### Python/Flask
Our app.py file is the python file we used to route different commands.
- / simply returns users to the homepage
- /login first clears any sessions that are currently running and lets new users login by checking if the login information input matches what the SQL database has in the users table.
- /logout logs users out by quitting any sessions currently running and then routes users back to the main page.
- /register allows users to register an account. If a username and password passes multiple checks, it will be input into our SQL database in the users table.
- /create lets users create their diary entries by collecting a user's unique id, and then also the date, title, content, and mood inputs that users fill out. If the user did not forget any input fields, the data will be inserted into the diary table and the user will be redirected to the entries page where they can view the entry they just inputted and any past entries.
- /entries saves all entries in the diary table so that they are able to be displayed.
- /settings routes users to the settings page
- /changepassword collects a user's unique id, checks if an old password input is correct, and collects the user's new password input after it passes multiple checks. It then generates a new password hash and we update the data in the users table w/ the new password hash. We wanted users to be able to change their password since a diary should be a private safe-space, as we should, so should any user's password be compromised, they are able to resecure it by changing it.

In our helpers file we utilized two functions both adapted from Finance to help us with our project:
- apology, which returns a meme of a cat with an associated apology message
- login_required that helps check if users are logged in since some pages are only accessible to a logged in user.

### HTML/CSS
We first created a layout template that sets the overall layout of every page with a navbar at the top. Using Jinja, we were able to extend that layout to all of our other HTML pages, since we wanted the navbar to always be accessible, and then the unique HTML we coded for each of the templates is embedded in the main content of each page. A lot of Bootstrap was also used in the process to help us easily beautify the website, as well as a CSS file we edited to our tastes.

## Diary 1 (3D Model)

## Javascript and HTML/CSS
- I used Three.js as primary javascript package we used to load and handle the 3D model that I created in Blender.
- We used Vite to bundle our website with the HTML, CSS, and Javascript
