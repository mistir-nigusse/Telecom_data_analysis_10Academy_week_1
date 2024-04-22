
# Network Analysis Python Package

## Overview

This Python package, `network_analysis`, is designed for conducting network analysis task. It provides tools and utilities to analyze network data, with a focus on handling Slack messages from a previous 10 Academy training program.

## What to do

Several code snippets have been provided to serve as a starting point for your project. However, it's essential to note that the code has not undergone thorough testing, and errors are expected. Your task is to identify and rectify errors, remove unnecessary components, and incorporate any missing elements.

Consider this initial code as a foundation for your solution, but do not rely on it in its current state. It's provided to give you a starting point, but you should be prepared to modify and enhance it to meet the specific requirements of your system.

As you commence your work, focus on exploring the dataset to gain a deep understanding of its structure and contents. Attempt to answer various intriguing questions that arise during your exploration.

For guidance on the specific questions to address, refer to the notebooks/parse_slack_data.ipynb notebook, where you'll find empty cells designed for your responses. Utilize these cells to document your findings, insights, and any challenges encountered.

Remember, this is an iterative process, and refining your code and analyses is a crucial part of the learning experience. Regularly post question on slack, and don't hesitate to reach out to tutors if you encounter difficulties. Best of luck with your exploration and analysis!

## Table of Contents

- [Installation](#installation)
  - [Creating a Virtual Environment](#virtual-env)
  - [Clone this package](#clone)
- [Usage](#usage)
  - [Configuration](#configuration)
  - [Data Loading](#data-loading)
  - [Utilities](#utilities)
- [Testing](#testing)
- [Documentation](#documentation)
- [Notebooks](#notebooks)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Creating a Virtual Environment

#### Using Conda

If you prefer Conda as your package manager:

1. Open your terminal or command prompt.

2. Navigate to your project directory.

3. Run the following command to create a new Conda environment:

    ```bash
    conda create --name your_env_name python=3.12
    ```
    Replace `your_env_name` with the desired name for your environment e.g. week0 and `3.12` with your preferred Python version.

4. Activate the environment:

    ```bash
    conda activate your_env_name
    ```

#### Using Virtualenv

If you prefer using `venv`, Python's built-in virtual environment module:

1. Open your terminal or command prompt.

2. Navigate to your project directory.

3. Run the following command to create a new virtual environment:

    ```bash
    python -m venv your_env_name
    ```

    Replace `your_env_name` with the desired name for your environment.

4. Activate the environment:

    - On Windows:

    ```bash
    .\your_env_name\scripts\activate
    ```

    - On macOS/Linux:

    ```bash
    source your_env_name/bin/activate
    ```

Now, your virtual environment is created and activated. You can install packages and run your Python scripts within this isolated environment. Don't forget to install required packages using `pip` or `conda` once the environment is activated.

### Clone this package

To install the `network_analysis` package, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/network_analysis.git
    ```
2. Navigate to the project directory:
    ```bash
    cd network_analysis
    ```
 
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

Please be aware that the existing requirements.txt file includes only a limited set of packages at the moment, and it might not encompass all the necessary packages for your analysis. Make sure to supplement it with any additional packages you plan to install.

## Usage
### Configuration
Configure the package by modifying the `src/config.py` file. Adjust parameters such as file paths, API keys, or any other configuration settings relevant to your use case.

### Data Loading
The package provides a data loader module (`loader.py`) in the src directory. Use this module to load your network data into a format suitable for analysis.

Example:

```python
from src.loader import DataLoader

# Initialize DataLoader
data_loader = DataLoader()

# Load data from a Slack channel
slack_data = data_loader.load_slack_data("path/to/slack_channel_data")
```

## Utilities
Explore the various utilities available in the `src/utils.py` module. This module contains functions for common tasks such as data cleaning, preprocessing, and analysis.

Example:

```python
from src.utils import clean_data, visualize_network

# Clean the loaded data
cleaned_data = clean_data(slack_data)

# Visualize the network
visualize_network(cleaned_data)
```

## Testing
Run tests using the following command:

```bash
make test
```

This will execute the unit tests located in the tests directory.

## Documentation
Visit the docs directory for additional documentation and resources. The documentation covers important aspects such as code structure, best practices, and additional usage examples.

## Notebooks
The notebooks directory contains Jupyter notebooks that demonstrate specific use cases and analyses. Refer to these notebooks for hands-on examples.

## Contributing
Contributions are welcome! Before contributing, please review our contribution guidelines.

##  License
This project is licensed under the MIT License.

## Network Analysis

This is a starter python package to analze the slack data to learn about

* Patter of users messaging behaviour
* Patter of replies and reactions of users to messages posted both by peers and admins
* Discover sub-communities by building network graphs of message senders and those who reply or react to those messages






