# Sphinx MD
Using Sphinx with Markdown to create documentation.

Uses [MyST](https://myst-parser.readthedocs.io/en/latest/index.html) to add the Markdown functionality to Sphinx,
replacing the RST syntax.

Mostly followed instructions in this course: 
[Static Sites with Sphinx and Markdown](https://training.talkpython.fm/courses/details/static-sites-with-sphinx-and-markdown)
(free at the time of this writing).

This project is intended to be used as reference to other projects on how to setup and use Sphinx with MyST.

Main features:

* Use MD syntax for documentation, which developers are usually more familiar with, instead of RST.
* Doc files are in the `/docs` folder.
* Using `inv` ([pyinvoke](https://www.pyinvoke.org/)) instead of `make`.<br>
  See `tasks.py` for more details on commands.
