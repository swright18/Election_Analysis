# counties_dict = {}
# counties_dict['Aparpahoe']=422829
# counties_dict['Denver']=463353
# counties_dict['Jefferson']=432438
# print(counties_dict)

# print(len(counties_dict))

# print(counties_dict.items())

# print(counties_dict.keys())

# print(counties_dict.values())

# print(counties_dict.get('Denver'))

# voting_data=[]
# voting_data.append({'county':'Arapahoe', 'registered_voters': 422829})
# voting_data.append({'county':'Denver', 'registered_voters': 463353})
# voting_data.append({'county':'Jefferson', 'registered_voters': 432438})
# print(voting_data)
# print(len(voting_data))

# voting_data.insert(1,{'county':'El Paso', 'registered_voters': 461149})
# voting_data.remove({'county':'Arapahoe', 'registered_voters':422829})
# voting_data.insert(3,{'county':'Denver', 'registered_voters': 463353})
# voting_data.pop(1)
# voting_data.append({'county':'Arapahoe', 'registered_voters': 422829})
# print(voting_data)

# counties=['Arapahoe','Denver','Jefferson']
# if counties[1]=='Denver':
#     print(counties[1])
# if counties[2] != 'Jefferson':
#     print(counties[2])




# #How many votes did you get? 
# my_votes = int(input('How many votes did you get in the election?'))

# #Total votes in the Election
# total_votes=int(input('What is the total votes in the election?'))

# #Calculate the percentage of votes you recieved.
# percent_votes = (my_votes/total_votes) * 100
# print('I received ' + str(percent_votes) + '% of the total votes.')





# temperature = int(input('What is the temperature outside?'))

# if temperature > 80:
#     print('Turn on the AC')
# else:
#     print('Open the windows.')




# #What is the score? 
# score=int(input("What is your test score?"))
# #Determine the grade
# if score >= 90:
#     print('Your grade is an A.')
# else:
#     if score >= 80:
#         print('Your grade is a B.')
#     else:
#         if score >= 70:
#             print('Your grade is a C.')
#         else:
#             if score >= 60:
#                 print('Your grade is a D.')
#             else:
#                 print('Your grade is an F.')


# #What is the score? 
# score = int(input("What is your test score?"))
# #Determine the grade.
# if score >= 90:
#     print('Your grade is an A.')
# elif score >= 80:
#     print('Your grade is a B.')
# elif score >= 70:
#     print('Your grade is a C.')
# elif score >=60:
#     print('Your grade is a D.')
# else:
#     print('Your grade is an F.')




# counties = ['Arapahoe', 'Denver', 'Jefferson']
# if 'El Paso' in counties:
#     print('El Paso is in the list of counties')
# else:
#     print('El Paso is not in the list of counties')
# if 'Arapahoe' in counties and 'El Paso' in counties:
#     print('Arapahoe and El Paso are in the list of counties.')
# else:
#     print('Arapahoe or El Paso is not in the list of counties.')
# if 'Arapahoe' in counties or 'El Paso' in counties:
#     print('Arapahoe or El Paso is in the list of counties')
# else:
#     print('Arapahoe and El Paso are not in the list of counties')
# if 'Arapahoe' in counties and 'El Paso' not in counties:
#     print('Only Arapahoe is in the list of counties')
# else:
#     print('Arapahoe is in the list of counties and El Paso is not in the list of Counties')





# #While loops
# x=0
# while x<=5:
#     print(x)
#     x=x+1

# count = 7
# while count < 1:
#     print('Hello World')


# #For Loops
# for county in counties: 
#     print(county)


# numbers = [0, 1, 2, 3, 4]
# for num in numbers:
#     print(num)

# for num in range(5):
#     print(num)

# for i in range(len(counties)):
#     print(counties[i])

# counties_tuple = ('Arapahoe', 'Denver', 'Jefferson')
# for i in range(len(counties_tuple)):
#       print(counties_tuple[i])
# for county in counties_tuple:
#     print(county)


#Iterate through Dictionary
# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county in counties_dict:
#     print(county)
# for county in counties_dict.keys():
#     print(county)
# for voters in counties_dict.values():
#     print(voters)
# for county in counties_dict:
#     print(counties_dict[county])

# # #Key-Value Pairs
# for county, voters in counties_dict.items():
#     print(county + 'county has'+ str(voters) + 'registered voters.')

# #Get each Dictionary in a list of dictionaries
# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     print(county_dict)

# for i in range(len(voting_data)):
#     print(voting_data[i])

# #Values from List of Dictionaries
# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)
# for county_dict in voting_data:
#     print(county_dict['registered_voters'])
# for county_dict in voting_data:
#     print(county_dict['county'])





# #PRINTING FORMATS
# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")

# #Using F-string to rewrite
# my_votes = int(input('How many votes did you get in the election?'))
# total_votes = int(input('What is the total votes in the election?'))
# print(f'I recieved {my_votes/total_votes * 100} % of the total votes.')


# #F-strings with dictionaries
# counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
# for county, voters in counties_dict.items():
#     print(county + " county has " + str(voters) + " registered voters.")

# for county, voters in counties_dict.items():
#     print(f'{county} county has {voters} registered voters.')


# #Multiline F-Strings and Floating Decimals
# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes:,} number of votes. "
#     f"The total number of votes in the election was {total_votes:,}. "
#     f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

# print(message_to_candidate)


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f'{county} county has {voters:,} registered voters.')



