class utils:

#function 1 - reversed
    def reversed(num: int) -> int: "takes num as an int and returns an int"
      if num < 0:  "make neg numbers temp pos"
        return -int(str(-num)[::-1]) "converts neg number to positive string and reverses using splicing and converts back to int"
      return int(str(num)[::-1]) "if pos, convert to string and revserse using splice, and convert back to int" 

#function 2 - formatter
    def formatter(num: int) -> dict: "takes num as an int and returns a dictionary"
      return {
          "binary": bin(num)[2:], "key value pair in binary (2: slices off prefix 0b in string)"
          "octal": oct(num)[2:] "key value pair in octal (2: slices off prefix 0o in string)"
      }



