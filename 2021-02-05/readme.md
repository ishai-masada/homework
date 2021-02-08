# l33t h4ck3r t1m3

This week you're gonna be cracking an encrypted password with a brute force
attack.

If you're not familiar with the term, a brute force attack is when you try every
possible combination until you've gotten the right answer. For instance,
brute-forcing a four-digit pin would look like this:

```
    0000
    0001
    0002
    ...
    3499
    3500
    3501 -- Correct. Terminating program.
```

I've hashed two different 'passwords' using SHA-1. Both are numbers which means
you can save time by not trying every possible combination of letters as well.
You can find these two passwords in `easy.txt` and `hard.txt`. The difficulty is
really just a matter of computing time, if you crack `easy.txt` you'll have no
problem cracking the other one.

In order to check whether you've guessed correctly you'll want to use passlib.

``` bash
python3 -m pip install passlib
```

Then to use it in your program you'll import it like this:

``` python3
from passlib.hash import pbkdf2_sha1
```

The method `pbkdf2_sha1.verify()` takes two arguments, the first being the
password you're validating and the second being the hash you're validating
against (In this case, the contents of either `easy.txt` or `hard.txt`). This
method will return a boolean denoting whether or not the passwords match.

Here's a sample hash of the word 'test' for you try the method with. This will
return True if you've done everything correctly.

```
$pbkdf2$131000$jTFmzBkDwLiXUiplbM3Zmw$Ze2arx7M2jEAsRQ8rhn4/BvwY9E
```

Good luck.
