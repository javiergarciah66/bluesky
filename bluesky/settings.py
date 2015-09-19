gui = 'qtgl'  # options: 'qtgl', 'pygame'

scenario_path = 'data/scenario'

# Simulation timestep [seconds]
simdt = 0.02

# Simulation thread update rate [Hz]
sim_update_rate = 50

# Import conig settings from settings.cfg if this exists, if it doesn't create an initial config file
import os
if os.path.isfile('settings.cfg'):
    print 'Reading config from settings.cfg'
    execfile('settings.cfg')
else:
    print 'Writing initial config file settings.cfg'
    with open(os.path.dirname(__file__) + '/settings.py') as fin, open('settings.cfg', 'w') as fout:
        for i in range(10):
            fout.write(fin.readline())
