# eGain_interview_2025
**Yilin (Danny) Huang's interview project to Sales Engineer @eGain**

This project demonstrates the end-to-end process of data cleansing, visualization, and web hosting. 
The workflow involves cleaning and preparing data using Python with the Pandas library, visualizing the results with Google Looker Studio, and finally embedding the visualizations in an HTML webpage hosted on GitHub.

**Table of Contents**
1. Overview
2. Technologies Used
3. Workflow
4. How to
5. Live Demo

**Overview**


The goal of this project is to transform raw weblogs data into actionable insights and present it in a user-friendly, interactive format. The workflow includes:
- Cleaning and preparing the dataset using Python.
- Creating an interactive dashboard using Google Looker Studio.
- Hosting the dashboard on a public webpage via GitHub Pages.


**Technologies Used**


**Python** For data preprocessing and cleaning
- Key Library: Pandas

  
**Google Looker Studio** For Creating interactive visualizations


**HTML** To initialize a webpage and embed Looker Studio dahboard.


**GitBub** For hosting the project and making it publicly accessible. 



**Workflow**
1. **Data Cleansing (Python with Pandas)**
- Loaded the dataset (CSV format) using Pandas.
- Performed data cleansing, including:
    - Handling missing values.
    - Formatting.
    - Dropping unnecessary columns.
    - Adding calculated fields for better analysis.
- Exported the cleansed dataset to a new CSV file



2. **Data Visualization (Google Looker Studio)**
- Imported the cleansed CSV file into Google Looker Studio.
- Built interactive dashboards.
- Generated an embed link for the dashboard.


  
3. **Web Hosting (GitHub Pages)**
- Created an  file to host the visualization.
- Embedded the Looker Studio dashboard using an iframe. 
- Pushed the HTML file to a GitHub repository and enabled GitHub Pages for hosting.



**How to Run This Project**


Prerequisites

- Python IDE installed on local machine.
- A Google account for Looker Studio.
- A GitHub account for webpage hosting.

Steps

1. Run Python script for data cleansing with the correct file path for raw data.
2. Visualize the Data by uploading the cleansed .csv file from previous step to Looker Studio. 
3. Host the visualization.
- Replace the embed link in  with your Looker Studio dashboard link.

**Live Demo**


Check out the live version of the dashboard here: [GitHub Pages Link](https://noname447.github.io/eGain_interview_2025/)
