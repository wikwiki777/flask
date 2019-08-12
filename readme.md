# Flask framework uage

## Advanced routing and forms

### Advanced routing

Allows us to create more specific routes.
By passing part of a route to a function as an argument

1.Create a new key and value in the json file i.e.

```json
{
    "name": "Gandalf",
    "description": "Originally called Olórin, he was accounted as the wisest of the Maiar. He was a Maia of Manwë and Varda. He also served under two other Valar, such as Irmo and Nienna. When the Valar decided to send the order of the Istari (also known as Wizards) to Middle-earth, to counsel and assist all those in Middle-earth who opposed the Dark Lord Sauron, Manwë and Varda decided to include Olórin among the five who were sent.",
    "image_source": "https://vignette.wikia.nocookie.net/lotr/images/8/8d/Gandalf-2.jpg/revision/latest?cb=20130209172436",
    "url": "gandalf"
}
```

2.Reference the key in the template:

```jinja
<h3><a href="/about/{{ member.url }}">{{ loop.index }}. {{ member.name }}</a></h3>
```

3.When u now click on the link u created you will get a error.
But when we have a look at the address bar, you can see that where we were tried to go to was about/Thorin(<http://127.0.0.1:5000/about/thorin).>
So it was picking up the URL that we created in our company.json file.

```htmlView
Not Found
The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.
```

To get this working then, we need to use some of the advanced routing features in Flask, which means we have to go back to our run.py file and create a new route and view.
We can't just modify our existing /about route here.
So I'm going to create a new route decorator: @app.route.("/about/<member_name>")
And then I'm going to create a new view, which is going to be: about_member
And that's going to take member_name as an argument.
So whenever we look at our about URL with something after it, that's going to be passed in to this view.

```python
@app.route('/about/<member_name>')
def about_member(member_name):
    member = {}

    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj

    return render_template("member.html", member=member)
```

And create a new member.html template:
```html
{% extends 'base.html' %} {% block content %}

<div class="row">
    <div class="col-md-5">
        <img src="{{ member.image_source }}" alt="Profile image for {{member.name}}" />
        <h2 class="col-md-7">{{ member.name }}</h2>
    </div>
</div>

<div class="col-md-12">
    <p>{{ member.description }}</p>
</div>

{% endblock %}
```

### Creating a Form in A Template

Allows us to submit data to the server

1.Create a form on the contact.html page

2.Wire it up to the backend by changing the following in the html:

- Use HTTP method POST ( GET is used to retrieve data, POST is used to send data to the server. )

```html
<form method="POST" name="sentMessage" id="contactForm" novalidate>
</form>
```

- Give all the input elements name's. The reason we're doing this is that this is how Python will refer to the different fields in our form. i.e.:

```html
                    <input type="email" class="form-control" placeholder="Email Address" name="email" id="email" required data-validation-required-message="Please enter your email address.">

```

3. You wil get a method not allowed error (405) from the server.
The reason is that by default, all of Flask's views will handle a GET request, but when we need to start handling anything outside of that, such as a POST, or the other methods DELETE or PUT, then we need to explicitly state that our route can accept that.
So we'll go down to our contact route here, and we're going to put in another argument.

```python
@app.route('/contact', methods=["GET", "POST"])
```

4.The first thing we need to do is import the request library from Flask.
And request is going to handle things like finding out what method we used, and also it will contain our form object when we've posted it.

```python
from flask import Flask, render_template, request

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        print(request.form)
    return render_template("contact.html", page_title="Contact")

```

The request object has a lot more things attached to it as well.
When we submit a form, it actually has the form object attached.
So remember that we gave each of our fields names.
Let's see what happens if we print out request.form.

```python
@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        print(request.form)
        print("hellow is anybody there")
    return render_template("contact.html", page_title="Contact")

```

Now because this is a dictionary, we can actually use a standard Python method of accessing the keys for that dictionary.
So if I do print(request.form["name"], let's see what happens.

```python
@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        print(request.form["name"])
        print("hellow is anybody there")
    return render_template("contact.html", page_title="Contact")

```

### Providing feedback to the user

Here we are going to use the flash functiont to allow us to provide users with feedback

1. Import the flash function.
Often, we want to display a non-permanent message to the user, something that only stays until we refresh the page or go to a different one.
These are called flashed messages in Flask.
And we want to display a flashed message when our visitor submits the contact form.

```python
from flask import Flask, render_template, request, flash

```

2.To use flashed messages, we need to create a secret key because Flask cryptographically signs all of the messages for security.
This might sound complicated, but really all we need to do is provide a secret key that Flask can use to sign the messages.
Generally, in production, we'd keep the secret key private.

```python
app.secret_key = "some_secret_key"
```

3.Use the flash function

```python
@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(request.form["name"]))
    return render_template("contact.html", page_title="Contact")

```

4.Update the template to receive the flashed messages i.e. contact.html

```jinja
{% with messages = get_flashed_messages() %} 
{% if messages %}
<ul class="flashes">
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
</ul>
{% endif %} 
{% endwith %}
```
