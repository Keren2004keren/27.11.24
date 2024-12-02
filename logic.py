# Start
# 1
def is_legal(brack: str) -> bool:
    while "()" in brack or "[]" in brack or "{}" in brack:
        brack = brack.replace("()", "").replace("[]", "").replace("{}", "")
    return brack == ""


# 2
def remove_dup(sort_dup: list) -> list:
    removed_dup = []
    for i in range(len(sort_dup)):
        if i == 0 or sort_dup[i] != sort_dup[i - 1]:
            removed_dup.append(sort_dup[i])
    return removed_dup

# 3
def sort_list(l1: list, l2: list) -> list:
    sorted_l = []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            sorted_l.append(l1[i])
            i += 1
        else:
            sorted_l.append(l2[j])
            j += 1
    while i < len(l1):
        sorted_l.append(l1[i])
        i += 1

    while j < len(l2):
        sorted_l.append(l2[j])
        j += 1
    return sorted_l

# Stop
