# 🌍 COVID-19 Data Visualization & Comparison Tool

### 📊 Analyze and Compare COVID-19 Trends Across Countries

## Project Overview

This project provides an interactive and customizable platform for visualizing and comparing various COVID-19 metrics, such as **cases, deaths, recoveries**, and more, between any two countries. It leverages powerful data manipulation and visualization tools to give insights into the impact of the pandemic across different regions and over time.

---

## Key Features

- **Flexible Country Comparison**:
  - Users can select **any two countries** to compare COVID-19 data, such as cases, deaths, or recoveries.

- **Customizable Metrics**:
  - The tool allows users to choose which metric they want to visualize (e.g., daily cases, monthly deaths, recoveries).
  
- **Data Aggregation by Time Period**:
  - Aggregates daily data into **monthly totals**, offering a clearer long-term trend view.
  
- **Dynamic Visualizations**:
  - Interactive line graphs to display trends over time, easily comparing selected countries.
  - Custom color-coded plots for each country, making it easy to differentiate between them.

---

## Technologies Used

- **Python**
  - Efficient scripting and data analysis.

- **Pandas**
  - Data manipulation: filtering, grouping, and aggregating.
  - Time-based operations for converting daily data to monthly or weekly summaries.

- **Matplotlib**
  - To generate high-quality visualizations comparing countries and COVID-19 metrics.

---

## Visualizations

This project generates **line graphs** to compare COVID-19 trends over time, such as confirmed cases, deaths, or recoveries between two selected countries. The user can select which metric to visualize and which countries to compare.

### Example Output:

- **Orange Line**: Selected metric for Country A.
- **Blue Line**: Selected metric for Country B.

![COVID-19 Data Comparison](https://i.imgur.com/LcpUcnT.png)  
*Graph comparing COVID-19 metrics (e.g., cases, deaths, recoveries) between two countries.*

---


## How to Run the Project

1. Clone the repository.
2. Install the necessary libraries:
   ```bash
   pip install pandas matplotlib
   ```
3. Run the script and select the desired **countries** and **COVID-19 metric** (e.g., cases, deaths, recoveries) to visualize the comparison.
4. View the generated plots in your preferred environment.

---

## Future Improvements

- Expand the tool to allow comparisons across more than two countries.
- Implement an **interactive UI** with dropdowns for country and metric selection.
- Add support for more COVID-19 metrics, such as vaccination rates and hospitalizations.
- Integrate with live COVID-19 data APIs for real-time analysis.


