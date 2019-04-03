sphinx-graphml
==============

A GraphML charts embedding extension for Sphinx_.

This extensions simply uses the GraphMLViewer_ tool provided by yWorks_. Admittedly, it is based
on Flash and will no longer be supported from the end of 2020, but this is still the easiest and
best option to display a ``.graphml`` chart created with yEd_ in a browser. Hopefully by the end
of 2020 there will be adequate svg-based solutions.


Installation
------------

As simple as it can be with ``pip``::

   pip install sphinx-graphml


Usage
-----

Add the extension name to your ``conf.py``::

   extensions = [
      ...
      'sphinx_graphml',
      ...
   ]


In your documentation::

   .. graphml:: rel/path/to/my_graph.graphml
      :height: 500px

(the default height is 300px)


Issues
------

If you load your documentation from a file (and not from a web server) using a flash player
version higher than 23, you won't see the charts. See
`this article <http://kb.yworks.com/article/676/>`_ and
`this other one <https://forums.adobe.com/thread/2209269>`_ for workarounds.


.. _Sphinx: http://www.sphinx-doc.org/
.. _GraphMLViewer: https://www.yworks.com/products/graphmlviewer
.. _yWorks: https://www.yworks.com/
.. _yEd: https://www.yworks.com/products/yed
