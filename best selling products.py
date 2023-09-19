import csv

sales_data = []

with open('supermarket_sales.csv', 'r') as file:
    reader = csv.reader(file)
    #Initialize an empty list to hold the data
    #Interate over each row in the CSV file
    for row in reader:
        #append the row to the data list
        sales_data.append(row)

list_len =  len(sales_data)
product_id = []
x = 1
while(x<list_len):
    if(sales_data[x][2] not in product_id):
        product_id.append(sales_data[x][2])
    x = x + 1    

product_qty = []

len_product_id = len(product_id)

count = 0


while(count<len_product_id):
    innerCount = 1
    totalQty = 0
    testList = []
    while(innerCount<list_len):
        if(product_id[count]==sales_data[innerCount][2]):
            totalQty = totalQty + float(sales_data[innerCount][4])
        innerCount = innerCount + 1
    testList.insert(0,product_id[count])
    testList.insert(1,totalQty)
    product_qty.append(testList)
    count = count + 1
#print(product_sales)

sorted_products_id_sales = sorted(product_qty,key = lambda x: x[1], reverse=True)
sorted_len = len(sorted_products_id_sales)
sorted_count = 0
while(sorted_count<sorted_len):
    print(sorted_products_id_sales[sorted_count])
    sorted_count = sorted_count + 1