# Overview
This is a Python Flask application with a single endpoint that takes in a list of boarding cards and returns a journey description based on the cards.

The BoardingCard and JourneyDescriptor classes are defined to represent the boarding cards and generate the journey description, respectively.

## Prerequisites
- Python 3.7 or higher
 - Flask 1.1.2 or higher

## Installation
Clone this repository to your local machine.
Install Flask by running pip install Flask in y Open a terminal and navigate to the project directory.

## Running the Application
1. Open a terminal and navigate to the project directory.
2.  Run the application by executing the command python app.py.
3.  The server will start and listen for requests on http://localhost:5000.
4. Send a POST request to http://localhost:5000/journey-description with a JSON payload containing a list of boarding cards.

Example Request:

```
POST /journey-description HTTP/1.1
Host: localhost:5000
Content-Type: application/json
Content-Length: 340

{
 "boardingCards": [
     {
         "origin": "Barcelona",
         "destination": "Gerona Airport",
         "transportation": "bus"
     },
     {
         "origin": "Gerona Airport",
         "destination": "Stockholm",
         "transportation": "flight",
         "transportationNumber": "SK455",
         "gate": "45B",
         "seatAssignment": "3A",
         "baggageDrop": "344",
         "baggageTransfer": true
     },
     {
         "origin": "Madrid",
         "destination": "Barcelona",
         "transportation": "train",
         "transportationNumber": "78A",
         "seatAssignment": "45B"
     },
     {
         "origin": "Stockholm",
         "destination": "New York JFK",
         "transportation": "flight",
         "transportationNumber": "SK22",
         "gate": "22",
         "seatAssignment": "7B",
         "baggageDrop": "55",
         "baggageTransfer": false
     }
 ]
}

```
Example Response:

```
HTTP/1.1 200 OK
Content-Type: application/json

{
 "journeyDescription": [
     "Take bus from Barcelona to Gerona Airport.",
     "From Gerona Airport, take flight SK455 to Stockholm. Gate 45B. Sit in seat 3A. Baggage drop at 344. Baggage will be automatically transferred from your last leg.",
     "Take train 78A from Madrid to Barcelona. Sit in seat 45B. No baggage drop available.",
     "From Stockholm, take flight SK22 to New York JFK. Gate 22. Sit in seat 7B. Baggage drop at 55.",
     "You have arrived at your final destination."
 ]
}
```

## Testing
1. Open a terminal and navigate to the project directory.
2. Run the tests by executing the command python test.py.