# Binary Search with Python

My objective is to compare the efficiency of binary search vs. linear search methods.
For this example I am using sample data provided by python's 'faker' library, which gave me 10,000 sample names (first + last).
`utils.py` pulls these names into a list that is used by `search_binary.py` and `search_linear.py` to return the index of a certain value (key).

In order to see the difference, we will search for every name in the list using both methods, and compare the results.

## To reproduce locally:
1. Fork this repository to your local machine & cd into the repository
2. From the command-line, `enter pip3 install faker`
3. from the command line (Linux/MacOS), create the 'names.txt' file by using the following command:
- `python3 name_generator.py 10000 > names.txt`
4. Finally, enter the following two commands and compare the results:
- `time python3 search_linear.py`
- `time python3 search_binary.py`


## Results from my machine
`python3 search_linear.py  2.19s user 0.01s system 99% cpu 2.199 total`

`python3 search_binary.py  0.06s user 0.01s system 95% cpu 0.073 total`





    
