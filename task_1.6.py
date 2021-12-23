from charset_normalizer import from_path
print(
        str(
from_path(
'test_file.txt'
).best()
)
)

with open("test_file.txt", encoding = "utf-8") as f:
    text = f.read()
    print(text)