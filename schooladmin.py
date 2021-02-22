import csv

def write_into_csv(info_list): 
   with open('stud_info.csv','a',newline=" ") as csv_file:
      writer = csv.writer(csv_file)
      if csv_file.tell()==0:
         writer.writerow(['new','age','contact number','email id'])
      writer.writerow(info_list)
      
if __name__=='__main__':      
  condition = True
  stud_num = 1
  while(condition):
     stud_info = input("Enter the student #{} information in the following format( Name Age Contact_number EmailID):")
   
     stud_info_list=stud_info.split(' ')
   
      print("\n The entered information is - \nNAme: {}\nAge: {}\nContact_number: {}\nEmailID: {}"
     .format(stud_info_list[0], stud_info_list[1], stud_info_list[2], stud_info_list[3])) 
    
     choice= input("Is the enetered information correct?(yes/no):")
     if choice=="yes":
        write_into_csv(stud_info_list)
    
        cond_check=input("Enter yes/no if you want to go for another entry-")
        if cond_check=="yes":
          condition = True
          stud_num= stud_num+1
        elif cond_check=="no":
          condition = False
elif choice=="no":
        print("\nPlease re-enter the values:")
