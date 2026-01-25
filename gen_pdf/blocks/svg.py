from typing import Optional
import io
import urllib.request
from .base import Block
from reportlab.platypus import Spacer

try:
    from svglib.svglib import svg2rlg
    SVGLIB_AVAILABLE = True
except ImportError:
    SVGLIB_AVAILABLE = False

class SvgBlock(Block):
    def __init__(self, path_or_data: str, width: Optional[float] = None, height: Optional[float] = None, is_url=False, is_string=False):
        self.path_or_data = path_or_data
        self.width = width
        self.height = height
        self.is_url = is_url
        self.is_string = is_string

    def render(self, context=None):
        if not SVGLIB_AVAILABLE:
            print("Warning: svglib not installed. SVG rendering is disabled. Please run 'pip install svglib'")
            return Spacer(self.width or 0, self.height or 0)
        
        drawing = None
        try:
            if self.is_string:
                 f = io.BytesIO(self.path_or_data.encode('utf-8'))
                 drawing = svg2rlg(f)
            elif self.is_url:
                 with urllib.request.urlopen(self.path_or_data) as response:
                     data = response.read()
                 f = io.BytesIO(data)
                 drawing = svg2rlg(f)
            else:
                 drawing = svg2rlg(self.path_or_data)
        except Exception as e:
            print(f"Error loading SVG: {e}")
            return Spacer(self.width or 0, self.height or 0)

        if drawing:
            ow = drawing.width
            oh = drawing.height
            
            scale_x = 1.0
            scale_y = 1.0
            
            if self.width and self.height:
                scale_x = self.width / ow
                scale_y = self.height / oh
            elif self.width:
                scale_x = self.width / ow
                scale_y = scale_x
            elif self.height:
                scale_y = self.height / oh
                scale_x = scale_y
            
            drawing.scale(scale_x, scale_y)
            drawing.width = ow * scale_x
            drawing.height = oh * scale_y
            
            return drawing
        
        return Spacer(self.width or 0, self.height or 0)
