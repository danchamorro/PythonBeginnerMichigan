# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a
# Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary
# is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

# name = input("Enter file:")
name = "mbox-short.txt"
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    line = line.strip()
    if not line.startswith("From "):
        continue
    words = line.split()
    emails = words[1].split()
    print(emails)
    for email in emails:
        counts[email] = counts.get(email, 0) + 1
print(counts)

largestcount = None
largestemail = None
for email, count in counts.items():
    if largestcount is None or count > largestcount:
        largestcount = count
        largestemail = email
print(largestemail, largestcount)
