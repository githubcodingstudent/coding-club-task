import requests
result = requests.get('http://api.football-data.org/v2/competitions')
data = result.json()

tier_input = input("Enter a tier: ")

if tier_input.lower() in ['four', '4']:
    tier_input = 'TIER_FOUR'
elif tier_input.lower() in ['three', '3']:
        tier_input = 'TIER_THREE'
elif tier_input.lower() in ['two', '2']:
    tier_input = 'TIER_TWO'
elif tier_input.lower() in ['one', '1']:
    tier_input = 'TIER_ONE'
else: print("Invalid Entry")


with open('footballcompetition.csv', 'w+', encoding='utf-8') as f:
    f.write("id,Name,Area/Country,Available Seasons, Tier\n")
    for competition in data['competitions']:
        if competition['plan']==tier_input:
          id = competition['id']
          name = competition['name']
          area = competition['area']['name']
          seasons = competition['numberOfAvailableSeasons']
          tier = competition['plan']
        f.write(str(id) + "," + name + "," + area + "," + str(seasons) +  ","+ tier +  '\n')