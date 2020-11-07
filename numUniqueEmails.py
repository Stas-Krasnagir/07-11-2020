def numUniqueEmails(emails):
    for i in range(len(emails)):
        emails[i] = emails[i].split("@")
        local_name = emails[i][0]
        domain_name = emails[i][1]
        if "+" in local_name:
            plus = local_name.index("+")
            local_name = local_name[:plus]
        if "." in local_name:
            local_name = local_name.replace(".", "")
        emails[i] = local_name + "@" + domain_name
    return len(set(emails))


emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
print(numUniqueEmails(emails))