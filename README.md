# Azure Serverless Deployment Monitor

<img width="1911" height="908" alt="Image" src="https://github.com/user-attachments/assets/f6dbdfe5-449b-41dc-b6c6-4aff8e1c12e9" />


## 📌 Project Overview

The **Azure Serverless Deployment Monitor** is a Python-based Azure Function that automatically monitors website availability on a scheduled timer, demonstrating how to build, test, and deploy a serverless monitoring solution using Azure Functions, Azure Storage, and Azure CLI.

The function runs every 5 minutes, checks configured URLs, and logs their availability status to Azure logs.

---

## Architecture

<img width="1897" height="528" alt="Image" src="https://github.com/user-attachments/assets/bd23ca10-eb99-4ccd-b43a-55a5f6a197da" />


This project uses a **serverless architecture** hosted in Microsoft Azure.

**Workflow:**

1. Azure Timer Trigger runs every 5 minutes
2. Python Azure Function executes
3. URLs are read from a configuration file
4. Each URL is checked using HTTP requests
5. Status results are logged to Azure

---

## Azure Services Used

* Azure Functions (Python)
* Azure Storage Account
* Azure Resource Group
* Azure Application Insights
* Azure CLI
* Azure Functions Core Tools
* Azurite (Local Storage Emulator)

---

## Technologies Used

* Python
* Azure Functions
* Git
* Azure CLI

## Future Improvements

Potential enhancements include:

* Store results in Azure Blob Storage
* Send email alerts when a site is down
* Add GitHub Actions CI/CD pipeline
* Create a web dashboard
* Add latency tracking
