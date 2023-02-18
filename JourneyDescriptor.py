

# This class that helps to organize  information regarding a journey. 
# The JourneyDescriptor class contains two methods, sort_boarding_card 
# and generate_journey_description. The sort_boarding_cards method sorts the boarding
# cards according to their origin and destination. 
# It first looks for a card that has a unique origin that does not appear 
# as a destination in any other card. This starting card found is added 
# to a sorted list of cards and the loop continues until it finds the other 
# cards and all cards have been included in the sorted list. 
# If the boarding cards do not form a valid sequence, it will raise a ValueError.

#The generate_journey_description method generates a description of the journey 
# based on the boarding cards. It takes in a single argument, sorted_cards, 
# which is a list of pre-sorted BoardingCard objects. It loops through each
#  card and creates a descriptive statement based on its attributes 
# (transportation, number, gate, seat assignment, baggage drop). 
# Finally, it appends the last statement and returns a list of statements
#  that describe the journey.

__author__      = "Gurpeet Bedi"
__copyright__   = "Copyright Feb, 2023"

class JourneyDescriptor():
    def __init__(self, cards):
        """
        Initialize JourneyDescriptor with a list of boarding cards.

        Args:
            cards (List[BoardingCard]): list of BoardingCard objects representing the journey's boarding cards
        """ 
        self.cards = cards
    
    def sort_boarding_cards(self):
        """
        Sort the boarding cards based on their origin and destination.

        Returns:
            List[BoardingCard]: sorted list of BoardingCard objects
        Raises:
            ValueError: when the boarding cards cannot form a valid sequence
        """
        # Find the starting card by looking for a card where the origin does not appear as a destination in any other card
        starting_card = None
        for card in self.cards :
            if not any(card.origin == other_card.destination for other_card in self.cards):
                starting_card = card
                break

        # Starting card found, now build the sorted list of cards
        sorted_cards = [starting_card]
        try:
            while len(sorted_cards) < len(self.cards):
                last_card = sorted_cards[-1]
                next_card = next(filter(lambda card: card.origin == last_card.destination, self.cards))
                sorted_cards.append(next_card)   
            print(sorted_cards) 
            return sorted_cards
        except:
            raise ValueError('Invalid boarding card sequence')
        
    def generate_journey_description(self, sorted_cards):
        """
        Generate a description of the journey based on the boarding cards.

        Args:
            sorted_cards (List[BoardingCard]): sorted list of BoardingCard objects
        
        Returns:
            List[str]: descriptive statements of each step in the journey
        """
        # Generate a description for each card in the sorted list
        journey_description = []
        for card in sorted_cards:
            if (card.transportation and card.transportation == 'flight'):
                description = f"From {card.origin}, take {card.transportation} {card.transportation_number} to {card.destination}."
            else:
                description = f"Take {card.transportation} {card.transportation_number} from {card.origin} to {card.destination}."
            if card.gate:
                description += f" Gate {card.gate}."
            if card.seat_assignment:
                if card.seat_assignment == 'NA':
                    description += f" No seat assignment."
                else:
                    description += f" Sit in seat {card.seat_assignment}."
            if card.baggage_drop:
                description += f" Baggage drop at {card.baggage_drop}."
            if card.baggage_transfer:
                description += " Baggage will be automatically transferred from your last leg."
            journey_description.append(description)
            
        journey_description.append("You have arrived at your final destination.")
        return journey_description
