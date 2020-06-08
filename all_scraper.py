from reo_scraper import get_reo_jobs
from so_scraper import get_so_jobs
from wwr_scraper import get_wwr_jobs


def get_jobs(word):
    jobs = []

    reo_jobs = get_reo_jobs(word)
    so_jobs = get_so_jobs(word)
    wwr_jobs = get_wwr_jobs(word)

    for job in so_jobs:
        jobs.append(job)
    for job in reo_jobs:
        jobs.append(job)
    for job in wwr_jobs:
        jobs.append(job)

    return jobs