#!/usr/bin/env python3.12

import re
import os


def find_consecutive_decorators(file_path):
    """Find consecutive @cdata_class decorators"""
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    duplicates_found = []
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        
        # If we find a @cdata_class decorator
        if line.startswith('@cdata_class'):
            decorator_start = i
            
            # Find the end of this decorator
            paren_count = 0
            decorator_lines = []
            j = i
            
            while j < len(lines):
                current_line = lines[j]
                decorator_lines.append(current_line)
                paren_count += current_line.count('(') - current_line.count(')')
                j += 1
                
                if paren_count == 0 and '@cdata_class' in current_line:
                    break
            
            # Now check what comes after this decorator
            while j < len(lines) and (lines[j].strip() == '' or lines[j].strip().startswith('#')):
                j += 1
            
            # If the next non-empty line is another @cdata_class, we found a duplicate
            if j < len(lines) and lines[j].strip().startswith('@cdata_class'):
                print(f"  🔍 Found consecutive decorators at lines {decorator_start + 1}-{j + 1}")
                print(f"      First decorator starts: {lines[decorator_start].strip()}")
                print(f"      Second decorator starts: {lines[j].strip()}")
                
                duplicates_found.append({
                    'start_line': decorator_start,
                    'end_line': j - 1,
                    'lines': decorator_lines
                })
            
            i = j
        else:
            i += 1
    
    return duplicates_found


def remove_consecutive_duplicates(file_path):
    """Remove consecutive duplicate decorators"""
    duplicates = find_consecutive_decorators(file_path)
    
    if not duplicates:
        return 0
    
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    # Remove duplicates in reverse order to maintain line numbers
    for duplicate in reversed(duplicates):
        start = duplicate['start_line']
        end = duplicate['end_line']
        
        # Remove the duplicate decorator lines
        del lines[start:end + 1]
        print(f"    Removed duplicate decorator at lines {start + 1}-{end + 1}")
    
    # Write back the cleaned content
    with open(file_path, 'w') as f:
        f.writelines(lines)
    
    return len(duplicates)


def main():
    """Find and fix consecutive duplicate decorators"""
    print("🔍 CONSECUTIVE DUPLICATE DECORATOR FINDER")
    print("=" * 45)
    
    py_files = [f for f in os.listdir('.') if f.endswith('_classes.py')]
    
    total_found = 0
    total_removed = 0
    
    for file_path in py_files:
        print(f"\n📄 Checking {file_path}...")
        
        duplicates = find_consecutive_decorators(file_path)
        
        if duplicates:
            print(f"  Found {len(duplicates)} consecutive duplicate patterns")
            removed = remove_consecutive_duplicates(file_path)
            total_found += len(duplicates)
            total_removed += removed
            
            # Validate syntax
            try:
                with open(file_path, 'r') as f:
                    compile(f.read(), file_path, 'exec')
                print(f"  ✅ Syntax validation passed after cleanup")
            except SyntaxError:
                print(f"  ❌ Syntax error after cleanup - reverting")
                os.system(f"git checkout -- {file_path}")
                total_removed -= removed
        else:
            print(f"  ✓ No consecutive duplicates found")
    
    print(f"\n🎯 Summary:")
    print(f"Total consecutive duplicates found: {total_found}")
    print(f"Total consecutive duplicates removed: {total_removed}")


if __name__ == "__main__":
    main()