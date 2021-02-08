from passlib.hash import pbkdf2_sha1

hash = '$pbkdf2$131000$jTFmzBkDwLiXUiplbM32mw$Ze2arx7M2jEAsRQ8rhn4/BvwY9E'

# answer = pbkdf2_sha1.verify('test', hash)
# print(answer)

hash2 = '$pbkdf2$131000$WCtlDAGAUKqVMuac0/rf.w$QwT.EB2WW4r.M58yOmlLRFvZ0zE'
hash3 = '$pbkdf2$131000$GeN87703pnRO6f1/7z2ntA$w1FL.xneBewY6JI2VZixRciwy5Y'

input('THIS, IS. LEVEL ONE SECURITY. press enter to begin decrypting level one: ')
while True:
    count = 0
    count += 1
    answer = pbkdf2_sha1.verify(str(count), hash2)
    if answer == True:
        print(answer, 'Correct. Program will cease and access will be granted.')
        break
    else:
        print('WRONG. ACCESS DENIED.')

input('YOU HAVE COMPLETED LEVEL ONE SECURITY. press enter to begin decrypting LEVEL TWO SECURITY: ')
while True:
    count = 0
    count += 1
    attempt = pbkdf2_sha1.verify(str(count), hash3)
    if answer == True:
        print(answer, 'Correct. Program will cease and access will be granted.')
        break
    else:
        print('WRONG. ACCESS DENIED.')
