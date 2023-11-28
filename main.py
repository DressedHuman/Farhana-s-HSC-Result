import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Get the current script's directory
script_directory = os.path.dirname(os.path.realpath(__file__))

# Set the path to the Chromedriver executable in the same directory as the script
chromedriver_path = os.path.join(script_directory, 'chromedriver.exe')

# Set up Chrome options for headless mode
chrome_options = Options()
# chrome_options.add_argument('--headless')  # Run in headless mode
chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration

# Use the Service class to set the path to the Chromedriver executable
chrome_service = Service(chromedriver_path)

# Create a new instance of the Chrome driver with headless options
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# URL of the form page
form_url = 'http://result.dinajpurboard.gov.bd/hsc_result2023/search/each.php'

# Function to submit form data and retrieve results
found_flag = False
def submit_form(roll):
    driver.get(form_url)

    # Replace the following lines with the actual code to interact with the form
    # For example, find form elements by ID and submit data
    driver.find_element(by=By.NAME, value='roll_no').send_keys(roll)
    driver.find_element(by=By.NAME, value='regi_no').send_keys(1817703276)
    driver.find_element(by=By.NAME, value='submit').click()

    # Wait for the result page to load (adjust wait time as needed)
    # time.sleep(2)

    # Replace the following line with the actual code to retrieve and process results
    # result = driver.find_element(by=By.NAME, value='result_element').text
    # print(f"Form submitted with data: {data}, Result: {result}")
    if (found_flag := not "No Result Found" in driver.page_source):
        print(found_flag)
        driver.save_screenshot('Farhana - HSC 2023 - Result Check with Selenium on Python.png')
        time.sleep(570)
    print(found_flag)


# Generate 500 sets of sample data (replace with your actual data)
roll_list = [
    289889, 289890, 289891, 289892, 289893, 289894, 289896, 289897, 289898,
    289899, 289900, 289901, 289902, 289903, 289904, 289905, 289906, 289907,
    289908, 289909, 289910, 289911, 289912, 289913, 289914, 289915, 289916,
    289917, 289918, 289919, 289920, 289921, 289922, 289924, 289925, 289926,
    289927, 289928, 289929, 289930, 289931, 289932, 289933, 289934, 289935,
    289936, 289937, 289938, 289939, 289940, 289941, 289942, 289943, 289944,
    289945, 289946, 289947, 289948, 289949, 289950, 289951, 289952, 289953,
    289954, 289955, 289956, 289957, 289958, 289959, 289960, 289961, 289962,
    289963, 289964, 289965, 289966, 289967, 289968, 289969, 289970, 289971,
    289972, 289973, 289974, 289975, 289976, 289977, 289978, 289979, 289980,
    289981, 289982, 289983, 289984, 289985, 289986, 289987, 289988, 289989,
    289990, 289991, 289992, 289993, 289994, 289995, 289996, 289997, 289998,
    289999, 290000, 290001, 290002, 290003, 290004, 290005, 290006, 290007,
    290008, 290009, 290010, 290011, 290012, 290013, 290014, 290015, 290016,
    290017, 290018, 290019, 290020, 290021, 290022, 290023, 290024, 290025,
    290026, 290027, 413521, 413522, 413524, 413525, 413526, 413527, 413528,
    413529, 413530, 413531, 413532, 413535, 413536, 413537, 413538, 413539,
    413540, 413541, 413542, 413543, 413544, 413545, 413547, 413548, 413549,
    413550, 413551, 413553, 413554, 413555, 413556, 413557, 413558, 413559,
    413560, 413561, 413562, 413563, 801986, 801987, 413523, 413533, 413534,
    413546, 413552,
]


# Loop through the data and submit the form for each set
for roll in roll_list:
    submit_form(roll)
    if found_flag:
        break

# Close the browser window
