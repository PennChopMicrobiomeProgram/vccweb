# vccweb

UPenn Human Virome Project VCC website

## Install

```bash
pip install -e .
```

## Launch website

The website loads data from a CSV file and uses a shared password
across all users.

```bash
vccweb --datafile data/mysamples.csv --password 123
```

Or put it into production as a system daemon with gunicorn.  Make sure
to set the env vars `VCCWEB_DATA` and `VCCWEB_PASSWORD` before
launching.

```bash
gunicorn --workers 2 --bind unix:/run/vccweb.sock vccweb/wsgi:app
```
