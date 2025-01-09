# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import annotations

import typing

from ansys.api.acp.v0 import solid_model_export_pb2

from .._utils.typing_helper import PATH as _PATH
from ._grpc_helpers.exceptions import wrap_grpc_errors
from .base import CreatableTreeObject
from .enums import (
    SolidModelExportFormat,
    SolidModelSkinExportFormat,
    solid_model_export_format_to_pb,
    solid_model_skin_export_format_to_pb,
)

__all__ = ["SolidModelExportMixin"]


class SolidModelExportMixin(CreatableTreeObject):
    """Mixin class for adding export functionality to the solid model and imported solid model classes."""

    def export(self, path: _PATH, *, format: SolidModelExportFormat) -> None:
        """Export the solid model to a file.

        Parameters
        ----------
        path :
            Path to the file where the solid model is saved.
        format :
            Format of the exported file. Available formats are ``"ansys:h5"``
            and ``"ansys:cdb"``.

        """
        with self._server_wrapper.auto_download(path) as export_path:
            with wrap_grpc_errors():
                self._get_stub().ExportToFile(  # type: ignore
                    solid_model_export_pb2.ExportToFileRequest(
                        resource_path=self._resource_path,
                        path=export_path,
                        format=typing.cast(typing.Any, solid_model_export_format_to_pb(format)),
                    )
                )

    def export_skin(self, path: _PATH, *, format: SolidModelSkinExportFormat) -> None:
        """Export the skin of the solid model to a file.

        Parameters
        ----------
        path :
            Path to the file where the solid model skin is saved.
        format :
            Format of the exported file. Available formats are ``"ansys:cdb"``,
            ``"step"``, ``"iges"``, and ``"stl"``.

        """
        with self._server_wrapper.auto_download(path) as export_path:
            with wrap_grpc_errors():
                self._get_stub().ExportSkin(  # type: ignore
                    solid_model_export_pb2.ExportSkinRequest(
                        resource_path=self._resource_path,
                        path=export_path,
                        format=typing.cast(
                            typing.Any, solid_model_skin_export_format_to_pb(format)
                        ),
                    )
                )
