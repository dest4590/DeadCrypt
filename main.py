import cryptor

# encrypt text
encrypted_text = cryptor.Encrypt('Hi').encrypt()

# decrypt text
decrypted_text = cryptor.Decrypt(encrypted_text).decrypt()

# make binary
cryptor.Encrypt("print('hi')").makebinary('hello')

# launch binary
cryptor.Binary('binares/hello.bin').launch()