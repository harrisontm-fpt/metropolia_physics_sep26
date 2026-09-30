"""WORKSHOP 1: UNITS AND CONVERSION | approximately 50 minutes

You need: variables, functions, return, lists, and a for loop.
Install once in your TERMINAL (not inside this file):
    python -m pip install matplotlib
Run: python conversion_workshop.py
On Windows you may use py instead of python; on macOS/Linux use python3.

WORKFLOW: predict on paper -> edit one TODO/BUG -> run -> explain the plot.
Start at STAGE = 0. Then change it to 1, 2, and 3 in order.
Stage 0 is a working demonstration. Later stages are intentionally incomplete.
Do not remove checks or change their expected answers to make them pass!
The plotting helpers are supplied: concentrate on the physics functions.
Every run saves a PNG next to this script, then opens a graph window.
If no window appears, open the PNG. Close the window before running again.

Connection to your printed Physics Period1 Exer1 sheet:
stage 1 -> Q5 and Q8; stage 2 -> Q1 and Q2; stage 3 -> Q6.
These are companion activities, not replacements for handwritten solutions.
"""

from math import isclose
from pathlib import Path
import matplotlib.pyplot as plt

STAGE = 2  # Change ONLY this number to select the next activity (0-3).
SHOW_PLOTS = True  # False saves PNGs without opening a window.


# STAGE 0 | 5 minutes | A completed example to read, run, and explain.
# PAPER: 2.5 km is how many metres? Write the cancelling units:
# 2.5 km * (1000 m / 1 km). Does the physical distance change?
def km_to_m(distance_km):
    return distance_km * 1000

def m_to_km(distance_m):
    return distance_m / 1000

# STAGE 1 | 15 minutes | Fix one bug; complete two functions.
# PAPER FIRST: convert 36 km/h to m/s, then reverse your answer.
# Write: (36 km / h) * (1000 m / km) * (1 h / 3600 s).
# The km and h cancel. What units remain?
# km = kilometers, h = hour, m = meters, s = seconds
def kmh_to_ms(speed_kmh):
    # BUG A: this program runs, but the operation is wrong. Fix this line.
    return (speed_kmh * 1000) / 3600  


def ms_to_kmh(speed_ms):
    # TODO B: reverse the previous conversion. Replace None with an expression.
    return (speed_ms * 3600) / 1000


def mph_to_ms(speed_mph):
    # TODO C: 1 mile = 1609.344 metres; 1 hour = 3600 seconds.
    # Use both conversion factors, not the km/h factor.
    return (speed_mph * 1609) / 3600


# PAUSE: complete Exer1 Q8 on paper, then Q5(a). Q5(b) can be an extension:
# use 1 foot = 0.3048 m. Keep intermediate digits; round only your final answer.
# Explain why a speed has a SMALLER numerical value in m/s than in km/h.


# STAGE 2 | 15 minutes | One reusable function for several metric prefixes.
# Each dictionary value is the number of base units in one prefixed unit.
# Examples: 1 kW = 1000 W; 1 nm = 1e-9 m. Here "" means no prefix.
# These are decimal SI prefixes, not binary computer-storage prefixes.
PREFIX = {"G": 1e9, "M": 1e6, "k": 1e3, "": 1.0,
          "c": 1e-2, "m": 1e-3, "u": 1e-6, "n": 1e-9, "f": 1e-15}


def convert_prefix(value, from_prefix, to_prefix):
    # TODO D: replace BOTH None values below.
    # 1. Convert the input to base units using PREFIX[from_prefix].
    # 2. Convert base units to the target using PREFIX[to_prefix].
    # We use "u" for micro so it is easy to type. Case matters: M != m.
    # This function assumes the SAME physical quantity (e.g. W -> W, m -> m).
    base_value = value * PREFIX[from_prefix]
    converted_value = value / PREFIX[to_prefix]
    return converted_value


# PAPER BREAK: Exer1 Q1, then Q2. Convert both diameters to metres
# before dividing them. Explain why the ratio has no units.
# GRAPH QUESTION: why do we use a logarithmic axis for W/kW/MW/GW?
# Each tick interval on a logarithmic axis represents multiplication,
# not addition. A different numerical value does not mean different power.


# STAGE 3 | 10 minutes | Optional: units raised to a power.
# PAPER: draw a 1 m square. Each edge is 100 cm. How many cm^2 fit inside?
# Then consider a 1 m cube. Why is multiplying volume by 100 not enough?
def metres_power_to_cm(value, dimension):
    # BUG E: correct for length, wrong for area and volume. Fix the factor.
    # dimension is 1 for m -> cm, 2 for m^2 -> cm^2, 3 for m^3 -> cm^3.
    # Python exponentiation is **, NOT ^ (which is bitwise XOR).
    return value * 100


