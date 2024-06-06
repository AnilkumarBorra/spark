# Requirements_Readme.md

## Recipes project For Data Engineering

### Overview

We have a big recipes archive that was created over the last 8 years. It is constantly being updated either by adding new recipes or by making changes to existing ones. We have a service that can ingest data in JSON format to a selected S3 location. We are interested in tracking changes to see available recipes, their cooking time, and difficulty level.

### Part 1

Using Apache Spark and Python, read the source data, pre-process it and persist (write) it to ensure optimal structure and performance for further processing. The source events are located in the input folder.

### Part 2

Using Apache Spark and Python read the processed dataset from Part 1 and:

1. Extract only recipes that have beef as one of the ingredients.
2. Calculate the average cooking time duration per difficulty level.
3. Persist the dataset as CSV to the output folder.

The dataset should have 2 columns: difficulty, avg_total_cooking_time.

Total cooking time duration can be calculated by the formula:

`total_cook_time = cookTime + prepTime`

Hint: times represent durations in ISO format.

### Criteria for Levels Based on Total Cook Time Duration:

- Easy: Less than 30 mins
- Medium: Between 30 and 60 mins
- Hard: More than 60 mins.

### Deliverables

- A deployable Spark Application written in Python.
- A separate ETL_README.md file with a brief explanation of the approach, data exploration, assumptions/considerations, and instructions on how to run the application.
- CSV output dataset from Part 2.

### Requirements

- **Well-structured code**: We expect maintainability, extensibility, readability, and well-defined abstractions with clear responsibilities.
- **Resiliency and scalability**: The application should be able to handle variability of the data and to scale if data volume increases.
- **Solution is runnable locally** on an isolated environment (e.g., Python virtual env or Docker container) and also deployable on a cluster (including dependency packaging). An iPython notebook is not sufficient.
- **Unit tests** for the different components.
- **Proper exception handling**.
- **Logging**.
- **Documentation**.
