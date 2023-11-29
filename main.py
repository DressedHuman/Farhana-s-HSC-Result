import os
import time
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options

# Get the current script's directory
script_directory = os.path.dirname(os.path.realpath(__file__))

# Set the path to the Chromedriver executable in the same directory as the script
# chromedriver_path = os.path.join(script_directory, 'chromedriver.exe')
edgedriver_path = os.path.join(script_directory, 'msedgedriver.exe')

# Set up Chrome options for headless mode
# chrome_options = Options()
edge_options = Options()
# chrome_options.add_argument('--headless')  # Run in headless mode
# chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration
edge_options.add_argument('--disable-gpu')  # Disable GPU acceleration

# Use the Service class to set the path to the Chromedriver executable
# chrome_service = Service(chromedriver_path)
edge_service = Service(edgedriver_path)
# Create a new instance of the Chrome driver with headless options
# driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver = webdriver.Chrome(service=edge_service, options=edge_options)
# URL of the form page
form_url = 'http://result.dinajpurboard.gov.bd/hsc_result2023/search/each.php'

# Function to submit form data and retrieve results
found_flag = False
def submit_form(roll):
    driver.get(form_url)

    # Replace the following lines with the actual code to interact with the form
    # For example, find form elements by ID and submit data
    driver.find_element(by=By.NAME, value='roll_no').send_keys(roll)
    driver.find_element(by=By.NAME, value='regi_no').send_keys(1817703269)
    driver.find_element(by=By.NAME, value='submit').click()

    # Wait for the result page to load (adjust wait time as needed)
    # time.sleep(2)

    # Replace the following line with the actual code to retrieve and process results
    # result = driver.find_element(by=By.NAME, value='result_element').text
    # print(f"Form submitted with data: {data}, Result: {result}")
    if (found_flag := not "No Result Found" in driver.page_source):
        print(found_flag)
        # driver.save_screenshot('Farhana - HSC 2023 - Result Check with Selenium on Python.png')
        time.sleep(570)
    print(found_flag)


# Generate 500 sets of sample data (replace with your actual data)
roll_list = [
    278052, 278053, 278054, 278055, 278056, 278057, 278058, 278059, 278060, 278061,
    278062, 278063, 278064, 278065, 278066, 278067, 278068, 278069, 278070, 278071,
    278072, 278073, 278074, 278075, 278076, 278077, 278078, 278079, 278080, 278081,
    278082, 278083, 278084, 278085, 278086, 278087, 278088, 278089, 278090, 278091,
    278092, 278093, 278094, 278095, 278096, 278097, 278098, 278099, 278100, 278101,
    278102, 278103, 278104, 278105, 278106, 278107, 278108, 278109, 278110, 278111,
    278113, 278114, 278115, 278116, 278117, 278118, 278119, 278120, 278121, 278122,
    278123, 278124, 278125, 278126, 278127, 278128, 278129, 278130, 278131, 278132,
    278133, 278135, 278136, 278137, 278138, 278139, 278140, 278141, 278142, 278143,
    278144, 278145, 278146, 278147, 278148, 278149, 278150, 278151, 278152, 278153,
    278154, 278155, 278156, 278157, 278158, 278159, 278160, 278161, 278162, 278163,
    278164, 278165, 278166, 278167, 278168, 278169, 278170, 278171, 278172, 278173,
    278174, 278175, 278176, 278177, 278178, 278179, 278180, 278181, 278182, 278183,
    278184, 278185, 278186, 278187, 278188, 278189, 278190, 278191, 278192, 278193,
    278194, 278195, 278196, 278197, 278198, 278199, 278200, 278201, 278202, 278203,
    278204, 278205, 278206, 278207, 278208, 278209, 278210, 278211, 278212, 278213,
    278214, 278215, 278217, 278218, 278219, 278220, 278221, 278222, 278223, 278224,
    278225, 278226, 278227, 278228, 278229, 278230, 278231, 278232, 278233, 278234,
    278235, 278236, 278237, 278238, 278239, 278240, 278241, 278242, 278243, 278244,
    278245, 278246, 278247, 278248, 278249, 278250, 278251, 278252, 278253, 278254,
    278255, 278256, 278257, 278258, 278259, 278260, 278261, 278262, 278263, 278264,
    278265, 278266, 278267, 278268, 278269, 278270, 278271, 278272, 278273, 278274,
    278275, 278276, 278277, 278278, 278279, 278280, 278281, 278282, 278283, 278284,
    278285, 278286, 278287, 278288, 278289, 278290, 278291, 278292, 278293, 278294, #Jannatul Ferdousi - 278294 - 4.50
    278295, 278296, 278297, 278298, 278299, 278300, 278301, 278303, 278304, 278305,
    278306, 278307, 278308, 278309, 278310, 278311, 278312, 278313, 278314, 278315
]


# Loop through the data and submit the form for each set
for roll in roll_list:
    submit_form(roll)
    if found_flag:
        break

# Close the browser window
