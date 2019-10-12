from solutions.CHK import checkout

class TestCheckout():
    def test_negative_case():
        items = "A,B,F,G"
        assert checkout(items) == -1
    
    def test_pos_case():
        items = "A,B,C"
        assert checkout(items) == 100
    
    def test_offer_case():
        items = "A,B,C,A,A"
        assert checkout(items) == 180
