class data:
    def __init__(self, url):
        import requests
        self.url = requests.get(url)
        self.content = self.url.content
        self.lines = self.content.splitlines()

    def find_user(self, id):

        class user:
            def __init__(self, id, age, gender, job, zip_code):
                self.id = id
                self.age = age
                self.gender = gender
                self.job = job
                self.zip_code = zip_code

        for line in self.lines:
            split_line = line.decode("ASCII").split("|")
            user_line = user(split_line[0],split_line[1],split_line[2],split_line[3],split_line[4])
            if user_line.id == str(id):
                break

        return f"{user_line.id}, {user_line.age}, {user_line.gender}, {user_line.job}, {user_line.zip_code}"
    
    def estadistics(self):

        print("trabajo \t media de edad \t maxima edad \t minima edad \t media de edad masculina \t media de edad femenina")

        class user:
            def __init__(self, id, age, gender, job, zip_code):
                self.id = id
                self.age = age
                self.gender = gender
                self.job = job
                self.zip_code = zip_code

        jobs = {} #numero de personas en cada trabajo
        jobs_M = {} #numero de personas masculinas por trabajo
        jobs_F = {} #numero de personas femeninas por trabajo
        med_age_job = {} #media de edad en cada trabajo
        max_age_job = {} #maxima de edad en cada trabajo   
        min_age_job = {} #minima de edad en cada trabajo
        med_age_job_M = {} #media de edad en cada trabajo para el genero masculino
        med_age_job_F = {} #media de edad en cada trabajo para el genero femenino



        for user_line in self.lines:
            split_line = user_line.decode("ASCII").split("|")
            user_line = user(split_line[0],split_line[1],split_line[2],split_line[3],split_line[4])
            if user_line.id == "user_id":
                continue
            elif user_line.job not in jobs:
                jobs[user_line.job] = 1
                med_age_job[user_line.job] = int(user_line.age)
                max_age_job[user_line.job] = int(user_line.age)
                min_age_job[user_line.job] = int(user_line.age)

                if user_line.gender == "M":
                    med_age_job_M[user_line.job] = int(user_line.age)
                    med_age_job_F[user_line.job] = 0
                    jobs_M[user_line.job] = 1
                    jobs_F[user_line.job] = 0
                else:
                    med_age_job_F[user_line.job] = int(user_line.age)
                    med_age_job_M[user_line.job] = 0 
                    jobs_F[user_line.job] = 1
                    jobs_M[user_line.job] = 0

            else:
                jobs[user_line.job] = jobs[user_line.job] + 1
                med_age_job[user_line.job] = med_age_job[user_line.job] + int(user_line.age)

                if max_age_job[user_line.job] < int(user_line.age):
                    max_age_job[user_line.job] = int(user_line.age)

                if min_age_job[user_line.job] > int(user_line.age):
                    min_age_job[user_line.job] = int(user_line.age)

                if user_line.gender == "M":
                    med_age_job_M[user_line.job] = med_age_job_M[user_line.job] + int(user_line.age)
                    jobs_M[user_line.job] = jobs_M[user_line.job] + 1
                else:
                    med_age_job_F[user_line.job] = med_age_job_F[user_line.job] + int(user_line.age)
                    jobs_F[user_line.job] = jobs_F[user_line.job] + 1

        for job in jobs:
            med_age_job[job] = med_age_job[job] / jobs[job]
            med_age_job[job] = int(med_age_job[job])
            if jobs_M[job] != 0:
                med_age_job_M[job] = med_age_job_M[job] / jobs_M[job]
                med_age_job_M[job] = int(med_age_job_M[job])
            else:
                med_age_job_M[job] = int(med_age_job_M[job])
            if jobs_F[job] != 0:
                med_age_job_F[job] = med_age_job_F[job] / jobs_F[job]
                med_age_job_F[job] = int(med_age_job_F[job])
            else: 
                med_age_job_F[job] = int(med_age_job_F[job])
            print(f"{job} \t \t {med_age_job[job]} \t \t {max_age_job[job]} \t \t {min_age_job[job]} \t \t \t {med_age_job_M[job]} \t \t \t \t {med_age_job_F[job]}")



        


m = data("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user")

print(m.find_user(1))

m.estadistics()


