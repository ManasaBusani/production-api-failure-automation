# Production API Failure Automation

I built this project to simplify how failed API transactions are tracked, instead of manually checking logs or running queries every day.

In many cases, identifying failures takes time because you have to go through logs repeatedly. The goal here was to make that process quicker by generating a simple report of failed APIs.

## What this project does

- Reads API log data from a file  
- Filters only the failed API transactions  
- Highlights important or critical failures  
- Generates a report for quick analysis  

## Why I built this

While working with backend systems, I noticed that a lot of time goes into manually identifying issues.  
This project is a small step toward automating that process and making it easier to understand what’s going wrong.
This kind of automation helps reduce manual effort and allows quicker identification of production issues.

## Tech used

- Python  
- Pandas  

## How to run

1. Make sure Python is installed  
2. Install dependencies:
3. Run the script:


## Notes

This is a simplified version using sample data, but the same idea can be extended to real systems by connecting to databases and integrating with monitoring tools like Splunk or AppDynamics.
