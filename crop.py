import sys
import os

try:
    from PIL import Image
    
    in_dir = sys.argv[1]
    out_dir = sys.argv[2]
    
    files = [
        "media_1789901139862.jpg",
        "media_1789901157914.jpg",
        "media_1789901175316.jpg",
        "media_1789901191807.jpg",
        "media_1789901206074.jpg"
    ]
    
    for f in files:
        if not os.path.exists(os.path.join(in_dir, f)):
            continue
        
        img = Image.open(os.path.join(in_dir, f))
        w, h = img.size
        
        # General crop to remove UI elements:
        # Google Maps UI has top left (info), top right (buttons), bottom left (map), bottom center (arrows), bottom right (zoom).
        # We can aggressively crop: top 10%, bottom 20%, left 2%, right 2% depending on image.
        
        # Image 1 (storefront): bottom has map, top has info.
        if f == "media_1789901139862.jpg":
            # crop more from top left? Or just crop top 15% and bottom 20%
            box = (int(w*0.0), int(h*0.13), int(w*1.0), int(h*0.84))
        # Image 2 (interior 1): arrows at bottom
        elif f == "media_1789901157914.jpg":
            box = (int(w*0.0), int(h*0.0), int(w*1.0), int(h*0.90))
        # Image 3 (threads): arrows at bottom
        elif f == "media_1789901175316.jpg":
            box = (int(w*0.0), int(h*0.0), int(w*1.0), int(h*0.92))
        # Image 4 (interior wide): has a lot of UI
        elif f == "media_1789901191807.jpg":
            box = (int(w*0.12), int(h*0.13), int(w*0.95), int(h*0.84))
        # Image 5 (bag): has arrows at bottom
        elif f == "media_1789901206074.jpg":
            box = (int(w*0.0), int(h*0.0), int(w*1.0), int(h*0.92))
            
        cropped = img.crop(box)
        cropped.save(os.path.join(out_dir, f))
        print(f"Cropped {f}")
        
except ImportError:
    print("Pillow not installed. Installing...")
    os.system("pip install pillow")
    print("Run script again.")

