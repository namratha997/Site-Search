# Site Data Search Application

This project is a web application built using Flask, which allows users to search for site data using a Site ID. It retrieves site data from the Wireless Guardian API and displays important dates related to the site.

## Table of Contents
- [Features](#features)
- [Tech Stack Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Tech Stack Used](#technologies-used)
- [Contributing](#contributing)


## Features
- Search site data by Site ID
- Display site information including validation date, go-live date, closeout package date, and cancellation date
- User-friendly interface with responsive design

## Tech Stack Used
- Python 3.x
- pip (Python package installer)
- Flask
- Pandas
  
## PreReqs:
1. **API Key:**
Make sure to replace the placeholder API key in app.py with your actual API key.

2. **API Endpoints:**
Make sure to replace the API endpoints with whatever endpoints you are working with. Replace the endpoints in Modules->WgDataApi.py

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/sitedata-search.git
   cd sitedata-search

## Usage
1. **Add your API key:**
   Replace the placeholder API key in `app.py` with your actual API key.

2. **Run the application:**
   ```bash
   python app.py
   
3. **Access the application:**
Open your web browser and navigate to http://127.0.0.1:5000.

4. **Search for site data:** Enter a Site ID in the input field. Click the "Search" button to retrieve and display the site data.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.




