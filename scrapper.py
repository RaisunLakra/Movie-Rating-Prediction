from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
import os
from contextlib import contextmanager

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@contextmanager
def get_driver():
    # Setup Chrome options
    options = Options()
    options.add_experimental_option("detach", True) # Keeps browser open after script finishes (debugging)

    if os.name == 'nt':
        # Set PATH only if it's not already set (Windows)
        chrome_driver_path = r'C:\Program Files (x86)\chromedriver.exe'
        if chrome_driver_path not in os.environ['PATH']:
            os.environ['PATH'] += f";{chrome_driver_path}"

    try:
        driver = webdriver.Chrome(options=options)
        logging.info("Driver successfully started")
        yield driver
    except Exception as e:
        logging.error("Failed to initialize Chrome driver", exc_info=True)
    finally:
        # Ensure the driver is closed properly
        try:
            driver.quit()
            logging.info("Driver closed")
        except Exception as e:
            pass

def get_all_Indian_movies(driver, no_of_movies=None):
    """ Ouput: List of movie names, release years, genres, director, lead actors, overview and IMDB ratings. """

    try:
        available_movies = driver.find_element_by_class_name("sc-13add9d7-3")
        logging.info(f"Available movies: {available_movies}")
    except Exception as e:
        logging.error("Failed to get available movies", exc_info=True)
        return
    
if __name__ == "__main__":
    with get_driver() as driver:
        driver.get("https://www.imdb.com/search/title/?countries=IN")
        driver.implicitly_wait(10)
        logging.info("Page loaded successfully")
        logging.info(f"Page title: {driver.title}")
        get_all_Indian_movies(driver)