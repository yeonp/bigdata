# 파일제어실습문제.py
# class 사용

class Item:
    def __init__(self, itemname, price):
        self.itemname = itemname
        self.price = price
        self.quantity = 0
        self.amount = 0

    def setSaleData(self, quantity, amount):
        self.quantity = quantity
        self.amount = amount
        return

    def setQuantity(self, quantity):
        self.quantity += int(quantity)
        self.CalcAmount()
        return

    def CalcAmount(self):
        self.amount = self.price * self.quantity
        return

    def writeItem(self, f):
        f.write(self.itemname + ' ')
        f.write(str(self.price) + ' ')
        f.write(str(self.quantity) + ' ')
        f.write(str(self.amount) + '\n')
        return

    def __repr__(self):
        return '{0:<10} {1:>5} {2:>3} {3:>8}'. \
            format(self.itemname, self.price, self.quantity, self.amount)


class Sales:
    def __init__(self):
        self.salesInfo = {}
        self.readSalesInfo()

    def readSalesInfo(self):
        try:
            with open('items.txt', 'r') as f:
                while True:
                    data = f.readline()
                    if not data:
                        break
                    itemdata = list(data.split())
                    item = Item(itemdata[0], int(itemdata[1]))
                    item.setSaleData(int(itemdata[2]), int(itemdata[3]))
                    self.salesInfo[item.itemname] = item
        except FileNotFoundError:
            pass

        return

    def saveSalesInfo(self):
        with open('items.txt', 'w') as f:
            for key in self.salesInfo:
                self.salesInfo[key].writeItem(f)
        return

    def registrationItemInfo(self, itemInfo):
        self.salesInfo[itemInfo.itemname] = itemInfo
        return

    def updateItemInfo(self, itemInfo):
        self.salesInfo[itemInfo.itemname] = itemInfo
        return

    def searchItemInfo(self, item):
        return self.salesInfo.get(item)

    def printSalesTable(self):
        with open('salesTable.txt', 'w') as f:
            print('\n\t     {0:*^19}\n'.format(' Sales Table '))
            f.write('\n\t     {0:*^19}\n\n'.format(' Sales Table '))
            for key in self.salesInfo:
                print('\t' + str(self.salesInfo[key]))
                f.write('\t' + str(self.salesInfo[key]) + '\n')


class SalesView:
    def __init__(self):
        self.sales = Sales()

    def menu(self):
        menu = '''
1. 품목 정보 등록
2. 판매 정보 등록
3. 판매 현황표 출력
0. 종료
select menu : '''
        func_dict = {1: self.inputItem, 2: self.inputSaleInfo, 3: self.printSalesTable}

        while True:
            print(menu, end=' ')
            selectMenu = int(input())

            if selectMenu == 0:
                self.sales.saveSalesInfo()
                break
            elif 1 <= selectMenu <= 3:
                func_dict[selectMenu]()
        return

    def inputItem(self):
        print('\n')
        item = input('Input item name : ')
        price = int(input('Input price : '))

        itemInfo = Item(item, price)
        self.sales.registrationItemInfo(itemInfo)
        return

    def inputSaleInfo(self):
        print('\n')
        item = input('Input item name : ')

        itemInfo = self.sales.searchItemInfo(item)
        if itemInfo != None:
            quantity = int(input('Input quantity : '))

            itemInfo.setQuantity(quantity)
            self.sales.updateItemInfo(itemInfo)
        else:
            print('Error : {:<10} not found!!!'.format(item))
        return

    def printSalesTable(self):
        self.sales.printSalesTable()
        return


if __name__ == '__main__':
    salesView = SalesView()
    salesView.menu()
