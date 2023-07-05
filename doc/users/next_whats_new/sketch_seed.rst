``sketch_seed`` parameter for rcParams
----------------------------------------------------

`~matplotlib.rcParams` now has a new parameter ``path.sketch_seed``.
It's default value is 0 and accepted values are any non negative integer.
This allows the user to set a value to the seed for the internal Pseudo number generator in one of three ways.

1) Directly changing the rcParam:
Eg. rcParams['path.sketch_seed']= 20

2) Passing a value to the new *seed* parameter of `~matplotlib.pyplot.xkcd` function:
Eg. plt.xkcd(seed=20)

3) Passing a value to the new *seed* parameter of `~matplotlib.artist.Artist.set_sketch_params` function:
Eg. Artist.set_sketch_params(seed=20)

Note that using any one of these 3 methods changes the value of rcParams['path.sketch_seed'] variable.
The seed will also have a rolling(auto incrementing) characteristic.
Two codes with the same parameters and same seed will be exactly same to one another.


.. plot::
    :include-source: true

    import matplotlib.pyplot as plt
    from matplotlib import rcParams

    rcParams['path.sketch_seed']=0
    with plt.xkcd():
        import matplotlib
        from matplotlib import gridspec
        rcParams['path.sketch']=(2,120,40)
        pat,txt=plt.pie([10,20,30,40],wedgeprops={'edgecolor':'black'})
        plt.legend(pat,['first','second','third','fourth'],loc='best')
        plt.title("seed = 0")
    plt.show()

.. plot::
    :include-source: true

    import matplotlib.pyplot as plt
    from matplotlib import rcParams
    from matplotlib.artist import Artist

    Artist().set_sketch_params(seed=20)
    with plt.xkcd():
        import matplotlib
        from matplotlib import gridspec

        rcParams['path.sketch']=(2,120,40)

        pat,txt=plt.pie([10,20,30,40],wedgeprops={'edgecolor':'black'})
        plt.legend(pat,['first','second','third','fourth'],loc='best')
        plt.title("seed = 20")
    plt.show()

.. plot::
    :include-source: true

    import matplotlib.pyplot as plt
    from matplotlib import rcParams

    with plt.xkcd(seed=19680801):
        import matplotlib
        from matplotlib import gridspec

        rcParams['path.sketch']=(2,120,40)

        pat,txt=plt.pie([10,20,30,40],wedgeprops={'edgecolor':'black'})
        plt.legend(pat,['first','second','third','fourth'],loc='best')
        plt.title("seed = 19680801")
    plt.show()
