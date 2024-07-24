def sample_responses(input_text):
    user_msg= str(input_text).lower()
    
    if user_msg in ("hello","hi","alo",):
        return 'Wassup'
    if user_msg in ("what are you","who are you"):
        return 'Im the bank bot'
    if user_msg in("ngu", "bot ngu"):
        return "co m ngu dcmm"
    return 'dcmm'
