import rubik.rotate as rotate
import hashlib
import random
[F11], [R11], [B11], [L11], [U11], [D11] = [0], [9], [18], [27], [36], [45]
[F12], [R12], [B12], [L12], [U12], [D12] = [1], [10], [19], [28], [37], [46]  #11 12 13
[F13], [R13], [B13], [L13], [U13], [D13] = [2], [11], [20], [29], [38], [47]  #21 22 23
[F21], [R21], [B21], [L21], [U21], [D21] = [3], [12], [21], [30], [39], [48]  #31 32 33
[F22], [R22], [B22], [L22], [U22], [D22] = [4], [13], [22], [31], [40], [49]  #Center
[F23], [R23], [B23], [L23], [U23], [D23] = [5], [14], [23], [32], [41], [50]
[F31], [R31], [B31], [L31], [U31], [D31] = [6], [15], [24], [33], [42], [51]
[F32], [R32], [B32], [L32], [U32], [D32] = [7], [16], [25], [34], [43], [52]
[F33], [R33], [B33], [L33], [U33], [D33] = [8], [17], [26], [35], [44], [53]

def _solve(parms):
    """Return rotates needed to solve input cube"""
    result = {}
    solution = ''
    encodedCube = parms.get('cube','None')       #STUB:  get "cube" parameter if present
    cube = list(encodedCube)
    
    if encodedCube == 'None' or encodedCube == '':
        encodedCube = list('n')
    
    cubecheckv = _cubeCheckValid(encodedCube)
    
    if cubecheckv.get('status', None) != 'ok':
        result = cubecheckv
    
    else: 
        solution = _getSolution(cube)
        token = _getToken(encodedCube, solution)
        result['rotations'] = solution 
        result['status'] = 'ok'
        result['token'] = token
    return result

def _getToken(encodeCube, solution):
    sha256Hash = hashlib.sha256()
    itemToTokenize = encodeCube + solution
    sha256Hash.update(itemToTokenize.encode())
    fullToken = sha256Hash.hexdigest()
    ranNumber = random.randint(0, len(fullToken)-9) 
    fullTokenlist = list(fullToken)
    tokenStr = fullTokenlist[ranNumber:ranNumber+8]
    retToken = ''.join(list(tokenStr))
    return retToken

def _getSolution(cube):
    solutionList = ''
    if (_bottomCrossCheck(cube) != 'ok'):
        solution = _getBottomCross(cube)
        resultr = ''.join(list(solution))
        cube = rotate._makeRotate(cube,resultr)
        solutionList = solutionList + resultr
    if (_bottomLayerCheck(cube) != 'ok'):
        solution = _getBottomLayer(cube)
        resultr = ''.join(list(solution))
        cube = rotate._makeRotate(cube,resultr)
        solutionList = solutionList + resultr
    if (_middleLayerCheck(cube) != 'ok'):
        solution = _getMiddleLayer(cube)
        resultr = ''.join(list(solution))
        cube = rotate._makeRotate(cube,resultr)
        solutionList = solutionList + resultr
    if ((_topCrossCheck(cube) != 4) or (_topCornerCheck(cube) != 4)):
        solution = _getTopFace(cube)
        resultr = ''.join(list(solution))
        cube = rotate._makeRotate(cube,resultr)
        solutionList = solutionList + resultr
    if ((_cornerBoundCheck(cube) != 'ok') or (_cornerEdgeCheck(cube) != 'ok') or (_edgeEdgeCheck(cube) != 'ok')):
        solution = _getTopEdge(cube)
        resultr = ''.join(list(solution))
        cube = rotate._makeRotate(cube,resultr)
        solutionList = solutionList + resultr
    fsolution = ''.join(list(solutionList))
    return fsolution    

'two checkcube one valid and one for process'
def _cubeCheckValid(encodedCube):
    result = {}
    cubestatus = rotate._checkCube(encodedCube)
    if cubestatus.get('status', None) != 'ok':
        result = cubestatus
    else:  
        result['status'] = 'ok'
    return result

