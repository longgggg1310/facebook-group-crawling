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

* Navigate to the project directory:
   ```bash
   cd facebook-group-crawling
* Install the dependencies:
   ```bash
   pip install -r requirements.txt
* Create a new file named .env in the project directory and add the following content:
   ```bash
  [POSTGRES]
   DB_USER= your_database_host
   DB_PASSWORD= your_database_password
   DB_HOST= your_database_host
   DB_PORT= your_database_port
   DB_NAME= your_database_name

   [FACEBOOK]
   email = your_facebook_email
   password = your_facebook_password

Replace your_database_host, your_database_name, your_database_user, your_database_password, your_facebook_email, your_database_port , and your_facebook_password with your actual database and Facebook credentials.
 * Run the crawler:

    ```bash
   python crawler.py

**Note:** 
* You can set up the depth of crawling by searching for the command "*fb = facebook(depth=yourDepth)*" in dataToDb.py, and set the depth to your desire.
