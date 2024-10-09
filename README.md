# Amazon E-commerce Customer Behavior Dashboard

## Background and Overview

The **Amazon E-commerce Customer Behavior Dashboard** is a data visualization project that analyzes customer interactions and behaviors within the Amazon ecosystem. The dataset includes customer demographics, purchase patterns, and feedback on service offerings. The goal is to provide actionable insights for e-commerce platforms like Amazon to optimize customer experience, marketing strategies, and overall service improvement.

For technical details on data preparation and dashboard design, please refer to:
- [Data Cleaning and Preparation](https://github.com/pbahrami2/Amazon-E-Commerce-Dashboard/blob/main/data_cleaning.py)
- Tableau Dashboard Design:
![image](https://github.com/user-attachments/assets/6d42739f-9e05-48b2-8fa0-42cfe2175bd9)


## Data Structure Overview

The dataset, sourced from [Amazon Consumer Behavior Dataset](https://www.kaggle.com/datasets/swathiunnikrishnan/amazon-consumer-behaviour-dataset), contains 24 fields, covering key customer interactions and feedback. The key fields include:

- **age**: Age of the customer.
- **gender**: Gender of the customer.
- **Purchase Frequency**: Frequency of purchases made by the customer.
- **Product Categories Purchased**: Types of products purchased.
- **Purchased Based on Recommendations**: Indicates if purchases were influenced by Amazon's recommendations.
- **Browsing Frequency**: How frequently the customer browses Amazon.
- **Service Appreciation**: Key aspects of Amazon’s services appreciated by customers.
- **Improvement Areas**: Areas where customers believe Amazon can improve.
- **Shopping Satisfaction**: A score reflecting the overall satisfaction of customers with Amazon's services.
- **Timestamp**: Date and time of customer interactions.

### Key Fields Used in Visuals:
- **Demographics**: Age, Gender
- **Customer Interaction**: Purchase Frequency, Browsing Frequency, Product Search Methods
- **Feedback**: Service Appreciation, Review Helpfulness, Improvement Areas, Shopping Satisfaction

## Executive Summary

This project analyzes Amazon's customer data using visualizations created in **Tableau**. The dashboard provides insights into key customer segments, purchasing trends, and feedback on services, allowing Amazon to optimize its engagement and marketing strategies. Key findings include:
- **Demographics**: The majority of Amazon customers are aged between 18-35, with males slightly outnumbering females.
- **Purchase Trends**: There is a clear peak in purchases around the mid-year, indicating seasonal shopping trends.
- **Feedback**: While customers appreciate Amazon’s competitive pricing and recommendations, product quality and customer service responsiveness remain areas for improvement.

These insights can help guide decision-making to improve customer satisfaction and sales performance.

## Insights Deep Dive

### 1. **Customer Demographics**
- **Metric**: Age and gender breakdown of Amazon customers.
- **Finding**: Customers aged 18-35 make up about 65% of the total base, with males accounting for roughly 52%.
- **Visualization**: Bar charts showing customer segmentation by age and gender, supporting targeted marketing strategies.

### 2. **Purchase Trends Over Time**
- **Metric**: Customer purchase frequency over time.
- **Finding**: Purchases peak during mid-year, indicating that seasonal campaigns should be emphasized during this period.
- **Visualization**: A line graph showing purchase frequency trends highlights key shopping seasons.

### 3. **Product Recommendation Accuracy**
- **Metric**: Accuracy of personalized product recommendations.
- **Finding**: The accuracy of Amazon’s recommendations is perceived to be 80%, indicating a positive but improvable experience for customers.
- **Visualization**: KPIs for recommendation accuracy, providing insight into the performance of the recommendation engine.

### 4. **Customer Feedback on Improvement Areas**
- **Metric**: Customer-suggested areas for improvement.
- **Finding**: Product quality and customer service are the most frequently mentioned areas for improvement, with 35% and 25% of feedback, respectively.
- **Visualization**: Bar chart showcasing the most mentioned improvement areas, helping Amazon identify where to focus its efforts.

## Recommendations

Based on the findings from this project, we recommend the following actions for Amazon to improve customer satisfaction and optimize its services:
- **Improve Product Quality**: Address customer concerns about product quality, especially in high-turnover product categories.
- **Enhance Customer Service**: Streamline customer service operations to resolve issues more quickly and effectively.
- **Refine Product Recommendations**: Improve the recommendation algorithm to increase accuracy and relevance, which could enhance the customer experience.
- **Leverage Seasonal Trends**: Use purchase trend insights to develop more targeted marketing campaigns during peak shopping seasons.

Implementing these recommendations can drive better customer retention, satisfaction, and ultimately, higher sales.

## Dashboard Design Guide

### How to Access the Dashboard
The Tableau dashboard can be accessed on [Tableau Public](https://public.tableau.com/app/profile/parsa.bahrami/viz/AmazonE-commerceCustomerBehaviour/Dashboard2?publish=yes).

### Main KPIs
- **Total Number of Consumers**: Total number of unique customers in the dataset.
- **Average Age**: Displays the average age of customers.
- **Shopping Satisfaction**: Average score reflecting customer satisfaction with their shopping experience.
- **Product Recommendation Accuracy**: Measures how accurately customers perceive product recommendations.

## Visuals Included:

1. **Customer Demographics Breakdown**: Bar chart showing age and gender distribution.
2. **Purchase Frequency Heatmap**: Color-coded heatmap showing the relationship between purchase and browsing frequency.
3. **Purchase Trends Over Time**: Line graph illustrating customer purchase patterns over time.
4. **Top Areas for Improvement**: Horizontal bar chart highlighting customer feedback on areas Amazon can improve.

## Conclusion

The **Amazon E-commerce Customer Behavior Dashboard** provides a comprehensive analysis of customer behavior, purchasing trends, and feedback. The insights gained can help e-commerce platforms like Amazon refine their services, enhance customer satisfaction, and develop more effective marketing strategies.

