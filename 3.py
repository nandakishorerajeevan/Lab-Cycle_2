import numpy as np

child_fee = 1.50
adult_fee = 4.00
total_tickets = 2200.00
collection = 5050.00

x, y = np.linalg.solve([[1, 1], [child_fee, adult_fee]], [total_tickets, collection])

print("\nFEE DETAILS")
print("-----------")
print("  - Child Ticket Fee : $", child_fee)
print("  - Adult Ticket Fee : $", adult_fee)
print("\nTotal Tickets Sold : ", int(total_tickets))
print("Total Collection : $", int(collection))
print("\ntotal CHILDREN participated : ", int(x))
print("total ADULTS participated : ", int(y), "\n")
