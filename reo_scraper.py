import requests
from bs4 import BeautifulSoup

def extract_job(html):
  title = html.find("h2").get_text(strip=True)
  company = html.find("h3").get_text(strip=True)
  job_id = html.find("a")["href"]
  
  return {"title":title, "company":company, "apply_link":f"https://remoteok.io{job_id}"}


def extract_jobs(url):
  jobs = []

  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find("table",{"id":"jobsboard"}).find_all("tr",{"class":"job"})

  for result in results:
      job = extract_job(result)
      jobs.append(job)

  return jobs

def get_reo_jobs(word):
  url = f"https://remoteok.io/remote-dev+{word}-jobs"
  jobs = extract_jobs(url)

  return jobs
