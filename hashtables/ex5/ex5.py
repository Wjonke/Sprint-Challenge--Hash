def finder(files, queries):

    """
    YOUR CODE HERE
    """

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))

# Given a list of full paths to files, and a list of filenames to query, report all the full paths that match that
# filename.
#
# Example input:
#
# paths = [
#     "/usr/local/share/foo.txt",
#     "/usr/bin/ls",
#     "/home/davidlightman/foo.txt",
#     "/bin/su"
# ]
#
# queries = [
#     "ls",
#     "foo.txt",
#     "nosuchfile.txt"
# ]
# Example return value:
#
# [ "/usr/local/share/foo.txt", "/usr/bin/ls", "/home/davidlightman/foo.txt" ]
# because that's where the foo.txt and ls files are.
#
# The file "nosuchfile.txt" is ignored because it's not in the paths.
#
# Return list can be in any order.
#
# Limits:
#
# Up to approximately 1,000,000 paths.
# Up to approximately 1,000,000 queries.
