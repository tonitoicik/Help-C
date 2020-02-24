import re
import json


CAT_MALE = ("кот", "кота", "коту", "котик", "котику", "котика")
CAT_FEMALE = ("кошка", "кошку", "кошке", "кошечка", "кошечку", "кошечке")
AGE_KEYS = ("лет", "год", "года")


def parse_text(in_text):
    result = {
      "cat": False, 
      "male": False, 
      "age": 0
    }
    
    in_text_lower = in_text.lower()
    cat_male_loc = re.search("("+")|(".join(CAT_MALE)+")", in_text_lower)
    cat_female_loc = re.search("("+")|(".join(CAT_FEMALE)+")", in_text_lower)
    age_loc = re.search("\d+\.?\d+"+"\W*("+")|(".join(AGE_KEYS)+")", in_text_lower.replace(",", "."))
    
    if cat_male_loc is not None:
        result["cat"] = True
        result["male"] = True
    elif cat_female_loc is not None:
        result["cat"] = True
    else:
        return result
      
    if age_loc is not None:
        age_str = in_text_lower[age_loc.start(): age_loc.end()].replace(",", ".")
        years_loc = re.search("\d+\.?\d+", age_str)
        result["age"] = float(age_str[years_loc.start(): years_loc.end()])
        
    return result


if __name__ == "__main__":
    in_text = input("Enter the text to parse: ")
    print(json.dumps(parse_text(in_text), indent=2, ensure_ascii=False))
