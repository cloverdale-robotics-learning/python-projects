import http.client
import json


def get_rates(curr):
    try:
        with open(f"rates_{curr}.json") as file:
            return json.load(file)
    except Exception:
        pass
    print("Requesting exchange rates...")
    try:
        conn = http.client.HTTPSConnection("open.er-api.com")
        conn.request("GET", f"/v6/latest/{curr}")
        response = conn.getresponse()
        if response.status != 200:
            raise Exception(response.reason)
        data = json.loads(response.read())["rates"]
        with open(f"rates_{curr}.json", "w") as file:
            json.dump(data, file, indent=4)
    except Exception as exc:
        print(f"Failed to get exchange rates: {exc}")
        raise SystemExit
    return data


from_curr = input("Enter currency to convert from (e.g. CAD): ").upper()
to_curr = input("Enter currency to convert to (e.g. USD): ").upper()

from_amount = float(input("Enter the amount to convert: "))
rates = get_rates(from_curr)
to_amount = from_amount * rates[to_curr]

print(f"{from_amount:.2f} {from_curr} = {to_amount:.2f} {to_curr}")
