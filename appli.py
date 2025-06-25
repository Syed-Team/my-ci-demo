from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Assalamu alaikum bhaiya! Khairiyat, I successfully deploy by render.com site which is free to create instances. Alhamdulillah!!!"

if __name__ == "__main__":
    app.run()
