<div id="top"></div>

# Movies Rating API

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#test-with">Test With</a></li>
        <li><a href="#styled-with">Styled With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

This web api allows you to perform all the operations necessary for the operation of the [Movie Rating](https://github.com/Hens94/movie-rating-app) application.

[![Product Name Screen Shot][product-screenshot]](https://movieratingapi.hens94.com/)

[![Product Name Screen Shot][product-screenshot2]](https://movieratingapi.hens94.com/)

### Built With

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [EB CLI](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html)
- [Swagger](https://swagger.io/)

### Test With

- [Postman](https://www.postman.com/)

### Hosting With

- [Amazon Web Services](https://aws.amazon.com/) ([https://movieratingapi.hens94.com/](https://movieratingapi.hens94.com/))

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

- [Visual Studio Code](https://code.visualstudio.com/)

### Installation

1. Clone the repo

   ```sh
   git clone https://github.com/Hens94/movie-rating-api.git
   ```

2. Create the following enviroment variables

   ```sh
   MOVIES_API_DB_HOST : moviedb.czz9g76uprds.us-east-1.rds.amazonaws.com
   MOVIES_API_DB_NAME : moviedb
   MOVIES_API_DB_USER : admin
   MOVIES_API_DB_PWD : Asdsk8freak
   ```

3. Open the project in Visual Studio Code

4. Create your python enviroment

5. Install requirement.txt dependencies

   ```sh
   pip install -r requirement.txt
   ```

6. Run de server application
   ```sh
   py manage.py runserver
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

### Swagger

![Swagger screen shot][product-screenshot]

### Postman

![Postman screen shot][product-screenshot2]

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->

## Roadmap

- [x] Homepage – List of movies sorted by Date or Average Rating
- [x] Page for views the details of a movie
- [x] Pages for creating / updating / deleting movies
- [x] Pages for creating and viewing ratings for specific movies
- [x] User account creation and authorization. Can create a new user and can only rate a movie when logged in with a valid user
- [x] Admin pages to manage users, movies, and ratings
- [x] Users should be able to add movies to a watchlist and access that list

- [x] Deploy to AWS
- [x] Swagger spec
- [x] Unique and creative styling
- [x] Integrate 3rd party data source

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Henry Gadea Mendoza - [LinkedIn](https://www.linkedin.com/in/henry-gadea-mendoza-599264153/) - [Github](https://github.com/Hens94) - henry_gadea@hotmail.com

Project Link: [https://github.com/Hens94/movie-rating-api](https://github.com/Hens94/movie-rating-api)

AWS API Link: [https://movieratingapi.hens94.com/](https://movieratingapi.hens94.com/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->

[product-screenshot]: https://i.imgur.com/z77HwHP.png
[product-screenshot2]: https://i.imgur.com/YxXAZrX.png
