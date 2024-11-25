.. vale off

This directory contains thumbnails for the gallery examples which are
not built in CI. The thumbnails are used in the gallery index page.

To update a thumbnail:
- Remove the ``# sphinx_gallery_thumbnail_path`` configuration in the
  example file.
- Build the documentation, running the example that you want to update.
  You may need to add a configuration option like
  ``# sphinx_gallery_thumbnail_number = -1`` to select the image which should
  be used as thumbnail. [1]
- Copy the generated thumbnail from the example directory to this one.
- Re-add the ``# sphinx_gallery_thumbnail_path`` configuration in the
  example file.

NOTE: If the example file has been renamed since the last time the thumbnail
was generated, the thumbnail filename will also be different.

[1] These options conflict with ``# sphinx_gallery_thumbnail_path``, so they
cannot be added permanently to the example file.
