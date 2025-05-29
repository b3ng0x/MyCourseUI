import os
import json
import shutil
import platform

def generate_course_structure(root_dir):
    structure = []

    for course_name in sorted(os.listdir(root_dir)):
        course_path = os.path.join(root_dir, course_name)
        if not os.path.isdir(course_path):
            continue

        course_data = {
            "title": course_name,
            "slug": course_name.replace(" ", "-").lower(),
            "chapters": []
        }

        for chapter_name in sorted(os.listdir(course_path)):
            chapter_path = os.path.join(course_path, chapter_name)
            if not os.path.isdir(chapter_path):
                continue

            chapter_data = {
                "title": chapter_name,
                "lessons": []
            }

            for file_name in sorted(os.listdir(chapter_path)):
                file_path = os.path.join(chapter_path, file_name)
                if os.path.isfile(file_path) and file_name.lower().endswith((".mp4", ".mov", ".mkv")):
                    chapter_data["lessons"].append({
                        "title": os.path.splitext(file_name)[0],
                        "path": os.path.relpath(file_path, root_dir).replace("\\", "/")
                    })

            if chapter_data["lessons"]:
                course_data["chapters"].append(chapter_data)

        if course_data["chapters"]:
            structure.append(course_data)

    return structure


# === CONFIGURATION ===
root_directory = "../Smart Contract Hacking Course"
public_dir = "./public"
link_name = "course"
link_path = os.path.join(public_dir, link_name)
output_file = os.path.join(public_dir, "courses-structured.json")

# === GENERATE JSON ===
os.makedirs(public_dir, exist_ok=True)
output = generate_course_structure(root_directory)
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)
print(f"✅ JSON written to: {output_file}")

# === CREATE LINK or COPY FOLDER ===
abs_source = os.path.abspath(root_directory)

# Remove existing link/folder
if os.path.exists(link_path):
    if os.path.islink(link_path) or os.path.isfile(link_path):
        os.unlink(link_path)
    else:
        shutil.rmtree(link_path)

try:
    os.symlink(abs_source, link_path, target_is_directory=True)
    print(f"🔗 Symlink created: {link_path} → {abs_source}")
except (OSError, NotImplementedError) as e:
    print(f"⚠️ Symlink failed ({e}), copying directory instead...")
    shutil.copytree(abs_source, link_path)
    print(f"📁 Directory copied to: {link_path}")
