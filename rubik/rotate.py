import rubik.cube as rubik
import collections

[F11], [R11], [B11], [L11], [U11], [D11] = [0], [9], [18], [27], [36], [45]
[F12], [R12], [B12], [L12], [U12], [D12] = [1], [10], [19], [28], [37], [46]  #11 12 13
[F13], [R13], [B13], [L13], [U13], [D13] = [2], [11], [20], [29], [38], [47]  #21 22 23
[F21], [R21], [B21], [L21], [U21], [D21] = [3], [12], [21], [30], [39], [48]  #31 32 33
[F22], [R22], [B22], [L22], [U22], [D22] = [4], [13], [22], [31], [40], [49]  #Center
[F23], [R23], [B23], [L23], [U23], [D23] = [5], [14], [23], [32], [41], [50]
[F31], [R31], [B31], [L31], [U31], [D31] = [6], [15], [24], [33], [42], [51]
[F32], [R32], [B32], [L32], [U32], [D32] = [7], [16], [25], [34], [43], [52]
[F33], [R33], [B33], [L33], [U33], [D33] = [8], [17], [26], [35], [44], [53]

def _checkCube(encodedCube):
    result = {}
    validCube = ['b', 'r', 'g', 'o', 'y', 'w']
        
    cubelis = list(encodedCube)
    cubeLetterCount = 0
    cubeColorCount = 0
    
    for letter in cubelis:
        if letter in validCube:
            cubeLetterCount += 1
            
    for cubecolor in encodedCube:
        cubeColorCount = encodedCube.count(cubecolor)
        
    if encodedCube == list('n'):
        result['status'] = 'error: Cube is missing'
    elif len(encodedCube) != 54:
        result['status'] = 'error: Invalid size'
    elif cubeLetterCount != len(cubelis): 
        result['status'] = 'error: invalid cube characters'
    elif len(set(encodedCube[i] for i in [F22, R22, B22, L22, U22, D22])) != 6:
        result['status'] = 'error: invalid centers'
    elif cubeColorCount != 9:
        result['status'] = 'error: Invalid number of colors'
    else:
        result['status'] = 'ok'

    return result

def _checkDir(parms):
    result = {}
    encodedDir = parms.get('dir',None)
    validDir = ['F', 'f', 'B', 'b', 'U', 'u', 'D','d','L','l','R','r']
    
    if encodedDir == None:
        encodedDir = 'F'
    if encodedDir == '':
        encodedDir = 'F'
         
    dirlis = list(encodedDir)
    dirLetterCount = 0
    
    for letter in dirlis:
        if letter in validDir:
            dirLetterCount += 1
            
    if dirLetterCount != len(dirlis):
        result['status'] = 'error: invalid dir characters'
    else:
        result['status'] = 'ok'
        
    return result
        
def _rotate(parms):
    rotateResult = {}
    
    encodedCube = parms.get('cube','None')       
    encodedDir = parms.get('dir',None)
    
    if encodedCube == 'None' or encodedCube == '':
        encodedCube = list('n')
    
    cubestatus = _checkCube(encodedCube)
    dirstatus = _checkDir(parms)
    
    if encodedDir == '':
        encodedDir = 'F'
    
    if cubestatus.get('status', None) != 'ok':
        rotateResult = cubestatus
    elif dirstatus.get('status', None) != 'ok':
        rotateResult = dirstatus
    else:
        rotatedCubeList = _makeRotate(encodedCube,encodedDir)
        rotatedCube = ''.join(list(rotatedCubeList))
        rotateResult['cube'] = rotatedCube
        rotateResult['status'] = 'ok'
    return rotateResult
   
