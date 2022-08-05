# Hudl Project Submission

This repository contains a series of UI tests for the Login Page for Hudl's main site written using Python + Selenium with the help of virtual environments, package managers, and BDD scripts to drive high-level user behavior.

## Setup

1. Install Python 3:
    * Ubuntu:
        * `sudo apt update && sudo apt upgrade`
        * `sudo apt install python3 python3-pip python3-dev python3-venv python3-tk libssl-dev`
    * Mac:
        * Get Homebrew: `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
        * `brew install python3`
    * Windows (NOTE - When testing this the installation is somewhat unstable and is not guaranteed to be compatible with Selenium Browser drivers):
        * Install a tool that allows a linux like command line 
         (options: WSL, ubuntu on windows)
       * Install python similarly to the Ubuntu installation and add Python location and DLLs location to your PATH 

2. Install a BrowserDriver to point to when running tests
   * For this project, I was only able to verify the functionality of the tests using the ChromeDriver which can be found [here](https://chromedriver.chromium.org/downloads).
     * Make sure you verify your version of Chrome to ensure the correct driver is installed
   * To correctly point to the browser driver when running the tests, edit line 63 in `test_login.py` where 
   * `page = webdriver.Chrome(executable_path="<path_to_driver>")`
     * Feel free to substitute this for another browser driver if it is installed, and you may need to include the driver as a part of your PATH depending on the OS (at the time of writing, this was only confirmed  with a Mac).


3. Change to the Automation directory inside hudl-project-submission: `cd Automation`


4. Install Poetry

    https://python-poetry.org/docs/#installation

    `wget https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py`

    If you have multiple versions of python remember to ensure this is running as python 3 
    `python get-poetry.py`
    
    Uninstall step if necessary
    `python get-poetry.py --uninstall`
   
    * For Windows:
    (From powershell) 
     ```bash
     (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python - 
     ```
     Add .poetry and .poetry\bin to your PATH
   * Verify that poetry is installed with `poetry --version`
   

5. Create a new environment variable called `USER_PASS` with the desired password that will be used to perform the tests. 
    ```bash
    export USER_PASS
     ```
   * This will override the default USER_PASS value when running the make target in the next step
   
   You can also directly replace the .env variables with your own if the email and password are known and can skip this step


6. Run the following in the project directory:

    ```bash
    make setup-env
    ```
   * If for some reason you need to uninstall & reinstall packages due to unknown issues, the following command has been added to the make target for convenience:
   ```bash
    make clean-env
    ```

## Environment setup

I'm using [environs](https://github.com/sloria/environs) to read the env file.

General configuration information is in `.env`.

To run the tests, ensure the EMAIL parameter is either the provided test account email, or feel free to subsitute your own.

For security reasons, no passwords are included with the repo in it's current for. You may replace the PASSWORD field with a known test account password or email the author (aidanrubenstein@gmail.com) for the password to the test account.

### Pytest

Run full test suite:
`poetry run pytest tests -vvv`

Run a specific test class:
`poetry run pytest tests/<specific test>`

Example: `poetry run pytest tests/test_login.py`. 

Run a single test case within a file:
`poetry run pytest tests/<specific test>::test_function_name`

Example: `poetry run pytest tests/test_login.py::test_view_password_reset`

### BDD

All tests in this repo use Behavior Driven Development with Pytest.
Please [check here](https://pytest-bdd.readthedocs.io/en/stable/) for more details.

### Code Structure

`page_objects/` Contains the page-object model for pages throughout the Hudl UI. Each page object model should accept
the page fixture where it will perform UI-based test functions.

`tests/` Contains tests that will be run. Each file should test a feature within the target site.

`test/conftest.py` This script is run before the tests using 'pytest magic'. This loads the appropriate env files & uses the function `pytest_generate_tests` to inject values in the tests
(with the BDD tests this only interacts with the functions tagged with `@scenario`). 

`features/` Contains the feature files which are written in Gherkin and define high-level behavior which drives the automated tests.

`util/` Includes utility helper classes for environment setup.

### Testing Items & Utilities I Would Include if Time and Resources were Unlimited

(in no particular order):

* Containerization of the testing suite using a Dockerfile in order to avoid installation issues and possible flakiness across multiple operating systems.
* Testing including multiple browser drivers such as Firefox and Edge.
  * Possibly using Browserstack to emulate mobile devices such as iOS and Android as well.
* Change password functionality once logged in, and then logging out/back in with the new password.
* A more full E2E test scenario for resetting a password with an email recovery.
    * Ideally this would be resetting the password via email, following new password creation steps, and logging in with the new password.
* Performance/loadtesting with several users attempting to login at once.
* Parallelization of tests using Selenium Grid.

