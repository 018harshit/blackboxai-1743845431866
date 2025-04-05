---

```markdown
# LaTeX Report Component Selector

## Project Overview
The LaTeX Report Component Selector is a PyQt5-based graphical user interface application that allows users to generate customized LaTeX reports. Users can open a LaTeX file, select the sections, subsections, and tables they want to include in the final PDF document, and then generate the PDF based on their selections.

## Installation
To get started with the LaTeX Report Component Selector, ensure you have Python installed on your machine along with the required packages. You can install the necessary dependencies using pip:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd latex_report_gui
   ```

2. Install the required packages:
   ```bash
   pip install PyQt5 pylatex
   ```

## Usage
To run the application, use the following command in your terminal:

```bash
python latex_report_gui.py
```
or for the enhanced version:
```bash
python latex_report_gui_enhanced.py
```

1. Open a `.tex` file through the file dialog.
2. Select the components (sections, subsections, and tables) you want to include in your PDF report using the checkboxes provided.
3. Click on the "Generate Custom PDF" button to create the report.
4. Choose a location to save your generated PDF.

## Features
- Open and parse LaTeX files to extract sections, subsections, and tables.
- Visually select components to include in the PDF report.
- Generate PDF files directly from the selected LaTeX components.
- User-friendly interface built with PyQt5.

## Dependencies
The project depends on the following Python packages:
- `PyQt5` - For creating the GUI application.
- `pylatex` - For generating PDF documents from LaTeX content.

You can install these dependencies using pip as mentioned in the Installation section.

## Project Structure
```
latex_report_gui/
│
├── latex_report_gui.py          # Main application file for generating a LaTeX report.
└── latex_report_gui_enhanced.py # Enhanced version of the main application file.
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.
```
