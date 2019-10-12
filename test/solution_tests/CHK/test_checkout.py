from solutions.CHK import checkout

class TestCheckout():

    def test_negative_case(offers):
        items = "A,B,F,G"
        result = checkout(items)
        assert result == -1