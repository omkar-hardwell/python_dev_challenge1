python dev challenge #1
=====================================

## Getting Started

### Installation

The installation is very straightforward, but make sure you are using at least
python 3.6.x

Make sure pip installed with python package. Create virtual environment using following commands.
```bash
$ cd python_dev_challenge1
$ pip install virtualenv
$ virtualenv env
```

On Linux/Mac
```bash
$ source env/bin/activate
```
or

On Windows
```bash

$ env\Scripts\activate
```

To install dependencies.
```bash
(env) $ pip install -r requirements.txt
```

### Running

When all dependencies have been installed, you can run the flask application
on your local instance by running:

```bash
(env) $ python src/app.py
```

You will have to access this application just entering following url on browser.
URL: http://127.0.0.1:5000/

Use .msg file to upload from https://github.com/omkar-hardwell/python_dev_challenge1/tree/master/src/uploads

### Testing

To run the tests, all you have to do is to run:

```bash
(env) $ py.test tests/ --cov src --cov-report term-missing
(env) $ flake8 src/ tests/
```

Note: Test cases are pending for this application.

### Updating

To install new dependencies.

```bash
(env) $ pip install -r requirements.txt
```
