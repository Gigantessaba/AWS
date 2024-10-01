from flask import Flask 
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Would!"

@app.route("/second")
def second():
    return "This is the second page!"

@app.route("/whichpage/<string:page_id>")
def whiichpage(page_id):
    if page_id.isdigit():
        message = f"The Id of this page is {page_id}!"
    else:
        message = f"{page_id} is not a number!"
    return message


if __name__ == '__main__':

    app.run(debug=True, port=80)
    # app.run(host= '0.0.0.0', port=8081)