#!/usr/bin/env python3.12

import re


def find_orphaned_decorators(file_path):
    """Find @cdata_class decorators that aren't followed by a class"""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Find all @cdata_class positions
    all_decorators = []
    for match in re.finditer(r'@cdata_class', content):
        line_num = content[:match.start()].count('\n') + 1
        all_decorators.append({
            'pos': match.start(),
            'line': line_num,
            'text': match.group()
        })
    
    # Find decorator-class pairs
    valid_pairs = []
    pattern = r'(@cdata_class\s*\([^@]*?\))\s*(class\s+([A-Z][A-Za-z0-9_]*)\s*\([^)]+\):)'
    for match in re.finditer(pattern, content, re.DOTALL):
        decorator_start = match.start()
        valid_pairs.append(decorator_start)
    
    print(f"\n📄 Analyzing {file_path}")
    print(f"Total @cdata_class occurrences: {len(all_decorators)}")
    print(f"Valid decorator-class pairs: {len(valid_pairs)}")
    print(f"Orphaned decorators: {len(all_decorators) - len(valid_pairs)}")
    
    # Find orphaned decorators
    orphaned = []
    for decorator in all_decorators:
        if decorator['pos'] not in valid_pairs:
            orphaned.append(decorator)
            
            # Show context around the orphaned decorator
            start = max(0, decorator['pos'] - 100)
            end = min(len(content), decorator['pos'] + 200)
            context = content[start:end]
            
            print(f"\n🔍 Orphaned decorator at line {decorator['line']}:")
            print("Context:")
            for i, line in enumerate(context.split('\n'), 1):
                marker = " >>> " if '@cdata_class' in line else "     "
                print(f"{marker}{line}")
                if i > 10:  # Limit context
                    break
    
    return orphaned


def main():
    """Find orphaned decorators in problematic files"""
    problem_files = ['ccp4xtaldata_classes.py', 'ccp4modeldata_classes.py', 'ccp4file_classes.py']
    
    for file_path in problem_files:
        find_orphaned_decorators(file_path)


if __name__ == "__main__":
    main()