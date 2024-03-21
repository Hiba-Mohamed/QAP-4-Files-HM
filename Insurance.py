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
    ProvinceList = ["NL", "NS", "NB", "PE", "PQ", "ON", "MB", "AB", "BC", "NT", "YT", "NV"]
    PaymentPreferenceList =["Full", "Monthly", "DownPay"]

    # Gather user inputs.
    CustomerFirstName       = input("Please enter customer's first name (\"END\" to finish): ")
    CustomerLastName        = input("Please enter customer's last name:  ")
    CustomerAddress         = input("Please enter customer's address:    ")
    CustomerCity            = input("Please enter customer's city:       ")
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
    CustomerPostalCode      = input("Please enter customer's postal code:  ")
    CustomerPhoneNumber     = input("Please enter customer's phone number: ")
    NumberOfCarsToBeInsured = input("Please enter the number of cars being insured: ")
    NumberOfCarsToBeInsured = int(NumberOfCarsToBeInsured)
    ExtraLiability          = input("Would you like to add extra liability (\"Y\" for Yes, \"N\" for No): ").upper()
    OptionalGlassCoverage   = input("Would you like to add optional glass coverage (\"Y\" for Yes, \"N\" for No): ").upper()
    OptionalLoanerCar       = input("Would you like to add optional loaner car (\"Y\" for Yes, \"N\" for No): ").upper()
    while True:
        PaymentPreference    = input("Please enter the payment preference (\"Full\", \"Monthly\", \"DownPay\"):   ")
        if PaymentPreference == "":
            print("Error - cannot be blank.")
        elif PaymentPreference == "DownPay":
            DownPaymentAmount = input("Please enter the amount of the down payment: ")
            DownPaymentAmount = float(DownPaymentAmount)
        elif PaymentPreference  not in PaymentPreferenceList:
            print("Error - invalid payment method.")
        else:
            break
    ClaimNumber = input("Please enter the claim number: ")
    ClaimDate = input("Please input the claim date:  ")
    AllPreviousCustomerClaims = input("Please enter the claim amount of all previous claims for the customer")

    if CustomerFirstName == "END":
        break
