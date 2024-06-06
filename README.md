# Funeral Products Research Assistant

This project is a comprehensive Funeral Products Research Assistant built using CrewAI. The system is designed to fetch data on funeral products offered by various insurers, analyze the data, and generate a detailed report with visualizations.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Agents and Tasks](#agents-and-tasks)
- [Utilities](#utilities)
- [Output](#output)
- [Contributing](#contributing)

## Introduction

The Funeral Products Research Assistant aims to provide detailed insights into the costs and features of funeral products offered by various insurers. This project involves multiple phases, including data exploration, collection, analysis, and report generation.

## Features

- Fetches a list of insurers from a given URL.
- Gathers detailed information on funeral products, including pricing, coverage, and customer reviews.
- Analyzes the collected data to extract meaningful insights.
- Generates a comprehensive report with visualizations.
- Utilizes specialized agents for different tasks.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/funeral-products-research-assistant.git
    cd funeral-products-research-assistant
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your environment variables by creating a `.env` file in the root directory with the following content:
    ```
    OPENAI_API_KEY=your_openai_api_key
    SERPER_API_KEY=your_serper_api_key
    ```

## Usage

1. Run the main script to start the research process in PyCharm or your preferred IDE:
    ```bash
    python main.py
    ```

2. The system will fetch data, analyze it, and generate a detailed report saved as `funeral_products_report.md`.

## Agents and Tasks

- **Researcher Agents**: Collect broad and specific data on insurers.
- **Analyst Agent**: Review and collate the data to identify specific requirements.
- **Spec Writer Agent**: Write detailed specifications for the data search.
- **Data Analyst Agent**: Process and analyze the collected data.
- **Writer Agent**: Summarize the data into a comprehensive report with visualizations.

### Task Flow

1. **Fetch Companies Task**: Fetches the list of insurers.
2. **Initial Research Task**: Collects broad data on each insurer.
3. **Review Task**: Analyzes the initial data to refine the data collection strategy.
4. **Spec Writing Task**: Writes detailed specifications for further research.
5. **Specialized Research Tasks**: Collects specific data on pricing, coverage, and customer reviews.
6. **Data Analysis Task**: Processes and analyzes the data.
7. **Writing Task**: Summarizes the findings into a detailed report.

## Utilities

- `utils.py` contains helper functions to load environment variables and pretty print the results.

### Helper Functions

- `load_env()`: Loads environment variables from a `.env` file.
- `get_openai_api_key()`: Retrieves the OpenAI API key.
- `get_serper_api_key()`: Retrieves the Serper API key.
- `pretty_print_result(result)`: Formats the result with line breaks for readability.

## Output

The final output is a detailed report saved as `funeral_products_report.md`, which includes:

- Overview of insurers and their funeral products.
- Detailed pricing and coverage information.
- Customer reviews and feedback.
- Data visualizations to enhance understanding.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests.
