import unittest
import rubik.rotate as rotate

class rotateTest(unittest.TestCase):
    
    
    def test010cubeisnone(self):
        inputcode = {}
        inputcode = list('n')
        
        ExpectedResults = {}
        ExpectedResults['status'] = 'error: Cube is missing'
        
        ActualResults = rotate._checkCube(inputcode)
        self.assertEqual(ExpectedResults['status'], ActualResults['status'])

    def test020cubeistoolong(self):
        inputcode = {}
        inputcode = list('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwwb')
        
        ExpectedResults = {}
        ExpectedResults['status'] = 'error: Invalid size'
        
        ActualResults = rotate._checkCube(inputcode)
        self.assertEqual(ExpectedResults['status'], ActualResults['status']) 
         
    def test025cubeistooshort(self):
        inputcode = {}
        inputcode = 'bbbbbbbbb'
        
        ExpectedResults = {}
        ExpectedResults['status'] = 'error: Invalid size'
        
        ActualResults = rotate._checkCube(inputcode)
        self.assertEqual(ExpectedResults['status'], ActualResults['status'])
        
    def test030cubehasinvalidcharacters(self):
        inputcode = {}
        inputcode = list('bbbbbbbbbrrrrrrrrr666666666oooooooooyyyyyyyyywwwwwwwww')
        
        ExpectedResults = {}
        ExpectedResults['status'] = 'error: invalid cube characters'
        
        ActualResults = rotate._checkCube(inputcode)
        self.assertEqual(ExpectedResults['status'], ActualResults['status'])  
        
    def test035cubehasinvalidcenter(self):
        inputcode = {}
        inputcode = list('rbbbbbbbbrrrrbrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww')
        
        ExpectedResults = {}
        ExpectedResults['status'] = 'error: invalid centers'
        
        ActualResults = rotate._checkCube(inputcode)
        self.assertEqual(ExpectedResults['status'], ActualResults['status'])  
    
    def test035cubehasinvalidcolor(self):
        inputcode = {}
        inputcode = list('bbbbbbbbbrrrrrrrrr666666666oooooooooyyyyyyyyywwwwwwwww')
        
        ExpectedResults = {}
        ExpectedResults['status'] = 'error: invalid cube characters'
        
        ActualResults = rotate._checkCube(inputcode)
        self.assertEqual(ExpectedResults['status'], ActualResults['status'])  

    def test040dirhasinvalidcharacts(self):
        inputcode = {}
        inputcode['op'] = 'rotate'
        inputcode['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwb'
        inputcode['dir'] = 'x'
        
        ExpectedResults = {}
        ExpectedResults['status'] = 'error: invalid dir characters'
        
        ActualResults = rotate._checkDir(inputcode)
        self.assertEqual(ExpectedResults['status'], ActualResults['status'])  
        
    def test045dirhasinvalidcharacts(self):
        inputcode = {}
        inputcode['op'] = 'rotate'
        inputcode['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwb'
        inputcode['dir'] = 'FF FF'
        
        ExpectedResults = {}
        ExpectedResults['status'] = 'error: invalid dir characters'
        
        ActualResults = rotate._checkDir(inputcode)
        self.assertEqual(ExpectedResults['status'], ActualResults['status'])  

    def test050rotateoutcome(self):
        inputcode = {}
        inputcode['op'] = 'rotate'
        inputcode['cube'] = 'goywrbbgorbggybwbrwroygrwwgbwbyogwoorwyywoyrbgyrgbrooy'
        inputcode['dir'] = 'F'
        
        ExpectedResults = {}
        ExpectedResults['status'] = 'ok'
        
        ActualResults = rotate._rotate(inputcode)
        self.assertEqual(ExpectedResults['status'], ActualResults['status'])
        
    def test060rotateF(self):
        inputcode = {}
        inputcode['op'] = 'rotate'
        inputcode['cube'] = 'oywyywyoorbgggyyobbgybrgrrbbwwyowowworyrbgroggrwowbrbg'
        inputcode['dir'] = 'F'
        
        ExpectedResults = {}
        ExpectedResults['status'] = 'ok'
        ExpectedResults['cube'] = 'yyooyyowwrbgogygobbgybrgrrbbwgyorowworyrbgwwwygrowbrbg'
        
        ActualResults = rotate._rotate(inputcode)
        self.assertEqual(ExpectedResults['cube'], ActualResults['cube'])   
        self.assertEqual(ExpectedResults['status'], ActualResults['status'])    

    def test065rotatef(self):
        inputcode = {}
        inputcode['op'] = 'rotate'
        inputcode['cube'] = 'yrooyoggbrrwywygryogrbrobwwoggwbbgbrwryyobbwbwwrggoyyo'
        inputcode['dir'] = 'f'
        
        ExpectedResults = {}
        ExpectedResults['status'] = 'ok'
        ExpectedResults['cube'] = 'oobrygyogrrwwwywryogrbrobwwogbwbwgbbwryyobryggbrggoyyo'
        
        ActualResults = rotate._rotate(inputcode)
        self.assertEqual(ExpectedResults['cube'], ActualResults['cube'])   
        self.assertEqual(ExpectedResults['status'], ActualResults['status'])  
        
    def test060rotateB(self):
        inputcode = {}
        inputcode['op'] = 'rotate'
        inputcode['cube'] = 'ooworggrbrgowyrwwbryogbogwrbobbgyyyrgbygobyrgowyrwywbw'
        inputcode['dir'] = 'B'
        
        ExpectedResults = {}
        ExpectedResults['status'] = 'ok'
        ExpectedResults['cube'] = 'ooworggrbrgwwybwwwggrwbyrooyobbgygyrorbgobyrgowyrwybby'
        
        ActualResults = rotate._rotate(inputcode)
        self.assertEqual(ExpectedResults['cube'], ActualResults['cube'])   
        self.assertEqual(ExpectedResults['status'], ActualResults['status'])
        
    def test060rotateb(self):
        inputcode = {}
        inputcode['op'] = 'rotate'
        inputcode['cube'] = 'wbwgrogrrobywoyygyorybbwrrwbgbrgyoowgobbywgorryoywwbgg'
        inputcode['dir'] = 'b'
        
        ExpectedResults = {}
        ExpectedResults['status'] = 'ok'
        ExpectedResults['cube'] = 'wbwgrogrrobgwooygbywwrbrobrbgbggygoworbbywgorryoywwyyy'
        
        ActualResults = rotate._rotate(inputcode)
        self.assertEqual(ExpectedResults['cube'], ActualResults['cube'])   
        self.assertEqual(ExpectedResults['status'], ActualResults['status'])
        
    
    def test060rotateU(self):
        inputcode = {}
        inputcode['op'] = 'rotate'
        inputcode['cube'] = 'ryrggrbbbgywobwoggrgbboywogoworrwyrgyrooyoybywgwwwybbr'
        inputcode['dir'] = 'U'
        
        ExpectedResults = {}
        ExpectedResults['status'] = 'ok'
        ExpectedResults['cube'] = 'gywggrbbbrgbobwoggowoboywogryrrrwyrgyoybyryoowgwwwybbr'
        
        ActualResults = rotate._rotate(inputcode)
        self.assertEqual(ExpectedResults['cube'], ActualResults['cube'])   
        self.assertEqual(ExpectedResults['status'], ActualResults['status']) 
    
    
    def test060rotateu(self):
        inputcode = {}
        inputcode['op'] = 'rotate'
        inputcode['cube'] = 'gywggrbbbrgbobwoggowoboywogryrrrwyrgyoybyryoowgwwwybbr'
        inputcode['dir'] = 'u'
        
        ExpectedResults = {}
        ExpectedResults['status'] = 'ok'
        ExpectedResults['cube'] = 'ryrggrbbbgywobwoggrgbboywogoworrwyrgyrooyoybywgwwwybbr'
        
        ActualResults = rotate._rotate(inputcode)
        self.assertEqual(ExpectedResults['cube'], ActualResults['cube'])   
        self.assertEqual(ExpectedResults['status'], ActualResults['status']) 
        
    def test060rotateD(self):
        inputcode = {}
        inputcode['op'] = 'rotate'
        inputcode['cube'] = 'wgyrwywyybooogbowyrwggyobgwyobrryorborwwogryrgbrbbbgwg'
        inputcode['dir'] = 'D'
        
        ExpectedResults = {}
        ExpectedResults['status'] = 'ok'
        ExpectedResults['cube'] = 'wgyrwyorbbooogbwyyrwggyoowyyobrrybgworwwogryrgbgwbbgbr'
        
        ActualResults = rotate._rotate(inputcode)
        self.assertEqual(ExpectedResults['cube'], ActualResults['cube'])   
        self.assertEqual(ExpectedResults['status'], ActualResults['status'])
        
    def test060rotated(self):
        inputcode = {}
        inputcode['op'] = 'rotate'
        inputcode['cube'] = 'woogbbggoyrrwrobgywrgygobyyrybbywgrwowbbwbyggryroorwwo'
        inputcode['dir'] = 'd'
        
        ExpectedResults = {}
        ExpectedResults['status'] = 'ok'
        ExpectedResults['cube'] = 'woogbbbgyyrrwrobyywrgygogrwrybbywggoowbbwbyggrroyowrow'
        
        ActualResults = rotate._rotate(inputcode)
        self.assertEqual(ExpectedResults['cube'], ActualResults['cube'])   
        self.assertEqual(ExpectedResults['status'], ActualResults['status']) 
        
    def test060rotateR(self):
        inputcode = {}
        inputcode['op'] = 'rotate'
        inputcode['cube'] = 'yroryrbyrbbyyrwooywwobooggogrwbbgboyryrwggboggbwgwwwyr'
        inputcode['dir'] = 'R'
        
        ExpectedResults = {}
        ExpectedResults['status'] = 'ok'
        ExpectedResults['cube'] = 'yrwrywbyroyborbywygwogoorgogrwbbgboyryowgrborgbggwbwyw'
        
        ActualResults = rotate._rotate(inputcode)
        self.assertEqual(ExpectedResults['cube'], ActualResults['cube'])   
        self.assertEqual(ExpectedResults['status'], ActualResults['status'])
        
    def test060rotater(self):
        inputcode = {}
        inputcode['op'] = 'rotate'
        inputcode['cube'] = 'gbbwyoygbwgbrrbwgrggrwbyorogoywworywyrrbgbwrgoyooowbyy'
        inputcode['dir'] = 'r'
        
        ExpectedResults = {}
        ExpectedResults['status'] = 'ok'
        ExpectedResults['cube'] = 'gbrwybyggbbrgrgwrwygrwbyorogoywworywyrobgwwrgoybooobyb'
        
        ActualResults = rotate._rotate(inputcode)
        self.assertEqual(ExpectedResults['cube'], ActualResults['cube'])   
        self.assertEqual(ExpectedResults['status'], ActualResults['status']) 
    
    def test060rotateL(self):
        inputcode = {}
        inputcode['op'] = 'rotate'
        inputcode['cube'] = 'wobobowyowgywywwborrbgowgoygboygyrybrgowwbyggybgrrrbrr'
        inputcode['dir'] = 'L'
        
        ExpectedResults = {}
        ExpectedResults['status'] = 'ok'
        ExpectedResults['cube'] = 'robwboyyowgywywwborrbgorgoyrygygbbyoygowwbbggwbgorrwrr'
        
        ActualResults = rotate._rotate(inputcode)
        self.assertEqual(ExpectedResults['cube'], ActualResults['cube'])   
        self.assertEqual(ExpectedResults['status'], ActualResults['status'])
        
    def test060rotatel(self):
        inputcode = {}
        inputcode['op'] = 'rotate'
        inputcode['cube'] = 'wrryrwboywgygobooyobgyywggbbygrgoorgyrwwbbrgorwbowbryw'
        inputcode['dir'] = 'l'
        
        ExpectedResults = {}
        ExpectedResults['status'] = 'ok'
        ExpectedResults['cube'] = 'rrrorwroywgygobooyobryywggygogygrbrowrwybbbgobwbwwbgyw'
        
        ActualResults = rotate._rotate(inputcode)
        self.assertEqual(ExpectedResults['cube'], ActualResults['cube'])   
        self.assertEqual(ExpectedResults['status'], ActualResults['status'])
        
    def test060rotatemany(self):
        inputcode = {}
        inputcode['op'] = 'rotate'
        inputcode['cube'] = 'bbbyybybryggyggwboygoyrwgowgrrrbwrobrrwoowooowwggwrbyy'
        inputcode['dir'] = 'LRFULFBLLRFRBFFbDRRlrbRLb'
        
        ExpectedResults = {}
        ExpectedResults['status'] = 'ok'
        ExpectedResults['cube'] = 'wyboyyooorrybgwggobrbbrrybyorgobygygrbwgowrgwrgywwwwob'
        
        ActualResults = rotate._rotate(inputcode)
        self.assertEqual(ExpectedResults['cube'], ActualResults['cube'])   
        self.assertEqual(ExpectedResults['status'], ActualResults['status'])  
        
    def test060rotatempty(self):
        inputcode = {}
        inputcode['op'] = 'rotate'
        inputcode['cube'] = 'oywyywyoorbgggyyobbgybrgrrbbwwyowowworyrbgroggrwowbrbg'
        inputcode['dir'] = ''
        
        ExpectedResults = {}
        ExpectedResults['status'] = 'ok'
        ExpectedResults['cube'] = 'yyooyyowwrbgogygobbgybrgrrbbwgyorowworyrbgwwwygrowbrbg'
        
        ActualResults = rotate._rotate(inputcode)
        self.assertEqual(ExpectedResults['cube'], ActualResults['cube'])   
        self.assertEqual(ExpectedResults['status'], ActualResults['status'])  