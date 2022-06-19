from flask import Flask, request, jsonify, send_from_directory
import requests
from collections import Counter
from flask_cors import CORS, cross_origin

app = Flask(__name__, static_folder='client/build', static_url_path='')
CORS(app)


@app.route("/searchRegion", methods=['POST'])
@cross_origin()
def searchRegion():

    Package = {
        "state": "",
        "disasterList": [
        ]
    }

    highestThree = {
        "Hurricane_count": 0,
        "Flood_count": 0,
        "Severe_Storm_count": 0,
        "Earthquake_count": 0,
        "Severe_Ice_Storm_count": 0,
        "Coastal_Storm_count": 0,
        "Fire_count": 0,
        "Snow_count": 0,
    }

    Selected_region = request.json['region']

    response = requests.get(
        "https://www.fema.gov/api/open/v1/FemaWebDisasterDeclarations")

    if response.ok == True:
        input_data = response.json()
        for i in range(0, len(input_data["FemaWebDisasterDeclarations"])):
            obj = input_data["FemaWebDisasterDeclarations"][i]
            if obj["incidentType"] == "Hurricane" and obj["stateName"] == Selected_region:
                highestThree["Hurricane_count"] += 1
            elif obj["incidentType"] == "Flood" and obj["stateName"] == Selected_region:
                highestThree["Flood_count"] += 1
            elif obj["incidentType"] == "Severe Storm(s)" and obj["stateName"] == Selected_region:
                highestThree["Severe_Storm_count"] += 1
            elif obj["incidentType"] == "Earthquake" and obj["stateName"] == Selected_region:
                highestThree["Earthquake_count"] += 1
            elif obj["incidentType"] == "Severe Ice Storm" and obj["stateName"] == Selected_region:
                highestThree["Severe_Ice_Storm_count"] += 1
            elif obj["incidentType"] == "Coastal Storm" and obj["stateName"] == Selected_region:
                highestThree["Coastal_Storm_count"] += 1
            elif obj["incidentType"] == "Fire" and obj["stateName"] == Selected_region:
                highestThree["Fire_count"] += 1
            elif obj["incidentType"] == "Snow" and obj["stateName"] == Selected_region:
                highestThree["Snow_count"] += 1

        mostCommon = Counter(highestThree).most_common(3)
        for i in mostCommon:
            if i[0] == "Hurricane_count":
                Package.setdefault("disasterList", []).append({
                    "disasterType": "Hurricane",
                    "items": [
                        {
                            "image": "https://m.media-amazon.com/images/I/613LtGZVGML._AC_UX679_.jpg",
                            "name": "Waterproof Ponchos",
                            "text": "Waterproof ponchos protect against wind and rain, and provide warmth."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/61566GUkLFL._AC_SX425_.jpg",
                            "name": "Waterproof Waste Bags",
                            "text": "Waste bags may both protect important items from moisture, and dispose of hazardous waste."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/61yiunepZ3L._AC_SX679_.jpg",
                            "name": "Hand Sanitizer",
                            "text": "Hand sanitizer protects you from diseases by killing germs on your skin."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/71k-8c9TTcL._AC_SX679_.jpg",
                            "name": "Rope",
                            "text": "Rope may be used as a sling in the case of injury, but can also be used to build a shelter by tying materials together."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/91LUqSEpIWL._AC_SX425_.jpg",
                            "name": "Duct Tape",
                            "text": "Duct tape is water resistant and allows leaks to be repaired."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/51KlcWdnU-L._AC_SX679_.jpg",
                            "name": "Hand Warmers",
                            "text": "In the case of a power outage, hand warmers may keep you warm."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/81Fv2e8rdTL._AC_SY879_.jpg",
                            "name": "Blankets",
                            "text": "In the case of a power outage or having to evacuate from home, blankets may keep you warm. Consider adding bedding to your disaster kit too."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/61BF97Cth3L._AC_SX679_.jpg",
                            "name": "Flotation Devices",
                            "text": "Flotation devices keep you buoyant and provide warmth."
                        }


                    ]
                })
            if i[0] == "Flood_count":
                Package.setdefault("disasterList", []).append({
                    "disasterType": "Flood",
                    "items": [
                        {
                            "image": "https://m.media-amazon.com/images/I/613LtGZVGML._AC_UX679_.jpg",
                            "name": "Waterproof Ponchos",
                            "text": "Waterproof ponchos protect against wind and rain, and provide warmth."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/61566GUkLFL._AC_SX425_.jpg",
                            "name": "Waterproof Waste Bags",
                            "text": "Waste bags may both protect important items from moisture, and dispose of hazardous waste."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/61yiunepZ3L._AC_SX679_.jpg",
                            "name": "Hand Sanitizer",
                            "text": "Hand sanitizer protects you from diseases by killing germs on your skin."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/71k-8c9TTcL._AC_SX679_.jpg",
                            "name": "Rope",
                            "text": "Rope may be used as a sling in the case of injury, but can also be used to build a shelter by tying materials together."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/91LUqSEpIWL._AC_SX425_.jpg",
                            "name": "Duct Tape",
                            "text": "Duct tape is water resistant and allows leaks to be repaired."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/51KlcWdnU-L._AC_SX679_.jpg",
                            "name": "Hand Warmers",
                            "text": "In the case of a power outage, hand warmers may keep you warm."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/81Fv2e8rdTL._AC_SY879_.jpg",
                            "name": "Blankets",
                            "text": "In the case of a power outage or having to evacuate from home, blankets may keep you warm. Consider adding bedding to your disaster kit too."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/61BF97Cth3L._AC_SX679_.jpg",
                            "name": "Flotation Devices",
                            "text": "Flotation devices keep you buoyant and provide warmth."
                        }


                    ]
                })
            if i[0] == "Severe_Storm_count":
                Package.setdefault("disasterList", []).append({
                    "disasterType": "Storm",
                    "items": [
                        {
                            "image": "https://m.media-amazon.com/images/I/613LtGZVGML._AC_UX679_.jpg",
                            "name": "Waterproof Ponchos",
                            "text": "Waterproof ponchos protect against wind and rain, and provide warmth."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/61566GUkLFL._AC_SX425_.jpg",
                            "name": "Waterproof Waste Bags",
                            "text": "Waste bags may both protect important items from moisture, and dispose of hazardous waste."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/61yiunepZ3L._AC_SX679_.jpg",
                            "name": "Hand Sanitizer",
                            "text": "Hand sanitizer protects you from diseases by killing germs on your skin."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/71k-8c9TTcL._AC_SX679_.jpg",
                            "name": "Rope",
                            "text": "Rope may be used as a sling in the case of injury, but can also be used to build a shelter by tying materials together."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/91LUqSEpIWL._AC_SX425_.jpg",
                            "name": "Duct Tape",
                            "text": "Duct tape is water resistant and allows leaks to be repaired."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/51KlcWdnU-L._AC_SX679_.jpg",
                            "name": "Hand Warmers",
                            "text": "In the case of a power outage, hand warmers may keep you warm."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/81Fv2e8rdTL._AC_SY879_.jpg",
                            "name": "Blankets",
                            "text": "In the case of a power outage or having to evacuate from home, blankets may keep you warm. Consider adding bedding to your disaster kit too."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/61BF97Cth3L._AC_SX679_.jpg",
                            "name": "Flotation Devices",
                            "text": "Flotation devices keep you buoyant and provide warmth."
                        }


                    ]
                })
            if i[0] == "Earthquake_count":
                Package.setdefault("disasterList", []).append({
                    "disasterType": "Earthquake",
                    "items": [
                        {
                            "image": "https://m.media-amazon.com/images/I/81KqeAvPE5L._AC_SX425_.jpg",
                            "name": "Heavy Duty Work Gloves",
                            "text": "Heavy duty work gloves protect your hands from debris."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/41d+4dS7g+L._AC_.jpg",
                            "name": "Tube Tent",
                            "text": "A tube tent provides an immediate shelter in the case that you are unable to live in your home."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/61566GUkLFL._AC_SX425_.jpg",
                            "name": "Waterproof Waste Bags",
                            "text": "Waste bags may both protect important items from moisture, and dispose of hazardous waste."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/61yiunepZ3L._AC_SX679_.jpg",
                            "name": "Hand Sanitizer",
                            "text": "Hand sanitizer protects you from diseases by killing germs on your skin."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/71k-8c9TTcL._AC_SX679_.jpg",
                            "name": "Rope",
                            "text": "Rope may be used as a sling in the case of injury, but can also be used to build a shelter by tying materials together."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/91LUqSEpIWL._AC_SX425_.jpg",
                            "name": "Duct Tape",
                            "text": "Duct tape is water resistant and allows leaks to be repaired."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/41SCMEsIhBL._AC_SX425_.jpg",
                            "name": "Crescent and Pipe Wrenches",
                            "text": "After an earthquake, use the pipes to turn off utilities, especially gas."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/81Fv2e8rdTL._AC_SY879_.jpg",
                            "name": "Blankets",
                            "text": "In the case of a power outage or having to evacuate from home, blankets may keep you warm. Consider adding bedding to your disaster kit too."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/81c9+KSL52L._AC_SX425_.jpg",
                            "name": "Dust Masks",
                            "text": "Dust masks protect you from inhaling debris."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/512RBSoiCvL._AC_SY879_.jpg",
                            "name": "Fire Extinguisher",
                            "text": "Dislodged gas and electrical lines may also lead to fires. A fire extinguisher extinguishes a fire."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/81TCEnhTgKL._AC_SX679_.jpg",
                            "name": "Bicycle Helmet",
                            "text": "A helmet will protect your head from falling debris."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/81L8xflDwOL._AC_UX575_.jpg",
                            "name": "Sneakers",
                            "text": "Sturdy sneakers protect your feet from injury."
                        }


                    ]
                })
            if i[0] == "Severe_Ice_Storm_count":
                Package.setdefault("disasterList", []).append({
                    "disasterType": "Ice Storm",
                    "items": [
                        {
                            "image": "https://m.media-amazon.com/images/I/71k-8c9TTcL._AC_SX679_.jpg",
                            "name": "Rope",
                            "text": "Rope may be used as a sling in the case of injury, but can also be used to build a shelter by tying materials together."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/51KlcWdnU-L._AC_SX679_.jpg",
                            "name": "Hand Warmers",
                            "text": "In the case of a power outage, hand warmers may keep you warm."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/81Fv2e8rdTL._AC_SY879_.jpg",
                            "name": "Blankets",
                            "text": "In the case of a power outage or having to evacuate from home, blankets may keep you warm. Consider adding bedding to your disaster kit too."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/71fqCQwdp0L._AC_UX679_.jpg",
                            "name": "Warm and Dry Clothes",
                            "text": "Extra clothing helps in keeping you warm."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/51LrI8n-fDL._AC_SX425_.jpg",
                            "name": "Windshield Scraper",
                            "text": "A windshield scraper assists with removing ice, frost, and snow."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/51Rber8gF3L._AC_SX679_.jpg",
                            "name": "Shovel",
                            "text": "A shovel assists with removing snow from your path."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/816lch3-Z6L._AC_SX679_.jpg",
                            "name": "Road Salt",
                            "text": "Road salt melts ice for safer travel. Sand may be used as a substitute."
                        }


                    ]
                })
            if i[0] == "Coastal_Storm_count":
                Package.setdefault("disasterList", []).append({
                    "disasterType": "Coastal Storm",
                    "items": [
                        {
                            "image": "https://m.media-amazon.com/images/I/613LtGZVGML._AC_UX679_.jpg",
                            "name": "Waterproof Ponchos",
                            "text": "Waterproof ponchos protect against wind and rain, and provide warmth."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/71k-8c9TTcL._AC_SX679_.jpg",
                            "name": "Rope",
                            "text": "Rope may be used as a sling in the case of injury, but can also be used to build a shelter by tying materials together."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/61BF97Cth3L._AC_SX679_.jpg",
                            "name": "Flotation Devices",
                            "text": "Flotation devices keep you buoyant and provide warmth."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/71fqCQwdp0L._AC_UX679_.jpg",
                            "name": "Warm and Dry Clothes",
                            "text": "Extra clothing helps in keeping you warm."
                        }


                    ]
                })
            if i[0] == "Fire_count":
                Package.setdefault("disasterList", []).append({
                    "disasterType": "Fire",
                    "items": [
                        {
                            "image": "https://m.media-amazon.com/images/I/81Fv2e8rdTL._AC_SY879_.jpg",
                            "name": "Blankets",
                            "text": "In the case of a power outage or having to evacuate from home, blankets may keep you warm. Consider adding bedding to your disaster kit too."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/81KqeAvPE5L._AC_SX425_.jpg",
                            "name": "Heavy Duty Work Gloves",
                            "text": "Heavy duty work gloves protect your hands from debris."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/81c9+KSL52L._AC_SX425_.jpg",
                            "name": "Dust Masks",
                            "text": "Dust masks protect you from inhaling debris."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/512RBSoiCvL._AC_SY879_.jpg",
                            "name": "Fire Extinguisher",
                            "text": "Dislodged gas and electrical lines may also lead to fires. A fire extinguisher extinguishes a fire."
                        }


                    ]
                })
            if i[0] == "Snow_count":
                Package.setdefault("disasterList", []).append({
                    "disasterType": "Snow",
                    "items": [
                        {
                            "image": "https://m.media-amazon.com/images/I/71k-8c9TTcL._AC_SX679_.jpg",
                            "name": "Rope",
                            "text": "Rope may be used as a sling in the case of injury, but can also be used to build a shelter by tying materials together."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/51KlcWdnU-L._AC_SX679_.jpg",
                            "name": "Hand Warmers",
                            "text": "In the case of a power outage, hand warmers may keep you warm."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/81Fv2e8rdTL._AC_SY879_.jpg",
                            "name": "Blankets",
                            "text": "In the case of a power outage or having to evacuate from home, blankets may keep you warm. Consider adding bedding to your disaster kit too."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/71fqCQwdp0L._AC_UX679_.jpg",
                            "name": "Warm and Dry Clothes",
                            "text": "Extra clothing helps in keeping you warm."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/51LrI8n-fDL._AC_SX425_.jpg",
                            "name": "Windshield Scraper",
                            "text": "A windshield scraper assists with removing ice, frost, and snow."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/51Rber8gF3L._AC_SX679_.jpg",
                            "name": "Shovel",
                            "text": "A shovel assists with removing snow from your path."
                        },
                        {
                            "image": "https://m.media-amazon.com/images/I/816lch3-Z6L._AC_SX679_.jpg",
                            "name": "Road Salt",
                            "text": "Road salt melts ice for safer travel. Sand may be used as a substitute."
                        }
                    ]
                })

        Package['state'] = Selected_region
        return jsonify(Package)


@app.route('/')
@cross_origin()
def serve():
    print(send_from_directory(app.static_folder, 'index.html'))
    print("testing")
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == "__main__":
    app.run(debug=True)
