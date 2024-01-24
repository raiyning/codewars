def hero(bullets, dragons):
    min_bullets_to_kill = 2 * dragons
    if bullets < min_bullets_to_kill:
        return False
    else: 
        return True

print (hero(10, 5))