from flask import Flask, request, send_file, render_template
# from stream import translate
# from util import getFragmentDir
import os
import time
app = Flask(__name__, template_folder="www", static_folder="www/assets" )
# static_folder="./www/assets", template_folder="public"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create.html')
def create():
    return render_template("create.html")

@app.route('/dashboard.html')
def dashboard():
    return render_template("dashboard.html")


@app.route('/login.html')
def login():
    return render_template("login.html")

    
@app.route('/practice')
def practice():
    return render_template("practice.html")

    
@app.route('/register.html')
def register():
    return render_template("register.html")

# @app.route('/download')
# def download():
#   video_id = request.args.get('id', '')
#   lang = request.args.get('lang', '')
#   url = "https://www.youtube.com/watch?v=" + video_id
#   translate(url, lang)
#   file = os.path.join(getFragmentDir(url, lang), "bg.complete.mp4")
#   while not os.path.exists(file):
#     time.sleep(0.01)
#   return send_file(file, conditional=True, attachment_filename=(video_id + ".mp4"))
  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)