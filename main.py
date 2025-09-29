class MortgagePayment:
    
    def paymentCalc(principal, r, n):
        #PV of A
        pvA = (1-(1+r)**(-n))/r;
        return principal/pvA;
    
    def payments(principal,annualR,years):
        annualR=annualR/100;

        monthlyR = (1+annualR/2)**(1/6)-1
        monthly=MortgagePayment.paymentCalc(principal, monthlyR, years*12)

        semiR = (1+annualR/2)**(1/24)-1
        semiM=MortgagePayment.paymentCalc(principal, semiR, years*24)

        biWeeklyR = (1+annualR/2)**(1/26)-1
        biWeekly=MortgagePayment.paymentCalc(principal, biWeeklyR, years*26)

        weeklyR = (1+annualR/2)**(1/52)-1
        weekly=MortgagePayment.paymentCalc(principal, weeklyR, years*52)

        acceleratedBi = monthly/2;

        AcceleratedW = monthly/4;

        return [monthly,semiM,biWeekly,weekly,acceleratedBi,AcceleratedW];

#principal = float(input("Enter Principal: "))
#annualRate = float(input("Enter Annual Rate: "))
#years = input("Enter # of Years: ")

#paymentsList = MortgagePayment.payments(principal,annualRate,years);

paymentsList = MortgagePayment.payments(100000,5.5,25);

typeList = ["Montly Payment: $","Semi-Montly Payment: $","Bi-Weekly Payment: $","Weekly Payment: $","Rapid Bi-Weekly Payment: $","Rapid Weekly Payment: $"];

#easier way to print?
for i in range(len(paymentsList)):
    print(typeList[i],paymentsList[i])

#round to cents


