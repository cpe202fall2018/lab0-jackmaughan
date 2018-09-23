#
#Name:  Jack Maughan
#Student ID: 012288610
#Date (last modified): 9/22/2018
#
# Lab 0
# Section 13/14
# Purpose of Lab: Introduce Python
# additional comments

def weight_on_planets():
	weight = int(input("What do you weigh on earth? "))
	mars = weight * .38
	jupitor = weight * 2.34
	print("\nOn Mars you would weigh {0} pounds.\nOn Jupiter you would weigh {1} pounds.".format(mars, jupitor))
   # write your code here
   
   
   
if __name__ == '__main__':
   weight_on_planets()
