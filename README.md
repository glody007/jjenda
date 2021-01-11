# Jjenda

_JJENDA_

![Vue Logo](/docs/vue-logo.png "Vue Logo") ![Flask Logo](/docs/flask-logo.png "Flask Logo")

## Features
* [Flask-RestPlus](http://flask-restplus.readthedocs.io) API with class-based secure resource routing
* Starter [PyTest](http://pytest.org) test suite
* [vue-cli 3](https://github.com/vuejs/vue-cli/blob/dev/docs/README.md) + yarn
* [Vuex](https://vuex.vuejs.org/)
* [Vue Router](https://router.vuejs.org/)
* [Axios](https://github.com/axios/axios/) for backend communication
* [react]() for dashboard
* [express]() to serve static files
* Sample Vue [Filters](https://vuejs.org/v2/guide/filters.html)
* Heroku Configuration with one-click deployment + Gunicorn

## Template Structure

The template uses Flask & Flask-RestPlus to create a minimal REST style API,
and let's VueJs + vue-cli handle the front end and asset pipline.
Data from the python server to the Vue application is passed by making Ajax requests.

### Application Structure

#### Rest Api

The Api is served using a Flask blueprint at `/api/` using Flask RestPlus class-based
resource routing.

#### Client Application

A Express endpoint is used to serve the `index.html` as an entry point into the Vue app at the endpoint `/`.

The template uses vue-cli 3 and assumes Vue Cli & Webpack will manage front-end resources and assets, so it does overwrite template delimiter.

The Vue instance is preconfigured with Filters, Vue-Router, Vuex; each of these can easilly removed if they are not desired.

#### Important Files

| Location                      |  Content                                         |
|-------------------------------|--------------------------------------------------|
| `/api/app`                    | Flask Application                                |
| `/api/app/api`                | Flask Rest Api (`/api`)                          |
| `/frontend/src`               | Vue App .                                        |
| `/frontend/server.js`  				| Express Application															 |
| `/frontend/src/main.js`       | JS Application Entry Point                       |
| `/frontend/public/index.html` | Html Application Entry Point (`/`)               |
| `/frontend/public/static`     | Static Assets                                    |
| `/frontend/dist/`             | Bundled Assets Output (generated at `yarn build` |


## Installation

##### Before you start

Before getting started, you should have the following installed and running:

-[X] Docker - [instructions] ()

## Development Server

Run the app in development mode

```
$ docker-compose build
```

## Production Server

This app is configured to work with Heroku + docker and it's pre-configured.

#### The Build Process

The buildpack will detect the `heroku.yml` and install all dependencies.

#### Production Sever Setup

Here are the commands we need to run to get things setup on the Heroku side:

	```
	$ heroku apps:create jjenda
	$ heroku git:remote --app jjenda
	$ heroku stack:set container
	$ heroku config:set FLASK_ENV=production
	$ heroku config:set FLASK_SECRET=SuperSecretKey

	$ git push heroku
	```
