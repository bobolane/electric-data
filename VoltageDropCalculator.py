# explain the relationship between the key and value by naming this dictionary properly
# for example, a key of 10 (awg) corresponds to the value 10380 (circmils)
awg_to_circmils = {
  10: 10380,
  8: 16510,
  6: 26240,
  4: 41740,
  3: 52620,
}

# think about how these functions differ from the dictionary above.
# in this case they perform a strict lookup as well. when might you use one or the other?
# would you use a function or dictionary to compute a bit of arithmetic?
# what if you had a large number of values that correspond 1:1 with a pre-computed output?
# what happens in the following functions when the input doesn't correspond to an output?
# what happens in the dictionary when a given key is not present?

def phase_modifier(phase):
  if phase == 1:
    return 2
  elif phase == 3:
    return 1.732

def wire_modifier(wire_type):
  if wire_type == "cu":
    return 12.9
  elif wire_type == "al":
    return 21.2

base_current = int(input("Current: "))
phase = int(input("Phase 1 or 3: "))
wire_type = raw_input("cu or al: ")

# let's only calculate current once; waiting to gather all the necessary derived inputs beforehand
# we have broken up the calculation into discrete units of computation
# this makes reading the algorithm for current (below) more straightforward
current = base_current * phase_modifier(phase) * wire_modifier(wire_type)

# might you want to move the input for length here?
# Then all requirments for 'numerator' would be met, and you could proceed to calculate denominator
# Of course if the order of input is important, then that's not a good idea
# But generally it's nice to keep related things together
voltage = int(input("Voltage: "))

awg = int(input("AWG#: "))
try:
  # Scope is important here. Even though wire is defined inside of the try block, it is accessible outside
  # what other ways might you do this?
  wire = awg_to_circmils[awg]
except KeyError:
  # this is equivalent to your else case (previously).
  # You could remove the try block to understand how I determined which exception to catch
  print("Unrecognized wire gauage; please try again.")
  # Might you want to exit() here?
  
length = int(input("Circuit Length: "))

# You could declare new functions to perform some or all of these calculations
# If so, what granularity makes sense, should there be one or many functions?
# What are the trade offs? Right now it is nice to see the intermediate values along the way

numerator = current * length
denominator = wire

volts_dropped = numerator / denominator
vd = voltage - volts_dropped
vd_percentage = vd / voltage
actual_vd_percentage = 1 - vd_percentage
percentage = actual_vd_percentage * 100
percentage = float(percentage)

print "Voltage drop for this circuit is %.2f%%." % percentage
