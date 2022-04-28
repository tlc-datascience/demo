from flask import Flask
from modules.fetchCSV import downloadCSV as getCSV

app = Flask(__name__)

from students import student_1, student_2

dict = {}
dict.update(student_1.functions())
dict.update(student_2.functions())

for k in dict.keys():
    app.add_url_rule(k, view_func=dict[k])

@app.route("/")
def main():
    return "This is my demo code!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80, use_reloader=True)