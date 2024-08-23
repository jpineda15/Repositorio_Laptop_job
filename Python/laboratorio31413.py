'''
3.1.4.13 LAB: Los conceptos básicos de las listas - The Beatles
'''
def theBeatles():
    beatles = []
    print("Step 1:", beatles)
    
    beatles.append("John Lennon")
    beatles.append("Paul McCartney")
    beatles.append("George Harrison")
    print(f"Step 2: {', '.join(map(str, beatles))}.")
    
    for member in range(2):
        beatles.append(input("New Band Member: "))
    print(f"Step 3: {', '.join(map(str, beatles))}.")
    
    del beatles[-1]
    del beatles[-1]
    print(f"Step 4: {', '.join(map(str, beatles))}.")
    
    beatles.insert(0, "Ringo Starr")
    print(f"Step 5: {', '.join(map(str, beatles))}.")
    
    print ("The Fab ", len(beatles))
theBeatles() 