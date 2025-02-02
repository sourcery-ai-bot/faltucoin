from backend.util.hashing import crypto_hash

HEX_TO_BINARY_CONVERSION_TABLE = {
  '0': '0000',
  '1': '0001',
  '2': '0010',
  '3': '0011',
  '4': '0100',
  '5': '0101',
  '6': '0110',
  '7': '0111',
  '8': '1000',
  '9': '1001',
  'a': '1010',
  'b': '1011',
  'c': '1100',
  'd': '1101',
  'e': '1110',
  'f': '1111'
}

def hex_to_binary(hex_string):
  return ''.join(
      HEX_TO_BINARY_CONVERSION_TABLE[character] for character in hex_string)

def main():
  number = 451
  hex_number = hex(number)[2:]

  print(f'hex number: {hex_number}')
  print(f'binary number: {hex_to_binary(hex_number)}')
  print(f'original number: {int(hex_to_binary(hex_number),2)}\n')

  hex_to_bin_crypto_hash = hex_to_binary(crypto_hash('test-data'))

  print(f'hex_to_bin_crypto_hash: {hex_to_bin_crypto_hash}')

if __name__ == '__main__':
  main()