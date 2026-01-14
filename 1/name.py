name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "James"
last_name = "Bond"

full_name = f"{first_name} {last_name}"

print(full_name)

print("")

print(f"Hello, {full_name.title()}")

message = f"Hello old friend,\t\n {full_name.title()}"

print(message.rstrip())

#removing Prefixes
nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://'))