def _makeRotate(encodedCube,encodedDir):
    
    if encodedCube == None:
        encodedCube = 'n'
        
    if encodedDir == None:
        encodedDir = 'F'
        
    dirlist = list(encodedDir)
    cubeList = list(encodedCube)
    rotatedCubeList = list(encodedCube)
    
    for x in dirlist:
        if x == 'F':
            rotatedCubeList = _F(cubeList)
            cubeList = rotatedCubeList[:]
        elif x == 'f':
            rotatedCubeList = _f(cubeList)
            cubeList = rotatedCubeList[:]
        elif x == 'B':
            rotatedCubeList = _B(cubeList)
            cubeList = rotatedCubeList[:]
        elif x == 'b':
            rotatedCubeList = _b(cubeList)
            cubeList = rotatedCubeList[:]
        elif x == 'U':
            rotatedCubeList = _U(cubeList)
            cubeList = rotatedCubeList[:]
        elif x == 'u':
            rotatedCubeList = _u(cubeList)
            cubeList = rotatedCubeList[:]
        elif x == 'D':
            rotatedCubeList = _D(cubeList)
            cubeList = rotatedCubeList[:]
        elif x == 'd':
            rotatedCubeList = _d(cubeList)
            cubeList = rotatedCubeList[:]
        elif x == 'R':
            rotatedCubeList = _R(cubeList)
            cubeList = rotatedCubeList[:]
        elif x == 'r':
            rotatedCubeList = _r(cubeList)
            cubeList = rotatedCubeList[:]
        elif x == 'L':
            rotatedCubeList = _L(cubeList)
            cubeList = rotatedCubeList[:]
        elif x == 'l':
            rotatedCubeList = _l(cubeList)
            cubeList = rotatedCubeList[:]

    return rotatedCubeList

#Front side clock
def _F(cubeList):
    rotatedCubeList = list(cubeList)
    
    rotatedCubeList[F13] = cubeList[F11]
    rotatedCubeList[F23] = cubeList[F12]
    rotatedCubeList[F33] = cubeList[F13]
    rotatedCubeList[F12] = cubeList[F21]
    rotatedCubeList[F22] = cubeList[F22]
    rotatedCubeList[F32] = cubeList[F23]
    rotatedCubeList[F11] = cubeList[F31]
    rotatedCubeList[F21] = cubeList[F32]
    rotatedCubeList[F31] = cubeList[F33]
    #up to right
    rotatedCubeList[R11] = cubeList[U31]
    rotatedCubeList[R21] = cubeList[U32]
    rotatedCubeList[R31] = cubeList[U33]
    #right to down
    rotatedCubeList[D13] = cubeList[R11]
    rotatedCubeList[D12] = cubeList[R21]
    rotatedCubeList[D11] = cubeList[R31]
    #down to left
    rotatedCubeList[L13] = cubeList[D11]
    rotatedCubeList[L23] = cubeList[D12]
    rotatedCubeList[L33] = cubeList[D13]
    #left to up
    rotatedCubeList[U31] = cubeList[L33]
    rotatedCubeList[U32] = cubeList[L23]
    rotatedCubeList[U33] = cubeList[L13]
    
    return rotatedCubeList

#reverse of F
def _f(cubeList):
    rotatedCubeList = list(cubeList)
    
    rotatedCubeList[F11] = cubeList[F13]
    rotatedCubeList[F12] = cubeList[F23]
    rotatedCubeList[F13] = cubeList[F33]
    rotatedCubeList[F21] = cubeList[F12]
    rotatedCubeList[F22] = cubeList[F22]
    rotatedCubeList[F23] = cubeList[F32]
    rotatedCubeList[F31] = cubeList[F11]
    rotatedCubeList[F32] = cubeList[F21]
    rotatedCubeList[F33] = cubeList[F31]
    #
    rotatedCubeList[U31] = cubeList[R11]
    rotatedCubeList[U32] = cubeList[R21]
    rotatedCubeList[U33] = cubeList[R31]
    #
    rotatedCubeList[R11] = cubeList[D13]
    rotatedCubeList[R21] = cubeList[D12]
    rotatedCubeList[R31] = cubeList[D11]
    #
    rotatedCubeList[D11] = cubeList[L13]
    rotatedCubeList[D12] = cubeList[L23]
    rotatedCubeList[D13] = cubeList[L33]
    #
    rotatedCubeList[L33] = cubeList[U31]
    rotatedCubeList[L23] = cubeList[U32]
    rotatedCubeList[L13] = cubeList[U33]

    return rotatedCubeList

