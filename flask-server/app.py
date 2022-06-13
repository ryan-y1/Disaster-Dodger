from re import A
from flask import Flask, request, jsonify
import requests
import json

#####
Top_Three=[]

Package = {
  "state": "",
  "disasterList": [
    {
      "disasterType": "",
      "items": [
        {
          # Rin is doing the individual item object
        }
      ]
    },
    {
      "disasterType": "",
      "items": [
        {
          # Rin is doing the individual item object
        }
      ]
    },
    {
      "disasterType": "",
      "items": [
        {
          # Rin is doing the individual item object
        }
      ]
    }
  ]
}

Hurricane_count = 0
Flood_count = 0
Severe_Storm_count = 0
Earthquake_count = 0
Severe_Ice_Storm_count = 0
Coastal_Storm_count = 0
Fire_count = 0
Snow_count = 0
Other_count = 0
#####


####
app = Flask(__name__)

@app.route("/searchRegion", methods=['POST'])
def returnTopThreeDisasters():
    Selected_region = ## NEED TO PUT IN SEL REG


    response = requests.get("https://www.fema.gov/api/open/v1/FemaWebDisasterDeclarations")

    if response.ok == True:
        input_data = response.json()

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

    ### NEED TO FILTER OUT FOR TOP 3
    Top_Three=

    ## PUT IN TOP 3 INTO "DISASTER TYPE"

    For i in range(0, len(Top_Three)):
        if Top_Three[i] == "Hurricane":
            ## PUT IN ITEMS RELATED TO HURRICANE
        elif Top_Three[i] == "":
            A
        elif Top_Three[i] == "":
            A
        elif Top_Three[i] == "":
            A
        elif Top_Three[i] == "":
            A
        elif Top_Three[i] == "":
            A
        elif Top_Three[i] == "":
            A

    ###



    ## ALSO PUT STATE INTO PACKAGE
        















elif response.ok != True:
    print("unsuccessful")




if __name__ == "__main__":
    app.run(debug=True)

####


####





