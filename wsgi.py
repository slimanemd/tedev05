#
from tedev.app import create_app

#
app = create_app()


from tedev.core.routes import *

#
if __name__ == "__main__":
    app.run()