#Back side clock
def _B(cubeList):
    rotatedCubeList = list(cubeList)
     
    rotatedCubeList[B13] = cubeList[B11]
    rotatedCubeList[B23] = cubeList[B12]
    rotatedCubeList[B33] = cubeList[B13]
    rotatedCubeList[B12] = cubeList[B21]
    rotatedCubeList[B22] = cubeList[B22]
    rotatedCubeList[B32] = cubeList[B23]
    rotatedCubeList[B11] = cubeList[B31]
    rotatedCubeList[B21] = cubeList[B32]
    rotatedCubeList[B31] = cubeList[B33]
    #
    rotatedCubeList[L31] = cubeList[U11]
    rotatedCubeList[L21] = cubeList[U12]
    rotatedCubeList[L11] = cubeList[U13]
    #
    rotatedCubeList[D31] = cubeList[L11]
    rotatedCubeList[D32] = cubeList[L21]
    rotatedCubeList[D33] = cubeList[L31]
    #
    rotatedCubeList[R33] = cubeList[D31]
    rotatedCubeList[R23] = cubeList[D32]
    rotatedCubeList[R13] = cubeList[D33]
    #
    rotatedCubeList[U13] = cubeList[R33]
    rotatedCubeList[U12] = cubeList[R23]
    rotatedCubeList[U11] = cubeList[R13]
    
    return rotatedCubeList

#reverse of B
def _b(cubeList):
    rotatedCubeList = list(cubeList)
    
    rotatedCubeList[B11] = cubeList[B13]
    rotatedCubeList[B12] = cubeList[B23]
    rotatedCubeList[B13] = cubeList[B33]
    rotatedCubeList[B21] = cubeList[B12]
    rotatedCubeList[B22] = cubeList[B22]
    rotatedCubeList[B23] = cubeList[B32]
    rotatedCubeList[B31] = cubeList[B11]
    rotatedCubeList[B32] = cubeList[B21]
    rotatedCubeList[B33] = cubeList[B31]
    #
    rotatedCubeList[U11] = cubeList[L31]
    rotatedCubeList[U12] = cubeList[L21]
    rotatedCubeList[U13] = cubeList[L11]
    #
    rotatedCubeList[L11] = cubeList[D31]
    rotatedCubeList[L21] = cubeList[D32]
    rotatedCubeList[L31] = cubeList[D33]
    #
    rotatedCubeList[D31] = cubeList[R33]
    rotatedCubeList[D32] = cubeList[R23]
    rotatedCubeList[D33] = cubeList[R13]
    #
    rotatedCubeList[R33] = cubeList[U13]
    rotatedCubeList[R23] = cubeList[U12]
    rotatedCubeList[R13] = cubeList[U11]
    
    return rotatedCubeList

#up side clock
def _U(cubeList):
    rotatedCubeList = list(cubeList)
    
    rotatedCubeList[U13] = cubeList[U11]
    rotatedCubeList[U23] = cubeList[U12]
    rotatedCubeList[U33] = cubeList[U13]
    rotatedCubeList[U12] = cubeList[U21]
    rotatedCubeList[U22] = cubeList[U22]
    rotatedCubeList[U32] = cubeList[U23]
    rotatedCubeList[U11] = cubeList[U31]
    rotatedCubeList[U21] = cubeList[U32]
    rotatedCubeList[U31] = cubeList[U33]
    #back to right
    rotatedCubeList[R11] = cubeList[B11]
    rotatedCubeList[R12] = cubeList[B12]
    rotatedCubeList[R13] = cubeList[B13]
    #right to front
    rotatedCubeList[F11] = cubeList[R11]
    rotatedCubeList[F12] = cubeList[R12]
    rotatedCubeList[F13] = cubeList[R13]
    #front to left
    rotatedCubeList[L11] = cubeList[F11]
    rotatedCubeList[L12] = cubeList[F12]
    rotatedCubeList[L13] = cubeList[F13]
    #left to back
    rotatedCubeList[B11] = cubeList[L11]
    rotatedCubeList[B12] = cubeList[L12]
    rotatedCubeList[B13] = cubeList[L13]
    
    return rotatedCubeList

#reverse of U
def _u(cubeList):
    rotatedCubeList = list(cubeList)
    
    rotatedCubeList[U11] = cubeList[U13]
    rotatedCubeList[U12] = cubeList[U23]
    rotatedCubeList[U13] = cubeList[U33]
    rotatedCubeList[U21] = cubeList[U12]
    rotatedCubeList[U22] = cubeList[U22]
    rotatedCubeList[U23] = cubeList[U32]
    rotatedCubeList[U31] = cubeList[U11]
    rotatedCubeList[U32] = cubeList[U21]
    rotatedCubeList[U33] = cubeList[U31]
    #
    rotatedCubeList[B11] = cubeList[R11]
    rotatedCubeList[B12] = cubeList[R12]
    rotatedCubeList[B13] = cubeList[R13]
    #
    rotatedCubeList[R11] = cubeList[F11]
    rotatedCubeList[R12] = cubeList[F12]
    rotatedCubeList[R13] = cubeList[F13]
    #
    rotatedCubeList[F11] = cubeList[L11]
    rotatedCubeList[F12] = cubeList[L12]
    rotatedCubeList[F13] = cubeList[L13]
    #
    rotatedCubeList[L11] = cubeList[B11]
    rotatedCubeList[L12] = cubeList[B12]
    rotatedCubeList[L13] = cubeList[B13]
    
    return rotatedCubeList

