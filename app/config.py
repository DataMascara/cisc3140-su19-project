import os

# grabs the folder where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))

# enable debug mode
DEBUG = True


#------------------------------------------------------------------------------#
# Sample Data for front end prototyping
#------------------------------------------------------------------------------#
#
# these values are for demonstration of front end w/o database connection

current_user = { "username": "guest"
               , "avatar": "profile_logo.png"
               }   # values when not logged in

trending_ports = [ {"name": "FOO", "mem": 0 }
                 , {"name": "BAR", "mem": 0 }
                 , {"name": "BAZ", "mem": 0 }
                 , {"name": "QUX", "mem": 0 }
                 , {"name": "QUUX", "mem": 0 }]
