# Flask framework uage

## Redering HTML Code

Use the render_template to use html files

1.Import render_template function from flask

```python3
from flask import Flask, render_template
```

2.When using render_template Flask expects to be a directory called templates:

<pre>dirtree
flask
|   run.py
|
|___templates
    |   <b>index.html</b>
    |   about.html

</pre>

3.Reference i.e. the index.html file in the function:

<pre>python3
@app.route("/")
def index():
    return render_template("<b>index.html</b>")

</pre>
