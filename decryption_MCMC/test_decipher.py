# This script is to test if the deciphering algorithm works correctly

from MCMC_functions import MCMC_sample_cipher, apply_cipher, \
    string_cipher

my_book = "had been my habit, I am now aware, \
    to speak somewhat lightly of the labors of \
        anthologists: to insinuate that they led \
            lives of bland sedentary ease. I shall \
                not do so again. When the publisher \
                    suggested a collection of \
                        representative contemporary \
                            essays, I thought it would \
                                be the most lenient of tasks. \
                                    But experience is a fine \
                                        aperitive to the mind."
# Set steps
n = 10000
# Gnerate a decipher
my_cipher = string_cipher("jebtnzihpmyfqsakdrcovgxlwu")
encrypted_book = apply_cipher(my_book, my_cipher)
# Get the best decipher
book_MCMC = MCMC_sample_cipher(encrypted_book, n)
# Use decipher to get results
decrypted_book = apply_cipher(encrypted_book, string_cipher(book_MCMC))


def test_MCMC():
    assert decrypted_book == my_book.lower()


# Gnerate a decipher
my_cipher2 = string_cipher("")
encrypted_book2 = apply_cipher(my_book, my_cipher2)
# Get the best decipher
book_MCMC2 = MCMC_sample_cipher(encrypted_book2, n)
# Use decipher to get results
decrypted_book2 = apply_cipher(encrypted_book2, string_cipher(book_MCMC2))


def test_edge_values():
    assert decrypted_book2 == my_book.lower()
