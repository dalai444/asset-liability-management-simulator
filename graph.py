import matplotlib.pyplot as plt

# Creates a histogram using matplotlib.pyplot to visualizing the different surpluses generated in our scenarios
def visualizing_data(surpluses):
    plt.figure(figsize=(10,6))
    plt.hist(surpluses, bins=20, edgecolor='black', color='skyblue')
    plt.axvline(x=0, color='red', linestyle='--', label='Break-even Surplus')
    plt.title("Distribution of Surplus Across 500 Scenarios")
    plt.xlabel("Surplus ($)")
    plt.ylabel("Frequency")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.show()