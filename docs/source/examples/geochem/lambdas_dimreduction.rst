.. rst-class:: sphx-glr-example-title

.. _sphx_glr_examples_geochem_lambdas_dimreduction.py:


lambdas: Dimensional Reduction
===============================

Orthogonal polynomial decomposition can be used for dimensional reduction of smooth
function over an independent variable, producing an array of independent values
representing the relative weights for each order of component polynomial.

In geochemistry, the most applicable use case is for reduction Rare Earth Element (REE)
profiles. The REE are a collection of elements with broadly similar physicochemical
properties (the lanthanides), which vary with ionic radii. Given their similar behaviour
and typically smooth function of normalised abundance vs. ionic radii, the REE profiles
and their shapes can be effectively parameterised and dimensionally reduced (14 elements
summarised by 3-4 shape parameters).

Here we generate some example data, reduce these to lambda values, and plot the
resulting dimensionally reduced data.


.. code-block:: default

    import numpy as np
    import pandas as pd
    from pathlib import Path
    import matplotlib.pyplot as plt
    from pyrolite.geochem.ind import REE, get_ionic_radii
    from pyrolite.plot.spider import REE_v_radii
    from pyrolite.util.math import lambdas, lambda_poly_func, OP_constants


    np.random.seed(82)







First we'll generate some example data:



.. code-block:: default

    no_analyses = 1000

    data_ree = REE(dropPm=True)
    data_radii = np.array(get_ionic_radii(data_ree, charge=3, coordination=8))
    data_radii = np.tile(data_radii, (1, no_analyses)).reshape(
        no_analyses, data_radii.shape[0]
    )

    noise = np.random.randn(*data_radii.shape) * 0.1
    constant = -0.1
    lin = np.tile(np.linspace(3.0, 0.0, data_radii.shape[1]), (no_analyses, 1))
    lin = (lin.T * (1.1 + 0.4 * np.random.rand(data_radii.shape[0]))).T
    quad = -1.2 * (data_radii - 1.11) ** 2.0

    lnY = noise + constant + lin + quad

    for ix, el in enumerate(data_ree):
        if el in ["Ce", "Eu"]:
            lnY[:, ix] += np.random.rand(no_analyses) * 0.6








.. code-block:: default

    df = pd.DataFrame(np.exp(lnY), columns=data_ree)








.. code-block:: default

    ax = df.pyroplot.REE(
        marker="D",
        alpha=0.01,
        c="0.5",
        markerfacecolor="k",
        markeredgecolor="k",
        index="elements",
    )
    plt.show()



.. image:: /examples/geochem/images/sphx_glr_lambdas_dimreduction_001.png
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    C:\ProgramData\Anaconda3_64\lib\site-packages\pandas\core\indexing.py:1494: FutureWarning: 
    Passing list-likes to .loc or [] with any missing label will raise
    KeyError in the future, you can use .reindex() as an alternative.

    See the documentation here:
    https://pandas.pydata.org/pandas-docs/stable/indexing.html#deprecate-loc-reindex-listlike
      return self._getitem_tuple(key)




From this data we can calculate and plot the lambda values:



.. code-block:: default

    ls = df.pyrochem.lambda_lnREE(
        exclude=["Ce", "Eu", "Pm"], degree=4, norm_to="Chondrite_PON"
    )









.. code-block:: default


    fig, ax = plt.subplots(1, 3, figsize=(9, 3))
    ax_labels = ls.columns

    for ix in range(ls.columns.size - 1):
        l1, l2 = ax_labels[ix], ax_labels[ix + 1]
        ax[ix].scatter(ls[l1], ls[l2], alpha=0.1, c="k")
        ax[ix].set_xlabel(l1)
        ax[ix].set_ylabel(l2)

    plt.tight_layout()
    fig.suptitle("lambdas for Dimensional Reduction", y=1.05)



.. image:: /examples/geochem/images/sphx_glr_lambdas_dimreduction_002.png
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    Text(0.5, 1.05, 'lambdas for Dimensional Reduction')



For more on using orthogonal polynomials to describe geochemical pattern data, see:
O’Neill, H.S.C., 2016. The Smoothness and Shapes of Chondrite-normalized Rare Earth
Element Patterns in Basalts. J Petrology 57, 1463–1508.
`doi: 10.1093/petrology/egw047 <https://doi.org/10.1093/petrology/egw047>`__.

.. seealso::

  Examples:
    `Visualising Orthogonal Polynomials <lambdavis.html>`__


.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  27.022 seconds)


.. _sphx_glr_download_examples_geochem_lambdas_dimreduction.py:


.. only :: html

 .. container:: sphx-glr-footer
    :class: sphx-glr-footer-example


  .. container:: binder-badge

    .. image:: https://mybinder.org/badge_logo.svg
      :target: https://mybinder.org/v2/gh/morganjwilliams/pyrolite/develop?filepath=docs/source/examples/geochem/lambdas_dimreduction.ipynb
      :width: 150 px


  .. container:: sphx-glr-download

     :download:`Download Python source code: lambdas_dimreduction.py <lambdas_dimreduction.py>`



  .. container:: sphx-glr-download

     :download:`Download Jupyter notebook: lambdas_dimreduction.ipynb <lambdas_dimreduction.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
