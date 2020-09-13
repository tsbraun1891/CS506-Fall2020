def draw_tree(height = 5):
    print("""
  ____________
 /            \\
|              |
|              |
 \____________/""")

    curHeight = 0

    while(curHeight < height-1):
        print("    |      |")
        curHeight += 1
            
    print("   /        \\")

    return
    