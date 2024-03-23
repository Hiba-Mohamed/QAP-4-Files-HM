# Description : A program for One Stop Insurance Company to enter and calculate insurance new policy information for its customers
# Author      : Hiba Mohamed 
# Date(s)     : March 20-21, 2024

# Define required libraries.
import FormatValues as FV
import datetime

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
CURRENT_DATE = datetime.datetime.today



# Define program functions.
def ParseDateYYYYMMDD(string):
    # function to parse a string into a datetime object
    ParsedDate = datetime.strptime(string, "%Y/%m/%d")
    return ParsedDate

# Main program starts here.
while True:
    ProvinceList          = ["NL", "NS", "NB", "PE", "PQ", "ON", "MB", "AB", "BC", "NT", "YT", "NV"]
    PaymentPreferenceList = ["Full", "Monthly", "Downpay"]

    # Gather user inputs.
    CustomerFirstName       = input("Please enter customer's first name (\"END\" to finish): ").title()
    if CustomerFirstName.upper() == "END":
        break
    CustomerLastName        = input("Please enter customer's last name:  ").title()
    CustomerAddress         = input("Please enter customer's address:    ")
    CustomerCity            = input("Please enter customer's city:       ").title()
    while True:
        CustomerProvince    = input("Please enter customer's province:   ")
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
        elif PaymentPreference  not in PaymentPreferenceList:
            print("Error - invalid payment method.")
        else:
            break

    while True:
        PreviousClaimsData =[]
        ClaimNumber               = int(input("Please enter the claim number (0000) when finished: "))
        if ClaimNumber == 00000:
            break
        ClaimDate                 = input("Please input the claim date (YYYY/MM/DD):  ")
        ParseDateYYYYMMDD(ClaimDate)
        ClaimAmount               = float(input("Please enter the claim amount: "))
        PreviousClaimsData.append((ClaimNumber, ClaimDate, ClaimAmount))

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

    # Display results
    print(f"")
    print(f"----------------------------------------------------------")
    print(f"")
    print(f"                One Stop  Insurance  Company")
    print(f" Customer name: {FV.FFullName(CustomerFirstName, CustomerLastName):<22s} ")
    print(f" Address: {FV.FAddress(CustomerAddress, CustomerCity, CustomerProvince, CustomerPostalCode):<} ")
    print(f" Phone number: {CustomerPhoneNumber:<14s} ")
    print(f"")
    print(f"----------------------------------------------------------")
    print(f" Number of cars: {NumberOfCarsToBeInsured:>2d}              Extra liability: {ExtraLiability:<1s}   ")
    print(f" Glass coverage: {OptionalGlassCoverage:<1s}             Loaner car: {OptionalLoanerCar:<1s}")
    print(f"----------------------------------------------------------")
    print(f"")
    if PaymentPreference == "Full" or PaymentPreference == "Monthly":
        print(f" Payment plan: {PaymentPreference}")
    if PaymentPreference == "Downpay":
        print(f" Payment plan: Monthly with down payment ")
    print(f"----------------------------------------------------------")
    print(f" Car premium cost             ") 
    print(f" Extra liability cost         ") 
    print(f" Glass coverage cost          ") 
    print(f" Optional loaner car cost     ") 
    print(f"----------------------------------------------------------")
    print(f" Subtotal                     ") 
    print(f" Taxes                        ") 
    print(f"----------------------------------------------------------")
    if PaymentPreference != "Full":
        print(f" Monthly processing fee   ")
    print(f" Total                        ") 
    print(f"----------------------------------------------------------")
    print(f"")
    if PaymentPreference !="Full":
        print(f"  Monthly payment      # of months      1st payment due ")
        print(f"----------------------------------------------------------")
        print(f"  {FV.FDollar2(MonthlyPaymentAmount):>10s}   8   {FV.FDateM(DateOfFirstPayment)}")
    print(f"----------------------------------------------------------")
    print(f"----------------------------------------------------------")
    print(" Previous customer claims: ")
    print("         Claim #       Claim Date        Amount")
    print(f"     ---------------------------------------------")
    for claim in PreviousClaimsData:
        print(f" {claim[0]:>5}   {FV.FDateM(claim[1]):>10s}  {FV.FDollar2:>10s}")
    print(f"     ---------------------------------------------")








