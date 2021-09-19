# 608-mod3 / custom-object.py
#
# Encapulate state & behavior into a reusable object
# Add class ClassName(object): to the top
# Add __init__ function for initializing a new object
# Explore use of self to refer to "this object"

# INDENTATION IS CRITICAL IN PYTHON
# Use 2 spaces for each level

# START CUSTOM OBJECT ******************************************

class Purchase(object):

  # Required __init__ method to construct/initialize a new object
  def __init__(self, amount):
    self.amount = amount # set self amount to what is passed in

  def calculateTax(self, taxPercent):
    return self.amount * taxPercent/100.0
    
  def calculateTip(self, tipPercent):
    return self.amount * tipPercent/100.0
    
  def calculateTotal(self, taxPercent, tipPercent):
    return self.amount * (1 * taxPercent/100.0 + tipPercent/100.0)
    
# END CUSTOM OBJECT ******************************************
    
# create Purchase object for a given amount
ourPurchaseObject = Purchase(100.0)

# set local tax and tip purcentages
localTaxPercent = 7.5
localTipPercent = 20.0

# use our new object to get tax and tip
tax = ourPurchaseObject.calculateTax(localTaxPercent)
tip = ourPurchaseObject.calculateTip(localTipPercent)

# display some useful results
print('Local Tax Percent: ', tax)
print('Local Tip Percent: ', tip)
print('Total Purchase in USD: $', ourPurchaseObject.calculateTotal(localTaxPercent, localTipPercent)) 

# print using string interpolation and new fstrings
# fstrings = formatted strings 
# display values inline inside curly braces
print(f'Total Purchase in USD: ${ ourPurchaseObject.calculateTotal(localTaxPercent, localTipPercent) }')

# use fstrings to show only 2 digits on a floating point number (.2f)
print(f'Total Purchase in USD: ${ ourPurchaseObject.calculateTotal(localTaxPercent, localTipPercent):.2f}')

# References
# Read more at: https://docs.python.org/3/tutorial/classes.html
# string interpolation at: python string interpolation
# Google python fstring to limit to 2 decimal places

