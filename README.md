# Election Analysis

## Project Overview
The purpose of this project was to analyze voter data in order to complete an election audit for a State Representative election for the election commission. Using Python, our goal was to execute the following: 

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received and calculate the percentage of votes each candidate won.
4. Determine the winner of the election based on popular vote.

In addition, the election commission requested the following: 

5. Calculate the voter turnout for each county.
6. Calculate the percentage of votes from each county our of the total count of votes.
7. Determine the county with the highest voter turnout. 

## Resources
-Data Source: election_results.csv
-Software: Python 3.9.2, Visual Studio Code, 1.38.1

## Analysis of Election Audit
- The analysis started by adding our dependencies, assign a variable to load a file from a path and assign a variable to save the file to a path.

![Image_1](https://user-images.githubusercontent.com/79758494/113524971-d0b37200-9577-11eb-8a55-e7eb9f5b2436.PNG)

- The total votes counter was then initialized. A list was created in order to identify all candidates names, and a dictionary was created for candidate votes. Another list was created in order to identify all counties within the data, and a dictionary was created for county votes. 

![Image_2](https://user-images.githubusercontent.com/79758494/113525126-c9409880-9578-11eb-86e6-2c2dc1ff1560.PNG)

- In order to track the winning candidate, vote count, and percentage, variables were created. Variables were also created to track the largest county and county voter turnout. 

![Image_3](https://user-images.githubusercontent.com/79758494/113525213-410ec300-9579-11eb-8492-e1c3c1daf847.PNG)

- In order to begin interpreting the data, we first needed to use Visual Studio Code to read the csv and convert it into a list of dictionaries. We then opened the data source (election_data). This is also where we created total_votes variable and started counting the total number of votes within the data source. 

![Image_4](https://user-images.githubusercontent.com/79758494/113525492-e8d8c080-957a-11eb-9e82-8fd165b21eeb.PNG)

- The candidates names were pulled from each row, and by using an if statement, made a list of candidates names, started tracking each candidates voter count and the votes for each candidate started being tallied. 

![Image_5](https://user-images.githubusercontent.com/79758494/113525493-ea09ed80-957a-11eb-8711-b82dbfe0e231.PNG)

- Similarly, an if statement was used to identify and make a list of each county, tracked counties votes, and began tallying those votes for each county. 

![Image_6](https://user-images.githubusercontent.com/79758494/113525495-eaa28400-957a-11eb-881a-7da4a5869297.PNG)

- The text file was opened and the Election results were saved onto that text file. 

![Image_7](https://user-images.githubusercontent.com/79758494/113525496-ebd3b100-957a-11eb-87b7-c9687807da87.PNG)

- A for loop was then created to retrieve the county vote count and to calculate the percentage of votes for each county. Those calculations were then printed to the terminal and the county results were saved to the text file. An if statement was then used to determine the winning county. The winning county was then printed to the terminal  and saved to the text file. 

![Image_8](https://user-images.githubusercontent.com/79758494/113525498-ed04de00-957a-11eb-9f80-275a554f510f.PNG)

- The same steps above were used to retrieve the vote count and percentage for each candidate, to determine the winner of the election, to print that information to the terminal and to save it to the text file. 

![Image_9](https://user-images.githubusercontent.com/79758494/113525499-ee360b00-957a-11eb-891a-ecb68b0ccde2.PNG)


## Election Audit Results

The analysis of the election show that:

1. There were 369,711 total votes cast.
2. . The candidates were:
	- Charles Casper Stockham
	- Diana DeGette
	- Raymon Anthony Doane
3. The candidate results were:
	- Charles Casper Stockham: 23.0% (85,213)
	- Diana DeGette: 73.8% (272,892)
	- Raymon Anthony Doane: 3.1% (11,606)
4. The winner of the election was:
	- Diana DeGette with 272,892 votes, which was 73.8% of the total votes. 
5. There were three counties identified in the data and their voter turnout is as follows: 
	- Jefferson: 38,855
	- Denver: 306,055
	- Arapahoe: 24,801
6. The percentage of votes in each county from the total votes is as follows: 
	  - Jefferson: 10.5% 
	  - Denver: 82.8% 
	  - Arapahoe: 6.7% 

This data can also be seen in the text file: 

![Image_10](https://user-images.githubusercontent.com/79758494/113525916-51c13800-957d-11eb-9b5b-eef42d35cd99.PNG)

## Election Audit Summary
This script can be used for any future election audit given the csv file is formatted similarly as the one this script was created for. That is one way this code could be modified, to be able to control for the potential for information being formatted differently within the csv file.
 
 
