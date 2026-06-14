import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

with open('port.html', 'rb') as f:
    content = f.read()

# Check slider slide CSS
idx = content.find(b'project-slider .slide{')
print("Slider slide CSS:")
print(content[idx:idx+200].decode('utf-8', errors='replace'))
print()

# Check quickpantry img tag
idx2 = content.find(b'quickpantry.png')
print("QuickPantry img context:")
print(content[idx2-200:idx2+100].decode('utf-8', errors='replace'))
