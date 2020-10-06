# wrap_opencv-python-headless
    rebrand opencv-python-headless as opencv-python

## Introduction

If you want to install [OpenCV](https://github.com/skvark/opencv-python.git) as a Python package, or include it as a dependency in another, (unless you want to build your own,) you'll first have to decide on a _flavour_ (and top-level package name):

> Select the correct package for your environment:

> There are four different packages (see options 1, 2, 3 and 4 below) and you should **SELECT ONLY ONE OF THEM**. Do not install multiple different packages in the same environment. There is no plugin architecture: all the packages use the same namespace (`cv2`). If you installed multiple different packages in the same environment, uninstall them all with ``pip uninstall`` and reinstall only one package.

> **a.** Packages for standard desktop environments (Windows, macOS, almost any GNU/Linux distribution)

>   - Option 1 - Main modules package: ``pip install opencv-python``
>   - Option 2 - Full package (contains both main modules and contrib/extra modules): ``pip install opencv-contrib-python`` (check contrib/extra modules listing from [OpenCV documentation](https://docs.opencv.org/master/))

> **b.** Packages for server (headless) environments (such as Docker, cloud environments etc.), no GUI library dependencies

> These packages are smaller than the two other packages above because they do not contain any GUI functionality (not compiled with Qt / other GUI components). This means that the packages avoid a heavy dependency chain to X11 libraries and you will have for example smaller Docker images as a result. You should always use these packages if you do not use `cv2.imshow` et al. or you are using some other package (such as PyQt) than OpenCV to create your GUI.

> - Option 3 - Headless main modules package: ``pip install opencv-python-headless``
> - Option 4 - Headless full package (contains both main modules and contrib/extra modules): ``pip install opencv-contrib-python-headless`` (check contrib/extra modules listing from [OpenCV documentation](https://docs.opencv.org/master/))

This creates a problem for dependent packages, though: Whatever OpenCV flavour you choose to depend on, your dependents will also rely on that particular choice. To make matters worse, `pip` does not consider these flavours as conflict when installed in parallel (despite all sharing the same submodule/subpackage name `cv2`).

So practically, if you depend on some OpenCV-dependent packages, but want to avoid the X11 dependencies, _any_ of your dependencies could drag them back in if it chose to require `opencv-python` instead of `opencv-python-headless`.

If, however, you know for certain that none of them _actually_ need X11, and might thus easily have been chosen `headless`, then this package is for you. It merely re-brands `opencv-python-headless` as `opencv-python` by requiring the former but providing the latter in an otherwise empty package.

You can install this package _prior_ to other dependencies and thus block any subsequent installation of the actual prebuilt `opencv-python`. (But to make this work including a mirrored version number, `opencv-python-headless` needs to be installed early, too. Thus, installing this package will also install `opencv-python-headless` if not already present.)

## Installation

    # git clone and chdir, then pip:
    pip install .
    # or, pip via git:
    pip install opencv-python@git+https://github.com/bertsky/wrap_opencv-python-headless


