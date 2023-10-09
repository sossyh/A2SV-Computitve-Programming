class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        requirments = {
            "8chars" : False,
            "one_lowercase" : False,
            "one_uppercase" : False,
            "one_digit" : False,
            "one_special_char" : False,
            "not_contain_adjecent" : True,
        }
        
        special_char_pattern = r'[^\w\s]'
        
        if len(password) >= 8:
            requirments["8chars"] = True
        
        for i in range(len(password)):
            if password[i].isdigit():
                requirments["one_digit"] = True
            elif password[i].isupper():
                requirments["one_uppercase"] = True
            elif password[i].islower():
                requirments["one_lowercase"] = True
            elif re.match(special_char_pattern, password[i]):
                requirments["one_special_char"] = True
            
            if i != 0:
                if password[i] == password[i-1]:
                    requirments["not_contain_adjecent"] = False
        
        strong_password = True
        
        for requirment in requirments:
            if requirments[requirment] == False:
                strong_password = False
        
        return strong_password
                