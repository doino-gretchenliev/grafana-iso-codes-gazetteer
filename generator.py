import json

countries = {}
with open("countries.json",encoding="utf-8") as file:
    countries = json.load(file)

subdivisions = {}
with open("subdivisions.json", encoding="utf-8") as file:
    subdivisions = json.load(file)


print(f"Number of countries: [{len(countries)}]")
grafana_gazetteer = []
for country_code_2, country_data in countries.items():
    grafana_gazetteer.append({
        "keys": [
            country_data["waf_2"],
            country_code_2,
            country_data["waf_3"],
            country_data["a3"],
        ],
        "latitude": country_data["latitude"],
        "longitude": country_data["longitude"],
        "name": country_data["name"]
    })

print(f"Number of subdivisions: [{len(subdivisions)}]")
for subdivision_code, subdivision_data in subdivisions.items():
    grafana_gazetteer.append({
        "keys": [
            subdivision_code,
        ],
        "latitude": subdivision_data["latitude"],
        "longitude": subdivision_data["longitude"],
        "name": subdivision_data["name"]
    })


grafana_gazetteer = sorted(grafana_gazetteer, key=lambda d: d['keys'][0]) 
with open("iso.json", mode="w", encoding="utf-8") as file:
    json.dump(
        grafana_gazetteer,
        file,
        indent=4,
        sort_keys=True,
        ensure_ascii=False,
    )

