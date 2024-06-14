from display_header import display_header

def test_display_header(capfd):
    # Call the function
    display_header()
    
    # Capture the output
    captured = capfd.readouterr()
    
    # Define the expected header
    expected_header = r"""
    
    
    

   /$$$$$$            /$$                               /$$            /$$$$$$  /$$$$$$
 /$$__  $$          | $$                              | $$           /$$__  $$|_  $$_/
| $$  \__/  /$$$$$$ | $$  /$$$$$$   /$$$$$$   /$$$$$$$| $$$$$$$     | $$  \ $$  | $$  
|  $$$$$$  /$$__  $$| $$ /$$__  $$ /$$__  $$ /$$_____/| $$__  $$    | $$$$$$$$  | $$  
 \____  $$| $$  \ $$| $$| $$  \ $$| $$  \ $$|  $$$$$$ | $$  \ $$    | $$__  $$  | $$  
 /$$  \ $$| $$  | $$| $$| $$  | $$| $$  | $$ \____  $$| $$  | $$    | $$  | $$  | $$  
|  $$$$$$/| $$$$$$$/| $$|  $$$$$$/|  $$$$$$/ /$$$$$$$/| $$  | $$ /$$| $$  | $$ /$$$$$$
 \______/ | $$____/ |__/ \______/  \______/ |_______/ |__/  |__/|__/|__/  |__/|______/
          | $$                                                                        
          | $$                                                                        
          |__/                                                                                                                                                                

     
    
    

     
    """
    
    # Assert the printed output matches the expected header
    assert captured.out.strip() == expected_header.strip()