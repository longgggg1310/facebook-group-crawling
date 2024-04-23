## Prerequisite
This project utilizes Selenium to crawl a real estate Facebook group. It automates the process of logging into Facebook, extracting cookies, and then using those cookies to crawl the group's content. The crawled data is then stored in a PostgreSQL database.

### Prerequisites
* Python 3.x (recommended 3.9.6)
* PostgreSQL
* Facebook account

## Setup
* Clone the repository:
   ```bash
   git clone https://github.com/your-username/real-estate-facebook-crawler.git

* python dataToDb.py

**Note:** 
* You can set up the depth of crawling by searching for the command "*fb = facebook(depth=yourDepth)*" in dataToDb.py, and set the depth to your desire.
