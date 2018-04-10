from swagger_server.models.job_info import JobInfo

nb_g = JobInfo("NaiveBayesGaussian","tabular","MDL_NAIVE_BAYES_GAUSSIAN",False,"Bayesian Algorithm for gaussian distribution",[])
nb_m = JobInfo("NaiveBayesMultiNomial","tabular","MDL_NAIVE_BAYES_MULTINOMIAL",False,"Bayesian Algorithm for MultiNomial distribution",[])
nb_b = JobInfo("NaiveBayesBernoulli","tabular","MDL_NAIVE_BAYES_BERNOULLI",False,"Bayesian Algorithm for Bernoulli distribution",[])
rf = JobInfo("RandomForests","tabular","MDL_RANDOM_FORESTS",False,"Algorithm which calculates conditional probability",[])
svm = JobInfo("SupportVectorMachine","tabular","MDL_SUPPORT_VECTOR_MACHINE",False,"Algorithm which uses support vectors for classification",[])


'''
order of the suggest algorithms:
Naive Bayes Gaussian
Naive Bayes Multinomial
Naive Bayes Bernoulli
Random Forests
Support Vector Machine
'''

def fetch_list():
    # nb_g = JobInfo("NaiveBayesGaussian","tabular","MDL_NAIVE_BAYES_GAUSSIAN",False,"Bayesian Algorithm for gaussian distribution",[])
    # nb_m = JobInfo("NaiveBayesBernoulli","tabular","MDL_NAIVE_BAYES_BERNOULLI",False,"Bayesian Algorithm for Bernoulli distribution",[])
    # nb_b = JobInfo("NaiveBayesMultiNomial","tabular","MDL_NAIVE_BAYES_MULTINOMIAL",False,"Bayesian Algorithm for MultiNomial distribution",[])
    # rf =  JobInfo("RandomForests","tabular","MDL_RANDOM_FORESTS",False,"Algorithm which calculates conditional probability",[])
    # svm = JobInfo("SupportVectorMachine","tabular","MDL_SUPPORT_VECTOR_MACHINE",False,"Algorithm which uses support vectors for classification",[])
    jobsList = []
    jobsList.append(rf)
    jobsList.append(nb_g)
    jobsList.append(nb_b)
    jobsList.append(nb_m)
    jobsList.append(svm)
    return jobsList
