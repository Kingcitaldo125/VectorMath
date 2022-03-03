from vecthree import vecthree as v3

def test_add_pass1():
    assert v3.add([1,2,3],[4,5,6]) == [5,7,9]
    assert v3.add([-1,2,3],[4,5,6]) == [3,7,9]
    assert v3.add([1,-2,3],[4,5,6]) == [5,3,9]
    assert v3.add([1,2,-3],[4,5,6]) == [5,7,3]
    assert v3.add([-1,-2,-3],[4,5,6]) == [3,3,3]
    assert v3.add([1,2,3],[-4,5,6]) == [-3,7,9]
    assert v3.add([1,2,3],[4,-5,6]) == [5,-3,9]
    assert v3.add([1,2,3],[4,5,-6]) == [5,7,-3]

def test_add_pass2():
    assert v3.add([0,0,0],[1,2,3]) == [1,2,3]
    assert v3.add([1,2,3],[0,0,0]) == [1,2,3]
    assert v3.add([-0,-0,-0],[1,2,3]) == [1,2,3]
    assert v3.add([1,2,3],[-0,-0,-0]) == [1,2,3]

def test_add_pass3():
    assert v3.add([0.1,0.5,0.9],[1,2,3]) == [1.1,2.5,3.9]
    assert v3.add([-0.1,0.5,0.9],[1,2,3]) == [0.9,2.5,3.9]
    assert v3.add([0.1,-0.5,0.9],[1,2,3]) == [1.1,1.5,3.9]
    assert v3.add([0.1,0.5,-0.9],[1,2,3]) == [1.1,2.5,2.1]
    assert v3.add([1,2,3],[0.1,0.5,0.9]) == [1.1,2.5,3.9]
    assert v3.add([1,2,3],[-0.1,0.5,0.9]) == [0.9,2.5,3.9]
    assert v3.add([1,2,3],[0.1,-0.5,0.9]) == [1.1,1.5,3.9]
    assert v3.add([1,2,3],[0.1,0.5,-0.9]) == [1.1,2.5,2.1]

def test_sub_pass1():
    assert v3.sub([11,22,33],[4,5,6]) == [7,17,27]
    assert v3.sub([-11,22,33],[4,5,6]) == [-15,17,27]
    assert v3.sub([11,-22,33],[4,5,6]) == [7,-27,27]
    assert v3.sub([11,22,-33],[4,5,6]) == [7,17,-39]
    assert v3.sub([-11,-22,-33],[4,5,6]) == [-15,-27,-39]
    assert v3.sub([11,22,33],[-4,5,6]) == [15,17,27]
    assert v3.sub([11,22,33],[4,-5,6]) == [7,27,27]
    assert v3.sub([11,22,33],[4,5,-6]) == [7,17,39]

def test_sub_pass2():
    assert v3.sub([0,0,0],[1,2,3]) == [-1,-2,-3]
    assert v3.sub([1,2,3],[0,0,0]) == [1,2,3]
    assert v3.sub([-0,-0,-0],[1,2,3]) == [-1,-2,-3]
    assert v3.sub([1,2,3],[-0,-0,-0]) == [1,2,3]

def test_sub_pass3():
    assert v3.sub([0.1,0.5,0.9],[1,2,3]) == [-0.9,-1.5,-2.1]
    assert v3.sub([-0.1,0.5,0.9],[1,2,3]) == [-1.1,-1.5,-2.1]
    assert v3.sub([0.1,-0.5,0.9],[1,2,3]) == [-0.9,-2.5,-2.1]
    assert v3.sub([0.1,0.5,-0.9],[1,2,3]) == [-0.9,-1.5,-3.9]
    assert v3.sub([1,2,3],[0.1,0.5,0.9]) == [0.9,1.5,2.1]
    assert v3.sub([1,2,3],[-0.1,0.5,0.9]) == [1.1,1.5,2.1]
    assert v3.sub([1,2,3],[0.1,-0.5,0.9]) == [0.9,2.5,2.1]
    assert v3.sub([1,2,3],[0.1,0.5,-0.9]) == [0.9,1.5,3.9]

def test_scale_pass1():
    assert v3.scale([0,0,0],1) == [0,0,0]
    assert v3.scale([0,1,0],1) == [0,1,0]
    assert v3.scale([0,0,1],1) == [0,0,1]
    assert v3.scale([0,1,1],1) == [0,1,1]
    assert v3.scale([1,0,0],1) == [1,0,0]
    assert v3.scale([1,1,0],1) == [1,1,0]
    assert v3.scale([1,0,1],1) == [1,0,1]
    assert v3.scale([1,1,1],1) == [1,1,1]

def test_scale_pass2():
    assert v3.scale([0,0,0],2) == [0,0,0]
    assert v3.scale([0,1,0],2) == [0,2,0]
    assert v3.scale([0,0,1],2) == [0,0,2]
    assert v3.scale([0,1,1],2) == [0,2,2]
    assert v3.scale([1,0,0],2) == [2,0,0]
    assert v3.scale([1,1,0],2) == [2,2,0]
    assert v3.scale([1,0,1],2) == [2,0,2]
    assert v3.scale([1,1,1],2) == [2,2,2]

