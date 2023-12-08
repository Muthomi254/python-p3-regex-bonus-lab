# import re

# my_pattern = r""
# my_regex = re.compile(my_pattern)
import re

# Your refined regular expression pattern
my_pattern = r".*"  # Matches lines ending with "today."

# Compile the regex pattern
my_regex = re.compile(my_pattern)

# Test using the fullmatch method
result = my_regex.fullmatch("It's such a lovely day today.")
print(result.group() if result else None)  # Should print the entire string or None

# Strings to be used for findall test
# FINDALL_STRING = """
#     It's such a lovely day today.
#     Some weather we're having today, huh?
#     Maybe today's just not my day.
#     Where'd all the time go?
# """

# # Test using the findall method
# matches = my_regex.findall(FINDALL_STRING)
# expected_matches = [
#     "It's such a lovely day today.",
#     "Some weather we're having today, huh?",
#     "Maybe today's just not my day.",
# ]

# assert matches == expected_matches
