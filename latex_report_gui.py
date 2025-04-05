import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QCheckBox, QPushButton, QScrollArea, QGroupBox,
                            QFileDialog, QMessageBox)
from PyQt5.QtCore import Qt
from pylatex import Document, Section, Subsection, Command
import re


class LaTeXComponentSelector(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LaTeX Report Component Selector")
        self.setGeometry(100, 100, 600, 800)
        
        # Parse the LaTeX file to identify components
        self.components = self.parse_latex_components()
        
        self.init_ui()
        
        def parse_latex_components(self):
        """Parse the LaTeX file to identify sections and components"""
        components = []
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open LaTeX File", "", "LaTeX Files (*.tex)"
        )
        
        if not file_path:
            return components
            
        try:
            with open(file_path, "r", encoding='utf-8') as f:
                content = f.read()
                
                # Extract sections with their content
                sections = re.findall(r'\\section\{(.*?)\}(.*?)(?=\\section|\\subsection|\\end{document})', 
                                    content, re.DOTALL)
                for section in sections:
                    title, section_content = section
                    components.append(("section", title.strip(), section_content.strip()))
                    
                    # Extract subsections within this section
                    subsections = re.findall(r'\\subsection\{(.*?)\}(.*?)(?=\\subsection|\\section|\\end{document})', 
                                           section_content, re.DOTALL)
                    for subsection in subsections:
                        sub_title, sub_content = subsection
                        components.append(("subsection", sub_title.strip(), sub_content.strip()))
                
                # Extract tables with their content
                tables = re.findall(r'(\\begin\{longtable\}.*?\\end\{longtable\})', 
                                  content, re.DOTALL)
                for i, table in enumerate(tables, 1):
                    components.append(("table", f"Table {i}", table))
                    
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to parse LaTeX file:\n{str(e)}")

            
        return components
        
    def init_ui(self):
        """Initialize the UI components"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Create scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        
        # Add checkboxes for each component
        self.checkboxes = []
        group = QGroupBox("Select Components to Include")
        group_layout = QVBoxLayout()
        
        for comp_type, comp_name in self.components:
            cb = QCheckBox(f"{comp_type.capitalize()}: {comp_name}")
            cb.setChecked(True)
            group_layout.addWidget(cb)
            self.checkboxes.append((cb, comp_type, comp_name))
            
        group.setLayout(group_layout)
        scroll_layout.addWidget(group)
        
        # Add generate button
        generate_btn = QPushButton("Generate Custom PDF")
        generate_btn.clicked.connect(self.generate_pdf)
        scroll_layout.addWidget(generate_btn)
        
        scroll.setWidget(scroll_content)
        layout.addWidget(scroll)
        
        def generate_pdf(self):
        """Generate PDF from selected components"""
        if not hasattr(self, 'checkboxes') or not self.checkboxes:
            QMessageBox.warning(self, "Warning", "No components available to generate PDF")
            return
            
        options = QFileDialog.Options()
        save_path, _ = QFileDialog.getSaveFileName(
            self, "Save PDF Report", "", "PDF Files (*.pdf)", options=options
        )
        
        if not save_path:
            return
            
        try:
            doc = Document()
            
            # Add selected components to the document
            for cb, comp_type, comp_name, comp_content in self.checkboxes:
                if cb.isChecked():
                    if comp_type == "section":
                        with doc.create(Section(comp_name)):
                            doc.append(comp_content)
                    elif comp_type == "subsection":
                        with doc.create(Subsection(comp_name)):
                            doc.append(comp_content)
                    elif comp_type == "table":
                        doc.append(comp_content)
            
            # Generate PDF
            doc.generate_pdf(save_path.replace('.pdf', ''), clean_tex=False)
            QMessageBox.information(self, "Success", 
                                  f"PDF successfully generated at:\n{save_path}")
            
        except Exception as e:
            QMessageBox.critical(self, "Error", 
                               f"Failed to generate PDF:\n{str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LaTeXComponentSelector()
    window.show()
    sys.exit(app.exec_())