def test_scale_pass3():
    assert v3.scale([0,0,0],-1) == [0,0,0]
    assert v3.scale([0,1,0],-1) == [0,-1,0]
    assert v3.scale([0,0,1],-1) == [0,0,-1]
    assert v3.scale([0,1,1],-1) == [0,-1,-1]
    assert v3.scale([1,0,0],-1) == [-1,0,0]
    assert v3.scale([1,1,0],-1) == [-1,-1,0]
    assert v3.scale([1,0,1],-1) == [-1,0,-1]
    assert v3.scale([1,1,1],-1) == [-1,-1,-1]

def test_scale_pass4():
    assert v3.scale([10,5,2],2) == [20,10,4]
    assert v3.scale([10,5,2],1) == [10,5,2]
    assert v3.scale([10,5,2],0.5) == [5,2.5,1]
    assert v3.scale([10,5,2],-2) == [-20,-10,-4]
    assert v3.scale([10,5,2],-1) == [-10,-5,-2]
    assert v3.scale([10,5,2],-0.5) == [-5,-2.5,-1]
    assert v3.scale([-10,-5,-2],2) == [-20,-10,-4]
    assert v3.scale([-10,-5,-2],1) == [-10,-5,-2]
    assert v3.scale([-10,-5,-2],0.5) == [-5,-2.5,-1]
    assert v3.scale([-10,-5,-2],-2) == [20,10,4]
    assert v3.scale([-10,-5,-2],-1) == [10,5,2]
    assert v3.scale([-10,-5,-2],-0.5) == [5,2.5,1]

def test_magnitude_pass():
    assert v3.magnitude([1,0,0]) == 1
    assert v3.magnitude([0,1,0]) == 1
    assert v3.magnitude([0,0,1]) == 1
    assert v3.magnitude([1,4,8]) == 9
    assert v3.magnitude([4,1,8]) == 9
    assert v3.magnitude([4,8,1]) == 9
    assert v3.magnitude([1,8,4]) == 9
    assert v3.magnitude([8,1,4]) == 9
    assert v3.magnitude([8,4,1]) == 9
    assert v3.magnitude([3,4,12]) == 13
    assert v3.magnitude([4,3,12]) == 13
    assert v3.magnitude([3,12,4]) == 13
    assert v3.magnitude([4,12,3]) == 13
    assert v3.magnitude([12,3,4]) == 13
    assert v3.magnitude([12,4,3]) == 13

def test_normalize_pass():
    assert v3.magnitude(v3.normalize([1,0,0])) <= 1
    assert v3.magnitude(v3.normalize([0,1,0])) <= 1
    assert v3.magnitude(v3.normalize([0,0,1])) <= 1
    assert v3.magnitude(v3.normalize([1,1,1])) <= 1
    assert v3.magnitude(v3.normalize([1,2,3])) <= 1
    assert v3.magnitude(v3.normalize([5,5,5])) <= 1
    assert v3.magnitude(v3.normalize([-1,-1,-1])) <= 1
    assert v3.magnitude(v3.normalize([1,-1,-1])) <= 1
    assert v3.magnitude(v3.normalize([-1,-1,1])) <= 1
    assert v3.magnitude(v3.normalize([-1,1,1])) <= 1
    assert v3.magnitude(v3.normalize([1,1,-1])) <= 1
    assert v3.magnitude(v3.normalize([-1,1,-1])) <= 1
    assert v3.magnitude(v3.normalize([1,-1,1])) <= 1
    assert v3.magnitude(v3.normalize([-1,-2,-3])) <= 1
    assert v3.magnitude(v3.normalize([-5,-5,-5])) <= 1

def test_dot_pass_one():
    '''
    Unit vector permutation calculations
    '''
    assert v3.dot([1,0,0],[-1,0,0]) == -1
    assert v3.dot([0,1,0],[0,-1,0]) == -1
    assert v3.dot([0,0,1],[0,0,-1]) == -1
    assert v3.dot([-1,1,1],[1,1,-1]) == -1
    assert v3.dot([0,0,0],[0,0,0]) == 0
    assert v3.dot([1,0,0],[0,0,1]) == 0
    assert v3.dot([1,0,0],[0,0,-1]) == 0
    assert v3.dot([1,0,0],[1,0,0]) == 1
    assert v3.dot([0,1,0],[0,1,0]) == 1
    assert v3.dot([1,-1,1],[1,1,1]) == 1
    assert v3.dot([1,1,1],[1,-1,1]) == 1
    assert v3.dot([-1,1,1],[1,1,1]) == 1
    assert v3.dot([1,1,1],[-1,1,1]) == 1
    assert v3.dot([1,1,1],[1,1,1]) == 3
    assert v3.dot([-1,-1,-1],[-1,-1,-1]) == 3
    assert v3.dot([-1,1,-1],[-1,1,-1]) == 3
    assert v3.dot([1,-1,1],[1,-1,1]) == 3

def test_dot_pass_two():
    '''
    Random dot product calculations
    '''
    assert v3.dot([1234,5,90],[45,77,63]) == 61585
    assert v3.dot([-5,70,7],[100,-90,555]) == -2915
    assert v3.dot([-900,-456,-2],[-2,-456,-900]) == 211536
