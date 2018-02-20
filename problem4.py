import csv

list_of_jobs_and_weights = []

with open('jobs.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)

	job_counter = 1

	for line in csv_reader:
		list_of_jobs_and_weights.append([int(line[0]), int(line[1]), job_counter])
		job_counter += 1
	print(list_of_jobs_and_weights)

def optimal_job_order(lst):
	job_order = []
	for i in lst:
		order = i[0]/i[1]
		i.insert(0,order)
	print(lst)
	lst.sort(reverse = True)
	for n in lst:
		job_order.append(n[3])
	return job_order


answer = optimal_job_order(list_of_jobs_and_weights)
print(answer)


