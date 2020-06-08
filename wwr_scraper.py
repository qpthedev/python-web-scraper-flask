import requests
from bs4 import BeautifulSoup


def extract_job(html):
    title = html.find("span", {"class":"title"}).get_text(strip=True)
    company = html.find("span", {"class":"company"}).get_text(strip=True)
    job_id = html.find("a", recursive=False)["href"]

    # print (title, company, job_id)
    # print('done')
    return  {"title" : title, "company" : company, "apply_link" : f"https://weworkremotely.com{job_id}"}

        


def extract_jobs(url):
    jobs = []

    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find("section", {"id":{"category-2"}}).find_all("li", {"class":"feature"})
    
    for result in results:
        job = extract_job(result)
        jobs.append(job)
    
    return jobs

    # print(results)



def get_wwr_jobs(word):
    url = f"https://weworkremotely.com/remote-jobs/search?term={word}"
    jobs = extract_jobs(url)

    return jobs