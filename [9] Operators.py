# ARITHMETIC OPERATORS

"""
Operator	Name	            Example	
+	        Addition	        x + y	
-	        Subtraction	        x - y	
*	        Multiplication	    x * y	
/	        Division	        x / y	
%	        Modulus	            x % y	
**	        Exponentiation	    x ** y	
//	        Floor division	    x // y
"""

# ASSIGNMENT OPERATORS

"""
=	    x = 5	    x = 5	
+=	    x += 3	    x = x + 3	
-=	    x -= 3	    x = x - 3	
*=	    x *= 3	    x = x * 3	
/=	    x /= 3	    x = x / 3	
%=	    x %= 3	    x = x % 3	
//=	    x //= 3	    x = x // 3	
**=	    x **= 3	    x = x ** 3	
&=	    x &= 3	    x = x & 3	
|=	    x |= 3	    x = x | 3	
^=	    x ^= 3	    x = x ^ 3	
>>=	    x >>= 3	    x = x >> 3	
<<=	    x <<= 3	    x = x << 3	
:=	    print(x := 3)	x = 3
"""

# LOGICAL OPERATORS

"""
and - Returns True if both statements are true
or - Returns True if one of the statements is true
not - Reverse the result, returns False if the result is true
"""

# IDENTITY OPERATORS

"""
is - Returns True if both variables are the same object
is not - Returns True if both variables are not the same object
"""

# MEMBERSHIP OPERATORS
 
"""
in - Returns True if a sequence with the specified value is present in the object
not in - Returns True if a sequence with the specified value is not present in the object
"""

# OPERATOR PRECEDENCE

# Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:
print((6 + 3) - (6 + 3)) 

#Multiplication * has higher precedence than addition +, and therefore multiplications are evaluated before additions:
print(3 + 6 * 2)

#Addition + and subtraction - has the same precedence, and therefore we evaluate the expression from left to right:
print(5 + 4 - 7 + 3)