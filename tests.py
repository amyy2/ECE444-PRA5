import requests
import time
import csv
import pandas as pd
import matplotlib.pyplot as plt

print("starting tests")

test_cases = [
    "The Earth is flat",
    "University of Toronto went bankrupt",
    "Kamala Harris is a 2024 presedential candidate",
    "There is a hurricane in Florida"
]

url = "http://PRA5-canada-env.eba-ivst4i9s.ca-central-1.elasticbeanstalk.com/"

"""
latency_dict = {}

# make 100 API calls to the server
for test_case in test_cases:
    print(test_case)
    for i in range(100):
        start_time = time.time()
        response = requests.post(url, data={'text': test_case})
        end_time = time.time()
        latency = end_time - start_time

        if test_case in latency_dict:
            latency_dict[test_case].append(latency)
        else:
            latency_dict[test_case] = [latency]

# save to a csv file
with open('latency_results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Test Case', 'Latency'])

    for test_case, latencies in latency_dict.items():
        for latency in latencies:
            writer.writerow([test_case, latency])
"""

# load csv file
df = pd.read_csv('latency_results.csv')

# boxplot
plt.figure()
df.boxplot(by='Test Case', column=['Latency'])
plt.title('Latency Boxplot')
plt.xlabel('Test Case')
plt.ylabel('Latency')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# average performance
average_latency = df.groupby('Test Case')['Latency'].mean()
print(f'Average latency: {average_latency}')