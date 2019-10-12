from solutions.CHK import checkout

class TestCheckout():
    def test_negative_case(offers):
        items = "A,B,F,G"
        assert checkout(items) == -1
    
    def test_pos_case(offers):
        items = "A,B,C"
        assert checkout(items) == 100
    
    def test_offer_case(offers):
        items = "A,B,C,A,A"
        assert checkout(items) == 180
