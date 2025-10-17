import requests
from bs4 import BeautifulSoup
import time
import csv

def fetch_part_time_n8n_jobs(page=1):
    url = "https://www.onlinejobs.ph/jobseekers/jobsearch"
    params = {
        "jobkeyword": "n8n",
        "skill_tags": "",
        "gig": "on",
        "partTime": "on",
        "fullTime": "off",   # ensure full time off
        "isFromJobsearchForm": "1",
        "page": page        # if pagination is supported
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; MyScraper/1.0)"
    }
    resp = requests.get(url, params=params, headers=headers)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    jobs = []
    # Find job listings
    for job_div in soup.find_all("div", class_="job-info"):  # class name is example
        # adapt the selectors to actual HTML
        title = job_div.find("a", class_="job-title").text.strip() if job_div.find("a", class_="job-title") else None
        company = job_div.find("div", class_="company").text.strip() if job_div.find("div", class_="company") else None
        pay = job_div.find("div", class_="pay").text.strip() if job_div.find("div", class_="pay") else None
        date_posted = job_div.find("div", class_="posted").text.strip() if job_div.find("div", class_="posted") else None
        # Confirm it’s part time
        job_type = job_div.find("div", class_="job-type").text.strip() if job_div.find("div", class_="job-type") else ""
        if "Part Time" in job_type:
            jobs.append({
                "title": title,
                "company": company,
                "pay": pay,
                "date_posted": date_posted,
                "type": job_type
            })
    return jobs

def scrape_all():
    all_jobs = []
    page = 1
    while True:
        jobs = fetch_part_time_n8n_jobs(page=page)
        if not jobs:
            break
        all_jobs.extend(jobs)
        print(f"Page {page}: found {len(jobs)} jobs")
        page += 1
        time.sleep(2)  # be nice
    # Save to CSV
    keys = ["title", "company", "pay", "date_posted", "type"]
    with open("part_time_n8n_jobs.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(all_jobs)
    print(f"Total jobs found: {len(all_jobs)}")

if __name__ == "__main__":
    scrape_all()
