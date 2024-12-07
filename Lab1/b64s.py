# Using Python, what is the Base-64 conversion for the
# string of “crypto”?
import base64

def to_base64(str):
    try:
        byte_str = str.encode("utf-8")
        result = base64.b64encode(byte_str)
        return result
    except Exception as e:
        print(f"An unexpected error occured! {e}")
        


my_string = to_base64("crypto1")

if my_string:
    print(my_string)

 