# Bit_Solver
Brute forces a solution to bit equations by finding patterns between nibble digits and single digit key values.

# Example
Find all patterns between ("0000", "1") and ("1001", "1") <br><br>

Bit_Solver performs logical operations on the first nibble in the set ("0000") that yield the desired output ("1") and finds which of these relevant operations can correctly solve other nibble-digit pairs. <br><br>

In this case the solver finds 7104 possible ways using logical operations to use nibble digits to get the desired answer. <br><br>

# Operations
Bit_Solver currently handles the following logical operations:
<ul>
<li>XOR
<li>OR
<li>AND
<li>NOT
<li>NOT USED
<li>NO CHANGE
</ul>

# Dependencies
Bit_Solver runs on Python 3.5+ and uses the following dependencies:
<ul>
<li> time
<li> inspect
<li> itertools
</ul>

# Instructions
WINDOWS: Run in cmd or bash using `python bruteforcer.py` <br>
OSX: Run in terminal using `python3 bruteforcer.py`