# SUPPLIED CODE BELOW. Read it if curious; no edits needed for core tasks.
def check(label, actual, expected):
    if actual is None:
        print(f"TODO: {label}: the function still returns None.")
        return False
    passed = isclose(actual, expected, rel_tol=1e-9, abs_tol=1e-9)
    print(f"{'PASS' if passed else 'CHECK'}: {label}: {actual:.8g}"
          f" (expected {expected:.8g})")
    return passed


def finish_plot(fig):
    fig.tight_layout()
    path = Path(__file__).with_name(f"conversion_stage_{STAGE}.png")
    fig.savefig(path, dpi=150)
    print(f"Graph saved: {path.name}")
    if SHOW_PLOTS:
        plt.show()
    plt.close(fig)


def main():
    if STAGE == 0:
        distances_km = [0, 1, 2, 3, 4, 5]
        distances_m = []
        for distance in distances_km:
            distances_m.append(km_to_m(distance))
        check("2.5 km -> m", km_to_m(2.5), 2500)
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(distances_km, distances_m, "o-")
        ax.set(xlabel="Distance (km)", ylabel="Same distance (m)",
               title="One distance, two units: what does the slope mean?")
        ax.grid(True, alpha=0.3)
        finish_plot(fig)
    elif STAGE == 1:
        check("36 km/h -> m/s", kmh_to_ms(36), 10)
        check("0 km/h -> m/s", kmh_to_ms(0), 0)
        check("10 m/s -> km/h", ms_to_kmh(10), 36)
        check("35 mi/h -> m/s", mph_to_ms(35), 15.6464)
        if ms_to_kmh(10) is not None:
            check("round trip: 72 km/h", ms_to_kmh(kmh_to_ms(72)), 72)
        speeds = [0, 18, 36, 54, 72, 90, 108]
        converted = []
        for speed in speeds:
            converted.append(kmh_to_ms(speed))
        if None in converted:
            print("Finish kmh_to_ms to unlock the graph.")
            return
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(speeds, converted, "o-", label="Your function (may be wrong)")
        ax.scatter([36], [10], s=90, marker="x", color="black",
                   label="Hand-calculated checkpoint")
        ax.set(xlabel="Speed (km/h)", ylabel="Same speed (m/s)",
               title="Does your conversion pass through the checkpoint?")
        ax.grid(True, alpha=0.3)
        ax.legend()
        finish_plot(fig)
    elif STAGE == 2:
        check("1000 MW -> W", convert_prefix(1000, "M", ""), 1e9)
        check("1000 MW -> GW", convert_prefix(1000, "M", "G"), 1)
        check("0.1 nm -> m", convert_prefix(0.1, "n", ""), 1e-10)
        check("1 fm -> m", convert_prefix(1, "f", ""), 1e-15)
        check("5 kW -> kW", convert_prefix(5, "k", "k"), 5)
        values = []
        for prefix in ["", "k", "M", "G"]:
            values.append(convert_prefix(1000, "M", prefix))
        if None in values or any(value <= 0 for value in values):
            print("Finish the prefix function with positive values to plot.")
            return
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.scatter(["W", "kW", "MW", "GW"], values, s=70)
        ax.set_yscale("log")
        ax.set(ylabel="Numerical value in the named unit (log scale)",
               title="The SAME power expressed in four different units")
        for i, value in enumerate(values):
            ax.annotate(f"{value:g}", (i, value), xytext=(8, 0),
                        textcoords="offset points")
        ax.grid(True, axis="y", alpha=0.3)
        finish_plot(fig)
    elif STAGE == 3:
        for dimension, expected in [(1, 100), (2, 10000), (3, 1000000)]:
            check(f"1 m^{dimension} -> cm^{dimension}",
                  metres_power_to_cm(1, dimension), expected)
        values = [metres_power_to_cm(1, d) for d in [1, 2, 3]]
        if None in values or any(value <= 0 for value in values):
            print("Provide positive conversion factors to unlock the graph.")
            return
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.scatter([1, 2, 3], values, s=70, label="Your conversion factors")
        ax.scatter([1, 2, 3], [100, 10000, 1000000], marker="x",
                   color="black", label="Paper checkpoints")
        ax.set_yscale("log")
        ax.set_xticks([1, 2, 3], ["Length", "Area", "Volume"])
        ax.set(ylabel="m-based to cm-based conversion factor (log scale)",
               title="Do not compare length, area and volume as one quantity")
        ax.grid(True, axis="y", alpha=0.3)
        ax.legend()
        finish_plot(fig)
    else:
        print("Choose STAGE = 0, 1, 2, or 3.")


# EXIT TICKET (write answers as comments here before submitting):
# 1. Why can a program run without errors and still be physically wrong?
# 2. Why is a round-trip test alone not enough to prove both functions right?
# 3. Show one conversion with cancelling units, without using Python.
# Submit this completed file, one plot, and your handwritten calculations.

if __name__ == "__main__":
    main()
