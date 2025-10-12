#!/usr/bin/env python3.12

import re
import os


def find_all_duplicates_advanced(file_path):
    """Find all decorator duplicates, including multi-line ones"""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Find all complete decorators with their associated classes
    pattern = r'(@cdata_class\s*\([^@]*?\))\s*(class\s+([A-Z][A-Za-z0-9_]*)\s*\([^)]+\):)'
    matches = list(re.finditer(pattern, content, re.DOTALL))
    
    print(f"\n📄 Analyzing {file_path}")
    print(f"Found {len(matches)} complete decorator-class pairs")
    
    # Group by class name
    class_groups = {}
    for match in matches:
        decorator_text = match.group(1)
        class_line = match.group(2) 
        class_name = match.group(3)
        full_match = match.group(0)
        
        if class_name not in class_groups:
            class_groups[class_name] = []
            
        class_groups[class_name].append({
            'decorator': decorator_text,
            'class_line': class_line,
            'full_match': full_match,
            'start': match.start(),
            'end': match.end(),
            'line_num': content[:match.start()].count('\n') + 1
        })
    
    # Find classes with multiple decorators
    duplicates_to_remove = []
    for class_name, decorators in class_groups.items():
        if len(decorators) > 1:
            print(f"  🔍 Class {class_name} has {len(decorators)} decorators!")
            
            # Show all decorators for this class
            for i, dec in enumerate(decorators):
                print(f"    Decorator #{i+1} at line {dec['line_num']}")
                # Show first line of decorator for identification
                first_line = dec['decorator'].split('\n')[0].strip()
                print(f"      Starts with: {first_line}")
            
            # Mark all but the last one as duplicates to remove
            # (Keep the last one as it's likely the most complete)
            duplicates_to_remove.extend(decorators[:-1])
    
    return duplicates_to_remove


def remove_duplicates_safe(file_path, duplicates):
    """Safely remove duplicate decorators"""
    if not duplicates:
        return 0
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Sort duplicates by position (reverse order to maintain positions)
    duplicates.sort(key=lambda x: x['start'], reverse=True)
    
    removed_count = 0
    for duplicate in duplicates:
        full_match = duplicate['full_match']
        class_line = duplicate['class_line']
        
        # Replace the full decorator+class with just the class
        if full_match in content:
            content = content.replace(full_match, class_line, 1)
            removed_count += 1
            print(f"    Removed duplicate decorator at line {duplicate['line_num']}")
        else:
            print(f"    Warning: Could not find duplicate to remove at line {duplicate['line_num']}")
    
    # Write back the cleaned content
    if removed_count > 0:
        with open(file_path, 'w') as f:
            f.write(content)
    
    return removed_count


def validate_syntax(file_path):
    """Validate Python syntax"""
    try:
        with open(file_path, 'r') as f:
            compile(f.read(), file_path, 'exec')
        return True
    except SyntaxError as e:
        print(f"  ❌ Syntax error: {e}")
        return False


def main():
    """Advanced duplicate finder that handles multi-line decorators"""
    print("🔍 ADVANCED DUPLICATE DECORATOR FINDER")
    print("=" * 42)
    
    py_files = [f for f in os.listdir('.') if f.endswith('_classes.py')]
    
    total_found = 0
    total_removed = 0
    files_modified = []
    
    for file_path in py_files:
        duplicates = find_all_duplicates_advanced(file_path)
        
        if duplicates:
            print(f"  Found {len(duplicates)} duplicate decorators to remove")
            
            removed = remove_duplicates_safe(file_path, duplicates)
            
            if removed > 0:
                # Validate syntax
                if validate_syntax(file_path):
                    files_modified.append(file_path)
                    total_found += len(duplicates)
                    total_removed += removed
                    print(f"  ✅ Removed {removed} duplicates, syntax OK")
                else:
                    print(f"  ❌ Syntax error after cleanup - reverting")
                    os.system(f"git checkout -- {file_path}")
        else:
            print(f"  ✓ No duplicate decorators found")
    
    print(f"\n🎯 Summary:")
    print(f"Total duplicate decorators found: {total_found}")
    print(f"Total duplicate decorators removed: {total_removed}")
    print(f"Files modified: {len(files_modified)}")
    
    if files_modified:
        print(f"\nModified files:")
        for file_path in files_modified:
            print(f"  - {file_path}")


if __name__ == "__main__":
    main()