import subprocess
import os
import tempfile

def convert_doc_to_docx(input_file):
    """Convert DOC to DOCX using libreoffice"""
    try:
        # Create output file in same directory as input
        base_name = os.path.splitext(os.path.basename(input_file))[0]
        docx_file = os.path.join(os.path.dirname(input_file), f"{base_name}_temp.docx")
        subprocess.run([
            "libreoffice",
            "--headless",
            "--convert-to", "docx",
            "--outdir", os.path.dirname(input_file),
            input_file
        ], check=True)
        
        # Get the actual converted file path
        converted_file = os.path.join(os.path.dirname(input_file), f"{base_name}.docx")
        if not os.path.exists(converted_file):
            raise FileNotFoundError(f"Converted file not found: {converted_file}")
            
        # Rename to our temporary file
        os.rename(converted_file, docx_file)
        return docx_file
        
    except subprocess.CalledProcessError as e:
        print(f"DOC to DOCX conversion failed: {str(e)}")
        return None
    except FileNotFoundError as e:
        print(f"Failed to find converted file: {str(e)}")
        return None
    except Exception as e:
        print(f"Unexpected error during DOC to DOCX conversion: {str(e)}")
        return None

def convert_docx_to_md(docx_file, output_file):
    """Convert DOCX to MD using pandoc"""
    try:
        subprocess.run([
            "pandoc",
            "-s",
            docx_file,
            "-t", "markdown",
            "-o", output_file
        ], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"DOCX to MD conversion failed: {str(e)}")
        return False

def convert_doc_to_md(input_file, output_file):
    # First convert DOC to DOCX
    docx_file = convert_doc_to_docx(input_file)
    if not docx_file:
        return False
        
    # Then convert DOCX to MD
    success = convert_docx_to_md(docx_file, output_file)
    
    # Clean up temporary DOCX file
    try:
        os.unlink(docx_file)
    except OSError:
        pass
        
    return success

if __name__ == "__main__":
    input_file = "example.doc"
    output_file = "example.md"
    
    if convert_doc_to_md(input_file, output_file):
        print(f"Successfully converted {input_file} to {output_file}")
    else:
        print("Conversion failed")
