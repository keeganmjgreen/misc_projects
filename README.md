# `misc_projects`

Some of my miscellaneous projects and scripts that are too short to warrant a dedicated repo.

## `dust_buster.py`

`dust_buster.py` applies a moving mode on four-dimensional arrays representing video signals for removing, for example, dust in front of a camera – hence the needlessly creative name. I first tested it with a stationary, non-moving mode (i.e., window width equal to the number of video frames) on a video of falling confetti with an unchanging background. I also tested it with and without a moving mode on the confetti portion of Tom Scott's well-known video ["Why Snow and Confetti Ruin YouTube Video Quality"](https://www.youtube.com/watch?v=r6Rp-uo6HmI), with poor results unless an impractically wide sliding window is used. I suspect this is due to finding the mode of per-pixel signals that are especially noisy due to the high video compression which – you guessed it – is meant to be a result of the confetti in the first place. One of many possible solutions is posterizing the video (which implements a clustering algorithm, by the way). Another possible solution to reduce the noise is applying a moving mean using a sliding window narrower than that of the moving mode. A moving mean instead of a more effective method of smoothing would be used to improve processing speed in relatively slow Python. This makes a case for using C++ for what would be processing a live camera feed in real time. This small project was created to remove dust particles illuminated by the near-infrared lights of a night-vision-enabled camera used to monitor a chicken coop. I used the `skvideo` Python library.

## `ga.py`

`ga.py` implements a simplified genetic algorithm for finding the global minimum (or one of multiple minima at a time) of a function, which is univariate and bounded. [Genetic algorithms](https://en.wikipedia.org/wiki/Genetic_algorithm) are numerical optimization methods. The script includes functions to convert back and forth between decimal and binary form, where each digit in binary form is a chromosome subject to possible randomized mutation with every iteration of the algorithm. My binary representations works with fractional and negative numbers. I am confident that this will be my only project ever with reference to "`mutants`".

## `spacial_descriptions.py`

`spacial_descriptions.py` defines simple classes dealing with the location of bodies in space, such as the position of a robot arm within its workspace. It is overkill and implements unit testing, as practice for creating classes representing relatively abstract concepts, adhering to [PEP 8](https://peps.python.org/pep-0008/), and using the built-in `unittest` Python library. `ReferenceFrame` sets up a reference frame and `Transformation` sets up a generalized transformation therebetween, as a base class for `Translation` and `Rotation`. I created this while studying advanced kinematics for robotic systems.

## `batch_rename.py`

`batch_rename.py` is run from a folder whose subfolders and files are to be renamed in bulk using a text editor with multi-cursoring, namely, Sublime Text. It opens, as a temporary file in the text editor, an alphabetical list of paths relative to the parent directory of subdirectories and files. When the buffer is saved, the text editor closes and the temporary file is cleaned up. I created this tool to name and rename experimental trials of vibration analyses of mine done on hydraulic power units, and I have used it many times since.

## `photo_folders.py`

`photo_folders.py` walks through a specified directory, listing the path of all folders therein containing at least 50% image files. I did this for the exercise "Identifying Photo Folders on the Hard Drive" in *Automate the Boring Stuff with Python*.

## `eating_persistence.py`

`eating_persistence.py` is my not-very-code-golfy solution to [this](https://codegolf.stackexchange.com/questions/213645/eating-persistence) code golf challenge.
