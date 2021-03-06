.. rst-class:: sphx-glr-example-title

.. _sphx_glr_examples_util_TAS.py:


TAS Classifier
==============

Some simple discrimination methods are implemented,
including the Total Alkali-Silica (TAS) classification.


.. code-block:: default

    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from pyrolite.util.classification import Geochemistry
    from pyrolite.util.synthetic import test_df, random_cov_matrix








We'll first generate some synthetic data to play with:



.. code-block:: default

    mean = np.array([49, 11, 15, 4, 0.5, 4, 1.5])
    df = (
        test_df(
            cols=["SiO2", "CaO", "MgO", "FeO", "TiO2", "Na2O", "K2O"],
            mean=mean,
            index_length=100,
            seed=82,
        )
        * mean.sum()
    )

    df.head(3)





.. only:: builder_html

.. raw:: html

            <div>
        <style scoped>
            .dataframe tbody tr th:only-of-type {
                vertical-align: middle;
            }

            .dataframe tbody tr th {
                vertical-align: top;
            }

            .dataframe thead th {
                text-align: right;
            }
        </style>
        <table border="1" class="dataframe">
          <thead>
            <tr style="text-align: right;">
              <th></th>
              <th>SiO2</th>
              <th>CaO</th>
              <th>MgO</th>
              <th>FeO</th>
              <th>TiO2</th>
              <th>Na2O</th>
              <th>K2O</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th>0</th>
              <td>50.949</td>
              <td>10.522</td>
              <td>14.147</td>
              <td>3.752</td>
              <td>0.435</td>
              <td>3.851</td>
              <td>1.342</td>
            </tr>
            <tr>
              <th>1</th>
              <td>47.525</td>
              <td>11.133</td>
              <td>15.962</td>
              <td>4.216</td>
              <td>0.513</td>
              <td>4.189</td>
              <td>1.462</td>
            </tr>
            <tr>
              <th>2</th>
              <td>48.273</td>
              <td>11.044</td>
              <td>16.082</td>
              <td>3.823</td>
              <td>0.479</td>
              <td>3.935</td>
              <td>1.363</td>
            </tr>
          </tbody>
        </table>
        </div>
        <br />
        <br />

We can visualise how this chemistry corresponds to the TAS diagram:



.. code-block:: default

    from pyrolite.util.classification import Geochemistry

    df["TotalAlkali"] = df["Na2O"] + df["K2O"]
    cm = Geochemistry.TAS()

    fig, ax = plt.subplots(1)

    ax.scatter(df["SiO2"], df["TotalAlkali"], c="k", alpha=0.2)
    cm.add_to_axes(ax, alpha=0.5, zorder=-1)




.. image:: /examples/util/images/sphx_glr_TAS_001.png
    :class: sphx-glr-single-img





We can now classify this data according to the fields of the TAS diagram, and
add this as a column to the dataframe. Similarly, we can extract which rock names
the TAS fields correspond to:



.. code-block:: default

    df["TAS"] = cm.classify(df)
    df["Rocknames"] = df.TAS.apply(
        lambda x: cm.clsf.fields.get(x, {"names": None})["names"]
    )
    df["TAS"].unique()




.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    array(['S1', 'U1', 'Bs', 'O1', 'S2', 'Ba'], dtype=object)



We could now take the TAS classes and use them to colorize our points for plotting
on the TAS diagram, or more likely, on another plot. Here the relationship to the
TAS diagram is illustrated:



.. code-block:: default


    colorize = {field: plt.cm.tab10(ix) for ix, field in enumerate(df["TAS"].unique())}

    fig, ax = plt.subplots(1)

    ax.scatter(
        df["SiO2"], df["TotalAlkali"], c=df["TAS"].apply(lambda x: colorize[x]), alpha=0.7
    )
    cm.add_to_axes(ax, alpha=0.5, zorder=-1)



.. image:: /examples/util/images/sphx_glr_TAS_002.png
    :class: sphx-glr-single-img






.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  3.106 seconds)


.. _sphx_glr_download_examples_util_TAS.py:


.. only :: html

 .. container:: sphx-glr-footer
    :class: sphx-glr-footer-example


  .. container:: binder-badge

    .. image:: https://mybinder.org/badge_logo.svg
      :target: https://mybinder.org/v2/gh/morganjwilliams/pyrolite/develop?filepath=docs/source/examples/util/TAS.ipynb
      :width: 150 px


  .. container:: sphx-glr-download

     :download:`Download Python source code: TAS.py <TAS.py>`



  .. container:: sphx-glr-download

     :download:`Download Jupyter notebook: TAS.ipynb <TAS.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
