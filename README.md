# asset-liability-management-simulator

The goal of this project is to simulate whether a company’s assets (for this project we will use a bond portfolio) will consistently provide enough liquid cash to cover the company’s liabilities. We need to quantify the size and timing any time we are unable to cover the liabilities. The logic behind this project is what allows companies to ensure that their liabilities will be paid out regardless of changing interest rates. 

Assets will be found in either a CSV, Excel, or SQL database and contain information about the bond portfolio. I would like to find actual bonds NYL is invested into and 





Liability payments are arbitrary and chosen to represent typical policy payments done by insurance companies.

Modeling will use stochastic methods to introduce randomness.

1. Calculating present day value of future cash flows
    - Future cash is worth less than present day cash due to inability to earn interest/reinvest over the years.
    - To calculate how much future cash is worth in the present day, we need to sum all of the future cash payments and apply a discount rate to each one.
    - We will be using an annual discount rate
        - r(t) = 


2. To get our assets (bond portfolio), the first step we take is going to https://content.naic.org/cis_consumer_information.htm and searching up New York Life Insurance.
    - Two options will appear, we chose the first one (company code 91596) since they handle the bulk of bond portfolios.
    - For each bond we need the following values:
        - name
        - principal (face)
        - coupon
        - frequency
        - maturity
    - This project creates the SQL database using Python's built in sqlite3 module
    - Values are then pulled out of this database and stored in a array for other uses


3. Our simulation is stochastic as it generates random noise using a Normal (Gauss) Distribution and adds it to our flat interest rate. This creates different possible scenarios of different interest rates for different   years.

4. Limitations of this project:
    - We do not calculate for reinvestment of cash earned through our bond portfolio


    - <img width="1732" height="1250" alt="image" src="https://github.com/user-attachments/assets/f00bbf42-6949-4f14-b0a7-8b4131530688" />
