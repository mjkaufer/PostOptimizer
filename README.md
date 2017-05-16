PostOptimizer
=============

Find best time to post to certain subreddits

Usage
-----

`GET /subreddits/update/:subreddit` logs and returns data for `:subreddit` from the top 100 posts
`GET /subreddits/stats/:subreddit` aggregates data for `:subreddit` from existing data stored



PostOptimizer saves the day and hour of submission of the top 100 posts of the month from a certain subreddit

[![Built with Cookiecutter Django]]

License
MIT

Settings
--------

Moved to [settings].

Basic Commands
--------------

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you’ll see a “Verify Your E-mail Address” page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user’s email should be verified and ready to go.
-   To create an **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with py.test

    $ py.test

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation].

### Sentry

Sentry is an error logging aggregator service. You can sign up for a free account at <https://sentry.io/signup/?code=cookiecutter> or download and host it yourself. The system is setup with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.

Deployment
----------

The following details how to deploy this application.

  [Built with Cookiecutter Django]: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
  [![Built with Cookiecutter Django]]: https://github.com/pydanny/cookiecutter-django/
  [settings]: http://cookiecutter-django.readthedocs.io/en/latest/settings.html
  [Live reloading and SASS compilation]: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html
