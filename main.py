from flask import Flask, render_template, request, redirect, send_file
from scraper import get_jobs
from exporter import save_to_file

app = Flask("SuperScraper")

db = {}


@app.route("/")
def home():
    return render_template("potato.html")


@app.route("/report")
def report():
    # print(request.args.get("word"))
    word = request.args.get("word")
    # location_zip = request.args.get("location_zip")
    # radius_zip = request.args.get("radius_zip")
    if word:
        word = word.lower()
        fromDb = db.get(word)

        if fromDb:
            jobs = fromDb
        else:
            jobs = get_jobs(word)
            db[word] = jobs

    else:
        return redirect("/")
    return render_template("report.html",
                           searchingBy=word,
                           # searchingNear = location_zip,
                           # searchingAround = radius_zip,
                           resultNumber=len(jobs),
                           jobs=jobs
                           )


@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        
        save_to_file(jobs)

        return send_file("jobs.csv")

    except:
        return redirect("/")


app.run()
