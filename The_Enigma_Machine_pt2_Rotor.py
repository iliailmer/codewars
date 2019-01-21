class Rotor(object):
    def __init__(self, name, wiring, notches, ring_position, start_position):
        """
        name: Arbitrary rotor name
        wiring: A string of 26 letters indicating the output mapping for letters A-Z in order
        notches: A string with at least 1 letter indicating when the next rotor should turn
        ring_position: The letter next to the rotor's dot
        start_position: The letter initially visible
        If any parameters are invalid an exception will be raised.
        """
        self.name = name
        self.wiring =
        pass

    def process(self, c, rotate):
        """
        Simulates the signal being received at the rotor input.
        c: The single character to process
        rotate: If True, the rotor should simulate rotation after processing this character
        returns: tuple(enciphered character, True if notch was present)
        """
        self.wiring
        return c, False
