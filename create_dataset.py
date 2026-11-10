
import os
import pandas as pd

# مجلد الصور داخل مجلد المشروع
dataset_path = "Tomato"

extensions = (".jpg", ".jpeg", ".png", ".bmp", ".webp")
data = []

for root, dirs, files in os.walk(dataset_path):
    for file in files:
        if file.lower().endswith(extensions):
            plant_class = os.path.basename(root)
            parts = plant_class.split("___", 1)
            plant_name = parts[0]
            disease = parts[1] if len(parts) > 1 else "Unknown"
            data.append({
                "Image_Name": file,
                "Plant_Class": plant_class,
                "Plant_Name": plant_name,
                "Disease": disease,
                "Image_Path": os.path.join(root, file)
            })

if not data:
    print("No images found. Check the PlantVillage folder.")
else:
    df = pd.DataFrame(data)

    print("Total images:", len(df))
    print("\nImages by class:")
    print(df["Plant_Class"].value_counts())

    df.to_csv("PlantVillage_PowerBI.csv", index=False)
    print("\nCSV created: PlantVillage_PowerBI.csv")
