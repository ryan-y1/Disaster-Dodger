import requests
import json

output_data = {}

Hurricane_count = 0
Flood_count = 0
Severe_Storm_count = 0
Earthquake_count = 0
Severe_Ice_Storm_count = 0
Coastal_Storm_count = 0
Fire_count = 0
Snow_count = 0
Other_count = 0

Selected_Region = ""






response = requests.get("https://www.fema.gov/api/open/v1/FemaWebDisasterDeclarations")
# print(response.status_code)
# print(response.elapsed)
# print(response.raise_for_status)
if response.ok == True:
    print("success")
    # print(response.url)
    # json.load(response.json())
    input_data = response.json()
    print(type(input_data["FemaWebDisasterDeclarations"][0]))
    print(input_data["FemaWebDisasterDeclarations"][0]["stateCode"])
    
    # print(input_data["stateName"])
    # print(len(response.keys()))
    # print(json.load(input_data)[0])


    # for i in range(0, len(input_data["FemaWebDisasterDeclarations"])):
    #     if input_data["FemaWebDisasterDeclarations"][i]["stateCode"] == "CA":
    #         AS_count += 1
    #     elif input_data["FemaWebDisasterDeclarations"][i]["stateCode"] == "TX":
    #         TX_count += 1
    #     else:
    #         continue
    # print(AS_count, TX_count)

        # print(input_data["FemaWebDisasterDeclarations"][i]["stateCode"])

    for i in range(0, len(input_data["FemaWebDisasterDeclarations"])):
        obj = input_data["FemaWebDisasterDeclarations"][i]
        if obj["incidentType"] == "Hurricane" and obj["stateName"] == Selected_region:
            Hurricane_count += 1
        elif obj["incidentType"] == "Flood" and obj["stateName"] == Selected_region:
            Flood_count += 1
        elif obj["incidentType"] == "Severe Storm(s)" and obj["stateName"] == Selected_region:
            Severe_Storm_count += 1
        elif obj["incidentType"] == "Earthquake" and obj["stateName"] == Selected_region:
            Earthquake_count += 1
        elif obj["incidentType"] == "Severe Ice Storm" and obj["stateName"] == Selected_region:
            Severe_Ice_Storm_count += 1
        elif obj["incidentType"] == "Coastal Storm" and obj["stateName"] == Selected_region:
            Coastal_Storm_count += 1
        elif obj["incidentType"] == "Fire" and obj["stateName"] == Selected_region:
            Fire_count += 1
        elif obj["incidentType"] == "Snow" and obj["stateName"] == Selected_region:
            Snow_count += 1
        else:
            Other_count += 1
    print(Hurricane_count, Flood_count, Severe_Storm_count, Severe_Ice_Storm_count, Coastal_Storm_count, Fire_count, Snow_count, Other_count)
        # print(input_data["FemaWebDisasterDeclarations"][i]["stateCode"])


    


elif response.ok != True:
    print("unsuccessful")
