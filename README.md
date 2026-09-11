# ENGT102 HW2: Pump Flow-Rate Calculator

Python program that takes the volume a pump moved during a timed test and how
long the test ran, and works out the average flow rate.

Program: `src/pump_flow_rate.py`

## IPO Analysis

Inputs:
- Volume of water transferred by the pump during the test, entered by the user in liters (L)
- Elapsed time of the timed test, entered by the user in seconds (s)

Process:
- Convert both entries from text to decimal numbers with `float()`
- Divide volume by time to get the average flow rate
- Save the result in a variable so it can be printed

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

## Testing

I did the expected values on paper before running anything.

### Test 1
- Volume (L): 18
- Time (s): 12
- Expected Flow Rate (L/s): 18 / 12 = 1.5
- Actual Flow Rate (L/s): 1.5
- Result: Pass

### Test 2
- Volume (L): 25
- Time (s): 40
- Expected Flow Rate (L/s): 25 / 40 = 0.625
- Actual Flow Rate (L/s): 0.625
- Result: Pass

### Test 3
- Volume (L): 7.5
- Time (s): 3
- Expected Flow Rate (L/s): 7.5 / 3 = 2.5
- Actual Flow Rate (L/s): 2.5
- Result: Pass

## Reflection

My first pseudocode did the input and the float conversion on one line. When
I typed the actual program I split it into two variables, one holding the
text from `input()` and one holding the float, because it was easier to see
where the conversion happens. I went back and changed the pseudocode to
match.
