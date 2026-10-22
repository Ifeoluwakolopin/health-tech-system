# MEDICIA
- An efficient patient management system for healthcare facilities

## Contributing
- Use Python 3.12–3.14, as required by the pinned Django 6.0 release.
- Clone the repository
- Enter main project directory ```cd medicia```
- Create an isolated environment with a supported Python, for example
  ```python3.14 -m venv .venv```, then activate it with
  ```source .venv/bin/activate```.
- Update the installer with ```python -m pip install --upgrade pip==26.2.2```
  and install required packages using ```pip install -r requirements.txt ```.
- Use development environment settings by using ```export DJANGO_SETTINGS_MODULE=medicia.settings.dev```
- run development build using ```python manage.py runserver```
- Work on the "develop" branch
- Make a PR before merging to main.
- Happy building!

## Dependency validation

The requirements pin Django 6.0.8 and sqlparse 0.6.0 for the security fixes
available as of October 21, 2026. After installation, run:

```bash
python -m pip check
DJANGO_SETTINGS_MODULE=medicia.settings.dev python manage.py check
python -m compileall -q medicia records manage.py
```

Run these commands from `medicia/`. The framework check does not migrate the
database or certify production configuration; `records/tests.py` currently
contains no test cases.