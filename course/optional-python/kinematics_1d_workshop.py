"""WORKSHOP 2: 1D KINEMATICS | 60 minutes + 15-minute free-fall extension

Install once in your TERMINAL: python -m pip install matplotlib
Run: python kinematics_1d_workshop.py
Use py on Windows or python3 on macOS/Linux if needed.
This file stands alone; the conversion workshop is not required to run it.
Prerequisites: variables, functions, return, lists, loops, simple algebra.

Start at STAGE = 0; then work through 1, 2, 3 and optional 4.
Predict on PAPER before running. Complete TODOs and fix marked BUGs.
Tests show PASS, CHECK, or TODO; do not change expected answers.
Plotting code is supplied. PNGs save beside this file on every plotted run.
If no graph window appears, open the PNG; otherwise close it to continue.

MODEL: a point object moving on one straight line; CONSTANT acceleration.
All calculations use metres, seconds, m/s and m/s^2 internally.
Positive x is right for the cart; positive height is UP for the falling ball.
x0 = initial position; v0 = initial velocity; a = signed acceleration.
Time t is elapsed time from the start of the selected motion segment.
There is no air resistance in the free-fall model.
We evaluate exact equations at many times, not an Euler numerical simulation.
"""

from math import isclose, sqrt
from pathlib import Path
import matplotlib.pyplot as plt

STAGE = 0
SHOW_PLOTS = True


# STAGE 0 | 5 minutes | Run this supplied constant-velocity example.
# PAPER: a cart starts at x0 = 2 m, with v = +3 m/s. Find x at t = 4 s.
# Then explain why its displacement is NOT equal to its final position.
def constant_velocity_position(x0, velocity, t):
    return x0 + velocity * t


# STAGE 1 | 15 minutes | Complete the velocity function.
# PAPER: a cart starts with v0 = +2 m/s and a = +1 m/s^2.
# Fill a table for t = 0, 1, 2, 3 s before coding.
def velocity_at_time(v0, a, t):
    # TODO A: use v = v0 + a*t. Replace None with your expression.
    # Explain why (m/s^2) * s has the same units as v0.
    return None


# STAGE 2 | 20 minutes | Fix the position equation.
# PAPER: x0 = 0 m, v0 = 2 m/s, a = 1 m/s^2, t = 4 s.
# Find x and v. Sketch position-time, velocity-time, acceleration-time graphs.
def position_at_time(x0, v0, a, t):
    # BUG B: the acceleration term is missing something. Repair it.
    # Correct model: x = x0 + v0*t + (1/2)*a*t^2.
    # Python uses ** for powers, not ^. Multiplication must be explicit.
    return x0 + v0 * t + 0.5 * a * t


# After fixing: try a = 0, then a = -1 in the STAGE 2 settings below.
# Predict before each run. A negative acceleration does NOT always mean
# slowing down: compare the signs of v and a on each side of the turning point.
# This unconstrained cart model reverses when v becomes negative.


# STAGE 3 | 20 minutes | Bring a toy cart to rest.
# PAPER: v0 = +6 m/s, stopping time = 3 s. Find a and displacement.
def acceleration_to_stop(v0, stopping_time):
    # TODO C: rearrange v = v0 + a*t with final v = 0.
    # stopping_time must be positive. Keep the sign of acceleration.
    return None


# PAPER BREAK: now solve Physics Period1 Exer3 Q5 on the printed sheet.
# Convert km/h to m/s FIRST. Calculate a, then stopping displacement.
# Only after the handwritten solution, substitute those inputs into STAGE 3.
# The classroom model assumes constant deceleration beginning immediately.
# It is not real-world runway planning or stopping-distance advice.


# STAGE 4 | optional 15 minutes | A simulated ball dropped from rest.
def fall_time(height, g):
    # TODO D: for a drop from rest, solve height = (1/2)*g*t^2 for t.
    # Here height >= 0 and g > 0 is a MAGNITUDE, not signed acceleration.
    # Use sqrt(...). Return the nonnegative physical time.
    return None


# PAPER: drop from height 20 m with v0 = 0, upward positive, g = 9.81.
# What signs should height, velocity and acceleration have during the fall?
# Predict impact time and impact SPEED; speed = abs(velocity).
# Then complete Exer3 Q3 on paper (ignore sound travel time as instructed).
# This is a simulated drop only; no physical drop experiment is required.


# SUPPLIED INFRASTRUCTURE: no changes needed below except experiment settings.
def check(label, actual, expected):
    if actual is None:
        print(f"TODO: {label}: complete the function returning None.")
        return False
    passed = isclose(actual, expected, rel_tol=1e-9, abs_tol=1e-9)
    print(f"{'PASS' if passed else 'CHECK'}: {label}: {actual:.8g}"
          f" (expected {expected:.8g})")
    return passed


def times_up_to(duration):
    # 101 samples, including both t=0 and t=duration; avoids float-loop drift.
    times = []
    for i in range(101):
        times.append(duration * i / 100)
    return times


def finish_plot(fig):
    fig.tight_layout()
    path = Path(__file__).with_name(f"kinematics_stage_{STAGE}.png")
    fig.savefig(path, dpi=150)
    print(f"Graph saved: {path.name}")
    if SHOW_PLOTS:
        plt.show()
    plt.close(fig)


