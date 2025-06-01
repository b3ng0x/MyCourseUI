import os
import json
import shutil

def is_video_file(filename):
    return filename.lower().endswith(('.mp4', '.mov', '.mkv'))

def generate_course_structure(course_path):
    course_data = {
        "title": os.path.basename(course_path),
        "slug": os.path.basename(course_path).replace(" ", "-").lower(),
        "chapters": []
    }

    has_videos = False

    for dirpath, _, filenames in os.walk(course_path):
        video_files = [f for f in sorted(filenames) if is_video_file(f)]
        if not video_files:
            continue

        has_videos = True
        rel_path = os.path.relpath(dirpath, course_path).replace(os.sep, "/")
        chapter_title = "Introduction" if rel_path == "." else rel_path

        lessons = [
            {
                "title": os.path.splitext(f)[0],
                "path": os.path.relpath(os.path.join(dirpath, f), course_path).replace(os.sep, "/")
            }
            for f in video_files
        ]

        course_data["chapters"].append({
            "title": chapter_title,
            "lessons": lessons
        })

    return [course_data] if has_videos else []


# === CONFIGURATION ===
root_directory = r"" #course dir
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

# === CREATE SYMBOLIC LINK OR COPY FOLDER ===
abs_source = os.path.abspath(root_directory)

if os.path.exists(link_path):
    if os.path.islink(link_path) or os.path.isfile(link_path):
        os.unlink(link_path)
    else:
        shutil.rmtree(link_path)

try:
    os.symlink(abs_source, link_path, target_is_directory=True)
    print(f"🔗 Symlink created: {link_path} → {abs_source}")
except Exception as e:
    print(f"⚠️ Symlink failed ({e}), copying directory instead...")
    shutil.copytree(abs_source, link_path)
    print(f"📁 Directory copied to: {link_path}")
