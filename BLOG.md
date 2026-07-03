# Building My First End-to-End ETL Pipeline

When I started this project, I wanted to go beyond writing Python scripts that simply read a CSV file and print a few rows. My goal was to build something that resembles a real data engineering workflow while understanding *why* each component exists.

This repository documents that journey.

## The Problem

Businesses collect data from many sources, but raw data is rarely ready for analysis. It often contains duplicates, missing values, inconsistent formatting, or incorrect data types. Before analysts or decision-makers can trust the data, it needs to be processed.

That is where ETL comes in.

ETL stands for:

- **Extract** – Read data from a source.
- **Transform** – Clean, validate, and enrich the data.
- **Load** – Store the processed data somewhere useful.

Rather than reading about these concepts, I wanted to build one myself.

---

# What I Built

This project reads raw sales data from a CSV file, validates it, cleans it, calculates useful business metrics, stores it in both a cleaned CSV file and a SQLite database, performs SQL analytics, generates visualizations, and finally produces an HTML dashboard.

The pipeline follows this workflow:

```
Raw CSV
    ↓
Extract
    ↓
Validate
    ↓
Transform
    ↓
Cleaned CSV
    ↓
SQLite Database
    ↓
SQL Analytics
    ↓
Charts
    ↓
HTML Dashboard
```

---

# Concepts I Learned

## Project Structure

Instead of placing everything inside one large Python file, I separated the project into modules.

This made the project easier to understand, maintain, and extend.

I learned that production code values readability just as much as functionality.

---

## Configuration Files

Initially, file paths were hardcoded into the script.

I later replaced them with a `config.json` file.

This small change taught me an important lesson:

**Configuration should live outside the application whenever possible.**

Changing a file path should not require editing the program itself.

---

## Logging

Rather than relying only on `print()` statements, I introduced Python logging.

This records important events such as:

- Pipeline started
- Data loaded
- Validation completed
- Data transformed
- Files saved

Logging provides a history of what happened during execution and makes debugging much easier.

---

## Data Validation

Real-world data cannot be trusted blindly.

Before processing any records, the pipeline verifies that:

- Required columns exist
- Numeric columns actually contain numbers

Failing early with meaningful error messages is much better than discovering incorrect results later.

---

## Modular Programming

As the project grew, I refactored it into reusable functions.

Instead of one long script, the pipeline now consists of:

- `extract()`
- `validate()`
- `transform()`
- `load()`
- `load_to_database()`
- `run_analytics()`
- `generate_report()`

Breaking problems into smaller functions made the code much easier to read and test.

---

## SQLite

Rather than stopping after producing another CSV file, I loaded the cleaned data into SQLite.

This introduced me to the idea that data engineering often ends with storing processed data in a database where it can be queried efficiently.

---

## SQL Analytics

Once the data was stored in SQLite, I used SQL to answer business questions such as:

- Total revenue
- Average order value
- Number of orders
- Highest-value customer

This showed me that ETL is not just about moving data but preparing it for decision-making.

---

## Data Visualization

Numbers become much easier to understand when visualized.

Using Matplotlib, I generated a revenue-by-product chart and included it in the final report.

This transformed raw data into something immediately understandable.

---

## HTML Reporting

Instead of limiting output to the terminal, I generated an HTML dashboard containing:

- Summary statistics
- Revenue chart
- Sales table
- Report generation timestamp

This demonstrated how data pipelines can produce outputs for both technical and non-technical users.

---

## GitHub Actions

One of my favorite additions was setting up GitHub Actions.

Every time I push new code:

- Dependencies are installed automatically.
- The ETL pipeline runs.
- GitHub reports whether the build passed or failed.

This introduced me to Continuous Integration (CI), an important part of modern software and data engineering workflows.

---

# Why I Built It This Way

One lesson I learned throughout this project is that engineering is not only about making something work.

It is about making it understandable, maintainable, and reliable.

For example:

- I used a configuration file instead of hardcoded paths because configurations change.
- I added validation because incorrect data should be caught early.
- I separated the project into modules because code grows over time.
- I added logging because debugging becomes much easier.
- I automated testing through GitHub Actions because software should verify itself whenever possible.

Each improvement solved a real problem instead of simply adding another feature.

---

# Challenges

Some parts were more difficult than expected.

Learning how different modules communicate, structuring the project cleanly, and understanding why software engineers organize code in a particular way required more thought than writing the code itself.

Those challenges taught me that good software design is just as important as programming syntax.

---

# What's Next

This project is only the beginning.

My next goals are to build pipelines that work with:

- Public APIs
- Cloud storage
- PostgreSQL
- Docker
- Apache Airflow
- Data warehouses
- Automated testing
- Larger datasets

Each new project will focus on solving a different real-world data engineering problem.

---

# Final Thoughts

This project represents an important milestone in my learning journey.

More importantly, it taught me how to think like a data engineer: build reliable pipelines, organize code thoughtfully, automate repetitive tasks, and produce outputs that others can trust.

I know there is still a lot to learn, but this repository reflects both what I have built and how my approach to software engineering is evolving.

Thank you for taking the time to explore my work.