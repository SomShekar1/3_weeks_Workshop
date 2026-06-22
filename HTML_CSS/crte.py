import os

for i in range(9, 21):
    folder = f"Module{i}"
    os.makedirs(folder, exist_ok=True)

    open(f"{folder}/index.html", "w").close()
    open(f"{folder}/style.css", "w").close()

print("20 modules created successfully!")