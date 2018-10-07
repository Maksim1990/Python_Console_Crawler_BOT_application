from classes.crawler import Crawler
from classes.console import Console
from config.config import Config

console=Console()
# Ask user input and return filtered result
# acceptable for further calculation
parameters=console.askInput()

# Set connection to the origin DB
config=Config()

# Initialize main calculation class
crawler=Crawler(config.config_initial)

# Check if user's input is correct
# and has valid characters for calculation
if parameters:
 # Perform position calculation
 result=crawler.calculateLocation(parameters)
 print(result)
