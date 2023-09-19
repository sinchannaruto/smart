import csv

sales_data = []


with open('supermarket_sales.csv', 'r') as file:
    reader = csv.reader(file)
    # Initialize an empty list to hold the data
    # Iterate over each row in the CSV file
    for row in reader:
        # Append the row to the data list
        sales_data.append(row)
list_len = len(sales_data)
customer_id = []
x = 1
while(x<list_len):
    if(sales_data[x][1] not in customer_id):
        customer_id.append(sales_data[x][1])
    x = x + 1
#print(customer_id)

customer_totAmount = []

len_customer_id = len(customer_id)

count = 0

while(count<len_customer_id):
    innerCount = 1
    totalSales = 0
    testList = []
    while(innerCount<list_len):
        if(customer_id[count]==sales_data[innerCount][1]):
            totalSales = totalSales + float(sales_data[innerCount][7])
        innerCount = innerCount + 1
    testList.insert(0,customer_id[count])
    testList.insert(1,totalSales)
    customer_totAmount.append(testList)
    count = count + 1
print("=======Based on Total Amount Spent=============")
print(customer_totAmount)
print("=======================================")

customer_totQty = []

count = 0

while(count<len_customer_id):
    innerCount = 1
    totalQty = 0
    testList = []
    while(innerCount<list_len):
        if(customer_id[count]==sales_data[innerCount][1]):
            totalQty = totalQty + float(sales_data[innerCount][4])
        innerCount = innerCount + 1
    testList.insert(0,customer_id[count])
    testList.insert(1,totalQty)
    customer_totQty.append(testList)
    count = count + 1

print("=======Based on Total Quantity=============")
print(customer_totQty)
print("=======================================")

