# Flask framework uage

## Adding Data

### Passing Data from a View To A Template

Passing data from server to client as expression:

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

### Using For Loops Inside HTML

1.Create a list in the run.py file i.e.:

```python
@app.route("/about")
def about():
    # passing data as expressions from server to client can be any name
    return render_template("about.html", page_title="About", list_of_numbers=[1, 2, 3])

```

2.Pass the variable list_of_numbers by using the
double curly bracket notation and then put the expression in there:

In the about.html i.e.
```jinja
{{ list_of_numbers }}

```

3.Using For Loop in the HTML to iterate over that list,
were using the {% %} notation because this is for statements ( logic control ):

In the about.html i.e. add the following for loop:

```jinja
{% extends "base.html" %}
{% block content %}

    {% for number in list_of_numbers %}
        <p>{{ number }}</p>
    {% endfor %}

    <h2>{{ page_title }}</h2>
{% endblock %}
```

### Reading from a JSON file

1.Create a valid JSON file i.e. company.json

2.In the run.py file import the JSON library to parse the data.

```python
import os
import json
from flask import Flask, render_template


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    # passing data as expressions from server to client can be any name
    return render_template("about.html", page_title="About", company=data)
```

And have look at the data in the template about.html:

```jinja
<!-- show all data -->
{{ company }}

<!-- show first object -->
{{ company[0] }}

<!-- show name field of first object -->
{{ company[0]["name"] }}
```

### Iterating over the JSON Data

Use a for loop to iterate over the company data:

```jinja
    <h2>{{ page_title }}</h2>
    <p>The formation of the group grew out of a meeting Gandalf had with Thorin in Bree which kindled Thorin's interest in recapturing his long lost family inheritance. Remembering that he had once known an adventurous Hobbit on his travels in The Shire, Gandalf
        decided to add Bilbo to their company because he knew that stealth and cunning were preferable to force. Gandalf also believed that someone like Bilbo could keep the sometimes prideful and stubborn Dwarves from rash action. The superstitious Dwarves
        also considered thirteen to be an unlucky number, and as Gandalf had planned to leave on other business, welcomed a fourteenth to fill in to their party.</p>

    {% for member in company %}
    <div class="row featurette">
        <div class="col-md-7">
            <h3>{{ member.name }}</h3>
            <p>{{ member.description }}</p>
        </div>
        <div class="col-md-5">
            <img class="featurette-image img-responsive" src="{{ member.image_source }}" alt="Picture of {{ member.name }}">
        </div>
    </div>
    <hr class="featurette-divider">
    {% endfor %}
```

### Using If Statements Inside Our HTML

When we create a for loop using the Jinja templating language,it also creates an object for us called loop.
And that object loop has a property which is .index.

And that shows us exactly which iteration of the loop we're on.

```jinja
{{ loop.index }}
```

- Using the if statement in the template

```jinja
    {% for member in company %}

    <div class="row featurette">

        {% if loop.index %2 != 0 %}

        <div class="col-md-7">
            <h3>{{ loop.index }} {{ member.name }}</h3>
            <p>{{ member.description }}</p>
        </div>
        <div class="col-md-5">
            <img class="featurette-image img-responsive" src="{{ member.image_source }}" alt="Picture of {{ member.name }}">
        </div>
        {% else %}
        <div class="col-md-5">
            <img class="featurette-image img-responsive" src="{{ member.image_source }}" alt="Picture of {{ member.name }}">
        </div>
        <div class="col-md-7">
            <h3>{{ loop.index }} {{ member.name }}</h3>
            <p>{{ member.description }}</p>
        </div>

        {% endif %}

    </div>

    {% if loop.index != 13 %}

    <hr class="featurette-divider">

    {% endif %}

    {% endfor %}
```