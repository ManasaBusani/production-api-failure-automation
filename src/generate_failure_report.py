import pandas as pd

print("Starting API failure report generation...")

df = pd.read_csv("data/sample_api_logs.csv")
failed = df[df["status"] == "FAILED"]

print("Found failed records:", len(failed))

failed.to_excel("failed_report.xlsx", index=False)
print("Report generated successfully.")
