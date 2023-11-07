# HarvardX CS50W: Web Programming with Python and JavaScript

## REQUIREMENTS

The final project is our opportunity to design and implement a dynamic website of our own. So long as our final project draws upon Harvard CS50W's lessons, the nature of our website will be entirely up to us.

In this project, we are asked to build a web application of our own. The nature of the application is up to us, subject to a few requirements:

* Your web application must utilize Django (including at least one model) on the back-end and JavaScript on the front-end.
* Your web application must be mobile-responsive.
* In a README.md in your project’s main directory, include a short writeup describing your project, what’s contained in each file you created, and (optionally) any other additional information the staff should know about your project. This file should also provide your justification for why you believe your project satisfies the distinctiveness and complexity requirements, mentioned above.
* If you’ve added any Python packages that need to be installed in order to run your web application, be sure to add them to a requirements.txt file!


---

## Distinctiveness and Complexity

- The project I created is a interactively styled weather site. You are able to search a city's name and get the current weather, and the time in the city, this will then also change the styling of the website to match the current weather of the city. During the course I realized that the thing I struggled in the most was the implementation of APIs. So I chose this project to challenge myself to become more comfortable with finding and applying APIs. For complexity I used multiple API's to get a multitude of information of the city, from date and time of the city to its current weather. I used Django for the framework with a models for the cities. I also used Javascript to get a interactive frontend design so that it would change depending on the current weather of the city that user inputted.

## Files Information
- Views.py contains all of the backend code for the project, the main functions are:
    - Index:
        - This functions does multiple things all at once. First when the user first open the website this is the first function that is run. It uses the multiple API's that I have sourced to get information for the initial view of the webpage. This function also does error handling, where if something was to mess when during the collection of data thorugh the API's it would then set the webpage to a default city of London.

    - MyLocation:
        - This is the function that runs when the user selects the button to get the current weather of their current location. This function goes through an API which get the IP of the users computer and then uses that IP to interact with another API where it gets all the information for the city's weather. 

- Models.py contains the model for the city:
    - City Model:
        - When a new city is search up it is saved into the database so that it can be used in the future when the user comes back to the webpage if they remain on the same browsing session.

- The static file contains all of the static files for this webpage:
    - Contains all of the HTML that is used to style the webpages with techniques such as flexbox
    - It also contains the css with all of the initial styling for the webpage
    - It contains the javascript file that changes the styling of the page based on the current weather of the city that the user searches up
- The templates files hold the main template for the webpage
    - The city template in the file is what is used for the base outline when the user first opens the page. It is then used and dynamically changed when the user inputs differents cities to search for their weather.

- Urls.py:
    - This holds a url to the main page, and has a url to each city by taking the user input

## How to Run the Application

- Install project dependencies by running pip install -r requirements.txt
- Make and apply migrations by running python manage.py makemigrations and python manage.py migrate in the project directory
