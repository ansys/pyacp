This directory contains thumbnails for the gallery examples which are
not built in CI. The thumbnails are used in the gallery index page.

To update a thumbnail:
- remove the ``# sphinx_gallery_thumbnail_path`` configuration in the
  example file
- build the documentation, running the example that you want to update
- copy the generated thumbnail from the example directory to this one
- re-add the ``# sphinx_gallery_thumbnail_path`` configuration in the
  example file
