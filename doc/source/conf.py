"""Sphinx documentation configuration file."""

from datetime import datetime
import inspect
import os
import pathlib
import sys
import warnings

import pyvista
from pyvista.plotting.utilities.sphinx_gallery import DynamicScraper
from sphinx.builders.latex import LaTeXBuilder
import sphinx.util.inspect

from ansys.acp.core import extras


def _signature(
    subject,
    bound_method: bool = False,
    type_aliases=None,
):
    """Monkeypatch for 'sphinx.util.inspect.signature'.

    This function defines a custom signature function which is used by the 'sphinx.ext.autodoc'.
    The main purpose is to force / fix using the class parameter type hints instead of the class
    attribute type hints.
    See https://github.com/sphinx-doc/sphinx/issues/11207 for context.
    """

    # Import classes which were guarded with a 'typing.TYPE_CHECKING' explicitly here, otherwise
    # the 'eval' in 'inspect.signature' will fail.
    # Some imports are needed because these types occur in a dataclass base class, which is
    # not in the same module as the documented class.
    from collections.abc import Sequence  # noqa: F401

    import numpy as np  # noqa: F401
    import pyvista  # noqa: F401
    from pyvista.core.pointset import PolyData, UnstructuredGrid  # noqa: F401

    from ansys.acp.core import (  # noqa: F401
        BooleanSelectionRule,
        CADComponent,
        GeometricalSelectionRule,
        Model,
        ModelingGroup,
    )

    # Import type aliases so that they can be resolved correctly.
    from ansys.acp.core._tree_objects.field_definition import (  # noqa: F401
        _SCOPE_ENTITIES_LINKABLE_TO_FIELD_DEFINITION,
    )
    from ansys.acp.core._tree_objects.linked_selection_rule import (  # noqa: F401
        _LINKABLE_SELECTION_RULE_TYPES,
    )
    from ansys.acp.core._tree_objects.oriented_selection_set import (  # noqa: F401
        _SELECTION_RULES_LINKABLE_TO_OSS,
    )
    from ansys.acp.core._tree_objects.sensor import _LINKABLE_ENTITY_TYPES  # noqa: F401
    from ansys.acp.core._tree_objects.sublaminate import _LINKABLE_MATERIAL_TYPES  # noqa: F401
    from ansys.acp.core._utils.typing_helper import StrEnum
    from ansys.acp.core.mesh_data import MeshData, ScalarData, VectorData  # noqa: F401
    from ansys.dpf.composites.data_sources import ContinuousFiberCompositesFiles  # noqa: F401
    from ansys.dpf.core import UnitSystem  # noqa: F401
    import ansys.mechanical.core as pymechanical  # noqa: F401

    signature = inspect.signature(subject, locals=locals(), eval_str=True)

    if signature.parameters:
        parameters = list(signature.parameters.values())
        if parameters[0].name == "self":
            parameters.pop(0)
        # dgresch Oct'24:
        # Hack to fix the remaining issues with the signature. This is simpler than
        # trying to get 'inspect.signature' to fully work, which would need to be done
        # inside the 'define_create_method' function.
        # I believe (speculation) the reason for this is that the 'create_' and 'add_'
        # methods have an explicit __signature__ attribute, which stops the
        # 'inspect.signature' from performing the 'eval'.
        for i, param in enumerate(parameters):
            if param.annotation in [
                "Sequence[_SCOPE_ENTITIES_LINKABLE_TO_FIELD_DEFINITION]",
                "Sequence[_SELECTION_RULES_LINKABLE_TO_OSS]",
                "Sequence[_LINKABLE_ENTITY_TYPES]",
                "_LINKABLE_MATERIAL_TYPES",
            ]:
                param = param.replace(annotation=eval(param.annotation))
            # Represent StrEnum defaults as their string value, since this is
            # easier to understand for library users. The enum type is still
            # available in the type annotations.
            if isinstance(param.default, StrEnum):
                param = param.replace(default=param.default.value)
            parameters[i] = param
        signature = signature.replace(parameters=parameters)
    return signature


sphinx.util.inspect.signature = _signature
napoleon_attr_annotations = False


LaTeXBuilder.supported_image_types = ["image/png", "image/pdf", "image/svg+xml"]
from ansys_sphinx_theme import (
    ansys_favicon,
    ansys_logo_white,
    ansys_logo_white_cropped,
    get_version_match,
    latex,
    watermark,
)

from ansys.acp.core import __version__

SKIP_GALLERY = os.environ.get("PYACP_DOC_SKIP_GALLERY", "0").lower() in ("1", "true")
SKIP_API = os.environ.get("PYACP_DOC_SKIP_API", "0").lower() in ("1", "true")
SOURCE_DIR = pathlib.Path(__file__).parent

# nested example index files are directly included in the parent index file
exclude_patterns = ["examples/*/index.rst"]
if SKIP_API:
    # Exclude all API documentation except the top-level index file:
    # Exclude files on the top level explicitly, except 'index.rst'
    for file_path in (SOURCE_DIR / "api").iterdir():
        if not file_path.name == "index.rst":
            pattern = str(file_path.relative_to(SOURCE_DIR).as_posix())
            exclude_patterns.append(pattern)
    # Exclude all files in nested directories
    exclude_patterns.append("api/**/*.rst")


jinja_contexts = {
    "conditional_skip": {"skip_api": SKIP_API, "skip_gallery": SKIP_GALLERY},
}

# Manage errors
pyvista.set_error_output_file("errors.txt")

# Ensure that offscreen rendering is used for docs generation
pyvista.OFF_SCREEN = True

# necessary when building the sphinx gallery
pyvista.BUILDING_GALLERY = True

# Set the plot theme to be used in the documentation
extras.set_plot_theme()

