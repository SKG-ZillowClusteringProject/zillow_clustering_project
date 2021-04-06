# Summaries for each phase of the pipeline
# Table of Contents:
#### Amanda anchor link queen will fix this part -> anchor links to copy and assign in notebook: <a id="id"></a>
[Acquire](#id)Acquire - Use acquire module to grab the data

[Prepare](#id)Prepare - Use prepare module to clean the data

[Explore](#id)Explore - Summarize key findings from explore

[Modeling](#id)Modeling - Creating 4 models to predict log error and determining the best performing one

[Conclusions](#id)Conclusions - Reasons for log error, best model to predict log error

# Plan
- Trello board link
- google docs link
## Background
#### The Zillow Data Science team wants us to uncover the drivers of the error in the Zestimate.  
> "The Zestimate® home valuation model is Zillow’s estimate of a home’s market value. The Zestimate incorporates public and user-submitted data, taking into account home facts, location and market conditions." [zillow.com]
## Goals
#### The goals of the project are to answer the following question and deliver the following products:
1. What features are driving the error in the zestimate?
2. Deliver a github repository with the following contents:
    A. Final notebook
    B. README.md
    C. Python modules
# Acquire
<div class="alert alert-block alert-success">
<b>Acquire Summary:</b> 
<br>- The get_connection() function from wrangle module acquires zillow dataset from Codeup database using Sequel Pro.
<br>- The zillow17() function creates a query that joins the 2017 properties and predictions data and filters data for single unit/single family homes.
<br>- The original, unprepared data set has 77574 rows and 68 columns.
</div>

# Prepare
<div class="alert alert-block alert-success">
<b>Prepare Summary:</b> 
<br>-  <b>Dropped: </b> <br>
- 45 columns and 4323 rows</b> 
<br>- <b>Why drop ?! </b> 
<br>We dropped columns that had > 60% of nulls and dropped rows that had 70% of nulls because we could not gather the missing information from other variables or impute the missing values without high skew.  We also dropped columns that contained redundant information and dropped columns that contained information we would not be using in our models.
<br>- <b>Outliers: </b> <br>
- We handled outliers in taxvaluedollarcnt by dropping values > $5 million
<br>- We handled outliers in calculatedfinishedsquarefeet by dropping values < 500 sqft and > 12500 sqft
<br>- <b>Remaining missing values:</b> <br>
- lotsizesquarefeet missing values were filled with median
<br>- buildingqualitytypeid missing values were filled with median
<br>- remaining missing values were dropped
<br>- <b>Renamed columns: </b> <br>
- 9 columns renamed to accurately represent the data they contain.
<br>- Ex). calculatedfinishedsquarefeet to sqft 
<br>- <b>New features: </b> <br>
- home_age, county, logerror_quartiles
</div>

# Explore 

# Model