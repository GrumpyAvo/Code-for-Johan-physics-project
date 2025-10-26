import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Data from tables
lengths_cm = np.array([10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0])
total_times = np.array([7.5, 9.8, 11.1, 12.2, 14.6, 14.4, 15.6, 16.3])
total_time_uncertainties = np.array([0.27, 0.10, 0.10, 0.05, 0.10, 0.10, 0.11, 0.50])

# Calculated data
periods = np.array([0.75, 0.98, 1.11, 1.22, 1.46, 1.44, 1.56, 1.63])
T_squared = np.array([0.56, 0.96, 1.23, 1.49, 2.13, 2.07, 2.43, 2.66])

# Calculate uncertainties for periods and T²
period_uncertainties = total_time_uncertainties / 10
T_squared_uncertainties = 2 * periods * period_uncertainties

# GRAPH 1: T² vs L
plt.figure(figsize=(10, 6))
slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(lengths_cm, T_squared)
x_fit1 = np.linspace(5, 50, 100)
y_fit1 = intercept1 + slope1 * x_fit1

plt.errorbar(lengths_cm, T_squared, yerr=T_squared_uncertainties, fmt='o', 
             capsize=5, capthick=2, markersize=8, color='blue', alpha=0.7)
plt.plot(x_fit1, y_fit1, 'r-', linewidth=2.5, label=f'T² = {intercept1:.3f} + {slope1:.3f}L')

plt.xlabel('Pendulum Length L (cm)', fontsize=12, fontweight='bold')
plt.ylabel('T² (s²)', fontsize=12, fontweight='bold')
plt.title('T² vs Pendulum Length', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend()

# Add results box
results_text = f'Regression: T² = {intercept1:.3f} + {slope1:.3f}L\nR² = {r_value1**2:.4f}'
plt.text(0.05, 0.95, results_text, transform=plt.gca().transAxes, fontsize=11,
         bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.8), verticalalignment='top')

plt.xlim(5, 50)
plt.ylim(0, 3.0)
plt.tight_layout()
plt.show()

# GRAPH 2: Total Time vs L
plt.figure(figsize=(10, 6))
slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(lengths_cm, total_times)
x_fit2 = np.linspace(5, 50, 100)
y_fit2 = intercept2 + slope2 * x_fit2

plt.errorbar(lengths_cm, total_times, yerr=total_time_uncertainties, fmt='s', 
             capsize=5, capthick=2, markersize=8, color='green', alpha=0.7)
plt.plot(x_fit2, y_fit2, 'r-', linewidth=2.5, label=f't = {intercept2:.2f} + {slope2:.2f}L')

plt.xlabel('Pendulum Length L (cm)', fontsize=12, fontweight='bold')
plt.ylabel('Total Time for 10 Oscillations (s)', fontsize=12, fontweight='bold')
plt.title('Total Time vs Pendulum Length', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend()

results_text = f'Regression: t = {intercept2:.2f} + {slope2:.2f}L\nR² = {r_value2**2:.4f}'
plt.text(0.05, 0.95, results_text, transform=plt.gca().transAxes, fontsize=11,
         bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.8), verticalalignment='top')

plt.xlim(5, 50)
plt.ylim(6, 18)
plt.tight_layout()
plt.show()

# GRAPH 3: L vs T (Single Period)
plt.figure(figsize=(10, 6))
slope3, intercept3, r_value3, p_value3, std_err3 = stats.linregress(periods, lengths_cm)
x_fit3 = np.linspace(0.7, 1.7, 100)
y_fit3 = intercept3 + slope3 * x_fit3

plt.errorbar(periods, lengths_cm, xerr=period_uncertainties, fmt='^', 
             capsize=5, capthick=2, markersize=8, color='purple', alpha=0.7)
plt.plot(x_fit3, y_fit3, 'r-', linewidth=2.5, label=f'L = {intercept3:.1f} + {slope3:.1f}T')

plt.xlabel('Period T (s)', fontsize=12, fontweight='bold')
plt.ylabel('Length L (cm)', fontsize=12, fontweight='bold')
plt.title('Pendulum Length vs Period', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend()

results_text = f'Regression: L = {intercept3:.1f} + {slope3:.1f}T\nR² = {r_value3**2:.4f}'
plt.text(0.05, 0.95, results_text, transform=plt.gca().transAxes, fontsize=11,
         bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.8), verticalalignment='top')

plt.xlim(0.7, 1.7)
plt.ylim(0, 50)
plt.tight_layout()
plt.show()

# Print regression results and uncertainty calculations
print("REGRESSION RESULTS:")
print("=" * 70)
print("GRAPH 1: T² vs L")
print(f"Regression: T² = {intercept1:.4f} + {slope1:.4f}L")
print(f"R² = {r_value1**2:.4f}")
print(f"Slope in m units: {slope1/100:.6f} s²/m")
g_experimental = (4 * np.pi**2) / (slope1/100)
print(f"Experimental g = {g_experimental:.3f} m/s²")

print("\nGRAPH 2: Total Time vs L")
print(f"Regression: Total Time = {intercept2:.3f} + {slope2:.3f}L")
print(f"R² = {r_value2**2:.4f}")

print("\nGRAPH 3: L vs T")
print(f"Regression: L = {intercept3:.2f} + {slope3:.2f}T")
print(f"R² = {r_value3**2:.4f}")

# Print uncertainty table
print("\n" + "=" * 70)
print("UNCERTAINTY CALCULATIONS:")
print(f"{'Length (cm)':<12} {'Δt_total (s)':<15} {'ΔT (s)':<10} {'ΔT² (s²)':<12} {'Calculation'}")
print("-" * 70)
for i in range(len(lengths_cm)):
    calculation = f"2 × {periods[i]:.2f} × {period_uncertainties[i]:.3f}"
    print(f"{lengths_cm[i]:<12.1f} {total_time_uncertainties[i]:<15.2f} {period_uncertainties[i]:<10.3f} {T_squared_uncertainties[i]:<12.4f} {calculation}")