# ignore the matplotlib warning when .show() is called
warnings.filterwarnings("ignore", category=UserWarning, message=".*is non-interactive.*")

# Project information
project = "ansys-acp-core"
copyright = f"(c) {datetime.now().year} ANSYS, Inc. All rights reserved"
author = "Ansys Inc."
release = version = __version__

# use the default pyansys logo
html_theme = "ansys_sphinx_theme"


cname = os.getenv("DOCUMENTATION_CNAME", "acp.docs.pyansys.com")
"""The canonical name of the webpage hosting the documentation."""

# specify the location of your github repo
html_theme_options = {
    "logo": "pyansys",
    "github_url": "https://github.com/ansys/pyacp",
    "show_prev_next": True,
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
    "numpydoc",
    "sphinx_copybutton",
    "sphinx_gallery.gen_gallery",
    "sphinx_design",  # needed for pyvista offlineviewer directive
    "sphinx_jinja",
    "pyvista.ext.plot_directive",
    "pyvista.ext.viewer_directive",
]

# Intersphinx mapping
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    # kept here as an example
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    # "matplotlib": ("https://matplotlib.org/stable", None),
    # "pandas": ("https://pandas.pydata.org/pandas-docs/stable", None),
    "grpc": ("https://grpc.github.io/grpc/python/", None),
    "protobuf": ("https://googleapis.dev/python/protobuf/latest/", None),
    "pyvista": ("https://docs.pyvista.org/", None),
    "ansys-dpf-core": ("https://dpf.docs.pyansys.com/version/stable/", None),
    "ansys-dpf-composites": ("https://composites.dpf.docs.pyansys.com/version/stable/", None),
    "ansys-mechanical-core": ("https://mechanical.docs.pyansys.com/version/stable/", None),
}

nitpick_ignore = [
    # Ignore TypeVar / TypeAlias defined within PyACP: they are either not recognized correctly,
    # or misidentified as a class.
    ("py:class", "_PATH"),
    ("py:class", "ChildT"),
    ("py:class", "CreatableValueT"),
]
nitpick_ignore_regex = [
    ("py:class", r"(typing\.|typing_extensions\.)?Self"),
    ("py:class", r"(numpy\.typing|npt)\.NDArray"),
    ("py:class", r"(numpy|np)\.float64"),
    ("py:class", r"(numpy|np)\.int32"),
    ("py:class", r"(numpy|np)\.int64"),
    ("py:class", r"ansys\.api\.acp\..*"),
    ("py:class", "None -- .*"),  # from collections.abc
    # Ignore TypeVars defined within PyACP: they are either not recognized correctly,
    # or misidentified as a class.
    ("py:class", r"^(.*\.)?ValueT$"),
    ("py:class", r"^(.*\.)?TC$"),
    ("py:class", r"^(.*\.)?TV$"),
    ("py:class", r"ansys\.acp.core\..*\.AttribT"),
    ("py:class", r"ansys\.acp.core\..*\.ChildT"),
    ("py:class", r"ansys\.acp.core\..*\.CreatableValueT"),
    ("py:class", r"ansys\.acp.core\..*\.ScalarDataT"),
    ("py:class", r"ansys\.acp.core\..*\.MeshDataT"),
]

# sphinx.ext.autodoc configuration
autodoc_typehints = "description"
autodoc_typehints_description_target = "documented_params"

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

if SKIP_GALLERY:
    # Generate the gallery without executing the code. The gallery will not
    # contain the output of the code cells.
    # This is useful for more quickly building the documentation.
    gallery_filename_pattern = "<MATCH NOTHING>"
else:
    if sys.platform == "win32":
        gallery_filename_pattern = r".*\.py"
    else:
        gallery_filename_pattern = (
            r"^(?!.*pymechanical.*\.py).*\.py"  # skip pymechanical examples on non-Windows
        )

examples_dirs_base = pathlib.Path("../../examples/")
gallery_dirs_base = pathlib.Path("examples/")
example_subdir_names = ["modeling_features", "workflows", "use_cases"]

# sphinx gallery options
sphinx_gallery_conf = {
    # convert rst to md for ipynb
    "pypandoc": True,
    # path to your examples scripts
    "examples_dirs": [str(examples_dirs_base / subdir) for subdir in example_subdir_names],
    # path where to save gallery generated examples
    "gallery_dirs": [str(gallery_dirs_base / subdir) for subdir in example_subdir_names],
    # Pattern to search for example files
    "filename_pattern": gallery_filename_pattern,
    # Remove the "Download all examples" button from the top level gallery
    "download_all_examples": False,
    # Sort gallery example by filename instead of number of lines (default)
    "within_subsection_order": "FileNameSortKey",
    # directory where function granular galleries are stored
    "backreferences_dir": "api/_gallery_backreferences",
    # Modules for which function level galleries are created.
    "doc_module": ("ansys.acp.core"),
    "exclude_implicit_doc": {"ansys\\.acp\\.core\\._.*"},  # ignore private submodules
    "image_scrapers": (DynamicScraper(), "matplotlib"),
    "ignore_pattern": r"__init__\.py",
    "thumbnail_size": (320, 240),
    "remove_config_comments": True,
}

# Favicon
html_favicon = ansys_favicon

# static path
html_static_path = ["_static"]

# Custom CSS files
# These paths are either relative to html_static_path or fully qualified paths (eg. https://...)
html_css_files = ["custom.css"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
source_suffix = {".rst": "restructuredtext"}

# The master toctree document.
master_doc = "index"

# additional logos for the latex coverpage
latex_additional_files = [watermark, ansys_logo_white, ansys_logo_white_cropped]

# change the preamble of latex with customized title page
# variables are the title of pdf, watermark
latex_elements = {"preamble": latex.generate_preamble(html_title)}
