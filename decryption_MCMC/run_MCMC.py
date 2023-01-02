# This script is to run MCMC to decipher text

from MCMC_functions import MCMC_sample_cipher, apply_cipher, string_cipher

with open(
    '/Users/yipu/statistical_computing/decryption-Yi-Pu/some_text_encrypt.txt',
        'r') as f:
    encrypted_text = f.read().replace('\n', '')

# Set steps
n = 10000
# Get the best decipher
MCMC = MCMC_sample_cipher(encrypted_text, n)
# Use decipher to get results
res = apply_cipher(encrypted_text, string_cipher(MCMC))
print('The decrypted text is:')
print(res)
# Save the decrypted text
with open(
    '/Users/yipu/statistical_computing/decryption-Yi-Pu/some text decrypt.txt',
        'w') as f:
    f.write(res)

# Test on some random bookes download:
with open(
    '/Users/yipu/Desktop/temp1.txt',
        'r') as f:
    my_book = f.read().replace('\n', '')
# Gnerate a decipher
my_cipher = string_cipher("jebtnzihpmyfqsakdrcovgxlwu")
encrypted_book = apply_cipher(my_book, my_cipher)
# Get the best decipher
book_MCMC = MCMC_sample_cipher(encrypted_book, n)
# Use decipher to get results
decrypted_book = apply_cipher(encrypted_book, string_cipher(book_MCMC))
print('The encrypted text is:')
print(encrypted_book)
print('The decrypted text is:')
print(decrypted_book)
