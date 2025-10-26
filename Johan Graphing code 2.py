import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Data from your tables
lengths_cm = np.array([10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0])
T_squared = np.array([0.56, 0.96, 1.23, 1.49, 2.13, 2.07, 2.43, 2.66])
total_time_uncertainties = np.array([0.27, 0.10, 0.10, 0.05, 0.10, 0.10, 0.11, 0.50])

# Calculate uncertainties for T²
periods = np.array([0.75, 0.98, 1.11, 1.22, 1.46, 1.44, 1.56, 1.63])
period_uncertainties = total_time_uncertainties / 10
T_squared_uncertainties = 2 * periods * period_uncertainties

# Linear regression for L vs T²
slope, intercept, r_value, p_value, std_err = stats.linregress(T_squared, lengths_cm)

plt.figure(figsize=(10, 6))

# Plot L vs T² with error bars on T²
plt.errorbar(T_squared, lengths_cm, xerr=T_squared_uncertainties, fmt='o', 
             capsize=5, capthick=2, markersize=8, color='red', alpha=0.7)

# Regression line
x_fit = np.linspace(0, 3.0, 100)
y_fit = intercept + slope * x_fit
plt.plot(x_fit, y_fit, 'b-', linewidth=2.5, label=f'L = {intercept:.2f} + {slope:.2f}T²')

plt.xlabel('T² (s²)', fontsize=12, fontweight='bold')
plt.ylabel('Length L (cm)', fontsize=12, fontweight='bold')
plt.title('Pendulum Length vs T²', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend()

# Results box
results_text = f'Regression: L = {intercept:.2f} + {slope:.2f}T²\nR² = {r_value**2:.4f}\nSlope = {slope:.2f} cm/s²\n '
plt.text(0.05, 0.95, results_text, transform=plt.gca().transAxes, fontsize=11,
         bbox=dict(boxstyle="round", facecolor="lightblue", alpha=0.8), verticalalignment='top')

plt.xlim(0, 3.0)
plt.ylim(0, 50)
plt.tight_layout()
plt.show()

# Print detailed results
print("L vs T² ANALYSIS:")
print("=" * 60)
print(f"Regression: L = {intercept:.3f} + {slope:.3f}T²")
print(f"R² = {r_value**2:.6f}")
print(f"Slope = {slope:.3f} cm/s²")
print(f"Slope in m units = {slope_m:.6f} m/s²")
print(f"Accepted g = 9.810 m/s²")

print("\nData Points:")
print(f"{'T² (s²)':<10} {'L (cm)':<10} {'Uncertainty in T²':<20}")
for i in range(len(T_squared)):
    print(f"{T_squared[i]:<10.2f} {lengths_cm[i]:<10.1f} {T_squared_uncertainties[i]:<20.4f}")

# What your data should look like if it perfectly followed T² ∝ L
ideal_periods = 2 * np.pi * np.sqrt(lengths_cm/100 / 9.81)  # Using L in meters

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Your actual data
ax1.plot(periods, lengths_cm, 'ro-', markersize=8, linewidth=2, label='Your Actual Data')
ax1.plot(ideal_periods, lengths_cm, 'bo--', markersize=6, linewidth=2, label='Ideal Data (if perfect)')
ax1.set_xlabel('Period T (s)')
ax1.set_ylabel('Length L (cm)')
ax1.set_title('Your Data vs Ideal Theoretical Data')
ax1.legend()
ax1.grid(True, alpha=0.3)

# The curvature difference
ax2.plot(ideal_periods, lengths_cm, 'bo-', markersize=8, linewidth=2, label='Ideal: Clear Curve')
ax2.set_xlabel('Period T (s)')
ax2.set_ylabel('Length L (cm)')
ax2.set_title('How It Should Look (Clear Curve)')
ax2.grid(True, alpha=0.3)

# Add theoretical curve
T_smooth = np.linspace(0.6, 1.7, 100)
L_smooth = (9.81 / (4 * np.pi**2)) * T_smooth**2 * 100
ax2.plot(T_smooth, L_smooth, 'g--', linewidth=2, label='Perfect Theory', alpha=0.7)
ax2.legend()

plt.tight_layout()
plt.show()
