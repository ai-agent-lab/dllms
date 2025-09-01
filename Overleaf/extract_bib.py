#!/usr/bin/env python3
"""
Script to extract all bibliography entries from DLLM.bib and format them as HTML.
"""

import re
import sys
from typing import Dict, List, Tuple

def parse_bibtex_file(filename: str) -> List[Dict[str, str]]:
    """Parse bibtex file and extract entry information."""
    entries = []
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all bibtex entries by looking for @type{key, patterns
    entry_pattern = r'(@\w+\{[^,]+,.*?)(?=\n@\w+\{|\Z)'
    entry_matches = re.findall(entry_pattern, content, re.DOTALL)
    
    for entry_text in entry_matches:
        entry_info = parse_single_entry(entry_text)
        if entry_info:
            entries.append(entry_info)
    
    return entries

def parse_single_entry(entry_text: str) -> Dict[str, str]:
    """Parse a single bibtex entry."""
    info = {}
    
    # Extract citation key
    key_match = re.search(r'^@\w+\{([^,]+),', entry_text, re.MULTILINE)
    if key_match:
        info['key'] = key_match.group(1)
    
    # Extract fields using more robust regex patterns
    # Handle nested braces properly
    def extract_field(field_name, text):
        pattern = rf'{field_name}\s*=\s*\{{([^}}]*(?:\{{[^}}]*\}}[^}}]*)*)\}}'
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if match:
            return match.group(1).strip()
        return None
    
    # Extract title - handle special cases
    title = extract_field('title', entry_text)
    if title:
        # Clean up title - preserve content in brackets and braces
        title = title.strip()
        # Remove outer braces only if they wrap the entire title
        if title.startswith('{') and title.endswith('}') and title.count('{') == title.count('}'):
            # Check if the braces are balanced around the whole title
            brace_count = 0
            for i, char in enumerate(title):
                if char == '{':
                    brace_count += 1
                elif char == '}':
                    brace_count -= 1
                    if brace_count == 0 and i < len(title) - 1:
                        # There are other parts after a complete brace pair
                        break
            if brace_count == 0 and i == len(title) - 1:
                title = title[1:-1]  # Remove outer braces
        
        # Normalize whitespace but preserve important formatting
        title = re.sub(r'\s+', ' ', title)
        # Handle LaTeX commands and special characters
        title = title.replace('\\textasciicircum', '^')
        title = title.replace('{', '').replace('}', '')  # Remove remaining braces
        info['title'] = title
    
    # Extract author
    author = extract_field('author', entry_text)
    if author:
        info['author'] = re.sub(r'\s+', ' ', author)
    
    # Extract year/date - prioritize date field over year field, and ignore urldate
    date_field = extract_field('date', entry_text)
    year_field = extract_field('year', entry_text)
    
    year = None
    # First try date field (publication date)
    if date_field and 'urldate' not in entry_text.lower().split('date')[0]:  # Make sure it's not urldate
        year_match = re.search(r'(\d{4})', date_field)
        if year_match:
            year = year_match.group(1)
    # Then try year field if no date found
    elif year_field:
        year_match = re.search(r'(\d{4})', year_field)
        if year_match:
            year = year_match.group(1)
    # More robust extraction - look for any date = {YYYY pattern, avoiding urldate
    else:
        date_pattern = r'(?<!url)date\s*=\s*\{[^}]*?(\d{4})'
        date_match = re.search(date_pattern, entry_text, re.IGNORECASE)
        if date_match:
            year = date_match.group(1)
    
    if year:
        info['year'] = year
    
    # Extract URL
    url = extract_field('url', entry_text)
    if url:
        info['url'] = url.strip()
    
    return info if info else None

def format_authors(author_str: str) -> str:
    """Format authors - last names only, with 'et al.' if more than 3."""
    if not author_str:
        return ""
    
    # Split authors by 'and'
    authors = re.split(r'\s+and\s+', author_str)
    
    last_names = []
    for author in authors:
        # Extract last name - it's usually after the last comma or the last word
        author = author.strip()
        if ',' in author:
            # Format: "Last, First Middle"
            last_name = author.split(',')[0].strip()
        else:
            # Format: "First Middle Last"
            parts = author.split()
            last_name = parts[-1] if parts else author
        
        last_names.append(last_name)
    
    if len(last_names) > 3:
        return f"{last_names[0]} et al."
    else:
        return ", ".join(last_names)

def sort_entries_by_year(entries: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Sort entries by year (newest first)."""
    def get_year(entry):
        year_str = entry.get('year', '0')
        try:
            return int(re.search(r'(\d{4})', year_str).group(1))
        except:
            return 0
    
    return sorted(entries, key=get_year, reverse=True)

def generate_html(entries: List[Dict[str, str]]) -> str:
    """Generate HTML for all entries."""
    html_entries = []
    
    for entry in entries:
        title = entry.get('title', 'Unknown Title')
        # Remove braces from title
        title = re.sub(r'[{}]', '', title)
        
        authors = format_authors(entry.get('author', ''))
        year = entry.get('year', '')
        url = entry.get('url', '#')
        
        # Extract year from various formats
        if year:
            year_match = re.search(r'(\d{4})', year)
            if year_match:
                year = year_match.group(1)
        
        html_entry = f'''<div class="publication-item">
  <span class="publication-title">
    <a href="{url}" target="_blank">{title}</a>
    <a href="{url}" target="_blank" class="link-icon">
      <i class="fas fa-external-link-alt"></i>
    </a>
  </span>
  <span class="publication-authors">{authors}, {year}</span>
</div>'''
        
        html_entries.append(html_entry)
    
    return '\n\n'.join(html_entries)

def main():
    filename = '/Users/moonshine/workspace/Diffusion-based-Large-Language-Models-Survey/Overleaf/DLLM.bib'
    
    try:
        entries = parse_bibtex_file(filename)
        print(f"Found {len(entries)} entries")
        
        # Sort by year (newest first)
        sorted_entries = sort_entries_by_year(entries)
        
        # Generate HTML
        html_output = generate_html(sorted_entries)
        
        print("\n" + "="*50)
        print("HTML OUTPUT:")
        print("="*50)
        print(html_output)
        
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0

if __name__ == '__main__':
    sys.exit(main())