#down side clock
def _D(cubeList):
    rotatedCubeList = list(cubeList)
    
    rotatedCubeList[D13] = cubeList[D11]
    rotatedCubeList[D23] = cubeList[D12]
    rotatedCubeList[D33] = cubeList[D13]
    rotatedCubeList[D12] = cubeList[D21]
    rotatedCubeList[D22] = cubeList[D22]
    rotatedCubeList[D32] = cubeList[D23]
    rotatedCubeList[D11] = cubeList[D31]
    rotatedCubeList[D21] = cubeList[D32]
    rotatedCubeList[D31] = cubeList[D33]
    #front to right
    rotatedCubeList[R31] = cubeList[F31]
    rotatedCubeList[R32] = cubeList[F32]
    rotatedCubeList[R33] = cubeList[F33]
    #right to back
    rotatedCubeList[B31] = cubeList[R31]
    rotatedCubeList[B32] = cubeList[R32]
    rotatedCubeList[B33] = cubeList[R33]
    #back to left
    rotatedCubeList[L31] = cubeList[B31]
    rotatedCubeList[L32] = cubeList[B32]
    rotatedCubeList[L33] = cubeList[B33]
    #left to front
    rotatedCubeList[F31] = cubeList[L31]
    rotatedCubeList[F32] = cubeList[L32]
    rotatedCubeList[F33] = cubeList[L33]
    
    return rotatedCubeList

#reverse of D
def _d(cubeList):
    rotatedCubeList = list(cubeList)
    
    rotatedCubeList[D11] = cubeList[D13]
    rotatedCubeList[D12] = cubeList[D23]
    rotatedCubeList[D13] = cubeList[D33]
    rotatedCubeList[D21] = cubeList[D12]
    rotatedCubeList[D22] = cubeList[D22]
    rotatedCubeList[D23] = cubeList[D32]
    rotatedCubeList[D31] = cubeList[D11]
    rotatedCubeList[D32] = cubeList[D21]
    rotatedCubeList[D33] = cubeList[D31]
    #
    rotatedCubeList[F31] = cubeList[R31]
    rotatedCubeList[F32] = cubeList[R32]
    rotatedCubeList[F33] = cubeList[R33]
    #
    rotatedCubeList[R31] = cubeList[B31]
    rotatedCubeList[R32] = cubeList[B32]
    rotatedCubeList[R33] = cubeList[B33]
    #
    rotatedCubeList[B31] = cubeList[L31]
    rotatedCubeList[B32] = cubeList[L32]
    rotatedCubeList[B33] = cubeList[L33]
    #
    rotatedCubeList[L31] = cubeList[F31]
    rotatedCubeList[L32] = cubeList[F32]
    rotatedCubeList[L33] = cubeList[F33]
    
    return rotatedCubeList

#right clock
def _R(cubeList):
    rotatedCubeList = list(cubeList)
    
    rotatedCubeList[R13] = cubeList[R11]
    rotatedCubeList[R23] = cubeList[R12]
    rotatedCubeList[R33] = cubeList[R13]
    rotatedCubeList[R12] = cubeList[R21]
    rotatedCubeList[R22] = cubeList[R22]
    rotatedCubeList[R32] = cubeList[R23]
    rotatedCubeList[R11] = cubeList[R31]
    rotatedCubeList[R21] = cubeList[R32]
    rotatedCubeList[R31] = cubeList[R33]
    #up to back
    rotatedCubeList[B11] = cubeList[U33]
    rotatedCubeList[B21] = cubeList[U23]
    rotatedCubeList[B31] = cubeList[U13]
    #back to down
    rotatedCubeList[D33] = cubeList[B11]
    rotatedCubeList[D23] = cubeList[B21]
    rotatedCubeList[D13] = cubeList[B31]
    #down to front
    rotatedCubeList[F13] = cubeList[D13]
    rotatedCubeList[F23] = cubeList[D23]
    rotatedCubeList[F33] = cubeList[D33]
    #front to up
    rotatedCubeList[U33] = cubeList[F33]
    rotatedCubeList[U13] = cubeList[F13]
    rotatedCubeList[U23] = cubeList[F23]
    
    return rotatedCubeList

