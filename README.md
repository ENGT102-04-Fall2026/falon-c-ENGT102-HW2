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

## Testing

Expected values were worked out by hand before running the program.

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

My first pseudocode read the input and converted it to a float on the same
line. In the Python program I split that into two steps: one variable holds
the raw text from `input()`, and a second holds the `float()` result.
Keeping the text and numeric values separate makes it clear where the
conversion happens and gives the variables more descriptive names, so I
updated the pseudocode to match.

The tests gave me confidence because I calculated every expected value by
hand before running the program and compared it to the actual output. They
covered a whole-number result, a result less than one, and a decimal input.
All three matched exactly, showing the inputs were converted correctly and
the division was set up in the right order.
