<div align="center">
    <a href="http://corona.bel3raby.net/dashboard/">
        <img src="static/logo-dark.png">
    </a>
</div>

# Corona Bel3raby
A COVID-19 dashboard focused on Egypt & Arab League analytics.

Check out the site live at:  [![CoronaBel3raby](https://img.shields.io/badge/webiste-live-brightgreen.svg?style=flat-square)](http://corona.bel3raby.net/dashboard/)

# How to
- **Worldwide** Results
<div align="center">
    <img src="static/img1.png">
</div>

- **Egypt** Results
<div align="center">
    <img src="static/img2.png">
</div>

- **Africe** & **Arab League** Results
<div align="center">
    <img src="static/img3.png">
</div>

- Mobile Screenshots

<p float="left">
  <img src="static/img4.png" width="400" height="600" />
  <img src="static/img5.png" width="400" height="600" />
</p>


# Sources
- [Worldometer](https://www.worldometers.info/coronavirus/)
- [JHU CSSE](https://github.com/CSSEGISandData/COVID-19/)


# Development Guidelines

## Backend
- Install python 3
- Install requirements.txt dependencies with pip
- Set the environment variable DATABASE_URL to db.dev location
- `python3 manage.py run` to run the API server
- Navigate to any of the API urls /api/reports

## Frontend
- Install node 10 or higher
- `npm install` to install the dependencies
- `npm run dev` to start nuxt development server