def _getBottomCross(cube):
    solutionList = ''
    while (_daisyChecke(cube) != 'ok'):
        result = _daisyChecke(cube)
        solutionStr = _makeDaisy(result,cube)
        solution = list(solutionStr)
        resultr = ''.join(list(solution))
        cube = rotate._makeRotate(cube,resultr)
        solutionList = solutionList + resultr
    else:
        while (_bottomCrossCheck(cube) != 'ok'):
                result = _stickCheck(cube)
                solutionStr = _makeBottomCross(result)
                solution = list(solutionStr)
                resultr = ''.join(list(solution))
                cube = rotate._makeRotate(cube,resultr)
                solutionList = solutionList + resultr
        else: 
            return solutionList

def _bottomCrossCheck(cube):
    result = {}
    if (cube[D22] != cube[D12]):
        result = 'fedge'
    elif (cube[D22] != cube[D23]):
        result = 'redge'
    elif (cube[D22] != cube[D32]):
        result = 'bedge'
    elif (cube[D22] != cube[D21]):
        result = 'ledge'
    
    elif (cube[L22] != cube[L32]):
        result = 'fstick'
    elif (cube[F22] != cube[F32]):
        result = 'lstick'
    elif (cube[R22] != cube[R32]):
        result = 'rstick'
    elif (cube[B22] != cube[B32]):
        result = 'bstick' 
    else:
        result = 'ok'
    return result

def _stickCheck(cube):
    result = {}
    
    if (cube[L22] == cube[L12] and cube[D22] == cube[U21]):
        result = 'Lstick'
    elif (cube[F22] == cube[F12] and cube[D22] == cube[U32]):
        result = 'Fstick'
    elif (cube[R22] == cube[R12] and cube[D22] == cube[U23]):
        result = 'Rstick'
    elif (cube[B22] == cube[B12] and cube[D22] == cube[U12]):
        result = 'Bstick'
    else: 
        result = 'needU'
    return result

def _daisyChecke(cube):
    result = {}
    if (cube[D22] != cube[U32]):
        result = 'Fedge'
    elif (cube[D22] != cube[U23]):
        result = 'Redge'
    elif (cube[D22] != cube[U12]):
        result = 'Bedge'
    elif (cube[D22] != cube[U21]):
        result = 'Ledge'
    else:
        result = 'ok'
    return result

def _makeBottomCross(result):
    solution = {}
    if result == 'Lstick':
        solution = 'LL'
    elif result == 'Fstick':
        solution = 'FF'
    elif result == 'Rstick':
        solution = 'RR'
    elif result == 'Bstick':
        solution = 'BB'
    elif result == 'needU':
        solution = 'U'
    return solution
    
def _makeDaisy(result,cube):
    solution = {}
    if result == 'Fedge':
        if (cube[D22] == cube[L23] or cube[D22] == cube[R21] or cube[D22] == cube[D12] or cube[D22] == cube[F12]):
            solution = 'F'
        elif (cube[D22] == cube[L12] or cube[D22] == cube[L21] or cube[D22] == cube[F21]):
            solution = 'L'  
        elif (cube[D22] == cube[R12] or cube[D22] == cube[R23] or cube[D22] == cube[R32] or cube[D22] == cube[F23]):
            solution = 'R'
        elif (cube[D22] == cube[B21]):
            solution = 'ur'
        elif (cube[D22] == cube[B23]):
            solution = 'UL'
        else:
            solution = 'D'
    elif result == 'Redge':
        if (cube[D22] == cube[F23] or cube[D22] == cube[B21] or cube[D22] == cube[D23]):
            solution = 'R'
        elif (cube[D22] == cube[B23] or cube[D22] == cube[B12] or cube[D22] == cube[B32]):
            solution = 'B'
        else:
            solution = 'U'
    elif result == 'Bedge':
        if (cube[D22] == cube[R23] or cube[D22] == cube[L21] or cube[D22] == cube[D32]):
            solution = 'B'
        elif (cube[D22] == cube[L12] or cube[D22] == cube[L23] or cube[D22] == cube[L32]):
            solution = 'L'
        else:
            solution = 'U'
    elif result == 'Ledge':
        if (cube[D22] == cube[B23] or cube[D22] == cube[F21] or cube[D22] == cube[D21]):
            solution = 'L' 
        elif (cube[D22] == cube[L12] or cube[D22] == cube[L23] or cube[D22] == cube[L32]):
            solution = 'L'
        else:
            solution = 'U'
    return solution

