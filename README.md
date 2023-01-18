# Ticket Machine - Python project 

#### This System asks you what activity you've come to complete and gives you a turn number based on the activity you chose.
#### In this example, you are going to design it for a drugstore that focuses on perfumery, pharmaceuticals, and cosmetics.
#### Your program will ask the consumer which of the places they wish to visit, and depending on the area they choose, 
#### it will assign them a relevant turn number.

#### For example:If you select cosmetics, it will return the letter C (as in cosmetics), - (hyphen) 54. Following that, 
#### it will ask us if we want to take another number to simulate the arrival of a new client, and the process will be repeated.

#### Customers will take different numbers for different areas (perfumes, medicine, cosmetics) indifferent orders, 
#### so the system must keep track of how many numbers it has given for each of those areas and produce the next number 
#### for each as they request it.You probably already realize that we need to use generators and their efficiency to 
#### accomplishthis.The message in which we inform the customer that they are waiting for a number should include some 
#### additional text before and after the number.