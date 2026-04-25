# Production API Failure Automation

I built this project to simplify how failed API transactions are tracked, instead of manually checking logs or running queries repeatedly.

In real backend systems, identifying failures can take time because you need to go through logs and data multiple times. The goal here was to automate that process and make it easier to quickly understand what’s going wrong.

## What this project does

- Reads API log data from a file  
- Filters only the failed API transactions  
- Highlights important or critical failures  
- Generates a report for quick analysis  

## Why I built this

While working with backend and production systems, I noticed that a lot of time goes into manually identifying issues.  
This project is a small step toward automating that process and improving how quickly failures can be analyzed.

This kind of approach can be extended to real systems where logs are collected through monitoring tools and stored in databases.

## Tech used

- Python  
- Pandas (for data processing)  
- SQL (for querying failure data)  
- REST APIs (backend service integration)  
- Logging & Telemetry (Splunk / AppDynamics monitoring)  
- Automation concepts (script-based scheduling)  
- Data analysis (for identifying failure patterns)  
- Basic exposure to .NET-based backend services  

## How to run

1. Make sure Python is installed  
2. Install dependencies: pip install pandas
3. Run the script : python src/generate_failure_report.py

## Notes

This is a simplified version using sample data, but in a real system this can be extended by connecting to databases, integrating with monitoring tools, and automating execution using schedulers like Jenkins.
