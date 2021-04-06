<div style="text-align:center"><img src="https://i.pinimg.com/originals/ba/d8/f6/bad8f6b66a410c907e62cca823eea463.png"/></div>

___

<a id='navigation'></a>

[[Scenario](#scenario)]
[[Project Planning](#project-planning)]
[[Key Findings](#key-findings)]
[[Tested Hypotheses](#tested-hypotheses)]
[[Take Aways](#take-aways)]
[[Data Dictionary](#data-dictionary)]
[[Workflow](#workflow)]

___

<a name="scenario"></a><h1><img src="https://i.pinimg.com/originals/cd/51/c7/cd51c7eb324f7092a391c2e6a9e08b2b.png"/></h1>

Selling homes in our new normal has just gotten easier with Zillow Offers®. Now home owners can hand over the burden of selling their property, by selling directly to us based on our state of the art Zestimate score.

The accuracy and itegrity of our Zestimate score is of high importance. As a junior data scientists on the Zillow data science team, we are tasked with uncovering what drivers most affect the validity of the Zestimate score. This is measured by our target variable: `logerror`. Which is the difference between Zillow's estimated Zestimate and actual sale price. 
>`logerror` = log (Zestimate) − log (ActualSalePrice)


[Jump to Navigation](#navigation)

<a name="project-planning"></a><h1><img src="https://i.pinimg.com/originals/08/5a/eb/085aeb8e6c5addd4114c7ecc12166145.png"/></h1>

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

<a name="key-findings"></a><h1><img src="https://i.pinimg.com/originals/82/02/e8/8202e8d3a1cfda0a8d828ea688b6b36e.png"/></h1>


[Jump to Navigation](#navigation)

<a name="tested-hypotheses"></a><h1><img src="https://i.pinimg.com/originals/f8/6c/1f/f86c1fc26068ad184455e11c7c5858cc.png"/></h1>

    
[Jump to Navigation](#navigation)

<a name="take-aways"></a><h1><img src="https://i.pinimg.com/originals/0b/24/91/0b2491f3c35b30155defee2f5ee6c3c3.png"/></h1>


[Jump to Navigation](#navigation)

<a name="data-dictionary"></a><h1><img src="https://i.pinimg.com/originals/2f/d4/c1/2fd4c1a67997f7c7c32b556aefd7ce1a.png"/></h1>

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

    
[Jump to Navigation](#navigation)

<a name="workflow"></a><h1><img src="wbar.png"/></h1>

    
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












































