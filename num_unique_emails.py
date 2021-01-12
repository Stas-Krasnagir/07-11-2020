def num_unique_emails(emails):
    new_emails = emails.copy()
    for i in range(len(emails)):
        new_emails[i] = new_emails[i].split("@")
        local_name = new_emails[i][0]
        domain_name = new_emails[i][1]
        if "+" in local_name:
            plus = local_name.index("+")
            local_name = local_name[:plus]
        if "." in local_name:
            local_name = local_name.replace(".", "")
        new_emails[i] = local_name + "@" + domain_name
    return len(set(new_emails))


emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
print(num_unique_emails(emails))
