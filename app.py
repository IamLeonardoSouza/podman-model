import time

from src.script_example_1 import make_request
from src.script_example_2 import manipulate_dataframe


def run_automation() -> None:
    """
    Runs the automation process by performing a series of steps:
    - Prints a start message.
    - Pauses for 2 seconds.
    - Calls the function to make a request.
    - Calls the function to manipulate a dataframe.
    - Pauses for another 2 seconds.
    - Prints a completion message.
    """
    print("Starting automation...")

    time.sleep(2)

    make_request()

    time.sleep(2)
    
    manipulate_dataframe()

    time.sleep(2)

    print("Automation completed!")


if __name__ == "__main__":
    run_automation()
