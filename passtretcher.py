import hashlib
import base64
import zlib
import binascii
import argparse
import sys

def transform_string(input_string, output_length=1024):
    """
    Transforms an input string into a long, seemingly random but deterministic string.
    
    Args:
        input_string (str): Input string to be transformed
        output_length (int): Desired length of output string (default: 1024)
    
    Returns:
        str: Transformed string with the requested length
    """
    if not input_string:
        return ""
    
    # Adjust number of iterations based on desired length
    iterations = max(3, min(10, output_length // 100))
    
    # Step 1: Apply multiple hash algorithms in sequence
    current_value = input_string.encode('utf-8')
    
    for i in range(iterations):
        # Rotate between different hash algorithms
        if i % 3 == 0:
            current_value = hashlib.sha3_512(current_value).digest()
        elif i % 3 == 1:
            current_value = hashlib.blake2b(current_value).digest()
        else:
            current_value = hashlib.sha512(current_value).digest()
    
    # Step 2: Apply different encodings
    encodings = [base64.b85encode, base64.b64encode, binascii.hexlify]
    for i, encoding_fn in enumerate(encodings):
        if i % 2 == 0:
            current_value = encoding_fn(current_value)
        else:
            current_value = encoding_fn(current_value).decode('utf-8').encode('utf-8')
    
    # Step 3: Use SHAKE to get exact length
    final_hash = hashlib.shake_256(current_value).hexdigest(output_length // 2)
    
    # If more characters are needed, repeat process with current hash
    while len(final_hash) < output_length:
        extra = hashlib.shake_256(final_hash.encode('utf-8')).hexdigest(output_length // 2)
        final_hash += extra
    
    return final_hash[:output_length]

def main():
    parser = argparse.ArgumentParser(
        description="Transforms a string into a long, seemingly random but deterministic version.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument(
        '-s', '--string',
        type=str,
        help="Input string to be transformed (use quotes if it contains spaces)"
    )
    
    parser.add_argument(
        '-l', '--length',
        type=int,
        default=1024,
        help="Desired length of output string (default: 1024)"
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help="Show additional processing information"
    )
    
    args = parser.parse_args()
    
    if not args.string:
        parser.print_help()
        print("\nError: You must provide an input string with -s")
        sys.exit(1)
    
    if args.length < 10:
        print("Warning: Minimum length adjusted to 10 characters", file=sys.stderr)
        args.length = 10
    
    if args.verbose:
        print(f"Processing input string: '{args.string}'")
        print(f"Generating output with {args.length} characters...")
    
    result = transform_string(args.string, args.length)
    
    if args.verbose:
        print("\nResult:")
    print(result)

if __name__ == "__main__":
    main()
