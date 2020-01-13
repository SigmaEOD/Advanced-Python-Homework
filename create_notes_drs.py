import os
def main():
    #Current Directory
    currentdir = os.getcwd() 
    #Directory To make
    directory = "CyberSecurity-Notes"
    #Specifies Location
    location = os.path.join(currentdir, directory)
    #Makes Location
    os.makedirs(location)
    #Specifies the Start of the counter for week
    start = 1
    #Makes Week Folders
    while start < 25:
        week_num = ("Week " + str(start))
        start = start + 1
        location2 = os.path.join(currentdir, directory, week_num)
        os.makedirs(location2)
    #Makes the Week folders into a list to be used in the Day folder creation
    weeks = os.listdir(path=location)
    #Creates Day Folders
    for week in weeks:
        days = ["Day 1", "Day 2", "Day 3"]
        for day in days:
            days = os.path.join(directory, week, day)
            os.makedirs(days)
#Runs The Program
main()
    