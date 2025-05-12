# From the Web to the Field - Automated Sports Data Scraper

## Project Description

This project automates the extraction of football match data from online sources using Python. It leverages the `requests` and `BeautifulSoup` libraries for efficient web scraping and utilizes PostgreSQL for structured data storage. The modular architecture ensures maintainability and scalability, making it ideal for sports data analysis.

## Features

* Real-time football match data scraping from online sources
* Modular pipeline for scraping, database interaction, and application logic
* Robust data storage using PostgreSQL for efficient querying and analysis

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/JamilAhmed00/Web_Scrap_Field_World_Final_Project.git
   ```
2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```
3. Set up the PostgreSQL database:

   * Configure the database connection in `database.py`

## Usage

1. Run the scraper:

   ```bash
   python scraper.py
   ```
2. Access the stored data:

   ```bash
   python main.py
   ```

## Technologies Used

* Python
* BeautifulSoup
* Requests
* PostgreSQL

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
