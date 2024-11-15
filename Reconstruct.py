from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes

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

# Example p and q (the factors you found)
p = 105562240273338916478843714629637708852536187485429610958652602149570916431654518811856170042497582053396436774656869520915225450202892379549983444463239932841504904924142811925441567952904913150856732738434780357666981857964002582637673402496296779397121918264942391052515402555700381652633503678300281025079
q = 170306190807129939690412689100267009410839715670044668790119233096021151435612522856303595661141547122685313993504411383348630072557330303417155851779988538103936406502468829627921649562683838513389253595547920588801306021954323830977412785764768545030785221221283314607363272029002055854344665414658802058459

# Public exponent (standard RSA value)
e = 65537

# Compute the private key exponent d
private_key_exponent = compute_private_key(p, q, e)

# Modulus N
N = p * q

# Print the private key exponent (d) and modulus (N)
print(f"Private key exponent (d): {private_key_exponent}")
print(f"Modulus (N): {N}")

# Reconstruct the RSA private key (d, N)
private_key = RSA.construct((N, e, private_key_exponent))

# Export the private key in PEM format
pem_key = private_key.export_key()

# Save the private key to a file
with open("private_key.pem", "wb") as f:
    f.write(pem_key)

print("Private key has been saved to private_key.pem.")

