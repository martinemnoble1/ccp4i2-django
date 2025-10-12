#!/usr/bin/env python3.12

import os
import re


def find_and_remove_duplicates(file_path):
    """Find and remove duplicate @cdata_class decorators from a file"""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Find all @cdata_class decorators with their positions
    decorator_pattern = r'(@cdata_class\s*\([^@]*?\))\s*(class\s+([A-Z][A-Za-z0-9_]*)\s*\([^)]+\):)'
    matches = list(re.finditer(decorator_pattern, content, re.DOTALL))
    
    duplicates_found = []
    class_decorators = {}
    
    for match in matches:
        decorator_text = match.group(1)
        class_line = match.group(2)
        class_name = match.group(3)
        
        if class_name not in class_decorators:
            class_decorators[class_name] = []
        
        class_decorators[class_name].append({
            'decorator': decorator_text,
            'class_line': class_line,
            'full_match': match.group(0),
            'start': match.start(),
            'end': match.end()
        })
    
    # Find classes with multiple decorators
    for class_name, decorators in class_decorators.items():
        if len(decorators) > 1:
            # Keep the last (most complete) decorator and mark others as duplicates
            for i in range(len(decorators) - 1):
                duplicates_found.append(decorators[i])
            print(f"  Found {len(decorators) - 1} duplicate decorators for {class_name}")
    
    if not duplicates_found:
        return 0
    
    # Remove duplicates (in reverse order to maintain positions)
    duplicates_found.sort(key=lambda x: x['start'], reverse=True)
    
    for duplicate in duplicates_found:
        # Find the decorator + class combination
        old_text = duplicate['full_match']
        new_text = duplicate['class_line']  # Keep only the class line
        
        if old_text in content:
            content = content.replace(old_text, new_text, 1)
        else:
            print(f"    Warning: Could not find duplicate text to remove")
    
    # Write the cleaned content back
    with open(file_path, 'w') as f:
        f.write(content)
    
    return len(duplicates_found)


def validate_syntax(file_path):
    """Validate Python syntax"""
    try:
        with open(file_path, 'r') as f:
            compile(f.read(), file_path, 'exec')
        return True
    except SyntaxError:
        return False


def main():
    """Main function to clean up duplicate decorators"""
    print("🧹 SAFE DUPLICATE DECORATOR CLEANUP")
    print("=" * 40)
    
    py_files = [f for f in os.listdir('.') if f.endswith('_classes.py')]
    
    total_removed = 0
    files_modified = []
    
    for file_path in py_files:
        print(f"\n📄 Checking {file_path}...")
        
        duplicates_removed = find_and_remove_duplicates(file_path)
        
        if duplicates_removed > 0:
            # Validate syntax
            if validate_syntax(file_path):
                files_modified.append(file_path)
                total_removed += duplicates_removed
                print(f"  ✅ Removed {duplicates_removed} duplicate decorators")
                print(f"  ✓ Syntax validation passed")
            else:
                print(f"  ❌ Syntax error after cleanup - reverting")
                os.system(f"git checkout -- {file_path}")
        else:
            print(f"  ✓ No duplicates found")
    
    print(f"\n🎯 Summary:")
    print(f"Files processed: {len(py_files)}")
    print(f"Files modified: {len(files_modified)}")
    print(f"Total duplicates removed: {total_removed}")
    
    if files_modified:
        print(f"\nCleaned files:")
        for file_path in files_modified:
            print(f"  - {file_path}")


if __name__ == "__main__":
    main()