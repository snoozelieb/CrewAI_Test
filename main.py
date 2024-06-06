import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, FileReadTool, ScrapeWebsiteTool
from utils import get_openai_api_key, get_serper_api_key, pretty_print_result
import matplotlib.pyplot as plt

# Set environment variables for API keys using utility functions
os.environ["SERPER_API_KEY"] = get_serper_api_key()
os.environ["OPENAI_API_KEY"] = get_openai_api_key()

# Create the tools
scrape_tool = ScrapeWebsiteTool()
search_tool = SerperDevTool()
file_read_tool = FileReadTool()

# Define the Fetch Companies Task
fetch_companies_task = Task(
    description="Fetch the list of insurers from the provided URL.",
    expected_output="A list of insurer names and details from the URL.",
    tools=[scrape_tool],
    input_data={'url': 'https://www.resbank.co.za/en/home/what-we-do/Prudentialregulation/insurers-list'},
    agent=None  # No specific agent needed for this initial task
)

# Define the Researcher Agents
researcher_general = Agent(
    role='General Researcher',
    goal='Gather broad information on each company to understand what data is available.',
    verbose=True,
    memory=True,
    backstory="You are a skilled researcher adept at finding detailed information on any topic.",
    tools=[search_tool],
    allow_delegation=True
)

researcher_pricing = Agent(
    role='Pricing Researcher',
    goal='Gather detailed pricing information for each company’s funeral products.',
    verbose=True,
    memory=True,
    backstory="You are an expert in extracting detailed pricing information.",
    tools=[search_tool],
    allow_delegation=True
)

researcher_coverage = Agent(
    role='Coverage Researcher',
    goal='Gather detailed coverage information for each company’s funeral products.',
    verbose=True,
    memory=True,
    backstory="You are an expert in extracting detailed coverage information.",
    tools=[search_tool],
    allow_delegation=True
)

researcher_reviews = Agent(
    role='Customer Reviews Researcher',
    goal='Gather customer reviews and feedback for each company’s funeral products.',
    verbose=True,
    memory=True,
    backstory="You are skilled at finding and analyzing customer reviews and feedback.",
    tools=[search_tool],
    allow_delegation=True
)

# Define the Analyst Agent
analyst = Agent(
    role='Analyst',
    goal='Review and collate the initial broad research data to determine specific data requirements.',
    verbose=True,
    memory=True,
    backstory="You are an expert in data analysis and can identify key data points from raw information.",
    tools=[file_read_tool],
    allow_delegation=False
)

# Define the Spec Writer Agent
spec_writer = Agent(
    role='Spec Writer',
    goal='Write detailed specifications for the additional data search based on the analyst’s findings.',
    verbose=True,
    memory=True,
    backstory="You are a proficient writer skilled in drafting detailed research specifications.",
    tools=[],
    allow_delegation=False
)

# Define the Data Analyst Agent
data_analyst = Agent(
    role='Data Analyst',
    goal='Process and analyze the collected data to extract meaningful insights.',
    verbose=True,
    memory=True,
    backstory="You are an expert in data processing and analysis.",
    tools=[],
    allow_delegation=False
)

# Define the Writer Agent
writer = Agent(
    role='Writer',
    goal='Summarize the research findings and present them in a well-structured report with visualizations.',
    verbose=True,
    memory=True,
    backstory="You have a knack for writing clear and concise reports based on detailed research.",
    tools=[],
    allow_delegation=False
)

# Define the Initial Research Task
initial_research_task = Task(
    description="Conduct initial broad research on each insurer to gather a wide range of information.",
    expected_output="A collection of broad data on each insurer.",
    tools=[search_tool],
    agent=researcher_general,
)

# Define the Review Task
review_task = Task(
    description="Analyze the initial broad research data to determine specific details to collect in the next phase.",
    expected_output="A detailed plan for specific data collection.",
    tools=[file_read_tool],
    agent=analyst  # Analyst Agent reviews the data
)

# Define the Spec Writing Task
spec_writing_task = Task(
    description="Write detailed specifications for the additional data search based on the analyst’s findings.",
    expected_output="A detailed specification document for further research.",
    tools=[],
    agent=spec_writer  # Spec Writer Agent drafts the specifications
)

# Define the Specialized Research Tasks
research_pricing_task = Task(
    description="Gather detailed pricing information for each company’s funeral products.",
    expected_output="Detailed pricing information for each insurer.",
    tools=[search_tool],
    agent=researcher_pricing,
)

research_coverage_task = Task(
    description="Gather detailed coverage information for each company’s funeral products.",
    expected_output="Detailed coverage information for each insurer.",
    tools=[search_tool],
    agent=researcher_coverage,
)

research_reviews_task = Task(
    description="Gather customer reviews and feedback for each company’s funeral products.",
    expected_output="Customer reviews and feedback for each insurer.",
    tools=[search_tool],
    agent=researcher_reviews,
)

# Define the Data Analysis Task
data_analysis_task = Task(
    description="Process and analyze the collected data to extract meaningful insights.",
    expected_output="Analyzed data with insights on funeral products.",
    tools=[],
    agent=data_analyst,
)

# Define the Writing Task
write_task = Task(
    description="Summarize the refined research findings and present them in a detailed report with visualizations.",
    expected_output="A comprehensive report on funeral products with visualizations.",
    tools=[],
    agent=writer,
    async_execution=False
)

# Form the Crew
crew = Crew(
    agents=[researcher_general, researcher_pricing, researcher_coverage, researcher_reviews, analyst, spec_writer,
            data_analyst, writer],
    tasks=[fetch_companies_task, initial_research_task, review_task, spec_writing_task, research_pricing_task,
           research_coverage_task, research_reviews_task, data_analysis_task, write_task],
    process=Process.sequential  # Sequential task execution
)

# Kickoff the process
result = crew.kickoff(inputs={'url': 'https://www.resbank.co.za/en/home/what-we-do/Prudentialregulation/insurers-list'})
formatted_result = pretty_print_result(result)
print(formatted_result)


# Additional utility to save the report to a file
def save_report(report, filename='funeral_products_report.md'):
    with open(filename, 'w') as file:
        file.write(report)


# Save the result to a file
save_report(formatted_result)


# Visualization example
def create_visualization(data, filename='visualization.png'):
    # Placeholder for actual data visualization logic
    plt.figure(figsize=(10, 6))
    plt.plot(data)  # Replace with actual data
    plt.title('Example Visualization')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.savefig(filename)


# Create a sample visualization (replace with actual data)
create_visualization([1, 2, 3, 4, 5])
