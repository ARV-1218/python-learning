from werkzeug.security import generate_password_hash, check_password_hash

password = "1234@rv"

hashed_password = generate_password_hash(password)

print("Hash:")
print(hashed_password)

print("\nCorrect password:")
print(check_password_hash(hashed_password, "1234@rv"))

print("\nWrong password:")