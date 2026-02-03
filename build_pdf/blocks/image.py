from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from build_pdf.styles.context import RenderContext
import os
import tempfile
import urllib.request
from reportlab.platypus import Image, Spacer
from reportlab.lib.utils import ImageReader
from .base import Block


class ImageBlock(Block):
    def __init__(self, path: str, style=None, fit_mode: Optional[str] = None):
        self.path = path
        self.style = style
        self.fit_mode = fit_mode

        self.width = getattr(style, "width", None) if style else None
        self.height = getattr(style, "height", None) if style else None
        self.border_radius = getattr(style, "border_radius", 0) or 0 if style else 0

    def render(self, context: Optional["RenderContext"] = None):
        if self.style:
            if self.width is None:
                self.width = getattr(self.style, "width", None)
            if self.height is None:
                self.height = getattr(self.style, "height", None)
            if self.border_radius == 0:
                radius = getattr(self.style, "border_radius", 0)
                self.border_radius = radius if radius is not None else 0

        image_path = self.path

        if self.path.startswith("http://") or self.path.startswith("https://"):
            try:
                import hashlib

                fname = hashlib.md5(self.path.encode()).hexdigest() + ".jpg"
                temp_path = os.path.join(tempfile.gettempdir(), fname)

                if not os.path.exists(temp_path):
                    req = urllib.request.Request(
                        self.path, headers={"User-Agent": "Mozilla/5.0"}
                    )
                    with urllib.request.urlopen(req) as response:
                        data = response.read()
                    with open(temp_path, "wb") as f:
                        f.write(data)

                image_path = temp_path
            except Exception as e:
                print(f"Failed to download image: {e}")
                return Spacer(0, 0)

        if self.fit_mode and self.width and self.height:
            try:
                from PIL import Image as PILImage, ImageOps

                try:
                    resample_method = PILImage.Resampling.LANCZOS
                except AttributeError:
                    resample_method = PILImage.LANCZOS

                if not image_path.startswith(tempfile.gettempdir()):
                    pass

                with PILImage.open(image_path) as im:
                    im = im.convert("RGBA")

                    scale = 3
                    target_w_px = int(self.width * scale)
                    target_h_px = int(self.height * scale)

                    processed_im = None

                    if self.fit_mode == "cover":
                        processed_im = ImageOps.fit(
                            im,
                            (target_w_px, target_h_px),
                            method=resample_method,
                            centering=(0.5, 0.5),
                        )
                    elif self.fit_mode == "contain":
                        processed_im = ImageOps.contain(
                            im, (target_w_px, target_h_px), method=resample_method
                        )
                    elif self.fit_mode == "stretch":
                        processed_im = im.resize(
                            (target_w_px, target_h_px), resample_method
                        )

                    if processed_im:
                        fd, new_path = tempfile.mkstemp(suffix=".png")
                        os.close(fd)
                        processed_im.save(new_path, format="PNG")
                        image_path = new_path

            except ImportError:
                print("Pillow not installed, skipping fit_mode")
            except Exception as e:
                print(f"Failed to apply fit_mode: {e}")

        if self.border_radius > 0:
            try:
                from PIL import Image as PILImage, ImageDraw

                try:
                    resample_method = PILImage.Resampling.LANCZOS
                except AttributeError:
                    resample_method = PILImage.LANCZOS

                with PILImage.open(image_path) as im:
                    im = im.convert("RGBA")

                    w, h = im.size

                    mask = PILImage.new("L", (w, h), 0)
                    draw = ImageDraw.Draw(mask)

                    current_scale = w / self.width if self.width else 1
                    px_radius = int(self.border_radius * current_scale)

                    draw.rounded_rectangle([(0, 0), (w, h)], radius=px_radius, fill=255)

                    im.putalpha(mask)

                    fd, new_path = tempfile.mkstemp(suffix=".png")
                    os.close(fd)
                    im.save(new_path, format="PNG")
                    image_path = new_path

            except ImportError:
                print("Pillow not installed, skipping border radius")
            except Exception as e:
                print(f"Failed to apply border radius: {e}")

        if (self.width is None or self.height is None) and self.width != self.height:
            try:
                utils = ImageReader(image_path)
                iw, ih = utils.getSize()
                aspect = ih / float(iw)

                if self.width and self.height is None:
                    self.height = self.width * aspect
                elif self.height and self.width is None:
                    self.width = self.height / aspect
            except Exception:
                pass

        return Image(image_path, width=self.width, height=self.height)
