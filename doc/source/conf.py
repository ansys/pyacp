"""Sphinx documentation configuration file."""

from datetime import datetime
import os

import pyvista
from pyvista.plotting.utilities.sphinx_gallery import DynamicScraper
from sphinx.builders.latex import LaTeXBuilder

LaTeXBuilder.supported_image_types = ["image/png", "image/pdf", "image/svg+xml"]
from ansys_sphinx_theme import (
    ansys_favicon,
    ansys_logo_white,
    ansys_logo_white_cropped,
    get_version_match,
    latex,
    pyansys_logo_black,
    watermark,
)
from sphinx_gallery.sorting import FileNameSortKey

from ansys.acp.core import __version__

SKIP_GALLERY = os.environ.get("PYACP_DOC_SKIP_GALLERY", "0").lower() in ("1", "true")
SKIP_API = os.environ.get("PYACP_DOC_SKIP_API", "0").lower() in ("1", "true")

exclude_patterns = []
if SKIP_API:
    exclude_patterns.append("api/*")


jinja_contexts = {
    "conditional_skip": {"skip_api": SKIP_API, "skip_gallery": SKIP_GALLERY},
}


# PyMAPDL and PyDPF override the default PyVista theme, so we need to import it
# here to have a chance of re-setting it.
import ansys.mapdl.core  # isort:skip
import ansys.dpf.core  # isort:skip # noqa: F401

# Manage errors
pyvista.set_error_output_file("errors.txt")

# Ensure that offscreen rendering is used for docs generation
pyvista.OFF_SCREEN = True

# necessary when building the sphinx gallery
pyvista.BUILDING_GALLERY = True

pyvista.global_theme = pyvista.themes.DocumentTheme()
pyvista.global_theme.cmap = "viridis_r"

# Project information
project = "ansys-acp-core"
copyright = f"(c) {datetime.now().year} ANSYS, Inc. All rights reserved"
author = "Ansys Inc."
release = version = __version__

# use the default pyansys logo
html_logo = pyansys_logo_black
html_theme = "ansys_sphinx_theme"


cname = os.getenv("DOCUMENTATION_CNAME", "acp.docs.pyansys.com")
"""The canonical name of the webpage hosting the documentation."""

# specify the location of your github repo
html_theme_options = {
    "github_url": "https://github.com/ansys/pyacp",
    "show_prev_next": False,
    "show_breadcrumbs": True,
    "additional_breadcrumbs": [("PyAnsys", "https://docs.pyansys.com/")],
    "switcher": {
        "json_url": f"https://{cname}/versions.json",
        "version_match": get_version_match(__version__),
    },
    "check_switcher": False,
}
html_title = html_short_title = "PyACP"

# Sphinx extensions
extensions = [
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "numpydoc",
    "sphinx_copybutton",
]
if not SKIP_GALLERY:
    extensions += ["sphinx_gallery.gen_gallery"]
extensions += [
    "sphinx_design",  # needed for pyvista offlineviewer directive
    "sphinx_jinja",
    "pyvista.ext.plot_directive",
    "pyvista.ext.viewer_directive",
]

# Intersphinx mapping
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    # kept here as an example
    # "scipy": ("https://docs.scipy.org/doc/scipy/reference", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    # "matplotlib": ("https://matplotlib.org/stable", None),
    # "pandas": ("https://pandas.pydata.org/pandas-docs/stable", None),
    "grpc": ("https://grpc.github.io/grpc/python/", None),
    "protobuf": ("https://googleapis.dev/python/protobuf/latest/", None),
    "pyvista": ("https://docs.pyvista.org/version/stable", None),
    "ansys-dpf-core": ("https://dpf.docs.pyansys.com/version/stable/", None),
    "ansys-dpf-composites": ("https://composites.dpf.docs.pyansys.com/version/stable/", None),
}

nitpick_ignore = [
    ("py:class", "typing.Self"),
    ("py:class", "numpy.float64"),
    ("py:class", "numpy.int32"),
    ("py:class", "numpy.int64"),
    # Ignore TypeVar / TypeAlias defined within PyACP: they are either not recognized correctly,
    # or misidentified as a class.
    ("py:class", "_PATH"),
]
nitpick_ignore_regex = [
    ("py:class", r"ansys\.api\.acp\..*"),
    ("py:class", "None -- .*"),  # from collections.abc
    # Ignore TypeVars defined within PyACP: they are either not recognized correctly,
    # or misidentified as a class.
    ("py:class", r"^(.*\.)?ValueT$"),
    ("py:class", r"^(.*\.)?TC$"),
    ("py:class", r"^(.*\.)?TV$"),
    ("py:class", r"ansys\.acp.core\..*\.ChildT"),
    ("py:class", r"ansys\.acp.core\..*\.CreatableValueT"),
    ("py:class", r"ansys\.acp.core\..*\.MeshDataT"),
    ("py:class", r"ansys\.acp.core\..*\.ScalarDataT"),
]
# sphinx_autodoc_typehints configuration
typehints_defaults = "comma"
simplify_optional_unions = False

# numpydoc configuration
numpydoc_show_class_members = False
numpydoc_xref_param_type = True

# Consider enabling numpydoc validation. See:
# https://numpydoc.readthedocs.io/en/latest/validation.html#
numpydoc_validate = True
numpydoc_validation_checks = {
    "GL06",  # Found unknown section
    "GL07",  # Sections are in the wrong order.
    # "GL08",  # The object does not have a docstring
    "GL09",  # Deprecation warning should precede extended summary
    "GL10",  # reST directives {directives} must be followed by two colons
    "SS01",  # No summary found
    "SS02",  # Summary does not start with a capital letter
    "SS03",  # Summary does not end with a period
    "SS04",  # Summary contains heading whitespaces
    "SS05",  # Summary must start with infinitive verb, not third person
    "RT02",  # The first line of the Returns section should contain only the
    # type, unless multiple values are being returned"
}
numpydoc_validation_exclude = {
    # Inherited from collections.abc; since these are internal-only it
    # doesn't make sense to overwrite the __doc__.fex
    r".*\.LinkedObjectList\.clear",
    r".*\.EdgePropertyList\.clear",
}

# sphinx gallery options
sphinx_gallery_conf = {
    # convert rst to md for ipynb
    "pypandoc": True,
    # path to your examples scripts
    "examples_dirs": ["../../examples/"],
    # path where to save gallery generated examples
    "gallery_dirs": ["examples/gallery_examples"],
    # Pattern to search for example files
    "filename_pattern": r"\.py",
    # Remove the "Download all examples" button from the top level gallery
    "download_all_examples": False,
    # Sort gallery example by file name instead of number of lines (default)
    "within_subsection_order": FileNameSortKey,
    # directory where function granular galleries are stored
    "backreferences_dir": None,
    # Modules for which function level galleries are created.  In
    "doc_module": "ansys-acp-core",
    "image_scrapers": (DynamicScraper(), "matplotlib"),
    "ignore_pattern": r"__init__\.py",
    "thumbnail_size": (350, 350),
    "remove_config_comments": True,
}

# Favicon
html_favicon = ansys_favicon

# static path
html_static_path = ["_static"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# additional logos for the latex coverpage
latex_additional_files = [watermark, ansys_logo_white, ansys_logo_white_cropped]

# change the preamble of latex with customized title page
# variables are the title of pdf, watermark
latex_elements = {"preamble": latex.generate_preamble(html_title)}
