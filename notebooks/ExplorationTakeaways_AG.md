- Ventura is a quarter of LA and OC is half of LA
- longitude shouldn't be negative?
    - bulk on the right
- lot size thrown off by outliers
- home_value med = $ 355_758
- land_value has a similar distribution to home_value, but priced lesser
- home_age is almost normally distributed.


feature engineer:
- lotsizexsqft clusters, k=6
    - smlot_smhome
    - smlot_avghome
    - smlot_lghome
    - mdlot
    - lglot
    - xllot

    -name the clusters (replace)
    - create dummies
    - 
- home_agexsqft clusters, k=6
    - young_smhome
    - middleaged_smhome
    - old_smhome
    - young_avghome
    - veteran_avghome
    - lghome
    
There is a relationship between home_age and logerror 
There is a relationship between lotsize and logerror
There is a relationship between home_value and logerror