def _bottomLayerCheck(cube):
    result = {}
    if (cube[D22] != cube[D11] or cube[F22] != cube[F31] or cube[L22] != cube[L33]):
        result = 'lfcorner'
    elif (cube[D22] != cube[D13] or cube[F22] != cube[F33] or cube[R22] != cube[R31]):
        result = 'rfcorner'
    elif (cube[D22] != cube[D31] or cube[B22] != cube[B33] or cube[L22] != cube[L31]):
        result = 'lbcorner'
    elif (cube[D22] != cube[D33] or cube[B22] != cube[B31] or cube[R22] != cube[R33]):
        result = 'rbcorner'
    else:
        result = 'ok'
    return result

def _getCorner(cube,corner):
    fulCorner = cube[F11] + cube[L13] + cube[U31]
    furCorner = cube[F13] + cube[R11] + cube[U33]
    fdlCorner = cube[F31] + cube[L33] + cube[D11]
    fdrCorner = cube[F33] + cube[R31] + cube[D13]
    bulCorner = cube[B13] + cube[U11] + cube[L11]
    burCorner = cube[R13] + cube[B11] + cube[U13]
    bdlCorner = cube[B33] + cube[D31] + cube[L31]
    bdrCorner = cube[D33] + cube[B31] + cube[R33]
    
    if corner == 'ful':
        verifyCorner = fulCorner
    elif corner == 'fur':
        verifyCorner = furCorner
    elif corner == 'fdl':
        verifyCorner = fdlCorner
    elif corner == 'fdr':
        verifyCorner = fdrCorner
    elif corner == 'bul':
        verifyCorner = bulCorner
    elif corner == 'bur':
        verifyCorner = burCorner
    elif corner == 'bdl':
        verifyCorner = bdlCorner
    elif corner == 'bdr':
        verifyCorner = bdrCorner
    
    return verifyCorner

def _getCornerColor(cube,color):
    fulColor = cube[F22] + cube[U22] + cube[L22]
    furColor = cube[F22] + cube[U22] + cube[R22]
    fdlColor = cube[F22] + cube[D22] + cube[L22]
    fdrColor = cube[F22] + cube[D22] + cube[R22]
    bulColor = cube[B22] + cube[U22] + cube[L22]
    burColor = cube[B22] + cube[U22] + cube[R22]
    bdlColor = cube[B22] + cube[D22] + cube[L22]
    bdrColor = cube[B22] + cube[D22] + cube[R22]
      
    if color == 'FUL':
        verifyColor = fulColor
    elif color == 'FUR':
        verifyColor = furColor
    elif color == 'FDL':
        verifyColor = fdlColor
    elif color == 'FDR':
        verifyColor = fdrColor
    elif color == 'BUL':
        verifyColor = bulColor
    elif color == 'BUR':
        verifyColor = burColor
    elif color == 'BDL':
        verifyColor = bdlColor
    elif color == 'BDR':
        verifyColor = bdrColor
    
    return verifyColor

def _cornerCheck(cube,corner,color):
    verifyCorner = _getCorner(cube,corner)
    verifyColor = _getCornerColor(cube,color)
    cornerCounter = 0
    for corner in verifyCorner:
        if corner in verifyColor:
            cornerCounter += 1
            
    downCounter = 0
    for corner in verifyCorner:
        if corner in cube[D22]:
            downCounter = 1
    if (cornerCounter != 3 and downCounter == 1):
        cornerCounter = -1
           
    return cornerCounter

