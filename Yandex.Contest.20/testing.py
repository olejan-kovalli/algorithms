import time

class Tester:
    """
    parser func should return (inp, outp)
    inp should be a tuple of all input parameters
    """
    def __init__(self, parser_func, target_func):
        self.parser_func = parser_func
        self.target_func = target_func

    def test(self, case):
        inp, expected = self.parser_func(case)

        actual = self.target_func(*inp)
        
        if actual == expected:
            print('pass')
        else:
            print('fail')
            
        print('\texpected ', expected)
        print('\tactual   ', actual)
    
    def test_big_case(self, case):
        start = time.process_time()
        self.test(case)
        print('%0.2f sec' % ( time.process_time() - start))