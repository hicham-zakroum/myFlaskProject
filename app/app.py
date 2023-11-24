from flask import Flask, render_template, request
import json
import xmltodict

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
@app.route('/jsontoxml', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            json_str = request.form.get("json")
            python_dict = json.loads(json_str)
            xml_string = xmltodict.unparse(python_dict)
            return render_template("index.html", json=json_str, xml=xml_string, jsonxml=True)
        except:
            return "you have to enter a valid data ,Back to hame dir <a href='/'>HOME</a>"


    return render_template("index.html",jsonxml=True)


@app.route('/xmltojson', methods=["GET", "POST"])
def xmltojson():
    if request.method == "POST":
        try:
            xml_str = request.form.get("xml")
            json_string = json.dumps(xmltodict.parse(xml_str))
            return render_template("xmltojson.html", json=json_string, xml=xml_str, jsonxml=False)
        except:
            return "you have to enter a valid data ,Back to hame dir <a href='/'>HOME</a>"

    return render_template("xmltojson.html",jsonxml=False)


# @app.route("/api/toxml", methods=["POST"])
# def toxml():
#     if request.method == "POST":
#         json_str = request.form.get("json")
#         python_dict = json.loads(json_str)
#         xml_string = xmltodict.unparse(python_dict)
#         return render_template("index.html", response=xml_string)
#     return ""

# Our main function which runs the Flask App
if __name__ == '__main__':
    app.run(debug=True)
