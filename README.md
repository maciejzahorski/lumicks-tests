# Lumicks Automated Tests
The funtional automated tests for Lumicks User Community.

Use them on your local machine, with Chrome and ChromeDriver (other browsers may be added in the future).

**Requirements**: Python 3.6 or higher.

**Notice**: Some tests can be marked with `@xfail` tag. These tests are expected to fail. You can exclude them by using:
```
--tags -xfail
```
option added to `behave` command.

# Table of contents
  1. [Installation](#installation)
  2. [Running](#running)

# HOWTOs
The instructions below are adjusted for Linux. If you use Windows, you need to adjust the commands properly.

## Installation

  1. Clone repository.
     ```
     cd <project_folder>
     git clone <pasted_repo_address_from_github>
     ```
  2. Create virtual environment, export `BASE_URL` variable and install requirements.
     ```
     python3 -m venv venv
     source venv/bin/activate
     cd automated-tests
     export BASE_URL=https://system-under-testing/
     pip install -r requirements.txt
     pip install -e .
     ```
  3. Setup ChromeDriver
     - Download [ChromeDriver](http://chromedriver.chromium.org/downloads)
     - Add the path to the folder with ChromeDriver to PATH variable. Example:
     ```
     export PATH=$PATH:~/selenium_drivers/
     ```

## Running
  Change directory:
  ```
  cd lumicks_automated_tests
  ```
  - To run whole suite, use:
  ```
  behave
  ```
  - To run a subset of tests marked with the same tag:
  ```
  behave -k -t @your_tag
  ```
  - To run a chosen feature file separately:
  ```
  behave -i you_feature_file.feature
  ```

  More run options can be found in [behave docs](https://behave.readthedocs.io/en/stable/)
