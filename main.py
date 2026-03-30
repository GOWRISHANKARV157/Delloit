# import the necessary modules and libraries
import json, unittest, datetime

#use the open function to open read the three json files
with open("C:/Users/Gowri Shankar/OneDrive/Desktop/Delloit/data-1.json","r", encoding="utf-8") as f:
    jsonData1 = json.load(f)
with open("C:/Users/Gowri Shankar/OneDrive/Desktop/Delloit/data-2.json","r", encoding="utf-8") as f:
    jsonData2 = json.load(f)
with open("C:/Users/Gowri Shankar/OneDrive/Desktop/Delloit/data-result.json","r", encoding="utf-8") as f:
    jsonExpectedResult = json.load(f)

from datetime import datetime, timezone

# convert json data from format 1 to the expected format
def convertFromFormat1(jsonObject):

    locationParts = jsonObject["location"].split("/")

    result = {
        'deviceID': jsonObject['deviceID'],
        'deviceType': jsonObject['deviceType'],
        'timestamp': jsonObject['timestamp'],
        # Assumed input location format: country/city/area/factory/section
        'location': {
            'country': locationParts[0],
            'city': locationParts[1],
            'area': locationParts[2],
            'factory': locationParts[3],
            'section': locationParts[4]
        },
        'data': {
            'status': jsonObject['operationStatus'],
            'temperature': jsonObject['temp']
        }
    }

    return result


# convert json data from format 2 to the expected format
def convertFromFormat2(jsonObject):

    # ISO → milliseconds (fixed)
    dt = datetime.strptime(jsonObject['timestamp'], '%Y-%m-%dT%H:%M:%S.%fZ') # Converted ISO 8601 timestamp to milliseconds since epoch (UTC)
    dt = dt.replace(tzinfo=timezone.utc)
    timestamp = int(dt.timestamp() * 1000)

    result = {
        'deviceID': jsonObject['device']['id'],
        'deviceType': jsonObject['device']['type'],
        'timestamp': timestamp,
        # Assumed input location format: country/city/area/factory/section
        'location': {
            'country': jsonObject['country'],
            'city': jsonObject['city'],
            'area': jsonObject['area'],
            'factory': jsonObject['factory'],
            'section': jsonObject['section']
        },
        'data': jsonObject['data'] 
    }

    return result


def main (jsonObject):

    result = {}

    if (jsonObject.get('device') == None):
        result = convertFromFormat1(jsonObject)
    else:
        result = convertFromFormat2(jsonObject)

    return result


# Test cases using unittest module
class TestSolution(unittest.TestCase):

    # Sanity test to ensure the expected result is as intended
    # converts json data to python objects usnig json.loads and json.dumps
    def test_sanity(self):

        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(
            result,
            jsonExpectedResult
        )

    def test_dataType1(self):

        result = main (jsonData1)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 1 failed'
        )

    def test_dataType2(self):

        result = main (jsonData2)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 2 failed'
        )

if __name__ == '__main__':
    # run the tests
    unittest.main()