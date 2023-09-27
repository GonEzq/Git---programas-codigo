import requests
from bs4 import BeautifulSoup

# URL of the Wikipedia page with the table you want to scrape
wiki_url = "https://es.wikipedia.org/wiki/Anexo:Medallas_ol%C3%ADmpicas"

# Send an HTTP GET request to fetch the webpage content
response = requests.get(wiki_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'lxml')
    
    # Find the table you want to scrape based on its class or other attributes
    table = soup.find('table', {'class': 'wikitable'})
    
    # Check if the table was found
    if table:
        # Initialize an empty list to store the table data
        table_data = []

        # Loop through the rows of the table
        for row in table.find_all('tr'):
            # Extract data from each cell in the row
            row_data = [cell.get_text(strip=True) for cell in row.find_all('td')]
            
            # Append the row data to the table_data list
            table_data.append(row_data)

        # Remove the header row if necessary (optional)
        if len(table_data) > 1:
            del table_data[0]

        # Print the table data
        for row in table_data:
            print(row)
    else:
        print("Table not found on the page.")
else:
    print("Failed to retrieve the Wikipedia page.")

