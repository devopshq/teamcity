############
Development
############

About library
=============================
soon...

How to build documentation?
=============================

We use sphinx to build docs::

    cd docs-sphinx
    make html
    # open ./docs-sphinx/_build/html/index.html on your browser

How to publish documentation?
=============================

For repositories admin:

  + All documentation saved in ``docs``-folder on branches.
  + We use ``gh-pages`` as source for publishing on github pages.

Run this script to publish new html (ensure that you on ``master``-branch!!)::

    cd docs
    bash ./publish-gh-pages.sh

