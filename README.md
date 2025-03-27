# NFSE Crawler (work in progress)

## 📌 Description
This project is designed to crawl the Brazil national invoice website. It runs automatically on a daily basis, retrieving information about invoices received or sent that day for my company.
The collected data is then sent to my email once a day.

## 📁 Project Structure
```
/nfse-crawler
│── .github/
│   └── workflows/
│       └── daily_routine.yml   # GitHub Actions workflow file for automation
│
│── scraper/                     # Main folder containing the scraping code
│   │── config.py                # Dynamo and SNS config
│   │── database.py              # Database management
│   │── insert_data.py           
│   │── main.py                  # Calls the scraper
│   │── nacional.py              # Scraper code
│
│── .gitignore                  
│── requirements.txt             # List of dependencies required for the project
```
