``seed`` parameter for ``path.sketch`` of rcParams
----------------------------------------------------

`~matplotlib.rcParams` ``path.sketch`` now has an optional *seed* parameter for the internal pseudo number generator.
It's default value is a randomly generated number.
It can be set to -1 to have a changing seed for every figure/subfigure produced.
Two codes with the same parameters and same seed will be exactly same to one another.

.. plot::
    :include-source: true

    import matplotlib.pyplot as plt
    from matplotlib import rcParams
    with plt.xkcd():
        import matplotlib
        from matplotlib import gridspec

        seed=0
        rcParams['path.sketch']=(2,120,40,seed)

        pat,txt=plt.pie([10,20,30,40],wedgeprops={'edgecolor':'black'})
        plt.legend(pat,['first','second','third','fourth'],loc='best')
        plt.title("seed = 0")
    plt.show()

.. plot::
    :include-source: true

    import matplotlib.pyplot as plt
    from matplotlib import rcParams
    with plt.xkcd():
        import matplotlib
        from matplotlib import gridspec

        seed=-1
        rcParams['path.sketch']=(2,120,40,seed)

        pat,txt=plt.pie([10,20,30,40],wedgeprops={'edgecolor':'black'})
        plt.legend(pat,['first','second','third','fourth'],loc='best')
        plt.title("seed = -1")
    plt.show()

.. plot::
    :include-source: true

    import matplotlib.pyplot as plt
    from matplotlib import rcParams
    with plt.xkcd():
        import matplotlib
        from matplotlib import gridspec

        seed=19680801
        rcParams['path.sketch']=(2,120,40,seed)

        pat,txt=plt.pie([10,20,30,40],wedgeprops={'edgecolor':'black'})
        plt.legend(pat,['first','second','third','fourth'],loc='best')
        plt.title("seed = 19680801")
    plt.show()
