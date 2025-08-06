# asset-liability-management-simulator

This project is a Stochastic Asset Liability Management simulator designed to model how an insurance company manages its bond portfolio to meet long-term liabilities (e.g., annuity payouts) under varying interest rate scenarios. It aims to test whether a portfolio of bonds can adequately fund scheduled liabilities across hundreds of simulated interest rate paths that vary using a Normal (Guassian) Distribution.

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

---


- <img width="1732" height="1250" alt="image" src="https://github.com/user-attachments/assets/f00bbf42-6949-4f14-b0a7-8b4131530688" />
