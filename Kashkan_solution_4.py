#!/usr/bin/python3
import urllib.request
import csv
import re

def book_csv_analyzer(url="https://pastebin.com/raw/tNmieVFn", delimiter = ';'):
    """Parcing CSV file of books price list and checking correctness of its' values.
    If pandas would be allowed it would be possible to do without a single loop...

    Args:
        url (str, optional): Web location of the CSV file. Defaults to "https://pastebin.com/raw/tNmieVFn".
        delimiter (str, optional): Delimiter of CSV file. Defaults to ';'.
    """
    
    response = urllib.request.urlopen(url)
    book_list = csv.reader(response.read().decode().splitlines(), delimiter=delimiter)
    # price_pattern purposely does not match negative numbers (which occur in our csv file)
    price_pattern = re.compile(r'^(\d+(?:[.,]\d{1,2})?)\s*(Kč|€)$')
    # Quick check showed that we don't have any ISBN-13 values here - all lines are clearly in ISBN10 format (without hyphens and spaces).
    # Knowing this makes search much easier - we don't need to invent monsterous regex patterns, which anyway are not ideal for ISBN search. 
    # In this case simple r'^\d{9}[\dX]$' will do the job.
    # I was thinking about ISBN verification with ISBNdb API, but it allows only 1 request per minute. Which is too slow.
    ISBN_pattern = re.compile(r'^\d{9}[\dX]$')

    for number, row in enumerate(book_list):
        number +=1  # enumerate work from 0, we want to count from 1
        if all(len(x) == 0 for x in row):
            print(f'Error! Line {number} is empty')
        elif len(row) != 4:
            print((f'Error! {len(row)} columns on line {number}!'))
        else: # if row is screwed - no reason to check further
            # if not - we have to check it by several separate `if's`, not by `if else`s
            if len(row[0].strip()) < 1:
                print(f'Missing title on line: {number}')
            if len(row[1].strip()) < 1:
                print(f'Missing author on line: {number}')
            if re.match(ISBN_pattern, row[2]) is None:
                print(f"Invalid ISBN on line: {number}")
            if re.match(price_pattern, row[3]) is None:
                print(f"Invalid price on line: {number}")

if __name__ == "__main__":
    user_url = input("Enter the url of the CSV file (no value == default url): ")
    user_delimiter = input("What is delimiter of this file? (no value == default url): ")
    if len(user_url.strip()) == 0 or len(user_delimiter.strip()) == 0:
        print("Test of the standard file:")
        print("***************************")
        book_csv_analyzer()
    else:
        book_csv_analyzer(user_url, user_delimiter)
