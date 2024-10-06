# Amazon E-commerce Customer Behaviour Dashboard

## Project Overview
The **Amazon E-commerce Customer Behaviour Dashboard** is a data visualization project aimed at analyzing customer behavior within the Amazon ecosystem. The dataset includes customer interactions, demographics, purchase behaviors, and review-related insights. The goal is to provide visual insights that help e-commerce platforms, such as Amazon, improve their customer experience, marketing strategies, and service offerings.

This project leverages **Tableau** for data visualization and **Python** for initial data cleaning. The dataset covers various customer interactions such as product categories purchased, personalized recommendations, and areas for improvement.

## Key Features
- **Data Cleaning & Preparation**: Python was used to clean and prepare the raw dataset for use in Tableau.
- **Interactive Tableau Dashboard**: Visualizes customer behavior insights for e-commerce, focusing on demographics, purchase trends, and feedback.
- **Key Performance Indicators (KPIs)**: Includes metrics such as Total Consumers, Average Age, Shopping Satisfaction, and Product Recommendation Accuracy.
- **Visualizations**: Heatmaps, bar charts, line graphs, and KPIs provide a comprehensive view of consumer behavior.

## Project Structure

### 1. **Data Cleaning in Python**
   - Handled missing values.
   - Standardized categorical columns (e.g., purchase frequency, service appreciation).
   - Transformed numerical columns for effective analysis and visualization.

### 2. **Dashboard Creation in Tableau**
   The Tableau dashboard consists of one page(currently):

   #### Dashboard 1 (Main Insights)
   - **KPIs**: Displays metrics such as Total Consumers, Average Age, Shopping Satisfaction, and Accuracy of Personalized Recommendations.
   - **Consumer Demographics Breakdown**: A bar chart showing customer segmentation by age group and gender.
   - **Purchase Trends Over Time**: A line graph showcasing customer purchase behavior based on the timestamp.
   - **Top Areas for Amazon to Improve**: A bar chart highlighting customer feedback on areas of improvement.
   - **Purchase Frequency Heatmap**: Shows customer purchase frequency in relation to their browsing habits.

## Dataset Description
The dataset used for this project was obtained from [Amazon Consumer Behavior Dataset](https://www.kaggle.com/datasets/swathiunnikrishnan/amazon-consumer-behaviour-dataset).

The dataset used in this project includes 24 columns representing customer interactions and feedback regarding Amazon’s services. Key fields include:

- **age**: Age of the consumer.
- **gender**: Gender of the consumer.
- **Purchase Frequency**: How often customers purchase from Amazon.
- **Purchase Categories**: Types of product categories typically purchased by consumers.
- **Purchased Based on Recommendations**: Whether the customer made purchases based on Amazon's product recommendations.
- **Browsing Frequency**: How often customers browse Amazon’s site or app.
- **Service Appreciation**: Aspects of Amazon’s services that are most appreciated by customers.
- **Improvement Areas**: Areas where customers feel Amazon could improve.
- **Shopping Satisfaction**: A score indicating overall customer satisfaction with Amazon.
- **Timestamp**: The date and time of customer interactions.

### Key Fields Used in Visuals:
- **Demographics**: Age, Gender
- **Interaction**: Purchase Frequency, Browsing Frequency, Product Search Method
- **Feedback**: Customer Reviews Importance, Review Helpfulness, Service Appreciation, Improvement Areas

## Dashboard Design Guide

### How to Access the Dashboard
The Tableau dashboard is published on [Tableau Public](https://public.tableau.com/app/profile/parsa.bahrami/viz/AmazonE-commerceCustomerBehaviour/Dashboard2?publish=yes).

**Here’s what the current dashboard looks like**:

![image](https://github.com/user-attachments/assets/299bbb93-0be9-4af2-a13b-f35976db7e63)


---

## Main KPIs
- **Total Number of Consumers**: Total number of unique customers in the dataset.
- **Average Age**: Displays the average age of customers.
- **Shopping Satisfaction**: An average score based on feedback about shopping experiences.
- **Product Recommendations Accuracy**: The accuracy of personalized recommendations, as perceived by customers.

---

## Visuals Included:
1. **Customer Demographics Breakdown**: Segmented bar chart showing customer distribution by age and gender.
2. **Purchase Frequency Heatmap**: Color-coded matrix showing customer purchase frequency against browsing frequency.
3. **Purchase Trends Over Time**: A line graph showing customer purchase trends over time (using the timestamp data).
4. **Top Areas for Improvement**: Horizontal bar chart showing areas customers feel Amazon can improve.


---

## Key Insights

- **Customer Segmentation**: The majority of customers fall in the 18-35 age range, with males representing a slightly larger portion.
- **Purchase Trends**: Purchases peak around mid-year, suggesting seasonal shopping patterns.
- **Areas for Improvement**: Customers indicate that product quality and customer service responsiveness are key areas for improvement.
- **Most Appreciated Services**: Amazon's competitive prices and product recommendations are highly valued by consumers.

---

## Conclusion

The Amazon E-commerce Customer Behaviour Dashboard effectively uses data visualization to analyze customer behavior and feedback. The project demonstrates how businesses like Amazon can extract valuable insights from customer data, allowing them to refine their marketing strategies and improve customer satisfaction.





