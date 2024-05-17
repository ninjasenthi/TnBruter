from datetime import datetime,timedelta

def render_day(year):
    
    date = datetime.strptime(f"01/01/{year}","%d/%m/%Y")
    data = [f"{year}-01-01"]
    
    if year==2008: #spcieal for leap year guys
            for d in range(365):
                date += timedelta(days=1)
                data.append(str(date)[0:10])
    else:
            for d in range(365):
                date += timedelta(days=1)
                data.append(str(date)[0:10])
    return data
    
def modify(day):
    ds= day.split("-")
    return str(f"{ds[2]}/{ds[1]}/{ds[0]}")
    
print("\n" + "Welcome To Dobsheet Manipulator")
filename = input(" filename -> ")
years = input(" years -> ").split(",")

with open(filename,"w") as file:
    data=[]
    for year in years:
        for date in render_day(year):
            data.append(date)
    for day in data:
        file.write(modify(day)+'\n')
        print(modify(day))
