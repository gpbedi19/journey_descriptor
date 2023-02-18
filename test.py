# The code then sets up two tests to verify the proper behaviour 
# of JourneyDescriptor. The test_sort_boarding_cards test verifies 
# that the sorted list of cards matches the expected one, while the 
# test_generate_journey_description tests whether the returned list 
# of statements is equal to the expected one.
#If all tests pass, a successful message is printed; otherwise, errors are reported.
 
 
__author__      = "Gurpeet Bedi"
__copyright__   = "Copyright Feb, 2023"

try:
    from app import app
    from BoardingCard import BoardingCard
    from JourneyDescriptor import JourneyDescriptor
    import unittest
except Exception as e:
    print("some modules are missing {}".format(e))

class TestJourneyDescriptor(unittest.TestCase):
    
    def test_sort_boarding_cards(self):
        card1 = BoardingCard("Los Angeles", "New York", "flight", "AA123")
        card2 = BoardingCard("San Francisco", "Los Angeles", "train", "Acela Express", gate="4B", seatAssignment="12A", baggageDrop="Baggage claim 3")
        card3 = BoardingCard("New York", "London", "flight", "BA456", gate="3A", seatAssignment="24F")
        card4 = BoardingCard("London", "Paris", "train", "Eurostar", gate="8C", seatAssignment="22C", baggageTransfer=True)
        cards = [card2, card1, card4, card3]
        journeyDescriptor = JourneyDescriptor(cards)
        sorted_cards = journeyDescriptor.sort_boarding_cards()
        self.assertEqual(sorted_cards, [card2, card1, card3, card4])
        
    def test_generate_journey_description(self):
        card1 = BoardingCard("Los Angeles", "New York", "flight", "AA123")
        card2 = BoardingCard("San Francisco", "Los Angeles", "train", "Acela Express", gate="4B", seatAssignment="12A", baggageDrop="Baggage claim 3")
        card3 = BoardingCard("New York", "London", "flight", "BA456", gate="3A", seatAssignment="24F")
        card4 = BoardingCard("London", "Paris", "train", "Eurostar", gate="8C", seatAssignment="22C", baggageTransfer=True)
        cards = [card2, card1, card4, card3]
        journeyDescriptor = JourneyDescriptor(cards)
        sorted_cards = journeyDescriptor.sort_boarding_cards()
        journey_description = journeyDescriptor.generate_journey_description(sorted_cards)
        expected_description = [
            "Take train Acela Express from San Francisco to Los Angeles. Gate 4B. Sit in seat 12A. Baggage drop at Baggage claim 3.",
            "From Los Angeles, take flight AA123 to New York.",
            "From New York, take flight BA456 to London. Gate 3A. Sit in seat 24F.",
            "Take train Eurostar from London to Paris. Gate 8C. Sit in seat 22C. Baggage will be automatically transferred from your last leg.",
            "You have arrived at your final destination."
        ]
        self.assertEqual(journey_description, expected_description)
        
if __name__ == '__main__':
    unittest.main()
