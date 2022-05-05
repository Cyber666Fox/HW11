import json

def load_candidates_from_json():                      #возвращает список всех кандидатов
    with open("candidates.json", "r", encoding="utf_8") as file:
        candidates = json.load(file)
    return candidates

def get_candidate(candidate_id):                      #возвращает одного кандидата по его id
    candidates = load_candidates_from_json()
    result = None
    for candidate in candidates:
        id_list = candidate["id"]
        if candidate_id == int(id_list):
            result = candidate
    return result        

def get_candidates_by_name(candidate_name):            #возвращает кандидатов по имени
    candidates = load_candidates_from_json()
    result = []
    for candidate in candidates:
        if candidate_name in candidate["name"].lower():
            result.append(candidate)
    return result   



def get_candidates_by_skill(skill_name):              #возвращает кандидатов по навыку
    candidates = load_candidates_from_json()
    result = []
    for candidate in candidates:
        skills = candidate["skills"].lower().split(", ")
        if skill_name in skills:
            result.append(candidate)
    return result 




