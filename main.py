import csv

#Make variables private 

#1 class
class MortgagePayment:

    def __init__(self, annualRate, years):
        self.annualRate = annualRate / 100  # convert % to decimal
        self.years = years
    
    def paymentCalc(self, principal, r, n):
        #Payments using the PV of Annuity formula
        pvA = (1-(1+r)**(-n))/r;
        return principal/pvA;
    
    def payments(self, principal):

        monthlyR = (1+self.annualRate/2)**(1/6)-1
        monthly=self.paymentCalc(principal, monthlyR, self.years*12)

        semiR = (1+self.annualRate/2)**(1/12)-1
        semiM=self.paymentCalc(principal, semiR, self.years*24)

        biWeeklyR = (1+self.annualRate/2)**(1/13)-1
        biWeekly=self.paymentCalc(principal, biWeeklyR, self.years*26)

        weeklyR = (1+self.annualRate/2)**(1/26)-1
        weekly=self.paymentCalc(principal, weeklyR, self.years*52)

        acceleratedBi = monthly/2;

        AcceleratedW = monthly/4;

        return [monthly,semiM,biWeekly,weekly,acceleratedBi,AcceleratedW];

#2 class
class ExchangeRates:

    def __init__(self, filename):
        with open(filename, newline="") as f:
            reader = csv.DictReader(f);
            column_data = [row["USD/CAD"] for row in reader]
            self.latestrate = float(column_data[-1])

    def convert(self, xAmount, xFrom, xTo):
        if (xFrom not in ["USD","CAD"]) or (xTo not in ["USD","CAD"]):
            print("You did not provide correct information.");
            return None
        elif xFrom == "USD" and xTo == "CAD":
            return xAmount * self.latestrate
        elif xFrom == "CAD" and xTo == "USD":
            return xAmount / self.latestrate
        else:
            print("You did not provide correct information.");
            return None

#main
if __name__ == "__main__":

    #1
    principal = float(input("Enter Principal: "))
    annualRate = float(input("Enter Annual Rate: "))
    years = float(input("Enter # of Years: "))

    mortgage = MortgagePayment(annualRate, years);
    paymentsList = mortgage.payments(principal);

    #paymentsList = MortgagePayment.payments(100000,5.5,25);

    typeList = ["Montly","Semi-Montly","Bi-Weekly","Weekly","Rapid Bi-Weekly","Rapid Weekly"];

    #print amd round to cents
    for i in range(len(paymentsList)):
        print(typeList[i]," Payment: $", round(paymentsList[i],2));

    #seperation
    print("------");

    #2
    print("USD/CAD Currency converter");

    filename = "BankOfCanadaExchangeRates.csv";
    exchange = ExchangeRates(filename);

    xAmount = float(input("Enter the $ Amount:   "));
    print("Enter 'USD' or 'CAD' ");
    xFrom = input("From:   ").upper();
    xTo = input("To:   ").upper();

    convertedAmount = exchange.convert(xAmount, xFrom, xTo);

    if convertedAmount is not None:
        print(xAmount, xFrom, "is equal to", round(convertedAmount,2), xTo);