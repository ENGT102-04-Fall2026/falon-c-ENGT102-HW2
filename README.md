# ENGT102 HW2: Pump Flow-Rate Calculator

A small Python program that calculates the average volumetric flow rate of a
water-transfer pump from the volume transferred and the elapsed time of a
timed test.

Program: `src/pump_flow_rate.py`

## IPO Analysis

Inputs:
- Volume of water transferred by the pump during the test, entered by the user in liters (L)
- Elapsed time of the timed test, entered by the user in seconds (s)

Process:
- Convert both text entries from the keyboard into decimal numbers with `float()`
- Divide the volume transferred (L) by the elapsed time (s) to get the average flow rate (L/s)
- Store the result in its own variable so it can be displayed

Output:
- The average volumetric flow rate of the pump, displayed in liters per second (L/s)

## Pseudocode

```
START
DISPLAY a prompt asking for the volume transferred in liters
INPUT the volume text from the user
SET volume_liters to the volume text converted to a float
DISPLAY a prompt asking for the elapsed time in seconds
INPUT the time text from the user
SET elapsed_seconds to the time text converted to a float
SET flow_rate_lps to volume_liters divided by elapsed_seconds
DISPLAY "Average flow rate: " followed by flow_rate_lps and the unit "L/s"
END
```
