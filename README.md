# My Blog — Django

A Django blog application with article listing/detail pages, categories, comments, authentication, and article management views.

## Features visible in the code
- Article listing with pagination and published-article detail pages
- Authenticated comment submission
- Article create/update workflows with login and permission mixins
- Category support
- django-allauth authentication and social-account provider configuration
- Django admin customization with django-jet

## Stack
- Python, Django, Django templates
- django-allauth
- django-taggit
- django-jet

## Run locally
Create and activate a virtual environment, install project dependencies, and configure `SECRET_KEY` through your local environment or an untracked `.env` file. Then run:

```bash
python manage.py migrate
python manage.py runserver
```

Social login requires provider credentials and callback URLs. Never commit `.env`, OAuth credentials, or production secrets.
