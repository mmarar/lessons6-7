# coding: utf-8
x = 0
y = 0
znak = ""
input_correct = False

while input_correct == False:
    x = int(input("Enter number on horizontal\t"))
    y = int(input("Enter number on vertical\t"))
    znak = raw_input("Select mark: X or O\t").upper()
    
    if x < 1 or x > 3 or y < 1 or y > 3 or znak != "0" and znak != "X":
        print (u"Значения X и Y должны быть от 1 до 3")
    else:
        print "%s,%s:%s" % (x, y, znak)
        input_correct = True

