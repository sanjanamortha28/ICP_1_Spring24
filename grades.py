def student():
  total=float(input("enter the total:"))
  per= float((total/500)*100)
  print(per)
  
  if(per>=90):
  
   print ( " A grade")
   
  elif(per>=80 and per<90):
    
    print( " B grade")
    
  elif(per>=70 and per<80):
   
    print(" C grade")
    
  elif(per>=60 and per<70):
  
     print ( " D grade")
     
  else:
      
       print("failed")
       
 
student()
