import math
import sympy

# Function to calculate GCD (Greatest Common Divisor)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Pollard's P-1 algorithm
def pollard_p1(n):
    a = 2
    i = 2
    while True:
        # Compute a^i % n using modular exponentiation
        a = pow(a, i, n)
        # Compute GCD of a-1 and n
        d = gcd(a - 1, n)
        if d > 1:
            return d
        i += 1

# Driver function to factorize the modulus N
def factorize_modulus(n):
    factors = []
    num = n
    while True:
        # Apply Pollard's P-1 to find a factor
        d = pollard_p1(num)
        factors.append(d)
        num //= d  # Divide by the found factor
        if sympy.isprime(num):  # If the reduced number is prime
            factors.append(num)
            break
    return factors

# Function to compute modular inverse (using Extended Euclidean Algorithm)
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

# Function to compute the private exponent d
def compute_private_key(p, q, e):
    # Euler's Totient function: φ(N) = (p - 1)(q - 1)
    phi = (p - 1) * (q - 1)
    
    # Compute modular inverse of e (private exponent d)
    d = mod_inverse(e, phi)
    return d

# Example usage with modulus N (replace with actual N)
N = 17977903034019354069644981802480507927978698472239270130268982099607186360687521777918981897967706063794906841297685336261647045604302249686734140350834882345170042540582931133624884735237597546391572852716769096627794708794127624765166472662358993169988859217646097678425318193724107739605766420252499277695198925095175994475739841682922637243505403562623971680638404095813809454376766531045786584427648989048626805075056322115685430497469778869059228650834946087465310274890187616966208601236422727815632687588858869826190174279202570202743079339465193119004569398769634463036068133996290459864771187346223803093261

# Factorizing the modulus N
factors = factorize_modulus(N)

# Assume e (public exponent) is 65537 (standard)
e = 65537

# Private key reconstruction
if len(factors) == 2:
    p, q = factors
    private_key = compute_private_key(p, q, e)
    print(f"Private key exponent (d): {private_key}")
else:
    print("Unable to factorize N correctly.")

