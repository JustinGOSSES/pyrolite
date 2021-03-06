Installation
================

pyrolite is available on `PyPi <https://pypi.org/project/pyrolite/>`_, and can be downloaded with pip:

.. code-block:: bash

   pip install pyrolite


.. note:: pyrolite is not yet packaged for Anaconda, and as such :code:`conda install pyrolite` will not work.


Upgrading pyrolite
--------------------

New versions of pyrolite are released frequently. You can upgrade to the latest edition
on `PyPi <https://pypi.org/project/pyrolite/>`_ using the :code:`--upgrade` flag:

.. code-block:: bash

   pip install --upgrade pyrolite

Optional Dependencies
-----------------------

Optional dependencies (`dev`, `skl`, `spatial`, `db`) can be specified during pip
installation. For example:

.. code-block:: bash

   pip install pyrolite[dev]

   pip install pyrolite[dev,skl,spatial,db]
