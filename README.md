# Online Course Assessment

A Django implementation of an online course application with assessment questions, answer choices, learner submissions, grading, an admin interface, and a Bootstrap-styled course and results experience.

## Run locally

```powershell
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit `/admin/` to create courses, lessons, questions, and answer choices.
