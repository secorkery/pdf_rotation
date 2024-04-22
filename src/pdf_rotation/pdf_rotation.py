"""Determines the orientation of a document.  If the document is not veritical, it will be rotated
   accordingly."""

from typing import Dict, List, Union
import math

ORIENTATIONS = ['Portrait', 'Landscape']

ROTATION_DEGREES = {
    'Portrait': {
        'Vertical': 0,
        'HorizontalRight': 270,
        'UpsideDown': 180,
        'HorizontalLeft': 90
    }
}

DEGREES_ZERO = 0
DEGREES_NINETY = 90
DEGREES_NEGATIVE_ONE_EIGHTY = -180
DEGREES_NEGATIVE_NINETY = -90

class DocumentRotation:
    """A class to determine the orientation of a document based on its polygon coordinates."""

    def __init__(self, orientation: str = 'Portrait', tolerance: int = 1) -> None:
        """
        Initialize DocumentRotation object.

        Args:
            orientation (str): The orientation of the document. Defaults to 'Portrait'.
            tolerance (int): The tolerance for angle comparison. Defaults to 1.
        """
        self._orientation = orientation
        self._tolerance = tolerance

    def get_rotation_angle(self, polygon: List[Dict[str, Union[int, float]]]) -> Union[int, None]:
        """
        Determine the rotation angle of the document based on its polygon.

        Args:
            polygon (list): A list of dictionaries representing the polygon coordinates of the
            document.

        Returns:
            int or None: The angle of orientation in degrees.
        """
        angle = self._calculate_text_angle(polygon)
        print(f'text angle = {angle}')

        if DEGREES_ZERO - self._tolerance < angle < DEGREES_ZERO + self._tolerance:
            return ROTATION_DEGREES[self._orientation]['Vertical']

        if DEGREES_NINETY - self._tolerance < angle < DEGREES_NINETY + self._tolerance:
            return ROTATION_DEGREES[self._orientation]['HorizontalRight']

        if DEGREES_NEGATIVE_ONE_EIGHTY - self._tolerance < angle \
            < DEGREES_NEGATIVE_ONE_EIGHTY + self._tolerance:
            return ROTATION_DEGREES[self._orientation]['UpsideDown']

        if (DEGREES_NEGATIVE_NINETY - self._tolerance < angle <
                DEGREES_NEGATIVE_NINETY + self._tolerance):
            return ROTATION_DEGREES[self._orientation]['HorizontalLeft']

        return None

    def _calculate_text_angle(self, polygon: List[Dict[str, Union[int, float]]]) -> float:
        """
        Calculate the angle of orientation of the document based on its polygon.

        Args:
            polygon (list): A list of dictionaries representing the polygon coordinates of the
            document.

        Returns:
            float: The angle of orientation in degrees.
        """
        x0, y0 = polygon[0]['X'], polygon[0]['Y']
        x1, y1 = polygon[1]['X'], polygon[1]['Y']

        dx, dy = x1 - x0, y1 - y0

        return math.degrees(math.atan2(dy, dx))
