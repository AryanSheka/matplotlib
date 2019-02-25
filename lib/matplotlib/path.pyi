from .bezier import BezierSegment
from .transforms import Affine2D, Transform, Bbox
from collections.abc import Generator, Iterable, Sequence

import numpy as np
from numpy.typing import ArrayLike

from typing import Any, overload

class Path:
    code_type: type[np.uint8]
    STOP: np.uint8
    MOVETO: np.uint8
    LINETO: np.uint8
    CURVE3: np.uint8
    CURVE4: np.uint8
    CLOSEPOLY: np.uint8
    NUM_VERTICES_FOR_CODE: dict[np.uint8, int]

    def __init__(
        self,
        vertices: ArrayLike,
        codes: ArrayLike | None = ...,
        _interpolation_steps: int = ...,
        closed: bool = ...,
        readonly: bool = ...,
    ) -> None: ...
    @property
    def vertices(self) -> ArrayLike: ...
    @vertices.setter
    def vertices(self, vertices: ArrayLike) -> None: ...
    @property
    def codes(self) -> ArrayLike: ...
    @codes.setter
    def codes(self, codes: ArrayLike) -> None: ...
    @property
    def simplify_threshold(self) -> float: ...
    @simplify_threshold.setter
    def simplify_threshold(self, threshold: float) -> None: ...
    @property
    def should_simplify(self) -> bool: ...
    @should_simplify.setter
    def should_simplify(self, should_simplify: bool) -> None: ...
    @property
    def readonly(self) -> bool: ...
    def copy(self) -> Path: ...
    def __deepcopy__(self, memo: dict[int, Any] | None = ...) -> Path: ...
    deepcopy = __deepcopy__

    @classmethod
    def make_compound_path_from_polys(cls, XY: ArrayLike) -> Path: ...
    @classmethod
    def make_compound_path(cls, *args: Path) -> Path: ...
    def __len__(self) -> int: ...
    def iter_segments(
        self,
        transform: Transform | None = ...,
        remove_nans: bool = ...,
        clip: tuple[float, float, float, float] | None = ...,
        snap: bool | None = ...,
        stroke_width: float = ...,
        simplify: bool | None = ...,
        curves: bool = ...,
        sketch: tuple[float, float, float, int] | None = ...,
    ) -> Generator[tuple[np.ndarray, np.uint8], None, None]: ...
    def iter_bezier(self, **kwargs) -> Generator[BezierSegment, None, None]: ...
    def cleaned(
        self,
        transform: Transform | None = ...,
        remove_nans: bool = ...,
        clip: tuple[float, float, float, float] | None = ...,
        *,
        simplify: bool | None = ...,
        curves: bool = ...,
        stroke_width: float = ...,
        snap: bool | None = ...,
        sketch: tuple[float, float, float, int] | None = ...
    ) -> Path: ...
    def transformed(self, transform: Transform) -> Path: ...
    def contains_point(
        self,
        point: tuple[float, float],
        transform: Transform | None = ...,
        radius: float = ...,
    ) -> bool: ...
    def contains_points(
        self, points: ArrayLike, transform: Transform | None = ..., radius: float = ...
    ) -> np.ndarray: ...
    def contains_path(self, path: Path, transform: Transform | None = ...) -> bool: ...
    def get_extents(self, transform: Transform | None = ..., **kwargs) -> Bbox: ...
    def intersects_path(self, other: Path, filled: bool = ...) -> bool: ...
    def intersects_bbox(self, bbox: Bbox, filled: bool = ...) -> bool: ...
    def interpolated(self, steps: int) -> Path: ...
    def to_polygons(
        self,
        transform: Transform | None = ...,
        width: float = ...,
        height: float = ...,
        closed_only: bool = ...,
    ) -> list[ArrayLike]: ...
    @classmethod
    def unit_rectangle(cls) -> Path: ...
    @classmethod
    def unit_regular_polygon(cls, numVertices: int) -> Path: ...
    @classmethod
    def unit_regular_star(cls, numVertices: int, innerCircle: float = ...) -> Path: ...
    @classmethod
    def unit_regular_asterisk(cls, numVertices: int) -> Path: ...
    @classmethod
    def unit_circle(cls) -> Path: ...
    @classmethod
    def circle(
        cls,
        center: tuple[float, float] = ...,
        radius: float = ...,
        readonly: bool = ...,
    ) -> Path: ...
    @classmethod
    def unit_circle_righthalf(cls) -> Path: ...
    @classmethod
    def arc(
        cls, theta1: float, theta2: float, n: int | None = ..., is_wedge: bool = ...
    ) -> Path: ...
    @classmethod
    def wedge(cls, theta1: float, theta2: float, n: int | None = ...) -> Path: ...
    @overload
    @staticmethod
    def hatch(hatchpattern: str, density: float = ...) -> Path: ...
    @overload
    @staticmethod
    def hatch(hatchpattern: None, density: float = ...) -> None: ...
    def clip_to_bbox(self, bbox: Bbox, inside: bool = ...) -> Path: ...

def get_path_collection_extents(
    master_transform: Transform,
    paths: Sequence[Path],
    transforms: Iterable[Affine2D],
    offsets: ArrayLike,
    offset_transform: Affine2D,
) -> Bbox: ...
