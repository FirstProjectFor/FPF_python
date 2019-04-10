class Solution:
    def numUniqueEmails(self, emails: list) -> int:
        result = set()

        for email in emails:
            result.add(self.get_actually_address(email))

        return len(result)

    def get_actually_address(self, email: str):
        local_name, domain_name = email.split("@")
        local_name = local_name.split("+")[0].replace(".", "")
        return "@".join([local_name, domain_name])


solution = Solution()
test_email = list()
test_email.append("sunfeilong@gmail.com")
test_email.append("sunfe.ilong@gmail.com")
test_email.append("sunfeilo+ng@gmail.com")
print(solution.numUniqueEmails(test_email))
