import os
import sys
import importlib
import matplotlib.pyplot as plt
import openbb_terminal.session.local_model as Local
import openbb_terminal.session.hub_model as Hub
from openbb_terminal.session.user import User
from openbb_terminal.helper_funcs import system_clear


def logout():
    """Logout and clear session."""
    system_clear()
    User.clear()

    # Clear openbb environment variables
    for v in os.environ:
        if v.startswith("OPENBB"):
            os.environ.pop(v)

    # Reload all openbb modules
    modules = sys.modules.copy()
    for module in modules:
        if module.startswith("openbb"):
            importlib.reload(sys.modules[module])

    Hub.delete_session()
    Local.remove_session_file()
    plt.close("all")
