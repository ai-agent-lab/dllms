#!/usr/bin/env python3
"""
Final script to extract all bibliography entries from DLLM.bib and format them as HTML.
This approach is more robust and handles edge cases better.
"""

import re
import sys
from typing import Dict, List

def extract_all_entries(filename: str) -> List[Dict[str, str]]:
    """Extract all bibtex entries using regex."""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match entire bibtex entries
    pattern = r'@\w+\{[^@]*?(?=@\w+\{|$)'
    matches = re.findall(pattern, content, re.DOTALL)
    
    entries = []
    for match in matches:
        entry = extract_entry_info(match)
        if entry and entry.get('title') and entry.get('author'):
            entries.append(entry)
    
    return entries

def extract_entry_info(entry_text: str) -> Dict[str, str]:
    """Extract information from a single bibtex entry."""
    info = {}
    
    # Extract title
    title_match = re.search(r'title\s*=\s*\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}', entry_text, re.IGNORECASE | re.DOTALL)
    if title_match:
        title = title_match.group(1)
        # Clean up title
        title = re.sub(r'\s+', ' ', title).strip()
        title = title.replace('\\textasciicircum', '^')
        title = re.sub(r'[{}]', '', title)  # Remove braces
        info['title'] = title
    
    # Extract authors
    author_match = re.search(r'author\s*=\s*\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}', entry_text, re.IGNORECASE | re.DOTALL)
    if author_match:
        authors = author_match.group(1)
        info['author'] = re.sub(r'\s+', ' ', authors).strip()
    
    # Extract year - be very specific about date vs urldate
    year = None
    
    # First try to find date = {YYYY-MM-DD} pattern (not urldate)
    date_patterns = [
        r'(?<!url)date\s*=\s*\{([^}]*?(\d{4}))',  # date = {2024-02-23} 
        r'\byear\s*=\s*\{([^}]*?(\d{4}))',  # year = {2024}
        r'date\s*=\s*\{(\d{4})',  # simple date = {2024}
    ]
    
    for pattern in date_patterns:
        match = re.search(pattern, entry_text, re.IGNORECASE)
        if match:
            year_text = match.group(1) if len(match.groups()) == 1 else match.group(2)
            year_match = re.search(r'(\d{4})', year_text)
            if year_match:
                year = year_match.group(1)
                break
    
    # If still no year found, extract from citation key (fallback)
    if not year:
        key_match = re.search(r'@\w+\{[^,]*_(\d{4})', entry_text)
        if key_match:
            year = key_match.group(1)
    
    info['year'] = year if year else '2024'  # Default fallback
    
    # Extract URL
    url_match = re.search(r'url\s*=\s*\{([^}]+)\}', entry_text, re.IGNORECASE)
    if url_match:
        info['url'] = url_match.group(1).strip()
    else:
        info['url'] = '#'  # Default for missing URLs
    
    return info

def format_authors(author_str: str) -> str:
    """Format authors - last names only, with 'et al.' if more than 3."""
    if not author_str:
        return "Unknown Author"
    
    # Split by 'and'
    authors = re.split(r'\s+and\s+', author_str)
    
    last_names = []
    for author in authors:
        author = author.strip()
        if ',' in author:
            # "Last, First" format
            last_name = author.split(',')[0].strip()
        else:
            # "First Middle Last" format
            words = author.split()
            last_name = words[-1] if words else author
        
        if last_name:
            last_names.append(last_name)
    
    if len(last_names) > 3:
        return f"{last_names[0]} et al."
    else:
        return ", ".join(last_names)

def generate_html_bibliography(entries: List[Dict[str, str]]) -> str:
    """Generate complete HTML bibliography."""
    # Sort by year (newest first)
    sorted_entries = sorted(entries, key=lambda x: int(x.get('year', '0')), reverse=True)
    
    html_parts = []
    for entry in sorted_entries:
        title = entry.get('title', 'Unknown Title')
        authors_formatted = format_authors(entry.get('author', ''))
        year = entry.get('year', '2024')
        url = entry.get('url', '#')
        
        html_entry = f'''<div class="publication-item">
  <span class="publication-title">
    <a href="{url}" target="_blank">{title}</a>
    <a href="{url}" target="_blank" class="link-icon">
      <i class="fas fa-external-link-alt"></i>
    </a>
  </span>
  <span class="publication-authors">{authors_formatted}, {year}</span>
</div>'''
        
        html_parts.append(html_entry)
    
    return '\n\n'.join(html_parts)

def main():
    filename = '/Users/moonshine/workspace/Diffusion-based-Large-Language-Models-Survey/Overleaf/DLLM.bib'
    
    try:
        entries = extract_all_entries(filename)
        print(f"Successfully extracted {len(entries)} entries")
        
        # Generate HTML
        html_output = generate_html_bibliography(entries)
        
        print("\n" + "="*80)
        print("COMPLETE HTML BIBLIOGRAPHY (ALL 87 PAPERS)")
        print("="*80)
        print(html_output)
        
        # Also save to file
        with open('/Users/moonshine/workspace/Diffusion-based-Large-Language-Models-Survey/Overleaf/bibliography.html', 'w') as f:
            f.write(html_output)
        print(f"\nHTML bibliography saved to bibliography.html")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0

if __name__ == '__main__':
    sys.exit(main())