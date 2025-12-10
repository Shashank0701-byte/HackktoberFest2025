"""
Enhanced Certificate Templates
Multiple certificate template designs for different events
"""

from PIL import Image, ImageDraw, ImageFont
import os


def get_modern_certificate_template(
    name: str, 
    event: str, 
    date: str, 
    output_path: str = "certificate.png",
    template_style: str = "modern"
) -> str:
    """
    Generate a modern, professional certificate
    """
    width, height = 1400, 1000
    
    if template_style == "modern":
        return _create_modern_template(name, event, date, output_path, width, height)
    elif template_style == "elegant":
        return _create_elegant_template(name, event, date, output_path, width, height)
    elif template_style == "tech":
        return _create_tech_template(name, event, date, output_path, width, height)
    else:
        return _create_modern_template(name, event, date, output_path, width, height)


def _create_modern_template(name, event, date, output_path, width, height):
    """Modern gradient design"""
    certificate = Image.new("RGB", (width, height), color="#f8f9fa")
    draw = ImageDraw.Draw(certificate)
    
    # Modern gradient background
    for y in range(height):
        color_ratio = y / height
        r = int(248 + (67 - 248) * color_ratio)
        g = int(249 + (56 - 249) * color_ratio) 
        b = int(250 + (101 - 250) * color_ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # Load fonts
    try:
        font_title = ImageFont.truetype("arial.ttf", 72)
        font_subtitle = ImageFont.truetype("arial.ttf", 36)
        font_name = ImageFont.truetype("arialbd.ttf", 56)
        font_body = ImageFont.truetype("arial.ttf", 32)
        font_small = ImageFont.truetype("arial.ttf", 24)
    except IOError:
        font_title = ImageFont.load_default()
        font_subtitle = ImageFont.load_default()
        font_name = ImageFont.load_default()
        font_body = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Modern border
    draw.rectangle([40, 40, width-40, height-40], outline="#2c3e50", width=8)
    draw.rectangle([50, 50, width-50, height-50], outline="#3498db", width=3)
    
    # Helper function
    def center_text(text, y, font, color="black"):
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        x = (width - text_width) // 2
        draw.text((x, y), text, font=font, fill=color)
    
    # Title
    center_text("CERTIFICATE", 120, font_title, "#2c3e50")
    center_text("OF ACHIEVEMENT", 200, font_subtitle, "#34495e")
    
    # Decorative elements
    draw.ellipse([width//2-100, 300, width//2+100, 500], outline="#3498db", width=4)
    center_text("🏆", 370, font_title)
    
    # Content
    center_text("This is to certify that", 550, font_small, "#7f8c8d")
    center_text(name, 600, font_name, "#2c3e50")
    
    # Underline
    bbox = draw.textbbox((0, 0), name, font=font_name)
    name_width = bbox[2] - bbox[0]
    name_x = (width - name_width) // 2
    draw.line([name_x, 670, name_x + name_width, 670], fill="#3498db", width=3)
    
    center_text("has successfully completed", 720, font_small, "#7f8c8d")
    center_text(event, 770, font_body, "#2c3e50")
    center_text(f"Date: {date}", 850, font_small, "#7f8c8d")
    
    certificate.save(output_path)
    return output_path


def _create_elegant_template(name, event, date, output_path, width, height):
    """Elegant design with classic styling"""
    certificate = Image.new("RGB", (width, height), color="#fdfefe")
    draw = ImageDraw.Draw(certificate)
    
    # Elegant border design
    border_color = "#8b4513"
    draw.rectangle([30, 30, width-30, height-30], outline=border_color, width=12)
    draw.rectangle([45, 45, width-45, height-45], outline="#d4af37", width=4)
    draw.rectangle([55, 55, width-55, height-55], outline=border_color, width=2)
    
    # Corner decorations
    corner_size = 80
    for corner in [(70, 70), (width-150, 70), (70, height-150), (width-150, height-150)]:
        draw.ellipse([corner[0], corner[1], corner[0]+corner_size, corner[1]+corner_size], 
                    outline="#d4af37", width=3)
    
    # Load fonts
    try:
        font_title = ImageFont.truetype("arial.ttf", 68)
        font_subtitle = ImageFont.truetype("arial.ttf", 34)
        font_name = ImageFont.truetype("arialbd.ttf", 52)
        font_body = ImageFont.truetype("arial.ttf", 30)
        font_small = ImageFont.truetype("arial.ttf", 22)
    except IOError:
        font_title = ImageFont.load_default()
        font_subtitle = ImageFont.load_default()
        font_name = ImageFont.load_default()
        font_body = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    def center_text(text, y, font, color="black"):
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        x = (width - text_width) // 2
        draw.text((x, y), text, font=font, fill=color)
    
    # Title
    center_text("CERTIFICATE", 140, font_title, "#8b4513")
    center_text("OF EXCELLENCE", 220, font_subtitle, "#d4af37")
    
    # Decorative line
    draw.line([200, 300, width-200, 300], fill="#d4af37", width=3)
    
    # Content
    center_text("This certifies that", 350, font_small, "#5d4e37")
    center_text(name, 420, font_name, "#8b4513")
    
    # Name underline with decorative ends
    bbox = draw.textbbox((0, 0), name, font=font_name)
    name_width = bbox[2] - bbox[0]
    name_x = (width - name_width) // 2
    draw.line([name_x-20, 490, name_x + name_width + 20, 490], fill="#d4af37", width=2)
    
    center_text("has demonstrated exceptional skill in", 540, font_small, "#5d4e37")
    center_text(event, 590, font_body, "#8b4513")
    center_text(f"Awarded on {date}", 700, font_small, "#5d4e37")
    
    # Signature lines
    sig_y = 800
    draw.line([200, sig_y, 450, sig_y], fill="#8b4513", width=2)
    draw.line([width-450, sig_y, width-200, sig_y], fill="#8b4513", width=2)
    center_text("Authorized Signature", sig_y + 15, font_small, "#5d4e37")
    
    certificate.save(output_path)
    return output_path


def _create_tech_template(name, event, date, output_path, width, height):
    """Technology-focused design"""
    certificate = Image.new("RGB", (width, height), color="#1a1a1a")
    draw = ImageDraw.Draw(certificate)
    
    # Tech-style grid background
    grid_color = "#333333"
    for x in range(0, width, 50):
        draw.line([(x, 0), (x, height)], fill=grid_color, width=1)
    for y in range(0, height, 50):
        draw.line([(0, y), (width, y)], fill=grid_color, width=1)
    
    # Neon-style borders
    neon_color = "#00ff41"
    draw.rectangle([40, 40, width-40, height-40], outline=neon_color, width=6)
    draw.rectangle([48, 48, width-48, height-48], outline="#0099ff", width=2)
    
    # Load fonts
    try:
        font_title = ImageFont.truetype("arial.ttf", 70)
        font_subtitle = ImageFont.truetype("arial.ttf", 35)
        font_name = ImageFont.truetype("arialbd.ttf", 54)
        font_body = ImageFont.truetype("arial.ttf", 32)
        font_small = ImageFont.truetype("arial.ttf", 24)
    except IOError:
        font_title = ImageFont.load_default()
        font_subtitle = ImageFont.load_default()
        font_name = ImageFont.load_default()
        font_body = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    def center_text(text, y, font, color="white"):
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        x = (width - text_width) // 2
        draw.text((x, y), text, font=font, fill=color)
    
    # Title with glow effect
    center_text("DIGITAL CERTIFICATE", 120, font_title, "#00ff41")
    center_text("TECHNOLOGY ACHIEVEMENT", 200, font_subtitle, "#0099ff")
    
    # Tech hexagon
    hex_center = (width//2, 340)
    hex_size = 60
    hex_points = []
    for i in range(6):
        angle = i * 60
        x = hex_center[0] + hex_size * 0.866  # cos(30°)
        y = hex_center[1] + hex_size * 0.5    # sin(30°)
        hex_points.append((x, y))
    
    # Content
    center_text("CERTIFIED THAT", 420, font_small, "#cccccc")
    center_text(name, 480, font_name, "#00ff41")
    
    # Neon underline
    bbox = draw.textbbox((0, 0), name, font=font_name)
    name_width = bbox[2] - bbox[0]
    name_x = (width - name_width) // 2
    draw.line([name_x, 550, name_x + name_width, 550], fill="#00ff41", width=3)
    
    center_text("HAS SUCCESSFULLY COMPLETED", 600, font_small, "#cccccc")
    center_text(event, 650, font_body, "#0099ff")
    center_text(f"COMPLETION DATE: {date}", 750, font_small, "#cccccc")
    
    # Tech corner elements
    corner_size = 40
    corners = [(60, 60), (width-100, 60), (60, height-100), (width-100, height-100)]
    for corner in corners:
        draw.rectangle([corner[0], corner[1], corner[0]+corner_size, corner[1]+corner_size], 
                      outline="#00ff41", width=2)
    
    certificate.save(output_path)
    return output_path
