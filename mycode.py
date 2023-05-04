import sys

def cEncoder(key:int, note: str) -> str:
    note = note.upper()
    cInput = ""
    count = 0
    
    for character in note:
        characterWord = ord(character)
        if characterWord < 65 or characterWord > 90:
            continue
        
        if count % 50 == 0 and len(cInput) != 0:
            cInput += "\n"
        elif count % 5 == 0 and len(cInput) != 0:
            cInput += " "
            
        cInput += chr(65 + (characterWord - 65 + key) % 26)
        count += 1
    
    return cInput

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv)>3:
        print("invalid input")
        sys.exit(1)
    
    key = int(sys.argv[1])
    
    if len(sys.argv) == 3:
        note = sys.argv[2]
    else:
        note = sys.stdin.read()
    
    print(cEncoder(key, note))
    sys.exit(0)