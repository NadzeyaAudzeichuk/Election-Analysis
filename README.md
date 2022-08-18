# election-analysis
PyPoll with Python

# Overview of Election-Audit: 

We will perform an election audit analysis for US Congressional precinct in Colorado. To begin with, we have a *csv* file with tabulated election results. The audit can be easily performed in Excel, but this project aims to automate the process using Python. Thus, the scrip we write can be used to audit not only congressional districts. 

# Election-Audit Results:

Here is a breakdown of the project:
1. Report the total number of votes cast, the voter turnout for each county, the percentage of votes from each county, and the county with the highest turnout.
2. Report the total number of votes, the percentage of votes for each candidate, and the election's winner based on popular vote. 
3. At the end, we generate a vote count report to certify this US congressional race. 

The data is retrieved from *election_results.csv*. Using repetition and conditional statements with logical operators, we have three counties, Arapahoe, Denver, and Jefferson, and three candidates, Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane. 
The total number of votes cast in the election is 369,711. 

With the total cast of votes, counties, and names of the candidates, we can determine voter turnout for each county and the county with the highest turn by using *Lists* and *Dictionaries*. Here are steps in detail for calculating the results:


```
# Create a county list and county votes dictionary.
county_list = []
votes_by_county = {}

# Track the largest county and county voter turnout.
highest_turnout_county = ""
county_turnout = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Get the county name from each row.
        county_name = row[1]

        # If the county does not match any existing county add it to
        # the county list.
        if county_name not in county_list:

            # Add the existing county to the list of counties.
            county_list.append(county_name)

            # Track the county's vote count.
            votes_by_county[county_name] = 0

        # Add a vote to that county's vote count.
        votes_by_county[county_name] += 1

    # For loop to get the county from the county dictionary.
    for county_name in votes_by_county:

         # Retrieve the county vote count.
         votes_count = votes_by_county.get(county_name)

         # Calculate the percentage of votes for the county.
         votes_count_percentage = float(votes_count)/float(total_votes) * 100
               
         # Write an if statement to determine the winning county and get its vote count.
         if (votes_count > county_turnout):
            county_turnout = votes_count
            highest_turnout_county = county_name

    # Print the county with the largest turnout to the terminal and to the file with analysis.
    print(county_winner)
    txt_file.write(county_winner)

```


After running that script, we get:
   - Jefferson 38,855 votes which are 10.5% of the total
   - Denver 306,055 votes which are 82.8% of the total 
   - Arapahoe 24,801 votes which are 6.7% of the total
  
The data shows that Denver has the largest voter turnout.

Similarly, using the same script, but by making slight changes in the code, we can find the total number of votes and its percentage for each candidate and the election winner. 

   - Charles Casper Stockham got 85,213 votes which are 23.0%  
   - Diana DeGette got 272,892 votes which is 73.8%
   - Raymon Anthony Doane got 11,606 votes which is 3.1%  

Based on that, the winner is Diana DeGette, with 272,892 votes cast and won the election with 73.8% based on the popular vote.

The results of the elections are saved in the *election_analysis.txt* file.
![Election_Results.png]()

# Election_Audit Summary:

In summary, as we can see, the audit is done successfully with Python. With some modifications in the script, this kind of analysis can be performed on any election data. It can be used not only in the congressional districts but also in senatorial districts or local elections. Even though the audit can be easily performed in Excel, automating the process with Python is a better choice.