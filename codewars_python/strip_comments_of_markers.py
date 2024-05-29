# Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

def strip_comments(string,markers):
    s_list = string.split("\n")
    print(s_list)
    n_list = []

    for item in s_list:
        s = ""
        for char in item:
            if char in markers:
                break
            else:
                s = s + char
        n_list.append(s.strip())
    return "\n".join(n_list)
     


print(strip_comments("a\nc\nd", ["#", "!"]))
        
