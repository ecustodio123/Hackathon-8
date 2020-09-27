# def isbn(self):

import random

isbn = []
isbn.append(str(random.randint(978 , 979)))
isbn.append("-")
isbn.append(str(612))
isbn.append("-")
isbn.append(str(random.randint(10000 , 99999)))
isbn.append("-")
isbn.append(str(random.randint(1 , 99)))
isbn.append("-")
isbn.append(str(random.randint(1 , 10)))

print(isbn)
paisesString = "".join(isbn)
print(paisesString)
