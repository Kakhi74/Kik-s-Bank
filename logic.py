from datetime import date
import os


def clearConsole():
    command = 'clear'
    # if Machine is running on Windows, use cls
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

class KiksBank:

    def __init__(self, Purchase_dept, Refund):
        self.dept = Purchase_dept
        self.refund = Refund


    def sum_dept(self):
        total = 0
        for cost in self.dept.values():
            for price in cost:
                total += price
        return total


    def sum_refund(self):
        total = 0
        for cost in self.refund.values():
            for price in cost:
                total += price
        return total


    def show_dept(self):
        graph = "\n\n                                        ______________________________________________\n" + "                                        ----------------- DEPT TABLE -----------------" + "\n                                        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾"
        for item, cost in self.dept.items():
            count = 0
            total = 0
            endline = " ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n"
            purshase = '\n\n\n' + f"< {item} >" + "\n"
            graph += purshase + " _________________________________\n"
            for dollar in cost:
                count += 1
                total += dollar
                item_price = f"{dollar:.2f}"
                price = f"| ● | Current... |    {item_price:^6} CAD$ |" + "\n"
                graph += price
                if count == len(cost):
                    total_line = f"[SUBTOTAL  =  {total:.2f} CAD$]"
                    graph += endline + total_line + "\n\n"
        graph += "\n\n\n" + "[ * ]   . . .   Your total DEPT goes up to   . . .\n\n"
        graph += f"[ ▪ ]  TOTAL DEPT =  {self.sum_dept():.2f} CAD$\n\n\n\n"
        return graph


    def show_refund(self):
        graph = "\n\n                                        ______________________________________________\n" + "                                        ---------------- REFUND TABLE ----------------" + "\n                                        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾"
        for item, cost in self.refund.items():
            count = 0
            total = 0
            endline = " ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n"
            purshase = '\n\n\n' + f"< {item} >" + "\n"
            graph += purshase + " _________________________________\n"
            for dollar in cost:
                count += 1
                total += dollar
                item_price = f"{dollar:.2f}"
                price = f"| ● | Current... |    {item_price:^6} CAD$ |" + "\n"
                graph += price
                if count == len(cost):
                    total_line = f"[SUBTOTAL  =  {total:.2f} CAD$]"
                    graph += endline + total_line + "\n\n"
        graph += "\n\n\n" + "[ * ]   . . .   Your total REFUND goes up to   . . .\n\n"
        graph += f"[ ▪ ]  TOTAL REFUND =  {self.sum_refund():.2f} CAD$\n\n\n\n"
        return graph


    def add_dept(self):
        item = input("Enter description of the item purshased: ")
        price = input("\nEnter the price of the item: ")

        switch = True
        start = 0
        stop = len(self.dept.keys())
        dept_keys = list(self.dept.keys())
        for obj in dept_keys:
            start += 1
            if item.upper() == obj.upper():
                switch = False
                self.dept[obj].append(float(price))
                item = obj
                break
            if (switch and start == stop):
                self.dept[item] = [float(price)]
        
        graph = "\n\n                                        ______________________________________________\n" + "                                        ---------------- ADDING DEPT -----------------" + "\n                                        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾"
        endline = " ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n"
        purshase = '\n\n\n' + f"< {item} >" + "\n"
        graph += purshase + " _________________________________\n"

        count = 0
        total = 0
        for dollar in self.dept[item]:
            count += 1
            total += dollar
            item_price = f"{dollar:.2f}"
            price = f"| ● | Current... |    {item_price:^6} CAD$ |" + "\n"

            if count == len(self.dept[item]):
                if len(self.dept[item]) > 1:
                    graph += endline
                price = " _________________________________\n" + f"| + | Adding ... |    {item_price:^6} CAD$ |" + "\n"
                if len(self.dept[item]) == 1:
                    price = f"| + | Adding ... |    {item_price:^6} CAD$ |" + "\n"
                graph += price
                total_line = f"[SUBTOTAL  =  {total:.2f} CAD$]"
                graph += endline + total_line + "\n\n"
                break
            graph += price

        graph += "\n\n\n" + "[ + ]   . . .   Your Purchasing Dept has been Recalculated   . . .\n\n"

        graph += f"[ ▪ ]  NEW TOTAL DEPT =  {self.sum_dept():.2f} CAD$\n\n\n\n"

        return graph


    def add_refund(self):
        item = input("\nProvide description of the item refunded (optionnal)\n\n                         OR\n\nIGNORE & press ENTER to perform a refund in cash : ")
        price = input("\n\nEnter the cost of the refund: ")

        today = date.today()
        d1 = today.strftime("%b-%d-%Y")
        if item == '':
            item = f"Refund {d1}"
        switch = True
        start = 0
        stop = len(self.refund.keys())
        refund_keys = list(self.refund.keys())
        for obj in refund_keys:
            start += 1
            if item.upper() == obj.upper():
                switch = False
                self.refund[obj].append(float(price))
                item = obj
                break
            if (switch and start == stop):
                self.refund[item] = [float(price)]
        
        graph = "\n\n                                        ______________________________________________\n" + "                                        ---------------- ADDING REFUND ---------------" + "\n                                        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾"
        endline = " ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n"
        purshase = '\n\n\n' + f"< {item} >" + "\n"
        graph += purshase + " _________________________________\n"

        count = 0
        total = 0
        for dollar in self.refund[item]:
            count += 1
            total += dollar
            item_price = f"{dollar:.2f}"
            price = f"| ● | Current... |    {item_price:^6} CAD$ |" + "\n"

            if count == len(self.refund[item]):
                if len(self.refund[item]) > 1:
                    graph += endline
                price = " _________________________________\n" + f"| + | Adding ... |    {item_price:^6} CAD$ |" + "\n"
                if len(self.refund[item]) == 1:
                    price = f"| + | Adding ... |    {item_price:^6} CAD$ |" + "\n"
                graph += price
                total_line = f"[SUBTOTAL  =  {total:.2f} CAD$]"
                graph += endline + total_line + "\n\n"
                break
            graph += price

        graph += "\n\n\n" + "[ + ]   . . .   Your Refund Balance has been Recalculated   . . .\n\n"

        graph += f"[ ▪ ]  NEW TOTAL REFUND  =  {self.sum_refund():.2f} CAD$\n\n\n\n"

        return graph


    def show_new_balance(self):
        balance = self.sum_dept() - self.sum_refund()
        output = "\n\n______________________________________________\n" + "----------- NEW BALANCE DIFFERENCE -----------" + "\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n\n\n"
        dept = f"[ + ]  . . .  TOTAL DEPT  =   {self.sum_dept():.2f} CAD$\n\n"
        refund = f"[ - ]  . . .  TOTAL REFUND  =   {self.sum_refund():.2f} CAD$\n\n\n\n"
        message = "*** Your balance has been recalculated ***\n\n\n\n"
        new_balance = f"[ = ]  . . .  NEW BALANCE  =   {balance:.2f} CAD$\n\n\n\n"
        output += dept + refund + message + new_balance
        return output


    def get_dept_refund(self):
        return [self.dept, self.refund]

    
    def delete_dept(self):
        dept_list = list(self.dept.keys())
        count = 0
        dept_dict = {}
        for dept in dept_list:
            count += 1
            dept_dict[str(count)] = dept
            print(f"[ {count} ]", " - ", dept)
        print("\n\n\n")
        num = input("Enter the number of the category you wish to delete from: ")
        clearConsole()
        item = dept_dict[num]
        price_list = self.dept[item]
        countt = 0
        price_dict = {}
        for price in price_list:
            countt += 1
            price_dict[str(countt)] = price
            print(f"[ {countt} ]", " - ", f"{price:.2f} CAD$")
        print("\n\n\n")
        num2 = int(input("Enter the number of the dept you wish to delete: ")) - 1
        clearConsole()
        pricee = self.dept[item][num2]
        self.dept[item].pop(num2)

        graph = "\n\n                                        ______________________________________________\n" + "                                        ---------------- DELETE DEPT -----------------" + "\n                                        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾"
        endline = " ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n"
        purshase = '\n\n\n' + f"< {item} >" + "\n"
        graph += purshase + " _________________________________\n"
        count = 0
        total = 0
        for dollar in self.dept[item]:
            count += 1
            total += dollar
            item_price = f"{dollar:.2f}"
            price = f"| ● | Current... |    {item_price:^6} CAD$ |" + "\n"
            graph += price

        if len(self.dept[item]) >= 1:
            graph += endline

        item_price = f"{pricee:.2f}"
        price = " _________________________________\n" + f"| - | Deleting...|    {item_price:^6} CAD$ |" + "\n"

        if len(self.dept[item]) == 0:
            price = f"| - | Deleting...|    {item_price:^6} CAD$ |" + "\n"
        graph += price
        total_line = f"[SUBTOTAL  =  {total:.2f} CAD$]"
        graph += endline + total_line + "\n\n"

        graph += "\n\n\n" + "[ + ]   . . .   Your Purchasing Dept has been Recalculated   . . .\n\n"

        graph += f"[ ▪ ]  NEW TOTAL DEPT =  {self.sum_dept():.2f} CAD$\n\n\n\n"

        if self.dept[item] == []:
            del self.dept[item]

        return graph


    def delete_refund(self):
        refund_list = list(self.refund.keys())
        count = 0
        refund_dict = {}
        for refund in refund_list:
            count += 1
            refund_dict[str(count)] = refund
            print(f"[ {count} ]", " - ", refund)
        print("\n\n\n")
        num = input("Enter the number of the category you wish to delete from: ")
        clearConsole()
        item = refund_dict[num]
        price_list = self.refund[item]
        countt = 0
        price_dict = {}
        for price in price_list:
            countt += 1
            price_dict[str(countt)] = price
            print(f"[ {countt} ]", " - ", f"{price:.2f} CAD$")
        print("\n\n\n")
        num2 = int(input("Enter the number of the Refund you wish to delete: ")) - 1
        clearConsole()
        pricee = self.refund[item][num2]
        self.refund[item].pop(num2)

        graph = "\n\n                                        ______________________________________________\n" + "                                        ---------------- DELETE REFUND -----------------" + "\n                                        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾"
        endline = " ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n"
        purshase = '\n\n\n' + f"< {item} >" + "\n"
        graph += purshase + " _________________________________\n"
        count = 0
        total = 0
        for dollar in self.refund[item]:
            count += 1
            total += dollar
            item_price = f"{dollar:.2f}"
            price = f"| ● | Current... |    {item_price:^6} CAD$ |" + "\n"
            graph += price

        if len(self.refund[item]) >= 1:
            graph += endline
        
        item_price = f"{pricee:.2f}"
        price = " _________________________________\n" + f"| - | Deleting...|    {item_price:^6} CAD$ |" + "\n"

        if len(self.refund[item]) == 0:
            price = f"| - | Deleting...|    {item_price:^6} CAD$ |" + "\n"
        graph += price
        total_line = f"[SUBTOTAL  =  {total:.2f} CAD$]"
        graph += endline + total_line + "\n\n"

        graph += "\n\n\n" + "[ + ]   . . .   Your Refund Balance has been Recalculated   . . .\n\n"

        graph += f"[ ▪ ]  NEW TOTAL DEPT =  {self.sum_refund():.2f} CAD$\n\n\n\n"

        if self.refund[item] == []:
            del self.refund[item]

        return graph