def _bottomCornerCheck(cube):
    result = {}
    if ((_cornerCheck(cube, 'fdl', 'FDL') == -1) and (_cornerCheck(cube, 'ful', 'FDL') != -1)):
        result = 'FUfu'
    elif ((_cornerCheck(cube, 'fdl', 'FDL') == -1) and (_cornerCheck(cube, 'ful', 'FDL') == -1)):
        result = 'U'
    elif((_cornerCheck(cube, 'fdr', 'FDR') == -1) and (_cornerCheck(cube, 'fur', 'FDR') != -1)):
        result = 'RUru'
    elif((_cornerCheck(cube, 'fdr', 'FDR') == -1) and (_cornerCheck(cube, 'fur', 'FDR') == -1)):
        result = 'U'
    elif((_cornerCheck(cube, 'bdl', 'BDL') == -1) and (_cornerCheck(cube, 'bul', 'BDL') != -1)):
        result = 'LUlu'
    elif((_cornerCheck(cube, 'bdl', 'BDL') == -1) and (_cornerCheck(cube, 'bul', 'BDL') == -1)):
        result = 'U'
    elif((_cornerCheck(cube, 'bdr', 'BDR') == -1) and (_cornerCheck(cube, 'bur', 'BDR') != -1)):
        result = 'BUbu'
    elif((_cornerCheck(cube, 'bdr', 'BDR') == -1) and (_cornerCheck(cube, 'bur', 'BDR') == -1)):
        result = 'U'
    else:
        result = 'ok'
    return result

def _bottomCornerReadyCheck(cube,status):
    result = {}
    if (status == 'lfcorner' and ( _cornerCheck(cube, 'ful', 'FDL') == 3 or _cornerCheck(cube, 'fdl', 'FDL') == 3)):
        result = 'FUfu'
    elif(status == 'rfcorner' and ( _cornerCheck(cube, 'fur', 'FDR') == 3 or _cornerCheck(cube, 'fdr', 'FDR') == 3)):
        result = 'RUru'
    elif(status == 'lbcorner' and ( _cornerCheck(cube, 'bul', 'BDL') == 3 or _cornerCheck(cube, 'bdl', 'BDL') == 3)):
        result = 'LUlu'
    elif(status == 'rbcorner' and (_cornerCheck(cube, 'bur', 'BDR') == 3 or _cornerCheck(cube, 'bdr', 'BDR') == 3)):
        result = 'BUbu'
    else:
        result = 'U'
    return result
      
def _getBottomLayer(cube):
    solutionList = ''
    if (_bottomLayerCheck(cube) != 'ok'):
        while (_bottomCornerCheck(cube) != 'ok'):
            solutionStr = _bottomCornerCheck(cube)
            solution = list(solutionStr)
            resultr = ''.join(list(solution))
            cube = rotate._makeRotate(cube,resultr)
            solutionList = solutionList + resultr 
        else:
            while (_bottomLayerCheck(cube) != 'ok'):
                status = _bottomLayerCheck(cube)    
                solutionStr = _bottomCornerReadyCheck(cube, status)
                solution = list(solutionStr)
                resultr = ''.join(list(solution))
                cube = rotate._makeRotate(cube,resultr)
                solutionList = solutionList + resultr 
            else:
                return solutionList

def _middleLayerCheck(cube):
    result = {}
    if (cube[L22] != cube[L23] or cube[F22] != cube[F21]):
        result = 'FLEdge'
    elif (cube[R22] != cube[R21] or cube[F22] != cube[F23]):
        result = 'FREdge'
    elif (cube[L22] != cube[L21] or cube[B22] != cube[B23]):
        result = 'BLEdge'
    elif (cube[R22] != cube[R23] or cube[B22] != cube[B21]):
        result = 'BREdge'
    else: 
        result = 'ok'
    return result

def _getEdge(cube,edge):
    flEdge = cube[F21] + cube[L23]
    frEdge = cube[R21] + cube[F23]
    blEdge = cube[L21] + cube[B23]
    brEdge = cube[R23] + cube[B21]
    fuEdge = cube[F12] + cube[U32]
    ruEdge = cube[R12] + cube[U23]
    buEdge = cube[B12] + cube[U12]
    luEdge = cube[L12] + cube[U21]
    
    if edge == 'fl':
        verifyEdge = flEdge
    elif edge == 'fr':
        verifyEdge = frEdge
    elif edge == 'bl':
        verifyEdge = blEdge
    elif edge == 'br':
        verifyEdge = brEdge
    elif edge == 'fu':
        verifyEdge = fuEdge
    elif edge == 'ru':
        verifyEdge = ruEdge
    elif edge == 'bu':
        verifyEdge = buEdge
    elif edge == 'lu':
        verifyEdge = luEdge
    return verifyEdge

