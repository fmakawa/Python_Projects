"""
N people (numbered 1 to N) are standing in a circle. Person 1 kills Person 2
with a a sword and gives it to person 3. Person 3 kills person 4  and gives the
sword to person 5. This process is repeated until only one person is alive.

Task:
(Medium) Given the number of people N, write a program to find the number of the
people to find the number of the person  the person that stays alive at the end.
(Hard) Show each step of the process.
"""
"""
For this solution I used lists. I created a List which was populated by the people
and then recursively removed after the list is created. You should be very careful
when creating your tests. I created a test for this that worked for number of
people that were odd but didn't work for even numbers. I had to refactor the code
a couple of time before it worked perfectly for all. 
"""
def kill_people (Npeople):
    list_of_people = []
    for i in range (1,Npeople+1):
        list_of_people.append(i)
        print(list_of_people)

    x = 0

    while len(list_of_people)>1:

        if x < (len(list_of_people)-1):
            to_be_killed = list_of_people[x+1]
            list_of_people.remove(to_be_killed)
            print ("%s killed %s" %(list_of_people[x], to_be_killed))
            x+=1
            print(x)
            print ("People left %s " %(list_of_people))
        elif x == len(list_of_people):
            to_be_killed =list_of_people[1]
            print ("%s killed %s" %(list_of_people[0], to_be_killed))
            list_of_people.remove(to_be_killed)
            x=1
            print(x)
            print ("People left %s " %(list_of_people))
        else :
            to_be_killed =list_of_people[0]
            print ("%s killed %s" %(list_of_people[x], to_be_killed))
            list_of_people.remove(to_be_killed)
            x=0
            print(x)
            print ("People left %s " %(list_of_people))
    print ("Alive in the end %s" %(list_of_people[0]))
    return list_of_people[0]

kill_people(17)
