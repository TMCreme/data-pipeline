# Data Pipeline to analyse Price Information of an online shop

## Introduction
This idea of this project is build a data pipeline from scrapping data from online shops (especially price data) up to analysing (inflation) and presenting the visualisation. 

## Technologies
* Python (BeautifulSoup, requests, boto3)
* AWS (Lambda, S3, EC2, Glue)
* Databricks (delta lake)

## Content
Only crawler1.py is complete for now. 
This file crawls from jumia's website(https://www.jumia.com.gh) twice daily. This web scraping logic howbeit general is specifically tailored to how the https://www.jumia.com.gh website handles their routing. 
The script also does an initial cleaning to load the data into a json file and drop on S3. 
The category data is stored in a dictionary with the format {"name":"link/href"}
The category data dictionary will be used to get the various products. Since the routing 
doesn't consider the sub-categories, I will be not use the sub categories because 
I will get the products when I use the category pages.
Using the category links, the product data will be taken and parsed into a CSV to be stored on AWS S3 


Other online shops will be included later. 






