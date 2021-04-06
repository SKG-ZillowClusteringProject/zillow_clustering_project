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
- The get_connection() function from wrangle module acquires zillow dataset from Codeup database using Sequel Pro.
- The zillow17() function creates a query that joins the 2017 properties and predictions data and filters data for single unit/single family homes.
- The original, unprepared data set has 77574 rows and 68 columns.
</div>

# Prepare
<b>Prepare Summary:</b> 
- <b>Dropped columns: </b> 
- 
</div>
# Explore 

# Model