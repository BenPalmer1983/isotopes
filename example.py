from isotopes import isotopes
  
  
# isotope_activities    protons/symbol, nucleons, parent starting amount, parent production rate, time
# time in seconds
# parent starting amount arbitrary
# parent production rate arbitrary amount per second
 
  
# Example 1
# Co 55

print("Cobalt 55")
nt = isotopes.isotope_activities('Co', 55, 10.0, 0.0, 60000, 'co55.txt')
isotopes.print_tally(nt)
print()
  
  
# Example 2
# Bi 214
print("Bismuth 214")
nt = isotopes.isotope_activities(83, 214, 10.0, 0.0, 1000, 'bi214.txt')
isotopes.print_tally(nt)
print()


# Example 3
# U 238
print("Uranium 238")
nt = isotopes.isotope_activities('U', 238, 10.0, 0.0, 1.0e10, 'u238.txt')
isotopes.print_tally(nt)
print()

