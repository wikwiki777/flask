# Flask framework uage

## Template Inheritance

### Routing

1. Create a new file i.e. base.html which will be the base for inheritance, in the template directory.

2. In the base.thml define a block, or an area, that we can inject content into:

    - Double curly brackets {} contain an expression, which is outputting something either to teh screen, or, in this case, into our href.

    - The curly bracket and percentage {% %} are for statements that control the flow or our template.

```html
<!-- base.html the template file -->
<body>
    <nav>
        <ul>
            <li><a href="{{ url_for('index') }}">Home</a></li>
            <li><a href="{{ url_for('about') }}">About</a></li>
            <li><a href="{{ url_for('contact') }}">Contact</a></li>
        </ul>
    </nav>

    {% block content %}
    {% endblock %}

</body>
```

3. Go to your index.html and delete everthing
and put in the following code:

```extendJinja
{% extends "base.html" %}
{% block content %}
    <h1>Home Page</h1>
{% endblock %}

```

- So what's happening here is that when our index.html file loads, Flask inherits everything from base.html.
It then looks for a block which we called content and injects this content into it
