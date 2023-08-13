from utils import *
from flask import Flask

app = Flask(__name__)
class_ = Condidate('condidate.json')


@app.route("/")
def page_index():
    candidate = class_.load_from_file()
    str_ = '<pre>'
    for can_ in candidate.values():
        str_ += f"{can_['name']}\n{can_['position']}\n{can_['skills']}\n\n"
    str_ += '</pre>'
    return str_


@app.route('/candidate/<int:x>')
def show_c(x):
    img = '<img src='
    img_of = class_.work_w_x(x)[0]
    # str_ = '<pre>'
    str_ = f"<img src={img_of}></img><pre>{class_.work_w_x(x)[1]}\n{class_.work_w_x(x)[2]}\n{class_.work_w_x(x)[3]}\n\n</pre>"
    # str_ += '</pre>'
    img_end = img + str(img_of) + '></img>'

    return str_


@app.route('/skills/<skill>')
def slills(skill):
    str_ = '<pre>'
    for can_ in class_.load_from_file().values():
        if skill in can_['skills'].split(', '):
            str_ += f"{can_['name']}\n{can_['position']}\n{can_['skills']}\n\n"
    str_ += '</pre>'
    return str_


app.run(debug=True)
