import csv
#import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt

class BankAccount():
    def __init__(self, *args):
        self.balance = 0
        self.initial_balance = 0
        self.goal = 0
        self.expenses = []
        self.incomes = []
        self.plotBalance = []
        self.plotDay = []

    def clear(self):
        self.balance = 0
        self.initial_balance = 0
        self.goal = 0
        self.expenses = []
        self.incomes = []
        self.plotBalance = []
        self.plotDay = []
        return

    def addExpense(self, dataList):
        expense = Datapoint(dataList[0], dataList[1], dataList[2], dataList[3])
        self.expenses.append(expense)
        return

    def addIncome(self, dataList):
        income = Datapoint(dataList[0], dataList[1], dataList[2], dataList[3])
        self.incomes.append(income)
        return

    def setBalance(self, balance):
        self.initial_balance = int(balance)
        self.balance = int(balance)
        return

    def setGoal(self, goal):
        self.goal = goal
        return
    
    def getNetOutput(self):
        net = int(self.balance) - int(self.initial_balance)
        return net
    
    def getGoalOutput(self):
        goal = int(self.balance) - int(self.goal)
        return goal

    def graphBalance(self, length):
        
        print(self.initial_balance)
        print(self.balance)
        print(self.goal)
        
        for expense in self.expenses:
            print(expense.amount)
            print(expense.timeframe)
        
        for days in range(0, length):
            for expense in self.expenses:
                if expense.timeframe == "Daily":
                    self.balance -= (expense.amount*expense.frequency)
            for income in self.incomes:
                if income.timeframe == "Daily":
                    self.balance += (income.amount*income.frequency)
            if (days % 7) == 0:
                for expense in self.expenses:
                    if expense.timeframe == "Weekly":
                        self.balance -= (expense.amount*expense.frequency)
                for income in self.incomes:
                    if income.timeframe == "Weekly":
                        self.balance += (income.amount*income.frequency)
            if (days % 30) == 0:
                for expense in self.expenses:
                    if expense.timeframe == "Monthly":
                        self.balance -= (expense.amount*expense.frequency)
                for income in self.incomes:
                    if income.timeframe == "Monthly":
                        self.balance += (income.amount*income.frequency)
            self.plotBalance.append(self.balance)
            self.plotDay.append(days+1)
            
            self.renderGraph()
        return
    
    def renderGraph(self):
        ## data
        #r = np.random.randn(9)*80+range(1,10)
        #print(r)
        #print(type(r))
        #df=pd.DataFrame({'x': range(1, 10), 'y': r})
         
        ## plot
        #plt.plot('x', 'y', data=df, linestyle='-', marker='o')
        #plt.show()
        points = []
        
        for point in self.plotBalance:
            points.append(point)
        print(points)
        
        plt.plot(points)
        plt.ylabel('Balance ($)')
        plt.xlabel("Day Number")
        plt.show()


class Datapoint():
    def __init__(self, name, amount, timeframe, frequency):
        self.name = name
        self.amount = amount
        self.timeframe = timeframe
        self.frequency = frequency

    def update(self, data):
        self.name = data[0]
        self.amount = data[1]
        self.timeframe = data[2]
        self.frequency = data[3]



class Model():
    def __init__(self):
        self.account = BankAccount()

    def saveCSVFile(self, fileName):
        with open(fileName, 'w', newline='') as save:
            writer = csv.writer(save)

            writer.writerow(["Account Balance", self.account.balance])
            writer.writerow(["Budget Goal", self.account.goal])

            writer.writerow(["Type", "Name", "Amount", "Time Frame", "Frequency"])

            for expense in self.account.expenses:
                writer.writerow(["Expense", expense.name, expense.amount, expense.timeframe, expense.frequency])

            for income in self.account.incomes:
                writer.writerow(["Income", income.name, income.amount, income.timeframe, income.frequency])


    def readCSVFile(self, fileName):
        self.account.clear()
        with open(fileName, 'r', newline='') as load:
            reader = csv.reader(load)
            for row in reader:
                if row[0] == "Account Balance":
                    self.account.setBalance(row[1])
                if row[0] == "Budget Goal":
                    self.account.setGoal(row[1])
                if row[0] == "Expense":
                    self.account.addExpense([row[1], row[2], row[3], row[4]])
                if row[0] == "Income":
                    self.account.addIncome([row[1], row[2], row[3], row[4]])


