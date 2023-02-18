# Class BoardingCard
# This class is used to construct objects that represent a basic boarding card. 
# It contains fields for the origin, destination, type of transportation (e.g. bus, train, or flight), 
# transportation number, gate number, seat assignment, baggage drop, and baggage transfer details.

__author__      = "Gurpeet Bedi"
__copyright__   = "Copyright Feb, 2023"

class BoardingCard():
    def __init__(self, origin, destination, transportation, transportationNumber, gate=None, seatAssignment=None, baggageDrop=None, baggageTransfer=None):
        self.origin = origin 
        self.destination = destination 
        self.transportation = transportation 
        self.transportation_number = transportationNumber 
        self.gate = gate
        self.seat_assignment = seatAssignment
        self.baggage_drop = baggageDrop
        self.baggage_transfer = baggageTransfer