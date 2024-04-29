# Daniela Baptiste
"""
This program to compute the rental cost of videos and oldies for some number of days
Algorithm:
1. Videos rent for $3.00 a day
2. Oldies rent for $2.00 a day
3. Ask the user for how many Days
4. Ask the user how many videos
5. Ask the user how many oldies
6. compute the bill bill = Days * videos * $3.00 * Days * oldies * $2.00
7. Output the result
"""
VideoCost = 3.0
OldiesCost = 2.0
Days = int(input(" How many days will be renting for?"))
NumVideos = int(input("How many videos do you want?"))
NumOldies = int(input("How many oldies?"))

Bill = Days * NumVideos * VideoCost * Days * NumOldies * OldiesCost
print("Your bill is $", Bill, "for", NumVideos, "videos and ", NumOldies, "oldies")
