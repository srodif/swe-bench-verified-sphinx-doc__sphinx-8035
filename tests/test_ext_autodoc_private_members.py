"""
    test_ext_autodoc_private_members
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Test the autodoc extension.  This tests mainly for private-members option.

    :copyright: Copyright 2007-2020 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import pytest

from test_ext_autodoc import do_autodoc


@pytest.mark.sphinx('html', testroot='ext-autodoc')
def test_private_field(app):
    app.config.autoclass_content = 'class'
    options = {"members": None}
    actual = do_autodoc(app, 'module', 'target.private', options)
    assert list(actual) == [
        '',
        '.. py:module:: target.private',
        '',
        '',
        '.. py:function:: _public_function(name)',
        '   :module: target.private',
        '',
        '   public_function is a docstring().',
        '',
        '   :meta public:',
        '',
    ]


@pytest.mark.sphinx('html', testroot='ext-autodoc')
def test_private_field_and_private_members(app):
    app.config.autoclass_content = 'class'
    options = {"members": None,
               "private-members": None}
    actual = do_autodoc(app, 'module', 'target.private', options)
    assert list(actual) == [
        '',
        '.. py:module:: target.private',
        '',
        '',
        '.. py:function:: _another_private_function(name)',
        '   :module: target.private',
        '',
        '   another_private_function is a docstring().',
        '',
        '   :meta private:',
        '',
        '',
        '.. py:function:: _public_function(name)',
        '   :module: target.private',
        '',
        '   public_function is a docstring().',
        '',
        '   :meta public:',
        '',
        '',
        '.. py:function:: _special_private_function(name)',
        '   :module: target.private',
        '',
        '   special_private_function is a docstring().',
        '',
        '   :meta private:',
        '',
        '',
        '.. py:function:: private_function(name)',
        '   :module: target.private',
        '',
        '   private_function is a docstring().',
        '',
        '   :meta private:',
        '',
    ]


@pytest.mark.sphinx('html', testroot='ext-autodoc')
def test_private_members_with_specific_names(app):
    app.config.autoclass_content = 'class'
    options = {"members": None,
               "private-members": "_another_private_function,_special_private_function"}
    actual = do_autodoc(app, 'module', 'target.private', options)
    assert list(actual) == [
        '',
        '.. py:module:: target.private',
        '',
        '',
        '.. py:function:: _another_private_function(name)',
        '   :module: target.private',
        '',
        '   another_private_function is a docstring().',
        '',
        '   :meta private:',
        '',
        '',
        '.. py:function:: _public_function(name)',
        '   :module: target.private',
        '',
        '   public_function is a docstring().',
        '',
        '   :meta public:',
        '',
        '',
        '.. py:function:: _special_private_function(name)',
        '   :module: target.private',
        '',
        '   special_private_function is a docstring().',
        '',
        '   :meta private:',
        '',
    ]


@pytest.mark.sphinx('html', testroot='ext-autodoc')
def test_private_members_with_single_name(app):
    app.config.autoclass_content = 'class'
    options = {"members": None,
               "private-members": "_special_private_function"}
    actual = do_autodoc(app, 'module', 'target.private', options)
    assert list(actual) == [
        '',
        '.. py:module:: target.private',
        '',
        '',
        '.. py:function:: _public_function(name)',
        '   :module: target.private',
        '',
        '   public_function is a docstring().',
        '',
        '   :meta public:',
        '',
        '',
        '.. py:function:: _special_private_function(name)',
        '   :module: target.private',
        '',
        '   special_private_function is a docstring().',
        '',
        '   :meta private:',
        '',
    ]
