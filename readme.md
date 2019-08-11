# Flask framework uage

## Applying Styles

### Using a Bootstrap  theme

1. Download a bootstrap theme from i.e. start bootstrap

2. Create a directory called static, and put your downloaded files in it.

```dirtree
flask
|   run.py
|
|___static
|   |___css
|       |   style.css
|
|___templates
    |   base.html
    |   index.html
    |   about.html

```

3. How to reference to a i.e. css file.
Go to your base.html and type the following code:

    - We're going to use url_for. But this time, url_for is going to take two arguments. The first argument is 'static' so that url_for knows to look in the static directory. The second argument is filename = 'css/clean-blog.min.css' And as we can see, the file name that I've typed here corresponds with the name of the file and the directory under static.

```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/clean-blog.min.css') }}">
```

4. Passing data from server to client as expression:

```python
# In the run.py
@app.route("/about")
def about():
    # passing data as expressions from server to client can be any name i.e. page_title = ""
    return render_template("about.html", page_title="About")
```

Then add to the corresponding view i.e. about.html

```html
{% extends "base.html" %}
{% block content %}
    <h2>{{ page_title }}</h2>
{% endblock %}
```
