import requests
from bs4 import BeautifulSoup
import csv
import json
from concurrent.futures import ThreadPoolExecutor
from lxml import html


# # Base URL of the webpage below code for magic bricks
# base_url = "https://www.magicbricks.com/mbutility/builders-in-Hyderabad?page="
#
# # Open the CSV file in write mode and set up the writer
# with open("developers_final.csv", "w", newline="", encoding="utf-8") as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["Developer Name", "URL"])
#
#     # Loop through 28 pages
#     for page_num in range(1, 29):
#         # Construct the URL for the current page
#         url = f"{base_url}{page_num}"
#
#         # Send HTTP GET request
#         response = requests.get(url)
#
#         # Parse HTML content
#         soup = BeautifulSoup(response.text, "html.parser")
#
#         # Extract developer names using CSS selector
#         developer_names = soup.select("h3.builder__name")
#         developer_names = [name.get_text(strip=True) for name in developer_names]
#
#         # Extract onclick attribute values using CSS selector
#         onclick_buttons = soup.select("button.card__CTA-see-builder")
#         onclick_values = [button['onclick'] for button in onclick_buttons]
#
#         # Extracting URL from onclick attribute value
#         urls = [onclick.split("'")[1] for onclick in onclick_values]
#
#         # Write each developer name and its respective URL to the CSV file
#         for name, url in zip(developer_names, urls):
#             writer.writerow([name, url])
#             print(f"Written to CSV: {name}, {url}")
#
# print("Data has been written to developers.csv")


# # Base URL pattern below code to get all housing .com projects-----------------------------------
# base_url = "https://housing.com/in/buy/projects-hyderabad/all-{}"
#
# # Open the CSV file in append mode
# with open("housing_all_projects.csv", "a", newline="", encoding="utf-8") as csvfile:
#     writer = csv.writer(csvfile)
#
#     # Loop through letters from 'a' to 'z'
#     for letter in range(ord('a'), ord('z')+1):
#         # Construct the URL for the current letter
#         url = base_url.format(chr(letter))
#
#         # Send HTTP GET request
#         response = requests.get(url)
#
#         # Parse HTML content
#         tree = html.fromstring(response.content)
#
#         # Extract text and href attributes using XPath
#         elements = tree.xpath("//a[@class='css-4huaz2']")
#
#         # Write each element's text and href to the CSV file
#         for element in elements:
#             text = element.text_content().strip()
#             href = element.get("href")
#             writer.writerow([text, href])
#             print(f"Appended to CSV: {text}, {href}")
#
# print("Data has been appended to projects.csv")

# #----------------------------------------------------------------------------------------------------------
# def extract_data_from_url(url):
#     print(url)
#     # Send HTTP GET request
#     global soup
#     response = requests.get(url)
#
#     # Parse HTML content
#     tree = html.fromstring(response.content)
#
#     # Extract text using XPath
#     div_class_texts = tree.xpath("//div[@class='_h3yh40 T_46c25558']/text()")
#
#     # Count the number of elements for div class '_h3yh40 T_46c25558'
#     number_of_elements = len(div_class_texts)
#
#     # Initialize columns
#     project_area = ""
#     floor_size = ""
#     avg_price = ""
#     project_size = ""
#     dates = []
#     configurations_list = []
#
#     # Loop through elements and categorize text into columns
#     for text in div_class_texts:
#         if "acres" in text.lower():
#             project_area = text
#         elif "sq.ft. -" in text.lower() or "sq.yd. -" in text.lower():
#             floor_size = text
#         elif "k/sq.yd" in text.lower() or "k/sq.ft" in text.lower():
#             avg_price = text
#         elif "units" in text.lower():
#             project_size = text
#         elif any(month in text.lower() for month in
#                  ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]):
#             dates.append(text)
#         elif "bhk" in text.lower() or "villa" in text.lower() or "apartment" in text.lower() or "plot" in text.lower():
#             configurations_list.append(text)
#
#     # Combine dates into a single cell if there are two dates
#     if len(dates) == 2:
#         dates_cell = ", ".join(dates)
#     else:
#         dates_cell = dates[0] if dates else ""
#
#     # Combine configurations into a single cell
#     configurations_cell = ", ".join(configurations_list)
#
#     # Extract latitude and longitude from JSON response in <script> tag
#     json_scripts = tree.xpath("//script[@type='application/ld+json']/text()")
#     latitude = None
#     longitude = None
#
#     for script in json_scripts:
#         json_data = json.loads(script)
#         if isinstance(json_data, list):
#             for data in json_data:
#                 if "geo" in data and "latitude" in data["geo"] and "longitude" in data["geo"]:
#                     latitude = data["geo"]["latitude"]
#                     longitude = data["geo"]["longitude"]
#                     break
#         if latitude is not None and longitude is not None:
#             break
#     # Extract the number of floors from the JSON data
#     floors_answerr = None
#     # Check if request was successful (status code 200)
#     if response.status_code == 200:
#         # Parse HTML response
#         soup = BeautifulSoup(response.text, 'html.parser')
#
#         # Find the div with data-q='faq' attribute
#         faq_div = soup.find('div', {'data-q': 'faq'})
#
#         if faq_div:
#             # Find the script tag containing the data within the faq_div
#             script_tag = faq_div.find('script', {'type': 'application/ld+json'})
#
#             if script_tag:
#                 # Extract the content of the script tag
#                 script_content = script_tag.string
#
#                 # Load the JSON data
#                 data = json.loads(script_content)
#
#                 # Find the question about the number of floors
#                 for item in data['mainEntity']:
#                     if item.get('name', '').lower().startswith('how many floors') and 'acceptedAnswer' in item:
#                         floors_answerr = item['acceptedAnswer']['text']
#                         print(floors_answerr)
#                         break  # Stop looping once the answer is found
#             else:
#                 print("Script tag containing JSON data not found.")
#         # Extract amenities
#     amenities = []
#     amenities_elements = soup.find_all('div',
#                                        class_="T_5990d116 _1q731trj _6w1e54 _9scj1k _fycs5v _ks15vq _c81fwx _h3ftgi label")
#     for element in amenities_elements:
#         amenities.append(element.text.strip())
#
#     # Extract developer name and URL
#     dev_name = ""
#     dev_url = ""
#     dev_span = tree.xpath("//span[@data-q='dev-name']")
#     if dev_span:
#         dev_name = dev_span[0].xpath("string()").strip()
#         dev_link = tree.xpath("//span[@data-q='dev-name']/parent::a")
#         if dev_link:
#             dev_url = dev_link[0].get('href')
#
#     # Extract address
#     address = None  # Default value is None
#     address_div = tree.xpath("//div[@data-q='address']")
#     if address_div and address_div[0].text:
#         address = address_div[0].text.strip()
#     print("price: ",avg_price)
#     return [url, dev_name, dev_url, address, number_of_elements, project_area, floor_size, project_size, avg_price,
#             dates_cell, configurations_cell, latitude,
#             longitude, floors_answerr, amenities]


