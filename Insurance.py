# Description : A program for One Stop Insurance Company to enter and calculate insurance new policy information for its customers
# Author      : Hiba Mohamed 
# Date(s)     : March 20-21, 2024

# Define required libraries.
import FormatValues as FV

# Define program constants.
# Open the defaults file and read the values into variables
f = open('Defaults.dat', 'r')
POLICY_NUMBER = int(f.readline())
BASIC_PREMIUM = float(f.readline())
ADDITIONAL_CARS_DISCOUNT = float(f.readline())
EXTRA_LIABILITY_COVERAGE_COST = float(f.readline())
GLASS_COVERAGE_COST = float(f.readline())
LOANER_CAR_COVERAGE_COST = float(f.readline())
HST_RATE= float(f.readline())
MONTHLY_PAYMENT_PROCESSING_FEE = float(f.readline())
f.close()


# Define program functions.



# Main program starts here.
while True:
    
    # Gather user inputs.
    
    break