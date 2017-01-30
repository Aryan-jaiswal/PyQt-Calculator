import sys
from math import *
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

num = 0.0
newNum = 0.0
sumAll = 0.0
operator = ""

opVar = False
sumIt = 0
check=0

class Main(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):

        self.line = QtGui.QLineEdit(self)                               #Text Box  Configuration
        self.line.setReadOnly(True)
        self.line.setAlignment(Qt.AlignRight)
        self.line.setGeometry(10,5,480,45)
        self.statusBar().showMessage('                                                    Aryan\'s Calculator')

        zero = QtGui.QPushButton("0",self)
        zero.setGeometry(70,330,60,70)

        one = QtGui.QPushButton("1",self)
        one.setGeometry(10,260,60,70)

        two = QtGui.QPushButton("2",self)
        two.setGeometry(70,260,60,70)

        three = QtGui.QPushButton("3",self)
        three.setGeometry(130,260,60,70)

        four = QtGui.QPushButton("4",self)
        four.setGeometry(10,190,60,70)

        five = QtGui.QPushButton("5",self)
        five.setGeometry(70,190,60,70)

        six = QtGui.QPushButton("6",self)
        six.setGeometry(130,190,60,70)

        seven = QtGui.QPushButton("7",self)
        seven.setGeometry(10,120,60,70)

        eight = QtGui.QPushButton("8",self)
        eight.setGeometry(70,120,60,70)

        nine = QtGui.QPushButton("9",self)
        nine.setGeometry(130,120,60,70)

        switch = QtGui.QPushButton("+/-",self)
        switch.setGeometry(10,330,60,70)
        switch.clicked.connect(self.Switch)

        point = QtGui.QPushButton(".",self)
        point.setGeometry(130,330,60,70)
        point.clicked.connect(self.pointClicked)

        div = QtGui.QPushButton("/",self)
        div.setGeometry(190,120,60,70)

        multiply = QtGui.QPushButton("*",self)
        multiply.setGeometry(190,190,60,70)

        mod=QtGui.QPushButton("%",self)
        mod.setGeometry(430,50,60,70)
        mod.clicked.connect(self.Percent)

        minus = QtGui.QPushButton("-",self)
        minus.setGeometry(190,260,60,70)
        
        plus = QtGui.QPushButton("+",self)
        plus.setGeometry(190,330,60,70)
        
        sqrt = QtGui.QPushButton("√",self)
        sqrt.setGeometry(250,190,60,70)
        sqrt.clicked.connect(self.Sqrt)

        squared = QtGui.QPushButton("x²",self)
        squared.setGeometry(250,120,60,70)
        squared.clicked.connect(self.Squared)

        fact=QtGui.QPushButton("n!",self)
        fact.setGeometry(250,260,80,70)
        fact.clicked.connect(self.Fact)

        sin=QtGui.QPushButton("sin",self)
        sin.setGeometry(310,260,60,70)
        sin.clicked.connect(self.trig)

        cos=QtGui.QPushButton("cos",self)
        cos.setGeometry(310,190,60,70)
        cos.clicked.connect(self.trig)

        tan=QtGui.QPushButton("tan",self)
        tan.setGeometry(310,120,60,70)
        tan.clicked.connect(self.trig)

        asin=QtGui.QPushButton("asin",self)
        asin.setGeometry(370,260,60,70)
        asin.clicked.connect(self.trig)

        acos=QtGui.QPushButton("acos",self)
        acos.setGeometry(370,190,60,70)
        acos.clicked.connect(self.trig)

        atan=QtGui.QPushButton("atan",self)
        atan.setGeometry(370,120,60,70)
        atan.clicked.connect(self.trig)

        rad=QtGui.QPushButton("ToRadians",self)
        rad.setGeometry(430,190,60,70)
        rad.clicked.connect(self.Conversion)

        deg=QtGui.QPushButton("ToDegrees",self)
        deg.setGeometry(430,120,60,70)
        deg.clicked.connect(self.Conversion)

        exp=QtGui.QPushButton("e",self)
        exp.setGeometry(310,50,60,70)
        exp.clicked.connect(self.Exp)

        pi=QtGui.QPushButton("pi",self)
        pi.setGeometry(370,50,60,70)
        pi.clicked.connect(self.Pi)

        power=QtGui.QPushButton("^",self)
        power.setGeometry(250,50,60,70)

        inv=QtGui.QPushButton("1/x",self)
        inv.setGeometry(430,260,60,70)
        inv.clicked.connect(self.Inverse)
        
        
        equal = QtGui.QPushButton("=",self)
        equal.setGeometry(250,330,120,70)
        equal.clicked.connect(self.Equal)
        equal.setStyleSheet("color:white;background-color:#222222;font-size:22px")

        ln = QtGui.QPushButton("ln",self)
        ln.setGeometry(370,330,60,70)
        ln.clicked.connect(self.Log)

        log = QtGui.QPushButton("log",self)
        log.setGeometry(430,330,60,70)
        log.clicked.connect(self.Log10)

        c = QtGui.QPushButton("C",self)
        c.setGeometry(70,50,60,70)
        c.clicked.connect(self.C)
        c.setStyleSheet("font-size:20px;color:white;background-color:#333333;")

        ce = QtGui.QPushButton("CE",self)
        ce.setGeometry(10,50,60,70)
        ce.clicked.connect(self.CE)
        ce.setStyleSheet("font-size:20px;color:white;background-color:#333333;")

        back = QtGui.QPushButton("Back",self)
        back.setGeometry(130,50,120,70)
        back.clicked.connect(self.Back)
        back.setStyleSheet("font-size:20px;color:white;background-color:#333333;")
        
        nums = [zero,one,two,three,four,five,six,seven,eight,nine]
        ops = [back,c,ce,div,multiply,minus,plus,power,exp,pi,deg,rad,equal]
        trig=[sin,cos,tan,asin,acos,atan]
        rest = [switch,squared,sqrt,fact,point,ln,log,inv,mod]

        for i in nums:
            i.setStyleSheet("color:red;background-color:black;font-size:12px")
            i.clicked.connect(self.Nums)

        for i in ops[3:12]:
            i.setStyleSheet("color:green;background-color:black;font-size:12px")
            
        for i in trig:
            i.setStyleSheet("color:purple;background-color:black;")

        for i in rest:
            i.setStyleSheet("color:blue;background-color:black;")

        for i in ops[3:8]:
            i.clicked.connect(self.Operator)

        self.setGeometry(550,280,500,420)
        self.setFixedSize(500,420)                                                      #Window Configurations
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QtGui.QIcon("‪calculator.png"))
        self.show()

    def Nums(self):
        global num
        global newNum
        global opVar
        global check


        if check==1:
            self.line.clear()
        sender = self.sender()

        newNum = int(sender.text())
        setNum = str(newNum)
        self.statusBar().showMessage(sender.text() + ' was pressed')

        if opVar == False:
            self.line.setText(self.line.text() + setNum)


        else:
            self.line.setText(setNum)
            opVar = False
        check=0


    def pointClicked(self):
        global opVar

        if "." not in self.line.text():
            self.line.setText(self.line.text() + ".")


    def Switch(self):
        global num

        num = float(self.line.text())

        num = -num

        numStr = str(num)

        self.line.setText(numStr)

    def Operator(self):
        global num
        global opVar
        global operator
        global sumIt

        sumIt += 1
        if sumIt > 1:
            self.Equal()
            sumIt=1
        num = self.line.text()

        sender = self.sender()

        operator = sender.text()

        opVar = True
            

    def Equal(self):
        global num
        global newNum
        global sumAll
        global operator
        global opVar
        global sumIt
        global check

        newNum = self.line.text()
        sender=self.sender()
        if sender.text()=="=":
            sumIt=0
        if opVar==True:
            self.C()
            self.statusBar().showMessage(' Consecutive operators are not allowed')
            self.line.setText("Syntax Error! Press C")
        else:
            if operator == "+":
                sumAll = float(num) + float(newNum)

            elif operator == "-":
                sumAll = float(num) - float(newNum)

            elif operator == "/":
                sumAll = float(num) / float(newNum)

            elif operator == "*":
                sumAll = float(num) * float(newNum)

            elif operator=="^":
                sumAll=(pow(float(num),float(newNum)))


            self.line.setText(str(sumAll))
            opVar = False
            sumIt=0
        check=1

    def C(self):
        global newNum
        global sumAll
        global operator
        global num
        global sumIt

        self.line.clear()

        num = 0.0
        newNum = 0.0
        sumAll = 0.0
        operator = ""
        sumIt=0
        opVar=False

    def CE(self):
        self.line.clear()
        
    def Back(self):
        self.line.backspace()

    def Sqrt(self):
        global num
        global check

        num = float(self.line.text())
        if num<0:
             self.statusBar().showMessage(str(num) + ' can\'t be negative ')
             self.line.setText("Math Error")
        else:
            n = sqrt(num)
            num = n
            self.line.setText(str(num))
        check=1

    def Squared(self):
        global num
        global check

        num = float(self.line.text())

        n = pow(num,2)

        self.line.setText(str(n))
        check=1

    def Percent(self):
        global num
        global check

        num=float(self.line.text())

        n=num/100

        self.line.setText(str(n))
        check=1

    def Log(self):
        global num
        global check

        num=float(self.line.text())
        if num<=0:
            self.line.setText("Math Error")
            self.statusBar().showMessage('Argument must be greater than 0')
        else:
            n=log(num)
            self.line.setText(str(n))
        check=1

    def Log10(self):
        global num
        global check

        num=float(self.line.text())
        if num<=0:
            self.line.setText("Math Error")
            self.statusBar().showMessage('Argument must be greater than 0')
        else:
            n=log10(num)
            self.line.setText(str(n))
        check=1
    
        

    def Fact(self):
        global num
        global check
        num=float(self.line.text())
        n=int(num)
        if (num-n)>0 or num<0:
            self.line.setText("Math Error")
            self.statusBar().showMessage(str(num) + ' can\'t be non-integer')
        else:   
            f=1
            i=1
            while(num>=1):
                f=f*i
                i=i+1
                num=num-1
            self.line.setText(str(f))
        check=1
        
    def Exp(self):
        
        global check
        
        n=exp(1)
        self.line.setText(str(n))
        check=1

    def Inverse(self):

        global check
        global num

        num=float(self.line.text())
        if num==0:
            self.line.setText("Math Error")
            self.statusBar().showMessage('Argument can\'t be 0 as value will tend to infinity')
        else:
            n=1/num
            self.line.setText(str(n))
        check=1

    def Pi(self):

        global check

        n=atan(1)*4
        self.line.setText(str(n))
        check=1

    def trig(self):

        global num
        global sumAll
        global operator
        global check

        num = self.line.text()
        sender = self.sender()
        operator = sender.text()
        
        if operator=="sin":
            sumAll=float(sin(float(num)))
            self.line.setText(str(sumAll))
            
        elif operator=="cos":
            sumAll=float(cos(float(num)))
            self.line.setText(str(sumAll))
            
        elif operator=="tan":
            if float(num)==2*atan(1):
                self.line.setText("Math Error")
                self.statusBar().showMessage('Argument can\'t be 90 degrees as value =infinity')
            else:
                sumAll=float(tan((float(num))))
                self.line.setText(str(sumAll))
                
        elif operator=="atan":
            sumAll=float(atan(float(num)))
            self.line.setText(str(sumAll))
            
        elif operator=="asin":
            if float(num)<-1 or float(num)>1:
                self.line.setText("Math Error")
                self.statusBar().showMessage('Argument must be between 1 and -1')
            else:
                sumAll=float(asin(float(num)))
                self.line.setText(str(sumAll))
                
        elif operator=="acos":
            if float(num)<-1 or float(num)>1:
                self.line.setText("Math Error")
                self.statusBar().showMessage('Argument must be between 1 and -1')
            else:
                sumAll=float(acos(float(num)))
                self.line.setText(str(sumAll))
        
        check=1

    def Conversion(self):

        global num
        global sumAll
        global operator
        global check

        num = float(self.line.text())
        sender = self.sender()
        operator = sender.text()

        if operator=="ToRadians":
            sumAll=float(radians(num))
        elif operator=="ToDegrees":
            sumAll=float(degrees(num))
        self.line.setText(str(sumAll))
        check=1
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    main= Main()
    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