def _getEdgeColor(cube,color):
    flColor = cube[F22] + cube[L22]
    frColor = cube[F22] + cube[R22]
    blColor = cube[B22] + cube[L22]
    brColor = cube[B22] + cube[R22]
    fuColor = cube[F22] + cube[U22]
    ruColor = cube[R22] + cube[U22]
    buColor = cube[B22] + cube[U22]
    luColor = cube[L22] + cube[U22]
    
    if color == 'FL':
        verifyColor = flColor
    elif color == 'FR':
        verifyColor = frColor
    elif color == 'BL':
        verifyColor = blColor
    elif color == 'BR':
        verifyColor = brColor
    elif color == 'FU':
        verifyColor = fuColor
    elif color == 'RU':
        verifyColor = ruColor
    elif color == 'BU':
        verifyColor = buColor
    elif color == 'LU':
        verifyColor = luColor
    return verifyColor 

def _middleEdgeCheck(cube, edge, color):
    verifyEdge = _getEdge(cube,edge)
    verifyColor = _getEdgeColor(cube,color)
    edgeCounter = 0
    for edge in verifyEdge:
        if edge in verifyColor:
            edgeCounter += 1
            
    upperCounter = 0
    for edge in verifyEdge:
        if edge in cube[U22]:
            upperCounter += 1
            
    if (upperCounter == 1) and (edgeCounter != 2):
        edgeCounter = -1
        
    return edgeCounter

def _middleEdgeReadyCheck(cube):
    result = {}
    if (_middleEdgeCheck(cube, 'fl', 'FL') != -1):
        if (_middleEdgeCheck(cube, 'ru', 'RU') == -1 or (_middleEdgeCheck(cube, 'ru', 'RU') == 2)):
            result = 'luLUFUfu'
        else:
            result = 'U'
    elif (_middleEdgeCheck(cube, 'fr', 'FR') != -1):
        if (_middleEdgeCheck(cube, 'bu', 'BU') == -1 or (_middleEdgeCheck(cube, 'bu', 'BU') == 2)):
            result = 'fuFURUru'
        else:
            result = 'U'
    elif (_middleEdgeCheck(cube, 'br', 'BR') != -1):
        if (_middleEdgeCheck(cube, 'lu', 'LU') == -1 or (_middleEdgeCheck(cube, 'lu', 'LU') == 2)):
            result = 'ruRUBUbu'
        else:
            result = 'U'
    elif (_middleEdgeCheck(cube, 'bl', 'BL') != -1):
        if (_middleEdgeCheck(cube, 'fu', 'FU') == -1 or (_middleEdgeCheck(cube, 'fu', 'FU') == 2)):
            result = 'buBULUlu'
        else:
            result = 'U'
    else:
        result = 'ok'
    return result

def _makeMiddleLayer(cube):
    result = {}
    if (cube[B12] == cube[L22]) and (_middleEdgeCheck(cube, 'bu', 'FL') == 2): # Right hand fist
        result = 'FUfuluLU'
    elif (cube[L12] == cube[F22]) and (_middleEdgeCheck(cube, 'lu', 'FR') == 2):
        result = 'RUrufuFU'
    elif (cube[F12] == cube[R22]) and (_middleEdgeCheck(cube, 'fu', 'BR') == 2):
        result = 'BUburuRU'
    elif (cube[R12] == cube[B22]) and (_middleEdgeCheck(cube, 'ru', 'BL') == 2):
        result = 'LUlubuBU'
        
    elif (cube[R12] == cube[F22]) and (_middleEdgeCheck(cube, 'ru', 'FL') == 2): # left hand fist
        result = 'luLUFUfu'
    elif (cube[B12] == cube[R22]) and (_middleEdgeCheck(cube, 'bu', 'FR') == 2):
        result = 'fuFURUru'
    elif (cube[L12] == cube[B22]) and (_middleEdgeCheck(cube, 'lu', 'BR') == 2):
        result = 'ruRUBUbu'
    elif (cube[F12] == cube[L22]) and (_middleEdgeCheck(cube, 'fu', 'BL') == 2):
        result = 'buBULUlu'
    else:
        result = 'U'
    return result

