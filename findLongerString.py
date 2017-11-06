name_list=[]
def find_longer_than_n(input_list,value):
    for var in input_list:
	    length=len(var)
	    if length > value:
		    name_list.append(var)

    for name in name_list:
        print (name)	

if __name__ == "__main__":
    input_list = ["sonam","savita","madhumitha","neha","nikhitha","shivangi","keerthi","banupriya"]
    value=input("Enter the length:")
    find_longer_than_n(input_list,value)
    
		
    
