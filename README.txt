# File Deduplicator & Renamer

This script performs the following operations in the folder where it is located:

1. **Moves unique files** from subfolders to the root folder.
2. **Deletes duplicate files** (with the same name).
3. **Deletes empty subfolders** after processing.
4. **Renames all files in the root folder**, adding a random 4-digit numeric prefix.

---

## 🛠 How It Works

- Files in subdirectories are compared by name against files in the root folder.
- If a filename already exists in the root, the duplicate is deleted.
- If it's unique, it is moved to the root folder.
- After moving and cleanup, all files in the root folder are renamed as follows:

