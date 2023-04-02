import requests

# Set the API endpoint URL
url = "https://api.hh.ru/vacancies"

# Set the query parameters
params = {
    "text": "python developer",
    "area": 1,
    "period": 30,
    "per_page": 100,
    "page": 0,
    "currency": "RUR",
    "experience": "noExperience",
    "schedule": "fullDay",
    "employment": "full",
    "order_by": "salary_desc",
    # "only_with_salary": True,
    # "search_field": "name",
    # "clusters": True,
    # "enable_snippets": True,
    # "salary_unit": "monthly",
    # "label": "with_address",
    # "describe_arguments": True,
    # "specialization": 1,
    # "industries": "7.19",
    # "employer_id": 1234,
    # "created_at": "30_days_ago",
    # "area": 1,
    # "metro": 11,
    # "metro_distance": 5,
    # "address": "Moscow",
    # "relocation": True,
    # "negotiations": True
}


# Set the HTTP headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

# Make the HTTP request and get the response in JSON format
response = requests.get(url, params=params, headers=headers).json()

# Print the first 10 vacancies
for vacancy in response["items"][:10]:
    print(vacancy["name"], vacancy["salary"], vacancy["employer"]["name"], vacancy["alternate_url"])
