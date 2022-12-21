## DigiHome
A web-based application where you can feel at home. Journal about your feelings, keep track of your mood, and visit your own digital room!

## Technologies
For main website:
Python, Flask, Jinja, SQL, HTML, CSS

For beta DigiRoom:
Javascript, Three.js, Node.js, Express.js, ViteJS, Blender

## BETA Digiroom Note
This application has a beta feature called DigiRoom. This is a part of the website where you can explore and navigate around a 3D model of a room. This is still under development and has more requirements than the rest of the website.

## Requirements
For main website:
Flask, Python

For beta Digiroom:
ViteJS, three.js, node.js

## Instructions for running the project
1. Copy over ALL the files in diary2
2. Run 'flask run' to view the website

* Additional instrucitons for Digiroom
In order to view and enter Digiroom, the steps are as follows

* complete these steps before clicking on the link to view DigiRoom
* you will NOT be able to enter DigiRoom before following these steps

1. Ensure that you have npm and node.js installed (using an installer like nvm may be helpful)
2. Copy over ALL the files in diary1
3. Run 'npm run dev' in your terminal
4. If you run into any issues at this point, check again to see if you have npm and node.js properly installed. See link: https://docs.npmjs.com/downloading-and-installing-node-js-and-npm
5. Now, the website should be locally hosted at a URL
6. You should be able to view the website from the website you loaded previously in flask, but if not, change the url in diary2/index.html to the url of your locally hosted website

## How to use DigiDiary!
Users will first make an account when clicking on "Register". The username must not be already taken, and the password must be at least 6 characters long, have at least one letter, and have at least one special character from a preselected sort. Once successfully logged in, the user will have access to creating diaries and viewing old diaries.

At the top of the page, there is a navbar, which users can use to view the 3D model of the room, create a new diary entry, view any previous diary entries, and also change their password at the settings tab.

When arrived at the 3d model, use your cursor and click and drag to rotate the room and/or to zoom in and out of the model.

The "Create" tab at the top will lead users to a page where they are allowed to create new diary entries. Users must input a corresponding date for the entry (which they may do so from a calendar date and time selector), a title for the entry, a description of their day, and an overall mood to describe their day. After pressing the create button, users will be redirected to the entries page, where they are able to view the entry they just submitted, and any previous entries if they exist.

The "Settings" tab leads users to a page that allows them to change their password, by clicking on a change password button which leads them to a form where they are able to enter in their old password and enter in a new password they would like to have it set to.

The logout button at the top right allows users to log out of the website securely once they are done with the diary!

## About the Files
Diary2 Details:

- In our folder static, we have our CSS file.
- In our templates folder, we have all of the html templates the website uses.
- app.py is the main file we used to write all of our Python code so that we could route commands and be able to bounce between html files.
- digidiary.db is the SQL database where our users and diary table is stored.
- helpers.py is another Python file, adapted largely from the Finance Pset, that contains some functions that we utilized in our app.py file.
- README.md is our markdown file that walks users through our app.
- DESIGN.md is our markdown file that explains more about the design choices we made.

Diary1 Details:
- Because this is using a Vite bundler, index.html is the entrypoint for this website
- main.js contains the main script that index.html calls on
- The Experience folder contains everything necesary to call on and handle the 3D model
- package.json contains all the dependencies for this project

https://youtu.be/SeSHh7BgHP4
