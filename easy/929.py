class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueSet = set()
        for email in emails:
            email = email.split("@")
            # print(email)
            print(email[0])
            new_email_name = ""
            letter = 0
            print(len(email[0]))
            while  letter < len(email[0]) and email[0][letter] != "+":
                print(email[0][letter])
                if email[0][letter] != ".":
                    new_email_name += email[0][letter]

                letter += 1
            print(new_email_name)
            email[0] = new_email_name
            email = "@".join(email)

            if email not in uniqueSet:
                uniqueSet.add(email)

            # print(uniqueSet)

        return len(uniqueSet)
