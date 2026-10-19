def inst_shop():

  instype = input("Enter instrument type: ")
  rent_price = input("Enter price: ")
  avail = input("Is instrument available? (Yes/No):  ")


  print(f'{instype} rental created with price P{rent_price}')

  action = input ("Rent or return? (Rent/Return): ")
  if action == "Rent" or "Return":
    if avail=="Yes":
      print(f'{instype} is available to {action}.')
    elif avail == "No":
      print(f'{instype} not available to {action}.')
    else:
      print(f'{instype} does not exist.')
  else:
    print("INVALID INPUT")

if __name__=="__main__":
  inst_shop()
  