#reverse of R
def _r(cubeList):
    rotatedCubeList = list(cubeList)
    
    rotatedCubeList[R11] = cubeList[R13]
    rotatedCubeList[R12] = cubeList[R23]
    rotatedCubeList[R13] = cubeList[R33]
    rotatedCubeList[R21] = cubeList[R12]
    rotatedCubeList[R22] = cubeList[R22]
    rotatedCubeList[R23] = cubeList[R32]
    rotatedCubeList[R31] = cubeList[R11]
    rotatedCubeList[R32] = cubeList[R21]
    rotatedCubeList[R33] = cubeList[R31]
    #
    rotatedCubeList[U33] = cubeList[B11]
    rotatedCubeList[U23] = cubeList[B21]
    rotatedCubeList[U13] = cubeList[B31]
    #
    rotatedCubeList[B11] = cubeList[D33]
    rotatedCubeList[B21] = cubeList[D23]
    rotatedCubeList[B31] = cubeList[D13]
    #
    rotatedCubeList[D13] = cubeList[F13]
    rotatedCubeList[D23] = cubeList[F23]
    rotatedCubeList[D33] = cubeList[F33]
    #
    rotatedCubeList[F13] = cubeList[U13]
    rotatedCubeList[F23] = cubeList[U23]
    rotatedCubeList[F33] = cubeList[U33]
    
    return rotatedCubeList

#left clock
def _L(cubeList):
    rotatedCubeList = list(cubeList)
    
    rotatedCubeList[L13] = cubeList[L11]
    rotatedCubeList[L23] = cubeList[L12]
    rotatedCubeList[L33] = cubeList[L13]
    rotatedCubeList[L12] = cubeList[L21]
    rotatedCubeList[L22] = cubeList[L22]
    rotatedCubeList[L32] = cubeList[L23]
    rotatedCubeList[L11] = cubeList[L31]
    rotatedCubeList[L21] = cubeList[L32]
    rotatedCubeList[L31] = cubeList[L33]
    #up to front
    rotatedCubeList[F11] = cubeList[U11]
    rotatedCubeList[F21] = cubeList[U21]
    rotatedCubeList[F31] = cubeList[U31]
    #front to down
    rotatedCubeList[D11] = cubeList[F11]
    rotatedCubeList[D21] = cubeList[F21]
    rotatedCubeList[D31] = cubeList[F31]
    #down to back
    rotatedCubeList[B33] = cubeList[D11]
    rotatedCubeList[B23] = cubeList[D21]
    rotatedCubeList[B13] = cubeList[D31]
    #back to up
    rotatedCubeList[U31] = cubeList[B13]
    rotatedCubeList[U21] = cubeList[B23]
    rotatedCubeList[U11] = cubeList[B33]
    
    return rotatedCubeList

#reverse of L
def _l(cubeList):
    rotatedCubeList = list(cubeList)
    
    rotatedCubeList[L11] = cubeList[L13]
    rotatedCubeList[L12] = cubeList[L23]
    rotatedCubeList[L13] = cubeList[L33]
    rotatedCubeList[L21] = cubeList[L12]
    rotatedCubeList[L22] = cubeList[L22]
    rotatedCubeList[L23] = cubeList[L32]
    rotatedCubeList[L31] = cubeList[L11]
    rotatedCubeList[L32] = cubeList[L21]
    rotatedCubeList[L33] = cubeList[L31]
    #
    rotatedCubeList[U11] = cubeList[F11]
    rotatedCubeList[U21] = cubeList[F21]
    rotatedCubeList[U31] = cubeList[F31]
    #
    rotatedCubeList[F11] = cubeList[D11]
    rotatedCubeList[F21] = cubeList[D21]
    rotatedCubeList[F31] = cubeList[D31]
    #
    rotatedCubeList[D11] = cubeList[B33]
    rotatedCubeList[D21] = cubeList[B23]
    rotatedCubeList[D31] = cubeList[B13]
    #
    rotatedCubeList[B13] = cubeList[U31]
    rotatedCubeList[B23] = cubeList[U21]
    rotatedCubeList[B33] = cubeList[U11]
                 
    return rotatedCubeList