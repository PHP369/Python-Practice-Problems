#Question Link: https://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html

'''
Question:
Create a dictionary (in your file) of names and birthdays. When you run your program it should 
ask the user to enter a name, and return the birthday of that person back to them.
'''

Bday_list = {
    'Aarin Bhakta': '06-04-2004',
    'Abhay Patel': '05-10-2004',
    'Aditya Panickar': '17-06-2003',
    'Armaan Patel': '10-08-2004',
    'Arpit Kathiriya': '25-06-2003',
    'Darsh Darji': '20-12-2004',
    'Darshil Patel': '12-09-2003',
    'Dev Bandhiya': '05-11-2003',
    'Devrajsinh Solanki': '04-12-2003',
    'Haresh Patel': '08-05-2003',
    'Harsh Jariwala': '28-12-2004',
    'Harshrajsinh Sangdot': '09-01-2004',
    'Kirtan Patel': '13-08-2004',
    'Krish Nariya': '14-11-2003',
    'Krutarth Tailor': '08-09-2004',
    'Kush Patel': '06-01-2004',
    'Luv Patel': '19-08-2003',
    'Manan Patel': '27-05-2004',
    'Mann Patel': '23-06-2004',
    'Mumukshu Patel': '10-03-2004',
    'Nirav K Patel': '20-12-2004',
    'Nirav R Patel': '15-03-2004',
    'Niravsinh Parmar': '31-03-2004',
    'Nirmaan Patel': '04-08-2004',
    'Nirman Jaiswal': '30-07-2004',
    'Nishant Patel': '02-06-2004',
    'Nishkam Patel': '03-04-2004',
    'Om Patel': '14-02-2005',
    'Om Thesia': '25-03-2004',
    'Parth Patel': '09-06-2004',
    'Poojan Patel': '30-08-2003',
    'Rudra Der': '04-05-2004',
    'Shaswat Patel': '27-04-2003',
    'Shrijit Patel': '25-04-2003',
    'Shrimad Patel': '24-12-2003',
    'Shrimed Sangani': '22-12-2003',
    'Sooraj Patel': '23-08-2004',
    'Utsav Choksi': '11-11-2003',
    'Vansh Chandak': '03-10-2004',
    'Vinit Patel': '01-02-2004',
    'Virat Rohit': '02-08-2004',
    'Vishnu Desai': '24-07-2003',
    'Vishnu Patel': '29-02-2004',
    'Yugma Vyas': '16-05-2003'
}
print("\n")
print("Welcome to the birthday dictionary. We know the birthdays of:")
for keys in Bday_list:
    print(keys)

print("\n")
ask = input("Who's birthday do you want to look up?: ")

print(ask,"'s birthday is on", Bday_list[ask])

