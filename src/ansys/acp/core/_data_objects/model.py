from dataclasses import dataclass

from .resource import Resource

__all__ = ["Model"]


@dataclass
class Model(Resource):
    use_nodal_thicknesses: bool
    draping_offset_correction: bool
    use_default_section_tolerances: bool
    angle_tolerance: float
    relative_thickness_tolerance: float
    minimum_analysis_ply_thickness: float
