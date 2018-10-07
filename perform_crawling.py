from classes.crawler import Crawler
from classes.console import Console
from config.config import Config

# Set connection to the origin DB
config=Config()

# Initialize main calculation class
crawler=Crawler(config.config_initial)

# Initialize console object
console=Console(config.getMinAllowedInputs())

# Check if user's input is correct
# and has valid characters for calculation
while True:
     # Ask user input and return filtered result
     # acceptable for further calculation
     parameters=console.askInput()
     if parameters and any(s in parameters for s in config.getMinAllowedInputs()):
       # Perform position calculation
       result=crawler.calculateLocation(parameters)
       print(result)
       break

     print("Initial parameters are not correct. Please try again")