def plot_motion(x0, v0, a, duration, title, vertical=False):
    times = times_up_to(duration)
    positions, velocities, accelerations = [], [], []
    for t in times:
        positions.append(position_at_time(x0, v0, a, t))
        velocities.append(velocity_at_time(v0, a, t))
        accelerations.append(a)
    if None in positions or None in velocities:
        print("Complete velocity_at_time and position_at_time to plot motion.")
        return
    fig, axes = plt.subplots(3, 1, figsize=(9, 9), sharex=True)
    fig.suptitle(title + "\nYour model output: verify the printed checks")
    axes[0].plot(times, positions, color="tab:blue")
    axes[0].set_ylabel("Height (m)" if vertical else "Position (m)")
    axes[1].plot(times, velocities, color="tab:orange")
    axes[1].fill_between(times, velocities, 0, alpha=0.2, color="tab:orange")
    axes[1].set_ylabel("Velocity (m/s)")
    axes[2].plot(times, accelerations, color="tab:green")
    axes[2].set(ylabel="Acceleration (m/s²)", xlabel="Elapsed time (s)")
    for ax in axes:
        ax.axhline(0, color="black", linewidth=0.7)
        ax.grid(True, alpha=0.3)
    displacement = positions[-1] - positions[0]
    # This trapezium formula is exact when acceleration is constant.
    signed_area = 0.5 * (velocities[0] + velocities[-1]) * duration
    print(f"Final position = {positions[-1]:.6g} m")
    print(f"Final velocity = {velocities[-1]:.6g} m/s")
    print(f"Displacement = {displacement:.6g} m")
    print(f"Signed area under velocity graph = {signed_area:.6g} m")
    check("area equals displacement", signed_area, displacement)
    print("Shaded area below zero is NEGATIVE displacement, not negative distance.")
    finish_plot(fig)


def main():
    if STAGE == 0:
        times = times_up_to(4)
        positions = [constant_velocity_position(2, 3, t) for t in times]
        check("final position (m)", positions[-1], 14)
        check("displacement (m)", positions[-1] - positions[0], 12)
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(times, positions)
        ax.set(xlabel="Elapsed time (s)", ylabel="Position (m)",
               title="Constant velocity: read the slope, not the graph's height")
        ax.grid(True, alpha=0.3)
        finish_plot(fig)
    elif STAGE == 1:
        check("v(0)", velocity_at_time(2, 1, 0), 2)
        check("v(4)", velocity_at_time(2, 1, 4), 6)
        check("negative acceleration", velocity_at_time(6, -2, 3), 0)
        times = times_up_to(4)
        velocities = [velocity_at_time(2, 1, t) for t in times]
        if None in velocities:
            print("Finish TODO A to unlock the graph.")
            return
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(times, velocities, label="Your velocity function")
        ax.scatter([0, 4], [2, 6], marker="x", color="black",
                   label="Paper checkpoints")
        ax.set(xlabel="Elapsed time (s)", ylabel="Velocity (m/s)",
               title="The slope of this graph is acceleration")
        ax.grid(True, alpha=0.3)
        ax.legend()
        finish_plot(fig)
    elif STAGE == 2:
        check("x(0)", position_at_time(5, 2, 1, 0), 5)
        check("x(4)", position_at_time(0, 2, 1, 4), 16)
        check("zero acceleration", position_at_time(5, 2, 0, 4), 13)
        # EXPERIMENT SETTINGS: change ONE variable, predict, then rerun.
        x0, v0, a, duration = 0, 2, 1, 4
        plot_motion(x0, v0, a, duration, "Cart with constant acceleration")
    elif STAGE == 3:
        check("stopping acceleration", acceleration_to_stop(6, 3), -2)
        check("leftward cart", acceleration_to_stop(-6, 3), 2)
        # EXPERIMENT SETTINGS: these are SI units. For Exer3 Q5, change
        # initial_speed_kmh to 220 and stopping_time to 29 (seconds).
        initial_speed_kmh, stopping_time = 21.6, 3
        if stopping_time <= 0:
            print("Stopping time must be greater than zero.")
            return
        v0 = initial_speed_kmh / 3.6
        a = acceleration_to_stop(v0, stopping_time)
        if a is None:
            print("Complete TODO C before plotting.")
            return
        # Stop the model at rest. Extending the same negative a would make
        # the cart reverse; it would NOT model a cart that stays parked.
        plot_motion(0, v0, a, stopping_time, "Braking: model ends at rest")
    elif STAGE == 4:
        check("fall time: 4.905 m", fall_time(4.905, 9.81), 1)
        check("fall time: 19.62 m", fall_time(19.62, 9.81), 2)
        height, g = 20, 9.81  # Experiment settings: height >= 0, g > 0.
        if height < 0 or g <= 0:
            print("Use height >= 0 and g > 0.")
            return
        duration = fall_time(height, g)
        if duration is None:
            print("Complete TODO D before plotting.")
            return
        print(f"Predicted impact time = {duration:.6g} s")
        # Upward is positive, so acceleration = -g; final height should be 0.
        # Terminate at first ground contact: no underground continuation.
        plot_motion(height, 0, -g, duration, "Free fall: model ends at ground",
                    vertical=True)
    else:
        print("Choose STAGE = 0, 1, 2, 3, or 4.")


# EXIT TICKET (answer as comments, not just screenshots):
# 1. What do the slopes of the position-time and velocity-time graphs mean?
# 2. What does signed area under a velocity-time graph measure?
# 3. At a turning point, can velocity be zero while acceleration is nonzero?
# 4. Change stage 2 to a = -1. Find total distance AND displacement on paper.
# Submit the completed code, one labelled plot and your paper working.

if __name__ == "__main__":
    main()
