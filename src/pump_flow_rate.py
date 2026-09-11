# Falon C.
# ENGT102 Homework 2: Pump Flow-Rate Calculator
# Asks for the volume transferred and elapsed time of a pump test, then
# calculates and displays the average flow rate in liters per second.

# Get the volume transferred and convert it to a decimal number
volume_text = input("Enter the volume transferred (L): ")
volume_liters = float(volume_text)

# Get the elapsed time and convert it to a decimal number
time_text = input("Enter the elapsed time (s): ")
elapsed_seconds = float(time_text)

# Flow rate (L/s) = Volume transferred (L) / Elapsed time (s)
flow_rate_lps = volume_liters / elapsed_seconds

# Display the result with its unit
print("Average flow rate:", flow_rate_lps, "L/s")
