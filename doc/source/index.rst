.. Satellite Communication documentation master file, created by
   sphinx-quickstart on Fri Aug 11 13:54:56 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Satellite Communication's documentation!
===================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Usage
=====

The Program can be used via a command line interface. Execute the sat_slot_counter.py file with the relative path to a datafile containing time windows to run the analysis and find all overlapping time windows with number of satellites observed during this time.

Running the script from the /src folder.
.. code-block::

   $ python sat_slot_counter.py ../dat/satellites.dat


For more information:

.. code-block::

   $ python sat_slot_counter.py -h


File Importer
=============

.. automodule:: importer
   :members:


Slots
=====

.. automodule:: slots
   :members:

