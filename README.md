<span style="font-family:Futura; font-size:14pt">


<div style="text-align:center"><img src="zillowprojlogo.png"/></div>

___
<a id='navigation'></a>

<button type="button" class="btn btn-outline-primary">[Scenario](#scenario)</button>
<button type="button" class="btn btn-info">[Project Planning](#project-planning)</button>
<button type="button" class="btn btn-info">[Key Findings](#key-findings)</button>
<button type="button" class="btn btn-info">[Tested Hypotheses](#tested-hypotheses)</button>
<button type="button" class="btn btn-info">[Take Aways](#take-aways)</button>
<button type="button" class="btn btn-info">[Data Dictionary](#data-dictionary)</button>
<button type="button" class="btn btn-info">[Workflow](#workflow)</button>
___


<div class="alert alert-info" role="alert"><a name="scenario"></a><h1><i class="fas fa-home"></i> Scenario</h1></div>
Selling homes in our new normal has just gotten easier with Zillow Offers®. Now home owners can hand over the burden of selling their property, by selling directly to us based on our state of the art Zestimate score.

The accuracy and itegrity of our Zestimate score is of high importance. As a junior data scientists on the Zillow data science team, we are tasked with uncovering what drivers most affect the validity of the Zestimate score. This is measured by our target variable: `logerror`. Which is the difference between Zillow's estimated Zestimate and actual sale price. 
>`logerror` = log (Zestimate) − log (ActualSalePrice)


[Jump to Navigation](#navigation)

<div class="alert alert-info" role="alert"><a name="project-planning"></a><h1><i class="fab fa-trello"></i> Project Planning</h1></div>
    
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
<div class="alert alert-info" role="alert"><a name="key-findings"></a><h1><i class="fas fa-highlighter"></i> Key Findings</h1></div>




[Jump to Navigation](#navigation)
<div class="alert alert-info" role="alert"><a name="tested-hypotheses"></a><h1><i class="fas fa-hippo"></i> Tested Hypotheses</h1></div>




[Jump to Navigation](#navigation)
<div class="alert alert-info" role="alert"><a name="take-aways"></a><h1><i class="fas fa-tasks"></i> Take Aways</h1></div>
 
 
 

[Jump to Navigation](#navigation)
<div class="alert alert-info" role="alert"><a name="data-dictionary"></a><h1><i class="fas fa-book"></i> Data Dictionary</h1></div>
    
</span>
    
|                   column_name                   |                                                       description                                                       |                   key                  |       dtype      |
|:-----------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------:|:----------------:|
| `bathrooms` / `bathroomcnt`                     | Number of bathrooms in home including fractional bathrooms                                                              |                                        | float64          |
| `bedrooms` /  `bedroomcnt`                      | Number of bedrooms in home                                                                                              |                                        | float64          |
| `square_feet` / `calculatedfinishedsquarefeet`  | Calculated total finished living area of the home                                                                       |                                        | float64          |
| `fips`                                          | Federal Information Processing Standard code -  see https://en.wikipedia.org/wiki/FIPS_county_code for more details     |                                        | float64 /  int64 |
| `lotsizesquarefeet`                             | Area of the lot in square feet                                                                                          |                                        | float64          |
| `parcelid`                                      | Unique identifier for parcels (lots)                                                                                    |                                        | int64            |
| `yearbuilt`                                     | The Year the principal residence was built                                                                              |                                        | float64 /  int64 |
| `home_value` / `taxvaluedollarcnt`              | The total tax assessed value of the parcel                                                                              |                                        | float64          |
| `taxes` /  `taxamount`                          | The total property tax assessed for that assessment year                                                                |                                        | float64          |
| `county`                                        | The county the property is located.                                                                                     |                                        | object           |
| `state`                                         | The state the property is located.                                                                                      |                                        | object           |
| `bdrm_3`                                        | Identifies if property is a 3 bedroom home.                                                                             | 1: 3 bedroom home 0: not a 3 bdrm home | int64            |
| `tax_rates`                                     | Calculated tax rate = `taxes` / `home_value`                                                                            |                                        | float64          |


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