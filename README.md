# Stochastic Asset Liability Management Simulator

This project is a Stochastic Asset Liability Management simulator designed to model how an insurance company manages its bond portfolio to meet long-term liabilities (e.g., annuity payouts) under varying interest rate scenarios. It aims to test whether a portfolio of bonds can adequately fund scheduled liabilities across hundreds of simulated interest rate paths that vary using a Normal (Guassian) Distribution.

This project integrates data from NAIC's Consumer Information Source to integrate real world data to the simulator. The real world data used is New York Life Ins & Ann Corp's 2024 Company Overview. From here we pull two key financials: total aggregate assets and liabilities. These values are $144,458,065,137 and $136,060,666,729 respectively.
- <img width="1732" height="1250" alt="image" src="https://github.com/user-attachments/assets/f00bbf42-6949-4f14-b0a7-8b4131530688" />
- https://content.naic.org/cis_refined_results.htm?TABLEAU=CIS_FINANCIAL&COCODE=91596&:refresh

 ## Key Features

- Simulates 500 stochastic interest rate paths using a basic Economic Scenario Generator (ESG)
- Calculates present value of asset and liability cash flows under each scenario
- Assesses surplus (assets minus liabilities) distribution over time
- Provides visual insight into risk via histogram of simulated outcomes
- Uses an SQLite database to manage bond portfolios dynamically

## Project Structure

| File             | Purpose |
|------------------|---------|
| `ALM.py`         | **Main driver** of the simulator. Pulls everything together: generates liabilities, pulls bonds from database, runs simulations, computes present values and surpluses, and visualizes results. |
| `asset.py`       | Generates cash flows for each bond based on coupon, face value, and maturity. |
| `bond.py`        | Defines the `Bond` class used throughout the project. |
| `db.py`          | Sets up the SQLite database, inserts sample bond data, and retrieves the bond portfolio as `Bond` objects. |
| `esg.py`         | Generates stochastic interest rate scenarios using a normal distribution. |
| `graph.py`       | Visualizes the surplus outcomes as a histogram. |

---

## Simulation Workflow

1. **Database Setup**:
   - Initializes an SQLite database (`alm.db`) and populates it with sample bond data based on the numbers from NYL.

2. **Bond Portfolio**:
   - Bonds are pulled from the database and turned into cash flows using coupon and face value.

3. **Liability Modeling**:
   - A level liability payment stream (based on the data from NYL) is generated.

4. **ESG (Stochastic Interest Rates)**:
   - 500 paths of interest rates are generated with randomness (mean = 3%, std dev = 3%).

5. **Present Value Calculation**:
   - For each scenario, the present value of liabilities and assets is calculated using the stochastic rates.

6. **Surplus Evaluation**:
   - The simulator calculates the surplus (PV assets − PV liabilities) under each scenario.

7. **Visualization**:
   - A histogram shows the distribution of surplus across all interest rate paths, highlighting risk.

---

## Output

 1. **Histogram of Surpluses**
    - <img width="1485" height="943" alt="image" src="https://github.com/user-attachments/assets/2b7087ad-b084-4183-97ed-f56ff43d7bb7" />

 2. **Arrays**
    - The simulator outputs 3 arrays: Liability Present Values, Asset Present Values, and the Surplus Distribution.
  3. **Negative Surpluses**
     - The last output is the count of all of the negative surpluses, or in other words the number of times that the bond portfolio's cash flows (incoming) were not enough to cover the liability cash flows (outgoing). 

     
## Limitations and Assumptions
1. This simulator uses the discount rate formula of DF = (1 + r)^-t. This formula is for a discrete annual compounding, when in reality continous or semi-annual compounding could be more viable options.
2. Interest rates are completely random, whereas in some situations a calculated interest rate would actually be more effective (CIR, Vasicek, or Hull-White).
3. I was unable to find any actual bond data to put into the simulator, so all values currenty chosen are arbitrary.
4. Bonds are assumed to compound annualy, whereas in reality they often compound more frequently.
5. This simulator does not account for reinvestment.
6. A single liability stream is not representitive of how real liabilities work at insurance companies.

---
The simulation can be reproduced by installing the relevant modules (numpy and matplotlib.pyplot) assuming a Python Environment is already set up. All that is needed is to fork the repository and run 'ALM.py'.
