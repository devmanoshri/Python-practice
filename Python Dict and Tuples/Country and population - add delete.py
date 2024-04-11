#

country_population={"China":143, "India":136,"Usa":32,"Pakistan":21}
choice = input("Enter your choice (add, remove, query or print):")

def print_all():
    print("List ...................")
    for key in country_population:
       print(key+"==>"+ str(country_population[key]))
def convert_to_lower(str):
    return(str.lower().strip())

if convert_to_lower(choice) == 'print':
    print_all()

elif convert_to_lower(choice) =='add':
    new_country=str(input("Add Country name:")).capitalize().strip()
    if new_country in country_population:
        print('Already exist')
    else:
        new_population=input("Enter population:")
        country_population[new_country] = new_population
        print_all()
elif convert_to_lower(choice) =='remove':
    del_country=str(input("Which country you want to remove:")).capitalize().strip()
    if del_country in country_population:
        del country_population[del_country]
        print_all()
    else:
        print(del_country+" does not exist in the list.")
elif convert_to_lower(choice) == 'query':
    info_country= input("Enter country name:").capitalize().strip()
    print('Population of '+info_country+" is: "+ str(country_population[info_country]))
else:
    print("Enter your choice properly")