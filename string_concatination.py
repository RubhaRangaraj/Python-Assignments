import os
import sys

def string_concat(name):    
    length=len(name)
    if length < 2:
        return None
    else:
        str_name=name[:2]
        con_name=str_name+(name[-2:])
        return con_name	
	
if __name__ == "__main__":
    name = input('Enter your name: ')
    concat_name=string_concat(name)
    print "Name after concatination:" + str(concat_name)
