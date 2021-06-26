from oct2py import octave
import numpy as np

octave.addpath('/path/to/directory')  # to add a folder use:
# to add folder with all subfolder in it use:
octave.addpath(octave.genpath('/path/to/directory'))
octave.run('fileName.m')  # to run the .m file :


# import matlab.engine
# eng = matlab.engine.start_matlab()
# eng.simple_script(nargout=0)
# eng.quit()

##########################################################
# import sys
# positionOfPath = 1
# sys.path.insert( positionOfPath, 'your matlab path' )
