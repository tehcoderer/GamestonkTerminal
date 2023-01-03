import sys

from openbb_terminal import integration_testing, terminal_controller
from openbb_terminal.plots_core.backend import BACKEND

if __name__ == "__main__":

    sent_args = sys.argv[1:]
    if "-t" in sent_args or "--test" in sent_args:
        integration_testing.parse_args_and_run()
    else:
        BACKEND.start()
        terminal_controller.parse_args_and_run()
