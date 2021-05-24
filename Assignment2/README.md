# CS172 - Assignment 2

## Team member 1 - Cristina Lawson
## Team member 2 - Shray GRover

###### Provide a short explanation of your design

We implemented a way to calculate the tf-idf of a query on a doc and then we ranked the docs from 1-10 based on the query.

The data structure implemented for the ranking was a max heap queue. The ranking was done by the tf-idf value.

According to the specs, we were determined to use imported extensions calculate tf-idf. Simple open/close file extraction was used for the numbers of the beginning of querys, doc similarity collection (docID) was done using Assignment 1 processes, and score was ranked using a heap queue.

###### Language used, how to run your code, if you attempted the extra credit (stemming), etc. 

Language used: Python

How to run code: python3 VSM.py query_list.txt output.txt

Be sure to delete the output.txt file if running more than once because the output only appends and doesn't overwrite the file.
