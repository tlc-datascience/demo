from flask import Flask

app = Flask(__name__)

# import declared routes
from students import student_1, student_2, student_3

@app.route("/")
def main():
    return "This is my demo code"
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)