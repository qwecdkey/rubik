import unittest
import rubik.solve as solve

class solveTest(unittest.TestCase):

    '''def test000solveforeachiterationi4RandomMiddleLayerAlready1(self):
        inputCode = {}
        inputCode['op'] = 'solve'
        inputCode['cube'] = 'oryrgygggbygooboooygoobgbbbbbgorgrrryyrrybyyrwwwwwwwww'
        
        ExpectedResults = {}
        ExpectedResults['status'] =  'ok'
        ExpectedResults['rotations'] = 'luLUFUfuUruRUBUbuUUbuBULUluLUlubuBUUUFUfuluLUUBUburuRUURUrufuFU'
        
        ActualResults = solve._solve(inputCode)
        self.assertEqual(ExpectedResults['status'], ActualResults['status'])  
        self.assertEqual(ExpectedResults['rotations'], ActualResults['rotations'])
        
    def test000solveforeachiterationi4randomMiddleLayerAlready2(self):
        inputCode = {}
        inputCode['op'] = 'solve'
        inputCode['cube'] = 'obgygogggoyygobooobryobgbbbrryyrrrrrggrbyobyywwwwwwwww'
        
        ExpectedResults = {}
        ExpectedResults['status'] =  'ok'
        ExpectedResults['rotations'] = 'UUfuFURUruUUruRUBUbuULUlubuBUUUFUfuluLUfuFURUruUUBUburuRU'
        
        ActualResults = solve._solve(inputCode)
        self.assertEqual(ExpectedResults['status'], ActualResults['status'])  
        self.assertEqual(ExpectedResults['rotations'], ActualResults['rotations'])
    
    def test000solveforeachiterationi4randomMiddleLayerAlready3(self):
        inputCode = {}
        inputCode['op'] = 'solve'
        inputCode['cube'] = 'ybyrgygggooogoooooyrygbobbbbrgyrbrrrryggybrybwwwwwwwww'
        
        ExpectedResults = {}
        ExpectedResults['status'] =  'ok'
        ExpectedResults['rotations'] = 'UluLUFUfuUUUruRUBUbuUUbuBULUluluLUFUfuUUUfuFURUruUBUburuRU'
    
    def test000solveforeachiterationi4randomMiddleLayerAlready4(self):
        inputCode = {}
        inputCode['op'] = 'solve'
        inputCode['cube'] = 'ybgbgygggyyooooooobyogbrbbbyrryrrrrrggygybborwwwwwwwww'
        
        ExpectedResults = {}
        ExpectedResults['status'] =  'ok'
        ExpectedResults['rotations'] = 'luLUFUfuUruRUBUbuUUFUfuluLUfuFURUruUbuBULUluruRUBUbu'
        '''
    def test010solveNoAction(self):
        inputCode = {}
        inputCode['op'] = 'solve'
        inputCode['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        
        ExpectedResults = {}
        ExpectedResults['status'] =  'ok'
        ExpectedResults['rotations'] = ''
        
        ActualResults = solve._solve(inputCode)
        self.assertEqual(ExpectedResults['status'], ActualResults['status'])  
        self.assertEqual(ExpectedResults['rotations'], ActualResults['rotations'])
        
    def test020solvecubecheckNone(self):
        inputCode = {}
        inputCode['op'] = 'solve'
        inputCode['cube'] = ''
        
        ExpectedResults = {}
        ExpectedResults['status'] = 'error: Cube is missing'
        ExpectedResults['rotations'] = ''
        
        ActualResults = solve._solve(inputCode)
        self.assertEqual(ExpectedResults['status'], ActualResults['status'])
    
    def test030bccTest(self):
        inputCode = list('gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy')
        
        ExpectedResults =  'ok'
        
        ActualResults = solve._bottomCrossCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)  
        
    def test030bccTestF(self):
        inputCode = list('bbbbbbbbbrrrrrrrrrgggggggggoooooooowyyyyyyyyywowwwwwww')
        
        ExpectedResults =  'fedge'
        
        ActualResults = solve._bottomCrossCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)  
        
    def test030bccTestL(self):
        inputCode = list('gggggggggrrrrrrrrrbbbbbbbbyooooooooowwwwwwwwwyyybyyyyy')
        
        ExpectedResults =  'ledge'
        
        ActualResults = solve._bottomCrossCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)  
        
    def test030bccTestR(self):
        inputCode = list('bbbbbbbbbrrrrrrrrwgggggggggoooooooooyyyyyyyyywwwwwrwww')
        
        ExpectedResults =  'redge'
        
        ActualResults = solve._bottomCrossCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)  
        
    def test030bccTestB(self):
        inputCode = list('bbbbbbbbbrrrrrrrrrggggggggwoooooooooyyyyyyyyywwwwwwwow')
        
        ExpectedResults =  'bedge'
        
        ActualResults = solve._bottomCrossCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)  
        
    def test040scTestL(self):
        inputCode = list('brbbbbbbbrgrrrrrrrgrgggggggoooooooooywywywywywywywywyw')
        
        ExpectedResults =  'Lstick'
        
        ActualResults = solve._stickCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)  
        
    def test040scTestF(self):
        inputCode = list('bbbbbbbbbrgrrrrrrrgogggggggoroooooooywywywywywywywywyw')
        
        ExpectedResults =  'Fstick'
        
        ActualResults = solve._stickCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)  
        
    def test040scTestR(self):
        inputCode = list('bgbbbbbbbrrrrrrrrrgogggggggoboooooooywywywywywywywywyw')
        
        ExpectedResults =  'Rstick'
        
        ActualResults = solve._stickCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)  
    
    def test040scTestB(self):
        inputCode = list('bgbbbbbbbrorrrrrrrgggggggggoboooooooywywywywywywywywyw')
        
        ExpectedResults =  'Bstick'
        
        ActualResults = solve._stickCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)  
        
    def test050dacTestF(self):
        inputCode = list('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww')
        
        ExpectedResults =  'Fedge'
        
        ActualResults = solve._daisyChecke(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
        
    def test050dacTestR(self):
        inputCode = list('bbbbbbbbbrrrrrrrrrgggggggggoooooooooywywyyywywywywwwyw')
        
        ExpectedResults =  'Redge'
        
        ActualResults = solve._daisyChecke(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)   
        
    def test050dacTestB(self):
        inputCode = list('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyywywywywwwywww')
        
        ExpectedResults =  'Bedge'
        
        ActualResults = solve._daisyChecke(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)  
        
    def test050dacTestL(self):
        inputCode = list('bbbbbbbbbrrrrrrrrrgggggggggoooooooooywyyywywywywwwywyw')
        
        ExpectedResults =  'Ledge'
        
        ActualResults = solve._daisyChecke(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)  
    
        
    def test050dacTestOK(self):
        inputCode = list('bbbbbbbbbrrrrrrrrrgggggggggoooooooooywywywywywywywywyw')
        
        ExpectedResults =  'ok'
        
        ActualResults = solve._daisyChecke(inputCode)
        self.assertEqual(ExpectedResults, ActualResults) 
    
    def test060solveBCwithDaisy(self):
        inputCode = list('rbyybyyowgobbrgogbrrwoggooroggyorwbrgwywywwwogybrwrbby')
        
        ExpectedResults = 'FFURRBBULL'
        
        ActualResults = solve._getBottomCross(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)  
        
    def test070solveBCok(self):
        inputCode = list('gbbgbbgbbrrorrorrobggbggbggroorooroowwywywwwyyywywyyyw')
        
        ExpectedResults = 'LLFFRRBB'
        
        ActualResults = solve._getBottomCross(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
        
    def test070solveBCU(self):
        inputCode = list('bgbbbbbbbrorrrrrrrgbgggggggoroooooooywywywywywywywywyw')
        
        ExpectedResults = 'UULLFFRRBB'
        
        ActualResults = solve._getBottomCross(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
        
    
    def test080solvegetdaisyok(self):
        inputCode = list('bbbbbbbbbrrrrrrrrrgggggggggoooooooooywywywywywywywywyw')
        
        ExpectedResults = 'LLFFRRBB'
        
        ActualResults = solve._getBottomCross(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
        
    def test090bcncTestlf(self):
        inputCode = list('bbyrbbybbrbbrrrrrrrggggggggoowooyoooyyyyyyoogbwwwwwwww')
        
        ExpectedResults =  'lfcorner'
        
        ActualResults = solve._bottomLayerCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults) 
        
    def test090bcncTestrf(self):
        inputCode = list('bbwbbybbbrrygrryrrgrrgggggggooooooooyyoyybyybwwrwwwwww')
        
        ExpectedResults =  'rfcorner'
        
        ActualResults = solve._bottomLayerCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults) 
        
    def test090bcncTestlb(self):
        inputCode = list('boobbbbbbbrrrrrrrrggwggygggooybooyoogyygyyryywwwwwwoww')
        
        ExpectedResults =  'lbcorner'
        
        ActualResults = solve._bottomLayerCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
        
    def test090bcncTestrb(self):
        inputCode = list('obbbbbbbbrrwrryrrrggyoggyggoggoooooobrryyyyyywwwwwwwwg')
        
        ExpectedResults =  'rbcorner'
        
        ActualResults = solve._bottomLayerCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
        
    def test090bcncTestrok(self):
        inputCode = list('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww')
        
        ExpectedResults =  'ok'
        
        ActualResults = solve._bottomLayerCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
        
    def test100ccTestrokful(self):
        inputCode = list('bbwbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyybwwywwwwww')
        inputCorner = 'fur'
        inputColor = 'FDR'
        ExpectedResults =  3
        
        ActualResults = solve._cornerCheck(inputCode, inputCorner,inputColor)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test100ccTestrokfur(self):
        inputCode = list('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww')
        inputCorner = 'fur'
        inputColor = 'FUR'
        ExpectedResults =  3
        
        ActualResults = solve._cornerCheck(inputCode, inputCorner,inputColor)
        self.assertEqual(ExpectedResults, ActualResults)
        
    def test100ccTestrokfdl(self):
        inputCode = list('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww')
        inputCorner = 'fdl'
        inputColor = 'FDL'
        ExpectedResults =  3
        
        ActualResults = solve._cornerCheck(inputCode, inputCorner,inputColor)
        self.assertEqual(ExpectedResults, ActualResults)

    def test100ccTestrokfdr(self):
        inputCode = list('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww')
        inputCorner = 'fdr'
        inputColor = 'FDR'
        ExpectedResults =  3
        
        ActualResults = solve._cornerCheck(inputCode, inputCorner,inputColor)
        self.assertEqual(ExpectedResults, ActualResults)

    def test100ccTestrokbul(self):
        inputCode = list('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww')
        inputCorner = 'bul'
        inputColor = 'BUL'
        ExpectedResults =  3
        
        ActualResults = solve._cornerCheck(inputCode, inputCorner,inputColor)
        self.assertEqual(ExpectedResults, ActualResults)

    def test100ccTestrokbur(self):
        inputCode = list('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww')
        inputCorner = 'bur'
        inputColor = 'BUR'
        ExpectedResults =  3
        
        ActualResults = solve._cornerCheck(inputCode,inputCorner,inputColor)
        self.assertEqual(ExpectedResults, ActualResults)

    def test100ccTestrokbdl(self):
        inputCode = list('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww')
        inputCorner = 'bdl'
        inputColor = 'BDL'
        ExpectedResults =  3
        
        ActualResults = solve._cornerCheck(inputCode, inputCorner,inputColor)
        self.assertEqual(ExpectedResults, ActualResults)

    def test100ccTestrokbdr(self):
        inputCode = list('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww')
        inputCorner = 'bdr'
        inputColor = 'BDR'
        ExpectedResults =  3
        
        ActualResults = solve._cornerCheck(inputCode, inputCorner,inputColor)
        self.assertEqual(ExpectedResults, ActualResults)

    def test105ccTestwrongfdl(self):
        inputCode = list('ybbrbyrboyoogrgbrryrrogogggggrboyoobybgryybyowwwwwwwww')
        inputCorner = 'fdl'
        inputColor = 'FDL'
        ExpectedResults =  -1
        
        ActualResults = solve._cornerCheck(inputCode, inputCorner,inputColor)
        self.assertEqual(ExpectedResults, ActualResults)

    def test105ccTestwrongfdr(self):
        inputCode = list('ybbrbyrboyoogrgbrryrrogogggggrboyoobybgryybyowwwwwwwww')
        inputCorner = 'fdr'
        inputColor = 'FDR'
        ExpectedResults =  -1
        
        ActualResults = solve._cornerCheck(inputCode, inputCorner,inputColor)
        self.assertEqual(ExpectedResults, ActualResults)

    def test105ccTestwrongbdl(self):
        inputCode = list('yoyrbyrbobbrgrbbrgggorgyogrbooboygobyrygyogyrwwwwwwwww')
        inputCorner = 'bdl'
        inputColor = 'BDL'
        ExpectedResults =  -1
        
        ActualResults = solve._cornerCheck(inputCode, inputCorner,inputColor)
        self.assertEqual(ExpectedResults, ActualResults)

    def test105ccTestwrongbdr(self):
        inputCode = list('yoyrbyrbobbrgrbbrgggorgyogrbooboygobyrygyogyrwwwwwwwww')
        inputCorner = 'bdr'
        inputColor = 'BDR'
        ExpectedResults =  -1
        
        ActualResults = solve._cornerCheck(inputCode, inputCorner,inputColor)
        self.assertEqual(ExpectedResults, ActualResults)

    def test110bcrcTestFLU(self):
        inputCode = list('bbyrbbybbrbbrrrrrrrggggggggoowooyoooyyyyyyoogbwwwwwwww')
        inputStatus = 'lfcorner'
        ExpectedResults = 'FUfu'
        
        ActualResults = solve._bottomCornerReadyCheck(inputCode, inputStatus)
        self.assertEqual(ExpectedResults, ActualResults)
        
    def test110bcrcTestFRU(self):
        inputCode = list('bbwbbybbbrrygrryrrgrrgggggggooooooooyyoyybyybwwrwwwwww')
        inputStatus = 'rfcorner'
        ExpectedResults = 'RUru'
        
        ActualResults = solve._bottomCornerReadyCheck(inputCode, inputStatus)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test110bcrcTestBLU(self):
        inputCode = list('boobbbbbbbrrrrrrrrggwggygggooybooyoogyygyyryywwwwwwoww')
        inputStatus = 'lbcorner'
        ExpectedResults = 'LUlu'
        
        ActualResults = solve._bottomCornerReadyCheck(inputCode, inputStatus)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test110bcrcTestBRU(self):
        inputCode = list('obbbbbbbbrrwrryrrrggyoggyggoggoooooobrryyyyyywwwwwwwwg')
        inputStatus = 'rbcorner'
        ExpectedResults = 'BUbu'
        
        ActualResults = solve._bottomCornerReadyCheck(inputCode, inputStatus)
        self.assertEqual(ExpectedResults, ActualResults)
        
    def test110bcrcTestFLD(self):
        inputCode = list('yrybbbobbbbyrrrrrrrggggggggoobooyoowyygyyooyrbwwwwwwww')
        inputStatus = 'lfcorner'
        ExpectedResults = 'FUfu'
        
        ActualResults = solve._bottomCornerReadyCheck(inputCode, inputStatus)
        self.assertEqual(ExpectedResults, ActualResults)
        
    def test110bcrcTestFRD(self):
        inputCode = list('bbwbbybbbrrygrryrrgrrgggggggooooooooyyoyybyybwwrwwwwww')
        inputStatus = 'rfcorner'
        ExpectedResults = 'RUru'
        
        ActualResults = solve._bottomCornerReadyCheck(inputCode, inputStatus)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test110bcrcTestBLD(self):
        inputCode = list('boobbbbbbbrrrrrrrrggwggygggooybooyoogyygyyryywwwwwwoww')
        inputStatus = 'lbcorner'
        ExpectedResults = 'LUlu'
        
        ActualResults = solve._bottomCornerReadyCheck(inputCode, inputStatus)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test110bcrcTestBRD(self):
        inputCode = list('obbbbbbbbrrwrryrrrggyoggyggoggoooooobrryyyyyywwwwwwwwg')
        inputStatus = 'rbcorner'
        ExpectedResults = 'BUbu'
        
        ActualResults = solve._bottomCornerReadyCheck(inputCode, inputStatus)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test110bcrcTestU(self):
        inputCode = list('rrwbbbbbbggyrryrrroggoggyggobbooooooyybyyryyrwwwwwwwwg')
        inputStatus = 'rbcorner'
        ExpectedResults = 'U'
        
        ActualResults = solve._bottomCornerReadyCheck(inputCode, inputStatus)
        self.assertEqual(ExpectedResults, ActualResults)
    '''   
    def test120getSolve(self):
        inputCode = list('gbwrryrrobroggyyggyoyoogoogbrwobgrbbrbgyybryowwbwwwyww')
        
        ExpectedResults = 'UUURUruRUruRUruRUruRUruLUluLUluLUlu'
        
        ActualResults = solve._getSolution(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    '''
    def test131mlcTestFL(self):
        inputCode = list('grgyryrrryrygoyoooogorbbbbbyoyygogggrbbbygrobwwwwwwwww')
        
        ExpectedResults = 'FLEdge'
        
        ActualResults = solve._middleLayerCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)    
        
    def test132mlcTestFR(self):
        inputCode = list('gbrrryrrrorggoyoooyoorbbbbbboyygggggybbyyorgywwwwwwwww')
        
        ExpectedResults = 'FREdge'
        
        ActualResults = solve._middleLayerCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test133mlcTestBL(self):
        inputCode = list('rgorrrrrrbgyooyooorogrbbbbbyogygggggbyobyyybywwwwwwwww')
        
        ExpectedResults = 'BLEdge'
        
        ActualResults = solve._middleLayerCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)  
        
    def test134mlcTestBR(self):
        inputCode = list('yogrrrrrrrobooyoooybgrbbbbbyyoggggggbyogyyrbywwwwwwwww')
        
        ExpectedResults = 'BREdge'
        
        ActualResults = solve._middleLayerCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test135mlcTestOK(self):
        inputCode = list('royrrrrrrbgbooooooyrrbbbbbbobgggggggyyoyyyyygwwwwwwwww')
        
        ExpectedResults = 'ok'
        
        ActualResults = solve._middleLayerCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
        
    def test141mecTestFL(self):
        inputCode = list('gbrrryrrrorggoyoooyoorbbbbbboyygggggybbyyorgywwwwwwwww')
        inputEdge = 'fl'
        inputColor = 'FL'
        
        ExpectedResults =  2
        
        ActualResults = solve._middleEdgeCheck(inputCode, inputEdge,inputColor)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test142mecTestFR(self):
        inputCode = list('royrrrrrrbgbooooooyrrbbbbbbobgggggggyyoyyyyygwwwwwwwww')
        inputEdge = 'fr'
        inputColor = 'FR'
        
        ExpectedResults =  2
        
        ActualResults = solve._middleEdgeCheck(inputCode, inputEdge,inputColor)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test143mecTestBL(self):
        inputCode = list('royrrrrrrbgbooooooyrrbbbbbbobgggggggyyoyyyyygwwwwwwwww')
        inputEdge = 'bl'
        inputColor = 'BL'
        
        ExpectedResults =  2
        
        ActualResults = solve._middleEdgeCheck(inputCode, inputEdge,inputColor)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test144mecTestBR(self):
        inputCode = list('royrrrrrrbgbooooooyrrbbbbbbobgggggggyyoyyyyygwwwwwwwww')
        inputEdge = 'br'
        inputColor = 'BR'
        
        ExpectedResults =  2
        
        ActualResults = solve._middleEdgeCheck(inputCode, inputEdge,inputColor)
        self.assertEqual(ExpectedResults, ActualResults)
        
    def test145mecTestFU(self):
        inputCode = list('rbgbbyoryroogrogoybwowgrrrwybwbooorgggywygbywwgrwwybyb')
        inputEdge = 'fu'
        inputColor = 'FU'
        
        ExpectedResults =  2
        
        ActualResults = solve._middleEdgeCheck(inputCode, inputEdge,inputColor)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test146mecTestRU(self):
        inputCode = list('gborbggggwrrrrwwobybwogwoggrbygowrrwbwbyyyooboorbwyyyy')
        inputEdge = 'ru'
        inputColor = 'RU'
        
        ExpectedResults =  2
        
        ActualResults = solve._middleEdgeCheck(inputCode, inputEdge,inputColor)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test147mecTestBU(self):
        inputCode = list('gborbggggwrrrrgworggowgowbybbywowrrwyyyyyyooboorbwybwb')
        inputEdge = 'bu'
        inputColor = 'BU'
        
        ExpectedResults =  2
        
        ActualResults = solve._middleEdgeCheck(inputCode, inputEdge,inputColor)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test148mecTestLU(self):
        inputCode = list('gboobgobywrrrrgrrwggwwgrgggrowwowybbbyyyyyrobywbywbooo')
        inputEdge = 'lu'
        inputColor = 'LU'
        
        ExpectedResults =  2
        
        ActualResults = solve._middleEdgeCheck(inputCode, inputEdge,inputColor)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test149mecTestFLU(self):
        inputCode = list('yoyyryrrrogyborooogbgybbbbbyyoogggggbgroyrrrbwwwwwwwww')
        inputEdge = 'fl'
        inputColor = 'FL'
        
        ExpectedResults =  -1
        
        ActualResults = solve._middleEdgeCheck(inputCode, inputEdge,inputColor)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test149mecTestFRU(self):
        inputCode = list('yoyyryrrrogyborooogbgybbbbbyyoogggggbgroyrrrbwwwwwwwww')
        inputEdge = 'fr'
        inputColor = 'FR'
        
        ExpectedResults =  -1
        
        ActualResults = solve._middleEdgeCheck(inputCode, inputEdge,inputColor)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test149mecTestBLU(self):
        inputCode = list('yrbyryrrryrggoyooorgorbbbbbyogygogggrbybygboowwwwwwwww')
        inputEdge = 'bl'
        inputColor = 'BL'
        
        ExpectedResults =  -1
        
        ActualResults = solve._middleEdgeCheck(inputCode, inputEdge,inputColor)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test149mecTestBRU(self):
        inputCode = list('yoyyryrrrogyborooogbgybbbbbyyoogggggbgroyrrrbwwwwwwwww')
        inputEdge = 'br'
        inputColor = 'BR'
        
        ExpectedResults =  -1
        
        ActualResults = solve._middleEdgeCheck(inputCode, inputEdge,inputColor)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test150mercTestFLLeftHand(self):
        inputCode = list('rrbgrrrrrgyogoroooygyobbbbboygogbgggbyrbyoyyywwwwwwwww')
        
        ExpectedResults = 'luLUFUfu'
        
        ActualResults = solve._middleEdgeReadyCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
        
    def test150mercTestFLLeftHandU(self):
        inputCode = list('bbogrrrrryoygoroooggbybbbbbgyoogbgggyyroyryyrwwwwwwwww')
        
        ExpectedResults = 'U'
        
        ActualResults = solve._middleEdgeReadyCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test151mercTestFRLeftHand(self):
        inputCode = list('ybyyrrrrrroogooooobygrbbbbbrbgogggggyrygyybyowwwwwwwww')
        
        ExpectedResults = 'fuFURUru'
        
        ActualResults = solve._middleEdgeReadyCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
        
    def test151mercTestFRLeftHandU(self):
        inputCode = list('rooyrrrrrbyggooooorbgrbbbbbybyogggggbgyyyroyywwwwwwwww')
        
        ExpectedResults = 'U'
        
        ActualResults = solve._middleEdgeReadyCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test151mercTestBRLeftHand(self):
        inputCode = list('orgyryrrrryyboooooobgrbbbbbyyrogggggbgbryoygywwwwwwwww')
        
        ExpectedResults = 'ruRUBUbu'
        
        ActualResults = solve._middleEdgeReadyCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test151mercTestBRLeftHandU(self):
        inputCode = list('ryyyryrrrobgboooooyyrrbbbbborgogggggyrbgygyobwwwwwwwww')
        
        ExpectedResults = 'U'
        
        ActualResults = solve._middleEdgeReadyCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test151mercTestBLLeftHand(self):
        inputCode = list('yyoyryrrryoyboroooogyybbbbbgbgogggggrrbgyrborwwwwwwwww')
        
        ExpectedResults = 'buBULUlu'
        
        ActualResults = solve._middleEdgeReadyCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test151mercTestBLLeftHandU(self):
        inputCode = list('yoyyryrrrogyborooogbgybbbbbyyoogggggbgroyrrrbwwwwwwwww')
        
        ExpectedResults = 'U'
        
        ActualResults = solve._middleEdgeReadyCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test151mercTestLeftHandOK(self):
        inputCode = list('ybgyryrrrygyborooorbyybobbbgrbygggggroooyrogbwwwwwwwww')
        
        ExpectedResults = 'ok'
        
        ActualResults = solve._middleEdgeReadyCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test160mmlTestRightHandFL(self):
        inputCode = list('grbyryrrrybgboroooygyybobbbrbyygggggorboygroowwwwwwwww')
        
        ExpectedResults = 'FUfuluLU'
        
        ActualResults = solve._makeMiddleLayer(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
        
    def test160mmlTestRightHandFR(self):
        inputCode = list('rbyrryrrrogyborooogybybobbbgryygggggygroyboobwwwwwwwww')
        
        ExpectedResults = 'RUrufuFU'
        
        ActualResults = solve._makeMiddleLayer(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test160mmlTestRightHandBR(self):
        inputCode = list('yorrrrrrrygyooyooooyygbobbbbyoyggggggbbrybrbgwwwwwwwww')
        
        ExpectedResults = 'BUburuRU'
        
        ActualResults = solve._makeMiddleLayer(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test160mmlTestRightHandBL(self):
        inputCode = list('yoyrrrrrrgbroooooooybbbbbbbgybygggggygyrygoyrwwwwwwwww')
        
        ExpectedResults = 'LUlubuBU'
        
        ActualResults = solve._makeMiddleLayer(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test161mmlTestLeftHandFL(self):
        inputCode = list('goyorgrrrrrbyoyoooybgbbybbbybyrgygggbgooygrrowwwwwwwww')
        
        ExpectedResults = 'luLUFUfu'
        
        ActualResults = solve._makeMiddleLayer(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test161mmlTestLeftHandFR(self):
        inputCode = list('oyyrrgrrrggbyoyooogoybbybbbrbyrgggggoryoybborwwwwwwwww')
        
        ExpectedResults = 'fuFURUru'
        
        ActualResults = solve._makeMiddleLayer(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test161mmlTestLeftHandBR(self):
        inputCode = list('bborrrrrryyyoogooogobbbybbbgborgggggyyroygyyrwwwwwwwww')
        
        ExpectedResults = 'ruRUBUbu'
        
        ActualResults = solve._makeMiddleLayer(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test161mmlTestLeftHandBL(self):
        inputCode = list('ygyrrrrrrgyroooooooobbbybbbgybrgggggyyygybobrwwwwwwwww')
        
        ExpectedResults = 'buBULUlu'
        
        ActualResults = solve._makeMiddleLayer(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test161mmlTestU(self):
        inputCode = list('rybrrrrrryogoooooorybbbbbbbgbyggggggyryyyyogowwwwwwwww')
        
        ExpectedResults = 'U'
        
        ActualResults = solve._makeMiddleLayer(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    '''def test170gmlGetedgereadyRandom(self):  #test input cube has been already solve until the middle layer
        inputCode = list('oryrgygggbygooboooygoobgbbbbbgorgrrryyrrybyyrwwwwwwwww')
        
        ExpectedResults = 'luLUFUfuUruRUBUbuUUbuBULUlu'
        
        ActualResults = solve._getSolution(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test170gmlGetedgereadyFLalready(self):  this just work for the get part of solution
        inputCode = list('rryggogggryyborooogyybbobbboobgrrrrrbgoyybyygwwwwwwwww')
        
        ExpectedResults = 'luLUFUfufuFURUruruRUBUbuUUUbuBULUlu'
        
        ActualResults = solve._getSolution(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
        
    def test170gmlGetedgereadyFRalready(self):
        inputCode = list('yyoggggggyorooboooyyrrbbbbbgyborrrrrygbryyobgwwwwwwwww')
        
        ExpectedResults = 'luLUFUfufuFURUruruRUBUbuUUUbuBULUlu'
        
        ActualResults = solve._getSolution(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
        
    def test170gmlGetedgereadyBRalready(self):
        inputCode = list('bygggggggoyooooooobygbbrbbbygybrrrrrrryyybroywwwwwwwww')
        
        ExpectedResults = 'luLUFUfufuFURUruruRUBUbuUUUbuBULUlu'
        
        ActualResults = solve._getSolution(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
        
    def test170gmlGetedgereadyalready(self):
        inputCode = list('gyyggggggoyyoooooorobbbbbbbrryrrrrrryygyygobbwwwwwwwww')
        
        ExpectedResults = ''
        
        ActualResults = solve._getSolution(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    '''
    
    def test180_TCC_TopCrossalready(self):
        inputCode = list('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww')
        
        ExpectedResults = 4
        
        ActualResults = solve._topCrossCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test180_TCCTopCross_0(self):
        inputCode = list('rybbbbbbbyyyrrrrrrgyrgggggggybooooooyboryoygowwwwwwwww')
        
        ExpectedResults = 0
        
        ActualResults = solve._topCrossCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test180_TCC_TopCross_2(self):#There is no way that the cube have 1 and 3 top color on top edge, it's unsolvable
        inputCode = list('ybrbbbbbbygyrrrrrrryygggggggyboooooooogryyoybwwwwwwwww')
        
        ExpectedResults = 2
        
        ActualResults = solve._topCrossCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)

    def test190_TCS_Line(self):
        inputCode = list('gyybbbbbbgbyrrrrrroyyggggggbgroooooorobyyyyrowwwwwwwww')
        
        ExpectedResults = '-Line'
        
        ActualResults = solve._topCrossStatus(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test190_TCS_1Line(self):
        inputCode = list('gbybbbbbboyyrrrrrrbgrgggggggyyooooooyyrryooybwwwwwwwww')
        
        ExpectedResults = '1Line'
        
        ActualResults = solve._topCrossStatus(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test190_TCS_ΓF(self):
        inputCode = list('ooobbbbbbbgrrrrrrryyyggggggrygoooooogbbryyyyywwwwwwwww')
        
        ExpectedResults = 'ΓFEdge'
        
        ActualResults = solve._topCrossStatus(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test190_TCS_ΓR(self):
        inputCode = list('rygbbbbbbooorrrrrrbgrggggggyyyoooooobyybyygrywwwwwwwww')
        
        ExpectedResults = 'ΓREdge'
        
        ActualResults = solve._topCrossStatus(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test190_TCS_ΓB(self):
        inputCode = list('yyybbbbbbrygrrrrrroooggggggbgrooooooyyyyyrbbgwwwwwwwww')
        
        ExpectedResults = 'ΓBEdge'
        
        ActualResults = solve._topCrossStatus(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test190_TCS_ΓL(self):
        inputCode = list('bgrbbbbbbyyyrrrrrrrygggggggoooooooooyrgyybyybwwwwwwwww')
        
        ExpectedResults = 'ΓLEdge'
        
        ActualResults = solve._topCrossStatus(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test190_TCS_None(self):
        inputCode = list('rybbbbbbbyyyrrrrrrgyrgggggggybooooooyboryoygowwwwwwwww')
        
        ExpectedResults = 'NoEdge'
        
        ActualResults = solve._topCrossStatus(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test200_MTC_Line(self):
        inputCode = '-Line'
        
        ExpectedResults = 'FRUruf'
        
        ActualResults = solve._makeTopCross(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test200_MTC_1Line(self):
        inputCode = '1Line'
        
        ExpectedResults = 'RBUbur'
        
        ActualResults = solve._makeTopCross(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test200_MTC_ΓF(self):
        inputCode = 'ΓFEdge'
        
        ExpectedResults = 'FRUruf'
        
        ActualResults = solve._makeTopCross(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test200_MTC_ΓR(self):
        inputCode = 'ΓREdge'
        
        ExpectedResults = 'RBUbur'
        
        ActualResults = solve._makeTopCross(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test200MTC_ΓB(self):
        inputCode = 'ΓBEdge'
        
        ExpectedResults = 'BLUlub'
        
        ActualResults = solve._makeTopCross(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test200MTC_ΓL(self):
        inputCode = 'ΓLEdge'
        
        ExpectedResults = 'LFUful'
        
        ActualResults = solve._makeTopCross(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test200MTC_None(self):
        inputCode = 'NoEdge'
        
        ExpectedResults = 'FRUruf'
        
        ActualResults = solve._makeTopCross(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    '''
    def test210GTC_Line(self):
        inputCode = list('gyybbbbbbgbyrrrrrroyyggggggbgroooooorobyyyyrowwwwwwwww')
        
        ExpectedResults = 'FRUruf'
        
        ActualResults = solve._getTopFace(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test210GTC_1Line(self):
        inputCode = list('gbybbbbbboyyrrrrrrbgrgggggggyyooooooyyrryooybwwwwwwwww')
        
        ExpectedResults = 'RBUbur'
        
        ActualResults = solve._getTopFace(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test210_GTC_ΓF(self):
        inputCode = list('ooobbbbbbbgrrrrrrryyyggggggrygoooooogbbryyyyywwwwwwwww')
        
        ExpectedResults = 'FRUrufRBUbur'
        
        ActualResults = solve._getTopFace(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test210_GTC_ΓR(self):
        inputCode = list('rygbbbbbbooorrrrrrbgrggggggyyyoooooobyybyygrywwwwwwwww')
        
        ExpectedResults = 'RBUburFRUruf'
        
        ActualResults = solve._getTopFace(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test210_GTC_ΓB(self):
        inputCode = list('yyybbbbbbrygrrrrrroooggggggbgrooooooyyyyyrbbgwwwwwwwww')
        
        ExpectedResults = 'BLUlubRBUbur'
        
        ActualResults = solve._getTopFace(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test210_GTC_ΓL(self):
        inputCode = list('bgrbbbbbbyyyrrrrrrrygggggggoooooooooyrgyybyybwwwwwwwww')
        
        ExpectedResults = 'LFUfulFRUruf'
        
        ActualResults = solve._getTopFace(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test210_GTC_None(self):
        inputCode = list('rybbbbbbbyyyrrrrrrgyrgggggggybooooooyboryoygowwwwwwwww')
        
        ExpectedResults = 'FRUrufFRUrufRBUbur'
        
        ActualResults = solve._getTopFace(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    '''
    
    def test220_TCC_TopCornerNone(self):
        inputCode = list('ygybbbbbbrryrrrrrrgorggggggybboooooobyoyyyoygwwwwwwwww')
        
        ExpectedResults = 0
        
        ActualResults = solve._topCornerCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test220_TCC_TopCornerFRisReady(self):
        inputCode = list('bogbbbbbbygorrrrrryrrggggggybooooooobygyyyyyrwwwwwwwww')
        
        ExpectedResults = 1
        
        ActualResults = solve._topCornerCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test220_TCC_TopCornerFRLareReady(self):
        inputCode = list('gogbbbbbbogrrrrrrrybyggggggorroooooobybyyyyyywwwwwwwww')
        
        ExpectedResults = 2
        
        ActualResults = solve._topCornerCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
        
    #There is no way that the cube have 3 top color on top corner, it's unsolvable
    
    def test220_TCC_TopCornerallreadyareReady(self):
        inputCode = list('rgobbbbbbbbrrrrrrrgogggggggorbooooooyyyyyyyyywwwwwwwww')
        
        ExpectedResults = 4
        
        ActualResults = solve._topCornerCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
        
    def test230_TCS_TopCorner_OnlyFLReady(self):
        inputCode = list('bogbbbbbbygorrrrrryrrggggggybooooooobygyyyyyrwwwwwwwww')
        
        ExpectedResults = 'RSide'
        
        ActualResults = solve._topCornerStatus(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test230_TCS_TopCorner_OnlyFRReady(self):
        inputCode = list('ybobbbbbbbogrrrrrrygoggggggyrroooooogyryyybyywwwwwwwww')
        
        ExpectedResults = 'BSide'
        
        ActualResults = solve._topCornerStatus(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test230_TCS_TopCorner_OnlyBRReady(self):
        inputCode = list('yrrbbbbbbyborrrrrrbogggggggygoooooooryyyyygybwwwwwwwww')
        
        ExpectedResults = 'LSide'
        
        ActualResults = solve._topCornerStatus(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test230_TCS_TopCorner_OnlyBLReady(self):
        inputCode = list('ygobbbbbbyrrrrrrrryboggggggbogooooooyybyyyrygwwwwwwwww')
        
        ExpectedResults = 'FSide'
        
        ActualResults = solve._topCornerStatus(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test230_TCS_TopCorner_2BlockReady_R(self):
        inputCode = list('obgbbbbbbyggrrrrrroobggggggrryooooooyyyyyybyrwwwwwwwww')
        
        ExpectedResults = 'RSide'
        
        ActualResults = solve._topCornerStatus(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test230_TCS_TopCorner_2BlockReady_B(self):
        inputCode = list('bgybbbbbbrrgrrrrrroorggggggybooooooobyyyyyyygwwwwwwwww')
        
        ExpectedResults = 'BSide'
        
        ActualResults = solve._topCornerStatus(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test230_TCS_TopCorner_2BlockReady_L(self):
        inputCode = list('oobbbbbbbrryrrrrrrobgggggggyggoooooorybyyyyyywwwwwwwww')
        
        ExpectedResults = 'LSide'
        
        ActualResults = solve._topCornerStatus(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test230_TCS_TopCorner_2BlockReady_F(self):
        inputCode = list('oorbbbbbbyborrrrrrbgyggggggrrgoooooogyyyyyyybwwwwwwwww')
        
        ExpectedResults = 'FSide'
        
        ActualResults = solve._topCornerStatus(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test230_TCS_TopCorner_NoneReady_F(self):
        inputCode = list('ybobbbbbbygyrrrrrrbryggggggoogoooooobyryyyrygwwwwwwwww')
        
        ExpectedResults = 'FSide'
        
        ActualResults = solve._topCornerStatus(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test240MTC_FSide(self):
        inputCode = 'FSide'
        
        ExpectedResults = 'ruRuruuR'
        
        ActualResults = solve._makeTopCorner(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test240MTC_RSide(self):
        inputCode = 'RSide'
        
        ExpectedResults = 'buBubuuB'
        
        ActualResults = solve._makeTopCorner(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test240MTC_BSide(self):
        inputCode = 'BSide'
        
        ExpectedResults = 'luLuluuL'
        
        ActualResults = solve._makeTopCorner(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test240MTC_LSide(self):
        inputCode = 'LSide'
        
        ExpectedResults = 'fuFufuuF'
        
        ActualResults = solve._makeTopCorner(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
        
    '''Only work for i5
    def test250GTF_CrossAlready_NoCorner(self):
        inputCode = list('ygybbbbbbrryrrrrrrgorggggggybboooooobyoyyyoygwwwwwwwww')
        
        ExpectedResults = 'ruRuruuRfuFufuuF'
        
        ActualResults = solve._getSolution(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test250GTF_CrossAlready_NoCorner2(self):
        inputCode = list('gorbbbbbbybbrrrrrrygyggggggrryoooooogyoyyyoybwwwwwwwww')
        
        ExpectedResults = 'ruRuruuRluLuluuLbuBubuuBfuFufuuF'
        
        ActualResults = solve._getSolution(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test250GTF_CrossAlready_NoCorner3(self):
        inputCode = list('rrybbbbbbgorrrrrrrybbggggggygyoooooooybyyygyowwwwwwwww')
        
        ExpectedResults = 'ruRuruuRbuBubuuB'
        
        ActualResults = solve._getSolution(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
        
    def test250GTF_CrossAlready_NoCorner4(self):
        inputCode = list('ybbbbbbbbygyrrrrrrrrygggggggoroooooooygyyybyowwwwwwwww')
        
        ExpectedResults = 'ruRuruuRluLuluuLfuFufuuFbuBubuuB'
        
        ActualResults = solve._getSolution(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    '''
    
    def test260_CBC_FnotBound(self):
        inputCode = list('rorrrrrrryroyyyyyywwyoooooooywwwwwwwbbbbbbbbbggggggggg')
        
        ExpectedResults = 'Fside'
        
        ActualResults = solve._cornerBoundCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test260_CBC_RnotBound(self):
        inputCode = list('oywrrrrrrroryyyyyyyrooooooowwywwwwwwbbbbbbbbbggggggggg')
        
        ExpectedResults = 'Rside'
        
        ActualResults = solve._cornerBoundCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test260_CBC_BnotBound(self):
        inputCode = list('wwyrrrrrroywyyyyyyrorooooooyrowwwwwwbbbbbbbbbggggggggg')
        
        ExpectedResults = 'Bside'
        
        ActualResults = solve._cornerBoundCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test260_CBC_LnotBound(self):
        inputCode = list('wgrwwwwwwgrwrrrrrrrwgggggggooooooooobbbbbbbbbyyyyyyyyy')
        
        ExpectedResults = 'Lside'
        
        ActualResults = solve._cornerBoundCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test260_CBC_NoneBound(self):
        inputCode = list('yrryyyyyywybbbbbbbrwyrrrrrrbbwwwwwwwoooooooooggggggggg')
        
        ExpectedResults = 'Fside'
        
        ActualResults = solve._cornerBoundCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
        
    def test260_CBC_ok(self):
        inputCode = list('boboooooowbwggggggowobbbbbbgggwwwwwwrrrrrrrrryyyyyyyyy')
        
        ExpectedResults = 'ok'
        
        ActualResults = solve._cornerBoundCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test260_MRB_FSide(self):
        inputCode = 'Fside'
        
        ExpectedResults = 'RbRffrBRffrr'
        
        ActualResults = solve._makeRightBound(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test260_MRB_RSide(self):
        inputCode = 'Rside'
        
        ExpectedResults = 'BlBrrbLBrrbb'
        
        ActualResults = solve._makeRightBound(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test260_MRB_BSide(self):
        inputCode = 'Bside'
        
        ExpectedResults = 'LfLbblFLbbll'
        
        ActualResults = solve._makeRightBound(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test260_MRB_LSide(self):
        inputCode = 'Lside'
        
        ExpectedResults = 'FrFllfRFllff'
        
        ActualResults = solve._makeRightBound(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test270_CEC_FUL(self):
        inputCode = list('obbbbbbbbrrorrrrrrbgrgggggggogooooooyyyyyyyyywwwwwwwww')
        
        ExpectedResults = 'notok'
        
        ActualResults = solve._cornerEdgeCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test270_CEC_FUR(self):
        inputCode = list('bbgbbbbbborbrrrrrrrgrgggggggooooooooyyyyyyyyywwwwwwwww')
        
        ExpectedResults = 'notok'
        
        ActualResults = solve._cornerEdgeCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test270_CEC_BUR(self):
        inputCode = list('bbgbbbbbborbrrrrrrrgrgggggggooooooooyyyyyyyyywwwwwwwww')
        
        ExpectedResults = 'notok'
        
        ActualResults = solve._cornerEdgeCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test270_CEC_BUL(self):
        inputCode = list('bbgbbbbbborbrrrrrrrgrgggggggooooooooyyyyyyyyywwwwwwwww')
        
        ExpectedResults = 'notok'
        
        ActualResults = solve._cornerEdgeCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test270_CEC_ok(self):
        inputCode = list('ogooooooogogggggggbwbbbbbbbwbwwwwwwwrrrrrrrrryyyyyyyyy')
        
        ExpectedResults = 'ok'
        
        ActualResults = solve._cornerEdgeCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test280_EEC_Fedge(self):
        inputCode = list('ooooooooogbgggggggbwbbbbbbbwgwwwwwwwrrrrrrrrryyyyyyyyy')
        
        ExpectedResults = 'Fedge'
        
        ActualResults = solve._edgeEdgeCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test280_EEC_Redge(self):
        inputCode = list('owooooooogggggggggbobbbbbbbwbwwwwwwwrrrrrrrrryyyyyyyyy')
        
        ExpectedResults = 'Redge'
        
        ActualResults = solve._edgeEdgeCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test280_EEC_Bedge(self):
        inputCode = list('owooooooogogggggggbbbbbbbbbwgwwwwwwwrrrrrrrrryyyyyyyyy')
        
        ExpectedResults = 'Bedge'
        
        ActualResults = solve._edgeEdgeCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test280_EEC_Ledge(self):
        inputCode = list('ogooooooogbgggggggbobbbbbbbwwwwwwwwwrrrrrrrrryyyyyyyyy')
        
        ExpectedResults = 'Ledge'
        
        ActualResults = solve._edgeEdgeCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test280_EEC_Noneedge(self):
        inputCode = list('ogooooooogogggggggbwbbbbbbbwbwwwwwwwrrrrrrrrryyyyyyyyy')
        
        ExpectedResults = 'Fedge'
        
        ActualResults = solve._edgeEdgeCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test280_EEC_ok(self):
        inputCode = list('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww')
        
        ExpectedResults = 'ok'
        
        ActualResults = solve._edgeEdgeCheck(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test290_MRE_Fedge(self):
        inputCode = 'Fedge'
        
        ExpectedResults = 'rUrururURUrr'
        
        ActualResults = solve._makeEdgeColor(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test290_MRE_Redge(self):
        inputCode = 'Redge'
        
        ExpectedResults = 'bUbububUBUbb'
        
        ActualResults = solve._makeEdgeColor(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test290_MRE_Bedge(self):
        inputCode = 'Bedge'
        
        ExpectedResults = 'lUlululULUll'
        
        ActualResults = solve._makeEdgeColor(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test290_MRE_Ledge(self):
        inputCode = 'Ledge'
        
        ExpectedResults = 'fUfufufUFUff'
        
        ActualResults = solve._makeEdgeColor(inputCode)
        self.assertEqual(ExpectedResults, ActualResults)
    
    def test300_Token_(self):
        inputCube = 'bobbbbbbbrbrrrrrrrgggggggggoroooooooyyyyyyyyywwwwwwwww'
        inputSolution = 'lUlululULUll'
        ExpectRange = '0d7063de88030411692ebf07c95dfa5aab44d67bf553462ca0305ce11111ee08'
        
        ActualResults = solve._getToken(inputCube, inputSolution)
        self.assertIn(ActualResults, ExpectRange)
        