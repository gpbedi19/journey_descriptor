# 
# /journey-description endpoint
# This endpoint takes in a list of boarding cards and 
# returns a journey description based on the cards.


__author__      = "Gurpeet Bedi"
__copyright__   = "Copyright Feb, 2023"

from flask import Flask, request, jsonify

from BoardingCard import BoardingCard
from JourneyDescriptor import JourneyDescriptor


app = Flask(__name__)
valid_transports = {"train", "bus", "flight"}

@app.route('/journey-description', methods=['POST'])
def get_journey_description():
    
    try:

        #Validate input
        data = request.get_json()
        if not data:
            return jsonify({'error': "Empty input"}), 400
        if not data.get('boardingCards'):
            return jsonify({'error': "BoardingCards list not found"}), 400
        for card in data.get('boardingCards'):
            if not card.get("origin"):
                return jsonify({'error': "Source not found for one of the cards".format(card)}), 400
            if not card.get("destination"):
                return jsonify({'error': "Destination not found for one of the cards".format(card)}), 400
            if not card.get("transportation"):
                return jsonify({'error': "Transportation type not found for one of the cards".format(card)}), 400
            if card.get("transportation") not in valid_transports:
                    return jsonify({'error': "Transportation type not valid".format(card)}), 400
        # Create a BoardingCard object for each card provided in data
        cards = [BoardingCard(**card) for card in data.get('boardingCards')]
        # Create a JourneyDescriptor object using the list of cards
        journeyDescriptor = JourneyDescriptor(cards)
        # Sort the given boarding cards
        sorted_cards = journeyDescriptor.sort_boarding_cards()
        # Generate a journey description based on the sorted list of boarding cards
        journey_description = journeyDescriptor.generate_journey_description(sorted_cards)
        # Return a json object with the generated journey description
        return jsonify({'journeyDescription': journey_description}), 200
    except (Exception) as e:
        print(e)
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
