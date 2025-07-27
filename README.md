# asset-liability-management-simulator

The goal of this project is to simulate whether a company’s assets (for this project we will use a bond portfolio) will consistently provide enough liquid cash to cover the company’s liabilities. We need to quantify the size and timing any time we are unable to cover the liabilities. The logic behind this project is what allows companies to ensure that their liabilities will be paid out regardless of changing interest rates. 

Assets will be found in either a CSV, Excel, or SQL database and contain information about the bond portfolio. Bond portfolio has been selected from actual bonds that New York Life is invested into.  

Liability payments are arbitrary and chosen to represent typical policy payments done by insurance companies.

Modeling will use stochastic methods to introduce randomness.

1. Calculating present day value of future cash flows
    - Future cash is worth less than present day cash due to inability to earn interest/reinvest over the years.
    - To calculate how much future cash is worth in the present day, we need to sum all of the future cash payments and apply a discount rate to each one.
    - We will be using an annual discount rate
        - r(t) = 