def _getMiddleLayer(cube):
    solutionList = ''
    if (_middleLayerCheck(cube) != 'ok'):
        while (_middleEdgeReadyCheck(cube) != 'ok'):
            solutionStr = _middleEdgeReadyCheck(cube)
            solution = list(solutionStr)
            resultr = ''.join(list(solution))
            cube = rotate._makeRotate(cube,resultr)
            solutionList = solutionList + resultr 
        else:
            while(_middleLayerCheck(cube) != 'ok'):
                solutionStr = _makeMiddleLayer(cube)
                solution = list(solutionStr)
                resultr = ''.join(list(solution))
                cube = rotate._makeRotate(cube,resultr)
                solutionList = solutionList + resultr
            else:
                return solutionList

def _topCrossCheck(cube):
    topCross = cube[U32] + cube[U23] + cube[U12] + cube[U21]
    blockCounter = 0
    for block in topCross:
        if (block == cube[U22]):
            blockCounter += 1
    return blockCounter

def _topCrossStatus(cube):
    result = {}
    if (cube[U22] == cube[U21] and cube[U22] == cube[U23]):
        result = '-Line'
    elif (cube[U22] == cube[U12] and cube[U22] == cube[U32]):
        result = '1Line'
    elif (cube[U22] == cube[U32] and cube[U22] == cube[U23]):
        result = 'ΓFEdge'
    elif (cube[U22] == cube[U23] and cube[U22] == cube[U12]):
        result = 'ΓREdge'
    elif (cube[U22] == cube[U12] and cube[U22] == cube[U21]):
        result = 'ΓBEdge'
    elif (cube[U22] == cube[U21] and cube[U22] == cube[U32]):
        result = 'ΓLEdge'
    else:
        result = 'NoEdge'
    return result

def _makeTopCross(status):
    result = {}
    if (status == '-Line' or status == 'ΓFEdge' or status == 'NoEdge'):
        result = 'FRUruf'
    elif(status == '1Line' or status == 'ΓREdge'):
        result = 'RBUbur'
    elif(status == 'ΓBEdge'):
        result = 'BLUlub'
    elif(status == 'ΓLEdge'):
        result = 'LFUful'
    return result

def _getTopFace(cube):
    solutionList = ''
    if ((_topCrossCheck(cube) != 4) or (_topCornerCheck(cube) != 4)):
        while (_topCrossCheck(cube) != 4):
            status = _topCrossStatus(cube)
            solutionStr = _makeTopCross(status)
            solution = list(solutionStr)
            resultr = ''.join(list(solution))
            cube = rotate._makeRotate(cube,resultr)
            solutionList = solutionList + resultr 
        else:
            while (_topCornerCheck(cube) != 4):
                status = _topCornerStatus(cube)
                solutionStr = _makeTopCorner(status)
                solution = list(solutionStr)
                resultr = ''.join(list(solution))
                cube = rotate._makeRotate(cube,resultr)
                solutionList = solutionList + resultr 
            else:
                return solutionList
        
def _topCornerCheck(cube):
    topCross = cube[U31] + cube[U33] + cube[U11] + cube[U13]
    blockCounter = 0
    for block in topCross:
        if (block == cube[U22]):
            blockCounter += 1
    return blockCounter
    
def _topCornerStatus(cube):
    result = {}
    if (_topCornerCheck(cube) == 1):
        if (cube[U31] == cube[U22]):
            result = 'RSide'
        elif (cube[U33] == cube[U22]):
            result = 'BSide'
        elif (cube[U13] == cube[U22]):
            result = 'LSide'
        elif (cube[U11] == cube[U22]):
            result = 'FSide'
    elif (_topCornerCheck(cube) == 2):
        if (cube[L13] == cube[U22]):
            result = 'RSide'
        elif (cube[F13] == cube[U22]):
            result = 'BSide'
        elif (cube[R13] == cube[U22]):
            result = 'LSide'
        elif (cube[B13] == cube[U22]):
            result = 'FSide'
    elif (_topCornerCheck(cube) == 0):
        result = 'FSide'
    return result

