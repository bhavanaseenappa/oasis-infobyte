import random

def generate_password(length, include_chars, exclude_chars):
    all_chars = []
    if 'l' in include_chars:
        all_chars.extend(list('abcdefghijklmnopqrstuvwxyz'))
    if 'u' in include_chars:
        all_chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if 'd' in include_chars:
        all_chars.extend(list('0123456789'))
    if 's' in include_chars:
        all_chars.extend(list('!@#$%^&*()_+[]{}|;:,.<>?'))

    all_chars = list(set(all_chars) - set(exclude_chars))

    if len(all_chars) == 0:
        print("Error: No characters available after excluding specified characters.")
        return None

    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired password length: "))
        include_chars = input("Include (l)etters, (u)pper case letters, (d)igits, (s)ymbols (e.g., luds): ").lower()
        exclude_chars = input("Exclude characters (if any): ")

        password = generate_password(length, include_chars, exclude_chars)

        if password:
            print(f"Generated password: {password}")

    except ValueError:
        print("Invalid input. Please enter a valid integer for password length.")

if __name__ == "__main__":
    main()