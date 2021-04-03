<span style="font-family:Futura; font-size:14pt">


<div style="text-align:center"><img src="zillowprojlogo.png"/></div>

___
<a id='navigation'></a>

<button class="button-save large">[Scenario](#scenario)</button>
<button class="button-save large">[Project Planning](#project-planning)</button>
<button class="button-save large">[Key Findings](#key-findings)</button>
<button class="button-save large">[Tested Hypotheses](#tested-hypotheses)</button>
<button class="button-save large">[Take Aways](#take-aways)</button>
<button class="button-save large">[Data Dictionary](#data-dictionary)</button>
<button class="button-save large">[Workflow](#workflow)</button>
___
    
    
<div class="alert alert-block alert-info"><a name="scenario"></a><h1><i class="fas fa-home"></i> Scenario</h1></div>
Selling homes in our new normal has just gotten easier with Zillow Offers®. Now home owners can hand over the burden of selling their property, by selling directly to us based on our state of the art Zestimate score.

The accuracy and itegrity of our Zestimate score is of high importance. As a junior data scientists on the Zillow data science team, we are tasked with uncovering what drivers most affect the validity of the Zestimate score. This is measured by our target variable: `logerror`. Which is the difference between Zillow's estimated Zestimate and actual sale price. 
>`logerror` = log (Zestimate) − log (ActualSalePrice)


[Jump to Navigation](#navigation)

<div class="alert alert-block alert-info"><a name="project-planning"></a><h1><i class="fab fa-trello"></i> Project Planning</h1></div>
    
### Goal: 
The goal for this project is to create a model that will accurately predict the Zestimate’s `logerror`. By doing so, we will uncover what features available on the Zillow Dataset are driving the amount of error.

### Initial Hypotheses:

> Hypothesis₁
>
> There is a relationship between `home_age` and `logerror`.

<details>
  <summary>Click to see full list. </summary>
    
> Hypothesis₂
>
> There is a relationship between `lot_sqft` and `logerror`.
    
> Hypothesis₃
>
> There is a relationship between `home_value` and `logerror`.
    
> Hypothesis₄
>
> There is a relationship between `zip_code` and `logerror`.
    
> Hypothesis₅
>
> There is a relationship between `sqft` and `logerror`.
    
> Hypothesis₆
>
> There is a relationship between `` and `logerror`.
    
> Hypothesis₇
>
> There is a relationship between `` and `logerror`.
</details>
    
    
[Jump to Navigation](#navigation)
<div class="alert alert-block alert-info"><a name="key-findings"></a><h1><i class="fas fa-highlighter"></i> Key Findings</h1></div>




[Jump to Navigation](#navigation)
<div class="alert alert-block alert-info"><a name="tested-hypotheses"></a><h1><i class="fas fa-hippo"></i> Tested Hypotheses</h1></div>




[Jump to Navigation](#navigation)
<div class="alert alert-block alert-info"><a name="take-aways"></a><h1><i class="fas fa-tasks"></i> Take Aways</h1></div>
 
 
 

[Jump to Navigation](#navigation)
<div class="alert alert-block alert-info"><a name="data-dictionary"></a><h1><i class="fas fa-book"></i> Data Dictionary</h1></div>
    
</span>

| column_name              | description                                                                                                         | key | dtype    |
|--------------------------|---------------------------------------------------------------------------------------------------------------------|-----|----------|
| `parcelid`               | Unique identifier for parcels (lots)                                                                                |     | int64    |
| `bathrooms`              | Number of bathrooms in home including fractional bathrooms                                                          |     | float64  |
| `bedrooms`               | Number of bedrooms in home                                                                                          |     | int64    |
| `property_quality`       | Overall assessment of condition of the building from best (lowest) to worst (highest)                               |     | int64    |
| `sqft`                   | Calculated total finished living area of the home                                                                   |     | float64  |
| `fips`                   | Federal Information Processing Standard code -  see https://en.wikipedia.org/wiki/FIPS_county_code for more details |     | int64    |
| `latitude`               | Latitude of the middle of the parcel multiplied by 10e6                                                             |     | float64  |
| `longitude`              | Longitude of the middle of the parcel multiplied by 10e6                                                            |     | float64  |
| `lot_sqft`               | Area of the lot in square feet                                                                                      |     | float64  |
| `rawcensustractandblock` | Census tract and block ID combined - also contains blockgroup assignment by extension                               |     | float64  |
| `regionidcity`           | City in which the property is located (if any)                                                                      |     | float64  |
| `regionidcounty`         | County in which the property is located                                                                             |     | int64    |
| `zip_code`               | Zip code in which the property is located                                                                           |     | int64    |
| `roomcnt`                | Total number of rooms in the principal residence                                                                    |     | int64    |
| `unitcnt`                | Number of units the structure is built into (i.e. 2 = duplex, 3 = triplex, etc...)                                  |     | int64    |
| `yearbuilt`              | The Year the principal residence was built                                                                          |     | int64    |
| `structure_value`        | The assessed value of the built structure on the parcel                                                             |     | float64  |
| `home_value`             | The total tax assessed value of the parcel                                                                          |     | float64  |
| `assessmentyear`         | The year of the property tax assessment                                                                             |     | int64    |
| `land_value`             | The assessed value of the land area of the parcel                                                                   |     | float64  |
| `taxamount`              | The total property tax assessed for that assessment year                                                            |     | float64  |
| `logerror`               | The log of the difference between Zestimate value and actual sale price.                                            |     | float64  |
| `transactiondate`        | Date property sold.                                                                                                 |     | object   |
| `county`                 | The county the property is located.                                                                                 |     | object   |
| `home_age`               | The current age in years of the home.                                                                               |     | int64    |
| `logerror_quartiles`     | `logerror` distributed into 4 bins.                                                                                 |     | category |
|                          |                                                                                                                     |     |          |
|                          |                                                                                                                     |     |          |
|                          |                                                                                                                     |     |          |
|                          |                                                                                                                     |     |          |

<span style="font-family:Futura; font-size:14pt">
    
[Jump to Navigation](#navigation)

<div class="alert alert-info" role="alert"><h1><i class="fas fa-project-diagram"><a name="workflow"></a></i> Workflow</h1></div>

    
Please pull the repo first to use the following links to guide you through the data science pipeline. Enjoy!

1. [Prep Your Repo](#prep-your-repo)
1. [Import](#import)
1. [Acquire Data](#acquire-data)
1. [Clean, Prep & Split Data](#clean-prep-and-split-data)
1. [Explore Data](#explore-data)
    - [Hypothesis Testing](#hypothesis-testing)
1. [Evaluate Data](#evaluate-data)
1. [Modeling](#modeling)
    - [Identify Baseline](#identify-baseline)
    - [Train / Validate](#train-validate)
    - [Test](#test)



[Jump to Navigation](#navigation)














</span>


- I must also recover the following features:
    - the state and county information for all of the properties
    - distribution of tax rates for each county
        - tax amounts and tax value of the home





<div class="alert alert-success" role="alert">
  <h4 class="alert-heading">Well done!</h4>
  <p>Aww yeah, you successfully read this important alert message. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.</p>
  <hr>
  <p class="mb-0">Whenever you need to, be sure to use margin utilities to keep things nice and tidy.</p>
</div>

<div class="alert alert-warning alert-dismissible fade show" role="alert">
  <strong>Holy guacamole!</strong> You should check in on some of those fields below.
  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
</div>