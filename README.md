
# 🖼️ PyQt6ImageFusion

This PyQt6-based desktop application loads **random geometric SVG images** from the [OpenMoji GitHub repository](https://github.com/hfg-gmuend/openmoji/tree/master/src/symbols/geometric), displays them on a canvas, and allows users to:

- **Select** images by clicking on them (border toggles on selection)
- **Drag** and move images freely around the window
- **Group** selected images into a single movable object

---

## 🔧 Features

- 🖱️ Drag-and-drop enabled for all rendered images  
- 🔄 Random image generation from an online repository (does not overwrite existing images)  
- ✅ Multi-image selection using left-click  
- 📦 Group selected images into one large image using the **Group Images** button  
- 🧹 Clears selected images after grouping

---

## 📦 Requirements

- Python 3.8+
- PyQt6
- `requests`

---

## 🚀 Getting Started

1. **Install dependencies:**

```bash
pip install PyQt6 requests
```

2. **Run the application:**

```bash
python main.py
```

> Make sure you have an internet connection since the app fetches SVG images from the GitHub API.

---

## 📁 Folder Structure

```text
├── main.py
├── README.md
└── images/
    └── desktop-icon.png
```

---

## 🧠 How it Works

- Fetches SVG files from GitHub's OpenMoji geometric symbols repo
- Randomly selects and downloads an SVG image
- Converts it into a QPixmap and displays it in a QLabel
- Allows user interaction for selection, dragging, and grouping
- Grouping renders a new QImage with all selected images and removes originals

---

## 📝 Notes

- Only SVG files are processed from the GitHub repository.
- Grouped images are currently rendered at a default position (`x=400, y=400`).
- You can extend the app to support:
  - Saving grouped images
  - Un-grouping
  - Rotation/scaling of images

---
