"""
==================================
Reading and writing an evoked file
==================================

"""
# Author: Alexandre Gramfort <gramfort@nmr.mgh.harvard.edu>
#
# License: BSD (3-clause)

print __doc__

from mne import fiff
from mne.datasets import sample
from mne.viz import plot_evoked

data_path = sample.data_path()

fname = data_path + '/MEG/sample/sample_audvis-ave.fif'

# Reading
evoked = fiff.Evoked(fname, setno='Left Auditory',
                     baseline=(None, 0), proj=True)

###############################################################################
# Show result

# Pick channels to view
picks = fiff.pick_types(evoked.info, meg=True, eeg=True, exclude='bads')
plot_evoked(evoked, picks=picks)
