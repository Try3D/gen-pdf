from typing import Optional
from .svg import SvgBlock

class IconBlock(SvgBlock):
    def __init__(self, path_or_url: str, size=None, color=None, is_url=True, style=None):
        super().__init__(path_or_url, width=size, height=size, is_url=is_url)
        self.target_color = color
        self.style = style

    def render(self, context=None):
        import urllib.request
        import re
        
        if context:
            resolved_style = self.style
            
            if resolved_style:
                s_color = getattr(resolved_style, 'color', None)
                s_size = getattr(resolved_style, 'size', None)
                
                if self.target_color is None and s_color:
                    self.target_color = s_color
                
                if self.width is None and s_size:
                    self.width = s_size
                    self.height = s_size
        
        try:
            svg_str = ""
            if self.is_url:
                with urllib.request.urlopen(self.path_or_data) as response:
                    svg_str = response.read().decode('utf-8')
            else:
                if self.path_or_data.strip().startswith('<svg'):
                    svg_str = self.path_or_data
                else:
                    with open(self.path_or_data, 'r') as f:
                        svg_str = f.read()

            color = self.target_color
            if not color: color = "#000000"
            
            svg_str = re.sub(r'currentColor', color, svg_str, flags=re.IGNORECASE)
            
            if 'stroke=' not in svg_str:
                svg_str = svg_str.replace('<svg ', f'<svg stroke="{color}" ')
            
            self.is_string = True
            self.is_url = False
            self.path_or_data = svg_str
            
        except Exception as e:
            print(f"Error fetching/coloring icon {self.path_or_data}: {e}")
        
        return super().render(context)
