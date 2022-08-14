# counties=["Arapahoe","Denver","Jefferson"]

# for county in range(len(counties)):
#     print(counties[county])

# counties_dict={"Arapahoe":422829,"Denver":463353,"Jefferson":432438}

# for key,value in counties_dict.items():
#     print(f"{key} county has {value:,} registered voters. ")

voting_data = [{"county":"Arapahoe","registered_voters":422829},
                {"county":"Denver","registered_voters":463353},
                {"county":"Jefferson","registered_voters":432438}]

# print all values
# for county in voting_data:
#     for voters in county.values():
#         print(voters)

# print registered_voters
# for county_dict in voting_data:
#         print(county_dict['registered_voters'])

for county_dict in voting_data:
    print(f"{county_dict['county']} county has {county_dict['registered_voters']:,} registered voters. ")

# candidate_votes=int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))

# message_to_candidate = (
#     f"You received {candidate_votes:,} number of votes. "
#     f"The total number of votes in the election was {total_votes:,}. "
#     f"You received {(candidate_votes/total_votes)*100:.2f}% of the total votes. ")

# print(message_to_candidate)

# --------------------------------------------------------

# Import the datetime class
import datetime as dt

# Use the no() attribute to get present time
now=dt.datetime.now()
print("The time is ",now)