# List of URLs to iterate through
# urls = [
#         #e URLs here...
#         ]
#
# # Define the number of threads
# num_threads = 10
#
# # Create a ThreadPoolExecutor
# with ThreadPoolExecutor(max_workers=num_threads) as executor:
#     # Write data to CSV file
#     with open("project_details_url_list_100.csv", "w", newline="", encoding="utf-8") as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(
#             ["URL", "dev_name", "dev_url", "address", "Number of Elements", "Project Area", "Floor Size",
#              "Project Size", "avg_price", "Dates", "Configuration",
#              "Latitude", "Longitude", "Floors", "Amenities"])
#
#         # Submit tasks to the executor and map them to the URLs
#         results = executor.map(extract_data_from_url, ["https://housing.com" + url for url in urls])
#
#         # Iterate through the results and write them to the CSV file
#         for result in results:
#             writer.writerow(result)
#
# print("Data has been written to project_details_url_list.csv")

#--------------------------------------------------------------------------

#
# # URL of the endpoint
# url = 'https://housing.com/in/buy/projects/page/235465-ambience-courtyard-by-koncept-ambience-in-manikonda'
#
# # Send GET request
# response = requests.get(url)
#
# # Check if request was successful (status code 200)
# if response.status_code == 200:
#     # Parse HTML response
#     soup = BeautifulSoup(response.text, 'html.parser')
#
#     # Find the div with data-q='faq' attribute
#     faq_div = soup.find('div', {'data-q': 'faq'})
#
#     if faq_div:
#         # Find the script tag containing the data within the faq_div
#         script_tag = faq_div.find('script', {'type': 'application/ld+json'})
#
#         if script_tag:
#             # Extract the content of the script tag
#             script_content = script_tag.string
#
#             # Load the JSON data
#             data = json.loads(script_content)
#
#             # Find the question about the number of floors
#             for item in data['mainEntity']:
#                 if item.get('name', '').lower().startswith('how many floors') and 'acceptedAnswer' in item:
#                     floors_answer = item['acceptedAnswer']['text']
#                     print(floors_answer)
#                     break  # Stop looping once the answer is found
#         else:
#             print("Script tag containing JSON data not found.")
#     else:
#         print("Div with data-q='faq' attribute not found.")
# else:
#     print('Failed to fetch data from the server.')
#=-------------------------------------------------------------------

def extract_rera_id(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        rera_id_element = soup.find('div', string='Rera Id')
        if rera_id_element:
            rera_id_link = rera_id_element.find_next('a')
            if rera_id_link:


                if len(rera_id_link.text.strip())==12:
                    return rera_id_link.text.strip()
    return None

def process_url(url):
    rera_id = extract_rera_id(url)
    if rera_id:
        with open('output1.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([url, rera_id])
        print(f"RERA ID extracted from {url}")
    else:
        print(f"RERA ID not found in {url}")


num_threads = 10

with ThreadPoolExecutor(max_workers=num_threads) as executor:
    executor.map(process_url, urlss)

print("All URLs processed.")






urlss = ['',
 ]