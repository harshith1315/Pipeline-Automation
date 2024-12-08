# PipeLine Automation
## Introduction
Pipeline automation has become an indispensable tool for streamlining workflows and enhancing efficiency in various domains. In this project, titled "Pipeline Automation," a robust system has been developed to automate the process of transferring data from Excel files to an Azure SQL database. Leveraging Flask for web development and Python for backend scripting, this project integrates seamlessly with Azure Blob Storage and Azure SQL, offering a comprehensive solution for data management tasks.

## Architecture Overview
The architecture of the Pipeline Automation project is designed to facilitate smooth data transfer from Excel files to an Azure SQL database. The system consists of several key components, including a Flask-based web application, Azure Blob Storage, Azure SQL, and a pipeline with event triggers for automation.
<p align="center">
  <img width="650" height="325" src="https://github.com/harshith1315/CICD-Automation/assets/111886682/c03c463b-65df-4da3-a971-472b88edad59"
>
</p>


## Process Description
The process begins with the creation of a website using Flask, providing users with a user-friendly interface to upload Excel files. Once a file is uploaded, it is stored in Azure Blob Storage, a scalable object storage solution offered by Microsoft Azure.

An event trigger is set up within the pipeline, ensuring that whenever a new file is created in the Azure Blob Storage, the pipeline is automatically initiated. This event-driven approach minimizes manual intervention and ensures timely processing of data.

Upon triggering, the pipeline orchestrates the transfer of the file from Azure Blob Storage to an Azure SQL table. Notably, each table is named after the timestamp of the file's creation, allowing for easy organization and retrieval of data.

Now, let's delve into each step of the process with accompanying images
### 1.Website Creation using Flask
The Flask-based website provides users with an intuitive platform to upload Excel files, initiating the data transfer process.

![image](https://github.com/harshith1315/pipeline-automation/assets/111886682/3c4e21e1-d9a3-4112-a5c2-03bb2ce3ebfe)
### 2.Excel File Upload to Azure Blob Storage
Uploaded Excel files are securely stored in Azure Blob Storage, ensuring scalability and reliability for data storage.
![image](https://github.com/harshith1315/pipeline-automation/assets/111886682/bd9f9e39-a0b1-429c-932b-39e0d4a8e409)
### 3.Event Trigger Setup in Pipeline:
A pipeline with event triggers is established to automate the process. Whenever a new file is detected in Azure Blob Storage, the pipeline is triggered.
### 4.Data Transfer to Azure SQL Table:
The pipeline orchestrates the seamless transfer of data from Azure Blob Storage to an Azure SQL table and also the tablename is the Timestamp by using Dynamic Content in Azure , facilitating efficient data management.

![image](https://github.com/harshith1315/pipeline-automation/assets/111886682/8a39ec62-1f2c-49ab-94f2-105b10ab8de7)
![image](https://github.com/harshith1315/pipeline-automation/assets/111886682/d1354729-8706-4595-8263-dabdcb919c38)

By automating the pipeline, this project significantly reduces manual effort and enhances data processing efficiency, making it a valuable asset for organizations dealing with large volumes of data.
## Contributors
KANUMURI HARSHITH(@harshith1315)
