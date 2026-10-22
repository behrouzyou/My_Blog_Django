# My Blog — Django

A Django blog application with article listing/detail pages, categories, comments, authentication, and article management views.

## Features visible in the code
- Article listing with pagination
- Published-article detail pages
- Authenticated comment submission
- Article create/update workflows with login and permission mixins
- Category support
- Authentication integrations through django-allauth, including configured social-account providers
- Django admin customization with django-jet

## Tech stack
- Python and Django
- Django templates
- django-allauth
- django-taggit
- django-jet

## Run locally
Requires Python and pip.

```bash
git clone https://github.com/behrouzyou/My_Blog_Django.git
cd My_Blog_Django
python -m venv .venv
```

Activate the environment and install the dependencies used by the project. Configure `SECRET_KEY` in your local environment or an untracked `.env` file before running:

```bash
python manage.py migrate
python manage.py runserver
```

## Configuration and security
Social login requires provider credentials and callback URLs to be configured in the local environment and Django admin. Do not commit `.env`, OAuth credentials, or production secrets. Use `.env.example` as a template.
