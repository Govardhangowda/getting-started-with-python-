karnataka={'shivamogga':'3','banglore':'45','mysore':'8','manglore':'13','hubli':'9'}
bigcity=[city for city,pop in karnataka.items() if int(pop)<10]
print(bigcity)
