# asset-liability-management-simulator

This project is a Stochastic Asset Liability Management simulator designed to model how an insurance company manages its bond portfolio to meet long-term liabilities (e.g., annuity payouts) under varying interest rate scenarios. It aims to test whether a portfolio of bonds can adequately fund scheduled liabilities across hundreds of simulated interest rate paths that vary using a Normal (Guassian) Distribution.

Key Features:
    - Simulates 500 stochastic interest rate paths using a basic Economic Scenario Generator (ESG)
    - Calculates the present value (pv) of asset and liability cash flows under each scenario
    - Calculates surpluses created for each different scenario based on the incoming and outgoing cashflows
    - Generates a histogram to help visualize surplus distributions across the 500 different interest rate paths
    - Uses a SQL database to store and manage the bond portfolio

Project Structure:

ALM.py:
    - Main driver of the simulator. Pulls everything together: generates liabilities, pulls bonds from database, runs simulations, computes present values and surpluses, and         visualizes results.
asset.py:
    - Generates the projected cash flow for each bond based on coupon, face value, and maturity
bond.py:
    - Defines the Bond class used throughout the project
db.py:
    - Sets up the SQL database using SQLite3 (a python package). Inserts bond data, retrieves that same bond data and stores it in an array of Bond objects.
esg.py:
    - Generates varying stochastic interest rates using a Normal (Guassian) Distribution, based on an originally flat rate of 3%
graph.py:
    - Uses matplotlib.pyplot to generate a histogram to visualize surplus data

1. **Database Setup**:
   - Initializes an SQLite database (`alm.db`) and populates it with sample bond data.

2. **Bond Portfolio**:
   - Bonds are pulled from the database and turned into cash flows using coupon and face value.

3. **Liability Modeling**:
   - A level liability payment stream (e.g., $15,000 annually for 20 years) is generated.

4. **ESG (Stochastic Interest Rates)**:
   - 500 paths of interest rates are generated with randomness (mean = 3%, std dev = 3%).

5. **Present Value Calculation**:
   - For each scenario, the present value of liabilities and assets is calculated using the stochastic rates.

6. **Surplus Evaluation**:
   - The simulator calculates the surplus (PV assets − PV liabilities) under each scenario.

7. **Visualization**:
   - A histogram shows the distribution of surplus across all interest rate paths, highlighting risk.



- <img width="1732" height="1250" alt="image" src="https://github.com/user-attachments/assets/f00bbf42-6949-4f14-b0a7-8b4131530688" />
