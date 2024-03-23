# Description : A program for One Stop Insurance Company to enter and calculate insurance new policy information for its customers
# Author      : Hiba Mohamed 
# Date(s)     : March 20-21, 2024

# Define required libraries.
import FormatValues as FV
import datetime
import time
import sys

# Define program constants.
# Open the defaults file and read the values into variables
f = open('Defaluts.dat', 'r')
POLICY_NUMBER = int(f.readline())                    # 1944
BASIC_PREMIUM = float(f.readline())                  # 869.00
ADDITIONAL_CARS_DISCOUNT = float(f.readline())       # 0.25   
EXTRA_LIABILITY_COVERAGE_COST = float(f.readline())  # 130.00
GLASS_COVERAGE_COST = float(f.readline())            # 86.00
LOANER_CAR_COVERAGE_COST = float(f.readline())       # 58.00
HST_RATE= float(f.readline())                        # 0.15
MONTHLY_PAYMENT_PROCESSING_FEE = float(f.readline()) # 39.99
f.close()
NUMBER_OF_MONTHS = 8
CURRENT_DATE = datetime.datetime.today()



# Define program functions.
def ParseDateYYYYMMDD(string):
    # function to parse a string into a datetime object
    ParsedDate = datetime.datetime.strptime(string, "%Y/%m/%d")
    return ParsedDate

