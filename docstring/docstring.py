from flask import Flask, url_for, request, abort, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/<name>')
def lookup(name):
    if name in d:
        typ, doc = d[name]
        return render_template('entry.html', name=name, typ=typ, doc=doc)
    else:
        abort(404)

def split(line):
    name, doc = line.split(sep="\n", maxsplit=1)
    if name.startswith("F"):
        typ = "function"
    else:
        typ = "variable"
    name = name[1:]
    return (name, (typ, doc))

with open('DOC') as f:
    x = f.read()
    l = x.split(sep="\u001F")
    d = dict([split(i) for i in l if i])
