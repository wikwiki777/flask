# Flask framework uage

## Simple flask app

```python3
import os
from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World"


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=5000, debug=True)

```

1.Install flask:

```bash
sudo pip3 install Flask
```

2.Create new python file that will run the application.
The Flask convention is to name it run.py or app.py:

```bash
touch run.py
```

3.Open the newly created file and
import the flask class:

```python3
from flask import Flask
```

4.Create instance of the imported flask class.
The Flask convention is to name the variable app:

```python3
app = Flask(__name__)
```

5.Use route decorator to tell Flask what URL should trigger the function that follows:

```python3
@app.route("/")
def index():
    return "Hello World"
```

6.Use the following to run the program directly if it is not imported:

```python3
if __name__ == "__main__":
app.run(host=os.environ.get("IP), port=5000, debug=True)
```
