# Flask framework uage

## Routing and basic Jinja Templating

### Routing

1.Use the decorator and specify the endpoint. It then returns the template from our index() function.
The root decorator binds the index() function to itself so that whenever that root is called, the function is called.
And this function is also called a view:

<pre><python3>
@app.route("/")
def index():
    return render_template("index.html")
</python3>
</pre>

2.Reference the endpoints in the html file, this should be the same as in the route decorator i.e.:

```html
<li><a href="/">Home</a></li>
<li><a href="/about">About</a></li>
```

### Using template logic - Basic Jinja templating language

1. So rather than typing the path in the html files we can use the Jinja templating language in the html file by using the {{  function() }}:

```htmlJinja
<!-- what we're doing is calling this url_for() function that looks up the view called index or the view called about(), and then injects some text, which is the actual route  -->

<li><a href="{{ url_for('index') }}">Home</a></li>
<li><a href="{{ url_for('about') }}">About</a></li>
<li><a href="{{ url_for('contact') }}">Contact</a></li>

```
