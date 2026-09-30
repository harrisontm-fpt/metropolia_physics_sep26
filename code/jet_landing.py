import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# --------------------------------------------------
# Initial conditions
# --------------------------------------------------

# Initial velocity: 270 km/h converted to m/s
v0 = 270 * 1000 / 3600

# Constant acceleration
a = -4.5  # m/s^2


# --------------------------------------------------
# Velocity function
# --------------------------------------------------

def velocity(t):
    return v0 + a * t


# --------------------------------------------------
# Calculate stopping time
# --------------------------------------------------

# v = v0 + at
# At stopping point, v = 0

stopping_time = -v0 / a

print(f"Initial velocity: {v0:.2f} m/s")
print(f"Stopping time: {stopping_time:.2f} s")


# --------------------------------------------------
# Use SciPy to calculate area under velocity graph
# --------------------------------------------------

distance, error = quad(velocity, 0, stopping_time)

print(f"Stopping distance: {distance:.2f} m")


# --------------------------------------------------
# Generate values for plotting
# --------------------------------------------------

times = np.linspace(0, stopping_time, 200)

velocities = velocity(times)


# --------------------------------------------------
# Create graph
# --------------------------------------------------

plt.figure(figsize=(10, 6))

# Plot velocity
plt.plot(
    times,
    velocities,
    linewidth=2,
    label="Velocity"
)

# Shade the area under the graph
plt.fill_between(
    times,
    velocities,
    0,
    alpha=0.3,
    label=f"Distance = {distance:.0f} m"
)

# Mark start and stop
plt.scatter([0, stopping_time], [v0, 0])

plt.text(
    0,
    v0 + 3,
    f"{v0:.0f} m/s"
)

plt.text(
    stopping_time,
    5,
    f"{stopping_time:.2f} s",
    ha="right"
)

# Labels
plt.xlabel("Time (seconds)")
plt.ylabel("Velocity (m/s)")

plt.title("Jetliner Braking: Velocity vs Time")

plt.grid(True)
plt.legend()

plt.xlim(0, stopping_time + 1)
plt.ylim(0, v0 + 10)

plt.show()