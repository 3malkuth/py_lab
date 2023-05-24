def get_pbi_basic_data(jira, issue_key: str) -> dict:
    # issue = jira.issue(issue_key)  # full description
    summary: str = jira.issue_field_value(issue_key, "summary")
    print(f"Issue Key: {issue_key}")
    print(f"Issue Summary: {summary}")
    pbi_basic_data: dict = {
        "issue_key": issue_key,
        "summary": summary
    }
    return pbi_basic_data
