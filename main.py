"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

from flask import Flask, render_template, request, redirect, send_file
from all_scraper import get_jobs
from generate_csv import save_to_file

app = Flask("JobScraper")

db = {}


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    term = request.args.get("term")

    if term:
        term = term.lower()
        jobsInDB = db.get(term)

        if jobsInDB:
            jobs = jobsInDB
        else:
            jobs = get_jobs(term)
            db[term] = jobs
    else:
        return redirect("/")

    return render_template(
        "search.html", searchTerm=term, searchNum=len(jobs), jobs=jobs)

@app.route("/export")
def export():
    try:
        term = request.args.get("term")
        
        if not term:
            raise Exception()

        term = term.lower()
        jobs = db.get(term)

        if not jobs:
            raise Exception()

        save_to_file(jobs, term)
        
        return send_file(f"{term}.csv", mimetype="text/csv",as_attachment=True, attachment_filename=f"{term}.csv")


    except:
        return redirect("/")



app.run()