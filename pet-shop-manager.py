'''
This application is made to hold records of products sold in a pet shop. 

Author: Clarissa G. Rodriguez

'''

def showMenu():
    print('Options: ')
    print('1. Add a product')
    print('2. View a product')
    print('3. View all products')
    print('4. Delete a product')
    print('5. Delete all products')
    print('0. Exit')
    choice = int(input('Enter choice: '))
    return choice

def addProduct():
    prodNo      = input("Product no.(P00x): ")
    brand       = input('Brand: ')
    typeProd    = input('Type: ')
    weight      = input('Weight: ')
    stock       = input('Stock (pcs): ')
    prodData    = {}
    prodData['Brand']       = brand
    prodData['Type']        = typeProd
    prodData['Weight']      = weight
    prodData['Stock']       = stock   
    records[prodNo]         = prodData

def viewProduct():
    prodNum = input('Enter product no.: ')
    if prodNum in records:
        aProd = records[prodNum]
        print('-------------------------------------')
        print('Brand: ','\t\t',"|",aProd['Brand'])
        print('Type: ','\t\t\t',"|",aProd['Type'])  
        print('Weight: ','\t\t',"|",aProd['Weight'])
        print('Stock (pcs): ','\t\t',"|",aProd['Stock'])
        print() 
    else:
        print('No product found')
 
def view_all():
    contentPy = (len(records))
    if contentPy > 0:
            print('\nHere are the records we have so far:')
            print('--------------------------------------------')
            for k in records:
                print("Product no.: ",'\t\t',"|",k)
                prodData = records[k]
                print('Brand: ','\t\t',"|",prodData['Brand'])
                print('Type: ','\t\t\t',"|",prodData['Type'])  
                print('Weight: ','\t\t',"|",prodData['Weight'])
                print('Stock (pcs): ','\t\t',"|",prodData['Stock'])
                print()
    else:
        print('No record found')

def delProduct():
    aProd = input('Enter product no.: ')
    if aProd in records:
        print('You have deleted:')
        print(records[aProd])
        del records[aProd]

def del_all():
    proceed = input('All records will be permanently deleted. Do you want to continue? (y/n): ')
    if proceed == 'y':
        records.clear()
        print('All records have been deleted.')
    elif proceed == 'n':
        print('Cancelled')
    else:
        print('Invalid input')

records = {}

while True:
    c = showMenu()
    if c == 1:
        addProduct()
    elif c == 2:
        viewProduct()
    elif c == 3:
        view_all()
    elif c == 4:
        delProduct()
    elif c == 5:
        del_all()
    elif c == 0:
        print('Thank you for using the application.')
        break
    else:
        print('Invalid input')
