def BookRoom():
  name=input("Name of Passenger: ")
  age=input("Age: ")
  cls=input(""" Suite: 
  (D-Deluxe\n E-Executive\n L-Luxury)""")
  occ= int(input("No. of people: "))
  print("Check In Date(dd-mm-yyyy): ")
  dd1, mm1, yy1 = map(str, input().split('-'))
  print("Check In Date(dd-mm-yyyy): ")
  dd2, mm2, yy2 = map(str, input().split('-'))
  L=[]
  while len(L)!=5:
      n=random.randint(10000,99999)
      if n not in L:
          L.append(n)
  P=n
  CR.execute(f"INSERT INTO Passenger values('{P}','{name}','{age}','{cls}','{occ}','{yy1}-{mm1}-{dd1}','{yy2}-{mm2}-{dd2}')")
  DB.commit()
