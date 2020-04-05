# Problem1
# Find all city names, which are best to live. 
# (It is best if there is bar with "Blue Horse" name, and there is both Facebook and LinkedIn companies )
import json
f = open ( "C:\\Users\\admin\\Downloads\\cities.json" )
data = json.load(f)
best_cities_comp = []
best_cities_bars = []
for city in data:
    L_F = [False, False]
    for comp in  city["company"]:
        comp_name = comp["name"]
        if comp_name == "Linkedin":
            L_F[0] = True;
        if comp_name == "Facebook":
            L_F[1] = True;
    # both Linkedin and Facebook companies are in this city(at least 1 time)        
    if  L_F[0] == True and L_F[1] == True: 
        if  city["city"] not in best_cities_comp:
            best_cities_comp.append(city["city"])
            
    # bars with "Blue Horse" name
    for bar in city["bars"]:
        if bar["name"] == "Blue Horse":
            if city["city"] not in best_cities_bars:
                best_cities_bars.append(city["city"])
            
for comp in best_cities_comp:
    if 	comp in best_cities_bars:
        print (comp) 

        
# Problem2 - not finished
# Find  dictionary of all cities, where key = "company name", value = "names of those cities, where this company is"
import json
f = open ( "C:\\Users\\admin\\Downloads\\cities.json" )
data = json.load(f)
Comp_to_city = {}
for city in data:
    for comp in city["company"]:
        comp_name = comp["name"]
        if Comp_to_city.get(comp_name) == None:
            Comp_to_city[comp_name] = []
            if city["city"] not in Comp_to_city[comp_name]:
                Comp_to_city[comp_name].append(city["city"])

for key, value in Comp_to_city.items():
  print(key, " : ", value)
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			