def _makeTopCorner(status):
    result = {}
    if (status == 'FSide'):
        result = 'ruRuruuR'
    elif (status == 'RSide'):
        result = 'buBubuuB'
    elif (status == 'BSide'):
        result = 'luLuluuL'
    elif (status == 'LSide'):
        result = 'fuFufuuF'
    return result

def _cornerBoundCheck(cube):
    result = {}
    if ((cube[F11] == cube[F13]) and (cube[R11] == cube[R13]) and (cube[B11] == cube[B13]) and (cube[L11] == cube[L13])):
        result = 'ok'
    elif (cube[F11] == cube[F13]):
        result = 'Fside'
    elif (cube[R11] == cube[R13]):
        result = 'Rside'
    elif (cube[B11] == cube[B13]):
        result = 'Bside'
    elif (cube[L11] == cube[L13]):
        result = 'Lside'
    else:
        result = 'Fside'
    return result

def _makeRightBound(status):
    result = {}
    if (status == 'Fside'):
        result = 'RbRffrBRffrr'
    elif (status == 'Rside'):
        result = 'BlBrrbLBrrbb'
    elif (status == 'Bside'):
        result = 'LfLbblFLbbll'
    elif (status == 'Lside'):
        result = 'FrFllfRFllff'
    return result

def _cornerEdgeCheck(cube):
    result = {}
    if ((_cornerCheck(cube, 'ful', 'FUL') != 3) or (_cornerCheck(cube, 'fur', 'FUR') != 3) or (_cornerCheck(cube, 'bur', 'BUR') != 3) or 
        (_cornerCheck(cube, 'bul', 'BUL') != 3)):
        result = 'notok'
    else:
        result = 'ok'
    return result

def _edgeEdgeCheck(cube):
    result = {}
    if (cube[F12] == cube[F22]):
        result = 'Fedge'
    elif (cube[R12] == cube[R22]):
        result = 'Redge'
    elif (cube[B12] == cube[B22]):
        result = 'Bedge'
    elif (cube[L12] == cube[L22]):
        result = 'Ledge'
    else:
        result = 'Fedge'
    if ((cube[F12] == cube[F22]) and (cube[R12] == cube[R22]) and (cube[B12] == cube[B22]) and (cube[L12] == cube[L22])):
        result = 'ok'
    return result

def _makeEdgeColor(status):
    result = {}
    if (status == 'Fedge'):
        result = 'rUrururURUrr'
    elif (status == 'Redge'):
        result = 'bUbububUBUbb'
    elif (status == 'Bedge'):
        result = 'lUlululULUll'
    elif (status == 'Ledge'):
        result = 'fUfufufUFUff'
    return result

def _getTopEdge(cube):
    solutionList = ''
    if ((_cornerBoundCheck(cube) != 'ok') or (_cornerEdgeCheck(cube) != 'ok') or (_edgeEdgeCheck(cube) != 'ok')):
        while (_cornerBoundCheck(cube) != 'ok'):
            status = _cornerBoundCheck(cube)
            solutionStr = _makeRightBound(status)
            solution = list(solutionStr)
            resultr = ''.join(list(solution))
            cube = rotate._makeRotate(cube,resultr)
            solutionList = solutionList + resultr 
        else:
            while (_cornerEdgeCheck(cube) != 'ok'):
                solutionStr = 'U'
                solution = list(solutionStr)
                resultr = ''.join(list(solution))
                cube = rotate._makeRotate(cube,resultr)
                solutionList = solutionList + resultr 
            else:
                while (_edgeEdgeCheck(cube) != 'ok'):
                    status = _edgeEdgeCheck(cube)
                    solutionStr = _makeEdgeColor(status)
                    solution = list(solutionStr)
                    resultr = ''.join(list(solution))
                    cube = rotate._makeRotate(cube,resultr)
                    solutionList = solutionList + resultr
                else:
                    return solutionList