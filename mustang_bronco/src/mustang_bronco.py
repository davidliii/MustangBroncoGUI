"""Module that contains the logic for the MustangBronco program 

    Typical usage examples:
    mustang_bronco(3)
      Mustang

    mustang_bronco(5)
      Bronco

    mustang_bronco(15)
      MustangBronco
    
    mustang_bronco(7)
      7
"""

def mustang_bronco(num : int) -> str:
  """Determines a string value to return based an integer input num

  If num is divisible by 3, 'Mustang' is returned. 
  If num is divisible by 5, 'Bronco' is returned. 
  If num is divisible by both 3 and 5, 'MustangBronco' is returned. 
  If num is neither divisible by 3 nor 5, the string form of num is returned.

  Args:
    num: A positive or negative integer

  Returns:
    Desired string to display, either 'Mustang', 'Bronco', 'MustangBronco' or
      the string form of the input number

  """

  # Check if input is divisible by 3 or 5
  divisible_3 = num % 3 == 0
  divisible_5 = num % 5 == 0

  # Return the appropriate string
  if divisible_3 and divisible_5:
    return 'MustangBronco'
  elif divisible_5:
    return 'Bronco'
  elif divisible_3:
    return 'Mustang'
  else:
    return str(num)

