from sentence_transformers import SentenceTransformer, util
import numpy as np
import webcolors
# Step 1: Use a stronger model
model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")

# Step 2: Define categories
categories = [
    "T-shirt", "Shoes", "Hoodie", "Cap", "Socks", "Backpack", 
    "Jacket", "Sweatpants", "Jewelry", "Phone Case",
    "Sweater", "Dress", "Skirt", "Blouse", "Jeans", "Shorts",
    "Scarf", "Gloves", "Belt", "Sunglasses", "Wallet", "Handbag",
    "Watch", "Earrings", "Necklace", "Bracelet", "Beanie", "Tank Top",
    "Leggings", "Coat", "Overalls", "Sandals"
]

# Step 3: Precompute category embeddings
category_embeddings = model.encode(categories, convert_to_tensor=True)

def assign_category(title):
    """
    Assign the closest matching category for a given product title 
    using sentence embedding similarity.
    """
    # Encode the product title
    title_embedding = model.encode(title, convert_to_tensor=True)
    
    # Compute cosine similarity with all category embeddings
    similarities = util.cos_sim(title_embedding, category_embeddings)[0]
    
    # Get the most similar category index
    best_idx = int(similarities.argmax())
    
    # Return the category with the highest similarity
    return categories[best_idx]


from PIL import Image
from sklearn.cluster import KMeans
import numpy as np

def get_dominant_color_from_center(image_path, k=3, crop_ratio=0.5):
    try:
        img = Image.open(image_path).convert("RGB")
        width, height = img.size

        # Calculate crop box: centered square based on crop_ratio
        new_width = int(width * crop_ratio)
        new_height = int(height * crop_ratio)
        left = (width - new_width) // 2
        top = (height - new_height) // 2
        right = left + new_width
        bottom = top + new_height

        # Crop to center region
        img_cropped = img.crop((left, top, right, bottom))
        img_cropped = img_cropped.resize((100, 100))  # Resize for speed

        # Convert to numpy and cluster
        pixels = np.array(img_cropped).reshape(-1, 3)
        kmeans = KMeans(n_clusters=k, random_state=0).fit(pixels)
        counts = np.bincount(kmeans.labels_)
        dominant_color = kmeans.cluster_centers_[np.argmax(counts)]

        return tuple(int(c) for c in dominant_color)

    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None

