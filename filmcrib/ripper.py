import requests
from bs4 import BeautifulSoup

# URL of the admin panel page
url = 'https://filmcrib.io/admin-cp/manage-videos'

# Login credentials
username = 'Benjamin'
password = 'Telltale10'

# Create a session to maintain the login state
session = requests.Session()

# Login to the admin panel
login_data = {
    'username': username,
    'password': password,
    # Include any other form fields required for login
}
login_response = session.post('https://filmcrib.io/admin-cp/login', data=login_data)

# Check if login was successful
if login_response.status_code == 200:
    print("Login successful")
else:
    print("Login failed")
    exit()

# Fetch the page with the video data after successful login
response = session.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Extract video data
video_data = []
videos_table = soup.find('table', {'class': 'table table-bordered'})
if videos_table:
    rows = videos_table.find_all('tr')
    for row in rows[1:]:  # Skip the header row
        cells = row.find_all('td')
        if len(cells) >= 3:  # Check if the row has enough cells
            title = cells[0].text.strip()
            description = cells[1].text.strip()
            # Extract other data as needed
            video_data.append({'title': title, 'description': description})
        else:
            print("Invalid row format")

# Display the extracted video data
for video in video_data:
    print(video)
