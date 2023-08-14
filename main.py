from utils import *
from flask import Flask

app = Flask(__name__)
class_ = Condidate('condidate.json')

candidate = class_.load_from_file()
@app.route("/")
def page_index():
    """
    YOU GET THE MAIN PAGE
    """
    str_ = '<pre>'
    for can_ in candidate.values():
        str_ += f"{can_['name']}\n{can_['position']}\n{can_['skills']}\n\n"
    str_ += '</pre>'
    return str_


@app.route('/candidate/<int:x>')
def show_c(x):
    """
    YOU ENTER THE PARAMETR AND GET PERSON WITH THIS ID
    """
    img_of = class_.work_w_x(x)[0]
    str_ = f"<img src={img_of}></img><pre>{class_.work_w_x(x)[1]}\n{class_.work_w_x(x)[2]}\n{class_.work_w_x(x)[3]}\n\n</pre>"

    return str_


@app.route('/skills/<skill>')
def slills(skill):
    """
    YOU ENTER THE PARAMETR AND GET PERSON WITH THESE SKILLS
    """
    str_ = '<pre>'
    for can_ in candidate.values():
        candidate1 = can_['skills'].split(', ')
        candidate1 = [x.lower() for x in candidate1]
        if skill in candidate1:
            str_ += f"{can_['name']}\n{can_['position']}\n{can_['skills']}\n\n"
    str_ += '</pre>'
    return str_


app.run()