# Main program starts here.
while True:
    ProvinceList          = ["NL", "NS", "NB", "PE", "PQ", "ON", "MB", "AB", "BC", "NT", "YT", "NV"]
    PaymentPreferenceList = ["Full", "Monthly", "Downpay"]

    # Gather user inputs.
    CustomerFirstName       = input("Please enter customer's first name (\"END\" to finish):   ").title()
    if CustomerFirstName.upper() == "END":
        break
    CustomerLastName        = input("Please enter customer's last name:    ").title()
    CustomerAddress         = input("Please enter customer's address:      ")
    CustomerCity            = input("Please enter customer's city:         ").title()
    while True:
        CustomerProvince    = input("Please enter customer's province:     ").upper()
        if CustomerProvince == "":
            print("Error - cannot be blank.")
        elif len(CustomerProvince ) != 2:
            print("Error - must be 2 characters only.")
        elif CustomerProvince  not in ProvinceList:
            print("Error - invalid province.")
        else:
            break
    CustomerPostalCode        = input("Please enter customer's postal code:  ")
    CustomerPhoneNumber       = input("Please enter customer's phone number: ")
    NumberOfCarsToBeInsured   = input("Please enter the number of cars being insured: ")
    NumberOfCarsToBeInsured   = int(NumberOfCarsToBeInsured)
    ExtraLiability            = input("Would you like to add extra liability (\"Y\" for Yes, \"N\" for No): ").upper()
    OptionalGlassCoverage     = input("Would you like to add optional glass coverage (\"Y\" for Yes, \"N\" for No): ").upper()
    OptionalLoanerCar         = input("Would you like to add optional loaner car (\"Y\" for Yes, \"N\" for No): ").upper()
    while True:
        PaymentPreference     = input("Please enter the payment preference (\"Full\", \"Monthly\", \"Downpay\"):   ").title()
        if PaymentPreference == "":
            print("Error - cannot be blank.")
        elif PaymentPreference == "Downpay":
            DownPaymentAmount = input("Please enter the amount of the down payment: ")
            DownPaymentAmount = float(DownPaymentAmount)
            break
        elif PaymentPreference  not in PaymentPreferenceList:
            print("Error - invalid payment method.")
        else:
            break
    print("    Previous Claims: ")

    PreviousClaimsData =[]
    while True:
        ClaimNumber               = int(input("Please enter the claim number (0) when finished: "))
        if ClaimNumber == 0:
            break
        ClaimDate                 = input("Please enter the claim date (YYYY/MM/DD):  ")
        ClaimDateParsed = ParseDateYYYYMMDD(ClaimDate)
        ClaimAmount               = float(input("Please enter the claim amount: "))
        PreviousClaimsData.append((ClaimNumber, ClaimDateParsed, ClaimAmount))
    print(PreviousClaimsData)

    # Calculations 
    BasicCarPremium               = BASIC_PREMIUM
    if NumberOfCarsToBeInsured    > 1:
        BasicCarPremium           = BASIC_PREMIUM + ((NumberOfCarsToBeInsured - 1) * (1 - ADDITIONAL_CARS_DISCOUNT))
    
    ExtraLiabilityCost            = 0.00
    if ExtraLiability             == "Y":
        ExtraLiabilityCost        = EXTRA_LIABILITY_COVERAGE_COST
    
    OptionalGlassCoverageCost     = 0.00
    if OptionalGlassCoverage      == "Y":
        OptionalGlassCoverageCost = GLASS_COVERAGE_COST 

    OptionalLoanerCarCost         = 0.00
    if OptionalLoanerCar          == "Y":
        OptionalLoanerCarCost     = LOANER_CAR_COVERAGE_COST

    ExtraCosts                  = ExtraLiabilityCost + OptionalGlassCoverageCost + OptionalLoanerCarCost
    TotalInsurancePremiumPreTax = BasicCarPremium + ExtraCosts
    Taxes                       = TotalInsurancePremiumPreTax * HST_RATE
    TotalCosts                  = TotalInsurancePremiumPreTax + Taxes

    if PaymentPreference != "Full":
        TotalCosts = MONTHLY_PAYMENT_PROCESSING_FEE + TotalCosts

    # Payment breakdown
    if PaymentPreference == "Full":
        MonthlyPaymentAmount = 0.00
    if PaymentPreference == "Monthly":
        MonthlyPaymentAmount = (MONTHLY_PAYMENT_PROCESSING_FEE + TotalCosts) / NUMBER_OF_MONTHS
    if PaymentPreference == "Downpay":
        MonthlyPaymentAmount = (MONTHLY_PAYMENT_PROCESSING_FEE + (TotalCosts - DownPaymentAmount)) / NUMBER_OF_MONTHS
 
    DateOfFirstPayment = CURRENT_DATE + datetime.timedelta(days=30)

    CustomerFullName = FV.FFullName(CustomerFirstName, CustomerLastName)
    CustomerFormattedAddress = FV.FAddress(CustomerAddress, CustomerCity, CustomerProvince, CustomerPostalCode)

    # Display results
    print(f"")
    print(f"")
    print(f"       One Stop  Insurance  Company")
    print(f" Customer name: {CustomerFullName:<22s} ")
    print(f" Address:       {CustomerFormattedAddress:<} ")
    print(f" Phone number:  {CustomerPhoneNumber:<14s} ")
    print(f"")
    print(f" Number of cars: {NumberOfCarsToBeInsured:<2d}     Extra liability: {ExtraLiability:<1s}   ")
    print(f" Glass coverage: {OptionalGlassCoverage:<1s}       Loaner car: {OptionalLoanerCar:<1s}")
    print(f"")
    if PaymentPreference == "Full" or PaymentPreference == "Monthly":
        print(f" Payment plan: {PaymentPreference}")
    if PaymentPreference == "Downpay":
        print(f" Payment plan: Monthly with down payment ")
    print(f"")
    print(f" Car premium cost             {FV.FDollar2(BasicCarPremium):>10s}") 
    print(f" Extra liability cost         {FV.FDollar2(ExtraLiabilityCost):>10s}") 
    print(f" Glass coverage cost          {FV.FDollar2(OptionalGlassCoverageCost):>10s}") 
    print(f" Optional loaner car cost     {FV.FDollar2(OptionalLoanerCarCost):>10s}") 
    print(f"                              ---------- ")
    print(f" Subtotal                     {FV.FDollar2(TotalInsurancePremiumPreTax):>10s}") 
    print(f" Taxes                        {FV.FDollar2(Taxes):>10s}") 
    print(f"                              ---------- ")
    if PaymentPreference != "Full":
        print(f" Monthly processing fee       {FV.FDollar2(MONTHLY_PAYMENT_PROCESSING_FEE):>10s}")
    print(f" Total                        {FV.FDollar2(TotalCosts):>10s} ") 
    print(f"                              ---------- ")
    print(f"")
    if PaymentPreference !="Full":
        print(f"  Monthly      # of      1st payment")
        print(f"  payment     months         due ")
        print(f"---------------------------------------")
        print(f" {FV.FDollar2(MonthlyPaymentAmount):>10s}     8       {FV.FDateS(DateOfFirstPayment)}")
    print(f"")
    if len(PreviousClaimsData) !=0:
        print(f"")
        print(" Previous customer claims: ")
        print("      Claim       Claim        Claim")
        print("        #          Date        Amount")
        print(f"     ---------------------------------")
        for claim in PreviousClaimsData:
            print(f"    {claim[0]:>5}      {FV.FDateS(claim[1]):>10s}  {FV.FDollar2(claim[2]):>10s}")
        print(f"     ---------------------------------")

    # Write the values to a data file called Insurance.dat.
    for _ in range(5):  # Change to control no. of 'blinks'
        print('Saving insurance data ...', end='\r')
        time.sleep(.3)  # To create the blinking effect
        sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns
        time.sleep(.3)

    f = open("Insurance.dat", "a")

    # All values written to file must be a string.  If you have a numeric
    # value, use the str() function to convert.
    f.write("{}, ".format(str(POLICY_NUMBER)))
    f.write("{}, ".format(str(CURRENT_DATE))) # This is the current system date
    f.write("{}, ".format(CustomerFullName))
    f.write("{}, ".format(CustomerFormattedAddress))
    f.write("{}, ".format(CustomerPhoneNumber))
    f.write("{}, ".format(CustomerFormattedAddress))
    f.write("{}, ".format(str(NumberOfCarsToBeInsured)))
    f.write("{}, ".format(ExtraLiability))
    f.write("{}, ".format(OptionalGlassCoverage))
    f.write("{}, ".format(OptionalLoanerCar))
    f.write("{}, ".format(PaymentPreference))
    if PaymentPreference == "Downpay":
        f.write("{}, ".format(str(DownPaymentAmount)))  
    f.write("{}, ".format(str(PreviousClaimsData)))
    f.write("{}\n".format(str(TotalInsurancePremiumPreTax)))
    f.close()


    print()
    print("Insurance data successfully saved ...", end='\r')
    time.sleep(1)  # To create the blinking effect
    sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns
    
    POLICY_NUMBER += 1

# Any housekeeping duties at the end of the program.

# Write the default values back to the Defaults.dat file
f = open('Defaluts.dat', 'w')
f.write("{}\n".format(str(POLICY_NUMBER )))
f.write("{}\n".format(str(BASIC_PREMIUM)))
f.write("{}\n".format(str(ADDITIONAL_CARS_DISCOUNT)))
f.write("{}\n".format(str(EXTRA_LIABILITY_COVERAGE_COST)))
f.write("{}\n".format(str(GLASS_COVERAGE_COST)))
f.write("{}\n".format(str(LOANER_CAR_COVERAGE_COST)))
f.write("{}\n".format(str(HST_RATE)))
f.write("{}\n".format(str(MONTHLY_PAYMENT_PROCESSING_FEE)))
f.close()





