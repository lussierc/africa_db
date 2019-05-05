"""Creates a command-line interface where users can interact with the database."""

def welcomeMessage():
    """Displays welcome message."""
    print("+-----------------------------------------+")
    print("|    Welcome to the AfricaDB Interface    |")
    print("+-----------------------------------------+")
    print()
    print("This interface allows users to interact with the following tables:")
    print(" - HPI: Happy Planet Index information about countries from around the world.")
    print(" - DevIndicators: GDP growth and GDP per capita information for countries from around the world.")
    print(" - RealGDPGrowth: Real GDP Growth data for a number of years.")
    print(" - Resources: Resource Rent data for countries.")
    print()

def displayTable():
    """Displays table of a user's choice."""


def main():
    """Manages the running of the interface."""
    welcomeMessage()