# Define a dictionary of CSS3 color names and their RGB values
CSS3_COLORS = {
    # Existing CSS3 colors (kept as-is)
    'aliceblue': (240, 248, 255),
    'antiquewhite': (250, 235, 215),
    'aqua': (0, 255, 255),
    'aquamarine': (127, 255, 212),
    'azure': (240, 255, 255),
    'beige': (245, 245, 220),
    'bisque': (255, 228, 196),
    'black': (0, 0, 0),
    'blanchedalmond': (255, 235, 205),
    'blue': (0, 0, 255),
    'blueviolet': (138, 43, 226),
    'brown': (165, 42, 42),
    'burlywood': (222, 184, 135),
    'cadetblue': (95, 158, 160),
    'chartreuse': (127, 255, 0),
    'chocolate': (210, 105, 30),
    'coral': (255, 127, 80),
    'cornflowerblue': (100, 149, 237),
    'cornsilk': (255, 248, 220),
    'crimson': (220, 20, 60),
    'cyan': (0, 255, 255),
    'darkblue': (0, 0, 139),
    'darkcyan': (0, 139, 139),
    'darkgoldenrod': (184, 134, 11),
    'darkgray': (169, 169, 169),
    'darkgreen': (0, 100, 0),
    'darkgrey': (169, 169, 169),
    'darkkhaki': (189, 183, 107),
    'darkmagenta': (139, 0, 139),
    'darkolivegreen': (85, 107, 47),
    'darkorange': (255, 140, 0),
    'darkorchid': (153, 50, 204),
    'darkred': (139, 0, 0),
    'darksalmon': (233, 150, 122),
    'darkseagreen': (143, 188, 143),
    'darkslateblue': (72, 61, 139),
    'darkslategray': (47, 79, 79),
    'darkslategrey': (47, 79, 79),
    'darkturquoise': (0, 206, 209),
    'darkviolet': (148, 0, 211),
    'deeppink': (255, 20, 147),
    'deepskyblue': (0, 191, 255),
    'dimgray': (105, 105, 105),
    'dimgrey': (105, 105, 105),
    'dodgerblue': (30, 144, 255),
    'firebrick': (178, 34, 34),
    'floralwhite': (255, 250, 240),
    'forestgreen': (34, 139, 34),
    'fuchsia': (255, 0, 255),
    'gainsboro': (220, 220, 220),
    'ghostwhite': (248, 248, 255),
    'gold': (255, 215, 0),
    'goldenrod': (218, 165, 32),
    'gray': (128, 128, 128),
    'green': (0, 128, 0),
    'greenyellow': (173, 255, 47),
    'grey': (128, 128, 128),
    'honeydew': (240, 255, 240),
    'hotpink': (255, 105, 180),
    'indianred': (205, 92, 92),
    'indigo': (75, 0, 130),
    'ivory': (255, 255, 240),
    'khaki': (240, 230, 140),
    'lavender': (230, 230, 250),
    'lavenderblush': (255, 240, 245),
    'lawngreen': (124, 252, 0),
    'lemonchiffon': (255, 250, 205),
    'lightblue': (173, 216, 230),
    'lightcoral': (240, 128, 128),
    'lightcyan': (224, 255, 255),
    'lightgoldenrodyellow': (250, 250, 210),
    'lightgray': (211, 211, 211),
    'lightgreen': (144, 238, 144),
    'lightgrey': (211, 211, 211),
    'lightpink': (255, 182, 193),
    'lightsalmon': (255, 160, 122),
    'lightseagreen': (32, 178, 170),
    'lightskyblue': (135, 206, 250),
    'lightslategray': (119, 136, 153),
    'lightslategrey': (119, 136, 153),
    'lightsteelblue': (176, 196, 222),
    'lightyellow': (255, 255, 224),
    'lime': (0, 255, 0),
    'limegreen': (50, 205, 50),
    'linen': (250, 240, 230),
    'magenta': (255, 0, 255),
    'maroon': (128, 0, 0),
    'mediumaquamarine': (102, 205, 170),
    'mediumblue': (0, 0, 205),
    'mediumorchid': (186, 85, 211),
    'mediumpurple': (147, 112, 219),
    'mediumseagreen': (60, 179, 113),
    'mediumslateblue': (123, 104, 238),
    'mediumspringgreen': (0, 250, 154),
    'mediumturquoise': (72, 209, 204),
    'mediumvioletred': (199, 21, 133),
    'midnightblue': (25, 25, 112),
    'mintcream': (245, 255, 250),
    'mistyrose': (255, 228, 225),
    'moccasin': (255, 228, 181),
    'navajowhite': (255, 222, 173),
    'navy': (0, 0, 128),
    'oldlace': (253, 245, 230),
    'olive': (128, 128, 0),
    'olivedrab': (107, 142, 35),
    'orange': (255, 165, 0),
    'orangered': (255, 69, 0),
    'orchid': (218, 112, 214),
    'palegoldenrod': (238, 232, 170),
    'palegreen': (152, 251, 152),
    'paleturquoise': (175, 238, 238),
    'palevioletred': (219, 112, 147),
    'papayawhip': (255, 239, 213),
    'peachpuff': (255, 218, 185),
    'peru': (205, 133, 63),
    'pink': (255, 192, 203),
    'plum': (221, 160, 221),
    'powderblue': (176, 224, 230),
    'purple': (128, 0, 128),
    'red': (255, 0, 0),
    'rosybrown': (188, 143, 143),
    'royalblue': (65, 105, 225),
    'saddlebrown': (139, 69, 19),
    'salmon': (250, 128, 114),
    'sandybrown': (244, 164, 96),
    'seagreen': (46, 139, 87),
    'seashell': (255, 245, 238),
    'sienna': (160, 82, 45),
    'silver': (192, 192, 192),
    'skyblue': (135, 206, 235),
    'slateblue': (106, 90, 205),
    'slategray': (112, 128, 144),
    'slategrey': (112, 128, 144),
    'snow': (255, 250, 250),
    'springgreen': (0, 255, 127),
    'steelblue': (70, 130, 180),
    'tan': (210, 180, 140),
    'teal': (0, 128, 128),
    'thistle': (216, 191, 216),
    'tomato': (255, 99, 71),
    'turquoise': (64, 224, 208),
    'violet': (238, 130, 238),
    'wheat': (245, 222, 179),
    'white': (255, 255, 255),
    'whitesmoke': (245, 245, 245),
    'yellow': (255, 255, 0),
    'yellowgreen': (154, 205, 50),
    
    # Newly added colors (X11, modern web colors, and common shades)
    'amaranth': (229, 43, 80),
    'amber': (255, 191, 0),
    'amethyst': (153, 102, 204),
    'apricot': (251, 206, 177),
    'babyblue': (137, 207, 240),
    'bronze': (205, 127, 50),
    'burgundy': (128, 0, 32),
    'charcoal': (54, 69, 79),
    'coffee': (111, 78, 55),
    'cream': (255, 253, 208),
    'denim': (21, 96, 189),
    'emerald': (80, 200, 120),
    'eggplant': (97, 64, 81),
    'fuchsia': (255, 0, 255),
    'golden': (255, 215, 0),
    'gunmetal': (42, 52, 57),
    'hazel': (142, 118, 24),
    'indigo': (75, 0, 130),
    'jade': (0, 168, 107),
    'kiwi': (142, 229, 63),
    'lavender': (230, 230, 250),
    'lilac': (200, 162, 200),
    'mauve': (224, 176, 255),
    'mustard': (255, 219, 88),
    'neonpink': (254, 1, 154),
    'olive': (128, 128, 0),
    'pearl': (234, 224, 200),
    'ruby': (224, 17, 95),
    'sapphire': (15, 82, 186),
    'scarlet': (255, 36, 0),
    'taupe': (72, 60, 50),
    'ultramarine': (18, 10, 143),
    'vermilion': (227, 66, 52),
    'wine': (114, 47, 55),
    'zinnia': (251, 223, 0),
    
    # Grayscale variants
    'darkcharcoal': (30, 30, 30),
    'lightgray2': (211, 211, 211),
    'smokegray': (112, 128, 144),
    'ashgray': (178, 190, 181),
    
    # Pastels
    'pastelblue': (174, 198, 207),
    'pastelgreen': (119, 221, 119),
    'pastelpink': (255, 209, 220),
    'pastelpurple': (179, 158, 181),
    
    # Darker/Lighter variants
    'darkbrown': (92, 64, 51),
    'lightbrown': (181, 101, 29),
    'darkpink': (231, 84, 128),
    'lightpink2': (255, 182, 193),
    'darkpurple': (75, 0, 110),
    'lightpurple': (197, 180, 227),
    
    # Metallic colors
    'silvermetallic': (192, 192, 192),
    'goldmetallic': (212, 175, 55),
    'bronzemetallic': (205, 127, 50),
    'coppermetallic': (184, 115, 51),
}

def closest_color_name(requested_rgb):
    min_distance = float('inf')
    closest_name = None
    
    for name, rgb in CSS3_COLORS.items():
        distance = (rgb[0] - requested_rgb[0])**2 + (rgb[1] - requested_rgb[1])**2 + (rgb[2] - requested_rgb[2])**2
        if distance < min_distance:
            min_distance = distance
            closest_name = name
    
    return closest_name

def rgb_to_name(rgb_tuple):
    try:
        return webcolors.rgb_to_name(rgb_tuple)
    except ValueError:
        return closest_color_name(rgb_tuple)

def get_dominant_color(image_path):
    rgb_tuple = get_dominant_color_from_center(image_path)
    if rgb_tuple:
        color_name = rgb_to_name(rgb_tuple)
        return color_name
    else:
        return None