def count_jobs(data:list, job:str) -> int:
    """
    Return the number of users with a given job

    Args:
        data (dict): A dictionary of values
        job (str): The job to search for
    Returns:
        int: The number of users with the given job
    """
    jobc = 0
    for i in data:
        for k,v in i.items():
            if v == job:
                jobc += 1
    return jobc
print(count_jobs([{'name': 'John', 'job': 'Developer'}, {'name': 'Mary', 'job': 'Developer'}], "Developer"))