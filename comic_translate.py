from PIL import Image, ImageDraw, ImageFont

# Load the image
image_path = 'images/image_170201.jpg'
image = Image.open(image_path)
draw = ImageDraw.Draw(image)

# Define the text and bounding boxes from the JSON data
text_data = [
    {
        "id": 1,
        "bbox": [88, 149, 396, 290],
        "text": "だからっ"
    },
    {
        "id": 2,
        "bbox": [28, 770, 395, 937],
        "text": "知らない私は\n言ってんだろうっ"
    },
    {
        "id": 3,
        "bbox": [538, 411, 747, 540],
        "text": "そんな\n俗物なんて…"
    },
    {
        "id": 4,
        "bbox": [479, 131, 608, 296],
        "text": "そうは\n言ってもなぁ"
    },
    {
        "id": 5,
        "bbox": [673, 114, 804, 276],
        "text": "レーネ…"
    }
]

# Set font and colors
try:
    font = ImageFont.truetype("arial.ttf", 20)
except IOError:
    font = ImageFont.load_default()

box_color = "red"
text_color = "blue"

# Draw the rectangles and text on the image
for item in text_data:
    bbox = item["bbox"]
    text = item["text"]
    
    # Bounding box coordinates for PIL ImageDraw
    x1, y1 = bbox[1], bbox[0]
    x2, y2 = bbox[3], bbox[2]

    # Draw the rectangle
    draw.rectangle([x1, y1, x2, y2], outline=box_color, width=3)
    
    # Draw the ID and text
    id_text = f"ID: {item['id']}"
    draw.text((x1, y1 - 20), id_text, fill=text_color, font=font)

# Save the modified image
output_path = "output_image.jpg"
image.save(output_path)

print(f"Annotated image saved to {output_path}")