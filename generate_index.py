import os
import glob

# --- Configuration ---
PAGE_TITLE = "Particle Event Reconstructions"
# Add any other directory names you want to skip
IGNORE_DIRS = ['.git', '.vscode', '__pycache__', 'css'] 
# ---------------------

def generate_html_index():
    """
    Scans subdirectories for .html files and generates a categorized index.html.
    """
    
    # Find all items in the current directory
    try:
        all_items = os.listdir('.')
    except FileNotFoundError:
        print("Error: Could not scan the current directory.")
        return
        
    # Filter for directories we want to scan
    subdirectories = [
        d for d in all_items 
        if os.path.isdir(d) and d not in IGNORE_DIRS
    ]
    
    if not subdirectories:
        print("⚠️ No subdirectories found to scan for plots.")
        return

    # --- Start building the HTML content ---
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{PAGE_TITLE}</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; line-height: 1.6; padding: 2em; max-width: 800px; margin: 0 auto; background-color: #f6f8fa; }}
        h1 {{ border-bottom: 2px solid #eaecef; padding-bottom: 0.3em; }}
        h2 {{ border-bottom: 1px solid #eaecef; padding-bottom: 0.2em; margin-top: 2.5em; font-size: 1.5em; }}
        ul {{ list-style-type: none; padding: 0; }}
        li {{ background-color: #fff; border: 1px solid #d1d5da; border-radius: 6px; margin-bottom: 10px; transition: transform 0.1s ease-in-out; }}
        li:hover {{ transform: scale(1.02); }}
        a {{ display: block; padding: 12px 16px; text-decoration: none; color: #0366d6; font-weight: 600; }}
        a:hover {{ background-color: #f6f8fa; border-radius: 6px; }}
    </style>
</head>
<body>
    <h1>{PAGE_TITLE}</h1>
"""
    
    total_plots_found = 0
    # --- Iterate over each found subdirectory ---
    for directory in sorted(subdirectories):
        search_path = os.path.join(directory, "*.html")
        plot_files = sorted(glob.glob(search_path))
        
        # If any HTML files are found, create a section for this directory
        if plot_files:
            # Capitalize directory name for a nice heading (e.g., "muon_data" -> "Muon data")
            heading = directory.replace('_', ' ').capitalize()
            html_content += f"    <h2>{heading}</h2>\n    <ul>\n"
            
            for plot_path in plot_files:
                filename = os.path.basename(plot_path)
                # The href must include the directory path for the link to work
                html_content += f'        <li><a href="{plot_path}">{filename}</a></li>\n'
                total_plots_found += 1
            
            html_content += "    </ul>\n"

    # --- Finalize the HTML file ---
    html_content += """
</body>
</html>
"""
    
    if total_plots_found > 0:
        with open("index.html", "w") as f:
            f.write(html_content)
        print(f"✅ Successfully generated index.html with {total_plots_found} links.")
    else:
        print("⚠️ No .html plot files were found in any subdirectories.")

if __name__ == "__main__":
    generate_html_index()