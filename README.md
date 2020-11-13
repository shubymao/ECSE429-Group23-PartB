# ECSE429 Project Part A
Project A
## Installing the Dependency
1. (Optional) create a virtual environment using virtualenv or python -m venv 
2. pip (or pip3) -r install requirement.txt
## Set the Environment Path Variable For the Jar to be Tested  
### Windows  
``` set JAR_PATH=<jar path>\runTodoManagerRestAPI-1.5.5.jar ```
### Mac/Linux
``` export JAR_PATH=<jar path>/runTodoManagerRestAPI-1.5.5.jar ```
## Running the test
Run the test by running ```pytest``` within the root directory.'
You might want to run ``` python -m pytest ``` to run the test in case the first command does not work.
