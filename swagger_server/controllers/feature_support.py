from swagger_server.models.job_info import *


NaiveBayesGaussian = "NaiveBayesGaussian"
NaiveBayesMultiNomial = "NaiveBayesMultiNomial"
NaiveBayesBernoulli = "NaiveBayesBernoulli"
RandomForests = "RandomForests"
SupportVectorMachine = "SupportVectorMachine"
CoxRegression = "CoxRegression"
KMFitter = "KaplanMeierFeietter"
KX = "KFoldCrossValidation"

jobs_list = [
                NaiveBayesGaussian,
                NaiveBayesMultiNomial,
                NaiveBayesBernoulli,
                RandomForests,
                SupportVectorMachine,
                CoxRegression,
                KMFitter,
                KX
            ]

def is_in_jobs_list(name):
    return name in jobs_list


nb_g = JobInfo(NaiveBayesGaussian,
               "tabular",
               "MDL_NAIVE_BAYES_GAUSSIAN",
               False,
               "Bayesian Algorithm for gaussian distribution",
               [])
nb_m = JobInfo(NaiveBayesMultiNomial,
               "tabular",
               "MDL_NAIVE_BAYES_MULTINOMIAL",
               False,
               "Bayesian Algorithm for MultiNomial distribution",
               [])
nb_b = JobInfo(NaiveBayesBernoulli,
               "tabular",
               "MDL_NAIVE_BAYES_BERNOULLI",
               False,
               "Bayesian Algorithm for Bernoulli distribution",
               [])
rf =   JobInfo(RandomForests,
               "tabular",
               "MDL_RANDOM_FORESTS",
               False,
               "Algorithm which calculates conditional probability",
               [])
svm =  JobInfo(SupportVectorMachine,
               "tabular",
               "MDL_SUPPORT_VECTOR_MACHINE",
               False,
               "Algorithm which uses support vectors for classification",
               [])
cox = JobInfo(CoxRegression,
               "tabular",
               "MDL_COX",
               False,
               "Cox regression!",
               [])
kmf =   JobInfo(KMFitter,
               "tabular",
               "MDL_KMF",
               False,
               "Kaplan meier feietter",
               [])
svm =  JobInfo(SupportVectorMachine,
               "tabular",
               "MDL_SUPPORT_VECTOR_MACHINE",
               False,
               "Algorithm which uses support vectors for classification",
               [])
cox = JobInfo(CoxRegression,
               "tabular",
               "MDL_COX",
               False,
               "Cox regression!",
               [])
kmf =   JobInfo(KMFitter,
               "tabular",
               "MDL_KMF",
               False,
               "Kaplan meier feietter",
               [])
kx =  JobInfo(KX,
               "tabular",
               "MDL_KX",
               False,
               "KX",
               [])
kx =  JobInfo(KX,
               "tabular",
               "MDL_KX",
               False,
               "KX",
               [])

# '''
#     order of the suggest algorithms:
#     Naive Bayes Gaussian
#     Naive Bayes Multinomial
#     Naive Bayes Bernoulli
#     Random Forests
#     Support Vector Machine
#     Cox Regression
#     Kaplan Meier Fitter
#     K-cross validation
# '''

def fetch_list():
    return [rf, nb_g, nb_b, nb_m, svm, cox, kmf, kx]
