from swagger_server.algorithms.classifier import *
from swagger_server.fitter.process import *
from swagger_server.fitter.ml_execute_fit import *


class ClassifierFitter:
    def __init__(self, functor, ycolumn, xcolumns=None, **kwargs):
        if functor == NaiveBayes:
            mtype = kwargs['modeltype']
            if mtype == NaiveBayes.GAUSSIAN:
                self.functor = NBG
            elif mtype == NaiveBayes.MULTINOMIAL:
                self.functor = NBM
            elif mtype == NaiveBayes.BERNOULLI:
                self.functor = NBB
            else:
                raise Exception('unknown nbtype: ' + str(mtype))
        elif functor == RandomForests:
            self.functor = RF
        elif functor == SupportVectorMachine:
            self.functor = SVM
        else:
            raise Exception("unknown functor: " + str(functor))
        self.id = kwargs['id']
        self.datafile = kwargs['datafile']
        self.columns = [ycolumn] + xcolumns
        self.process = Process('tmp_success_' + str(self.id))

    def start(self, model_out):
        self.process.start([
                            './ml_execute_fit.py',
                            self.functor,
                            self.datafile,
                            model_out] + self.columns)

    def is_finished(self):
        return self.process.is_finished()

    def stop(self):
        self.process.kill()

    def finalize(self):
        self.process.finalize()


class CoxRegressionFitter:
    def __init__(self, dcolumn, ecolumn, ycolumn, xcolumns=None **kwargs):
        self.functor = COX
        self.D = dcolumn
        self.E = ecolumn
        self.datafile = kwargs['datafile']
        self.columns = [ycolumn] + xcolumns
        self.process = Process('tmp_success_' + str(self.id))

    def start(self, output, report_output):
        self.process.start([
                           './ml_execut_fit.py',
                           self.functor,
                           self.datafile,
                           output,
                           report_output,
                           self.D,
                           self.E] + self.columns)

    def is_finished(self):
        return self.process.is_finished()

    def stop(self):
        self.process.kill()

    def finalize(self):
        self.process.finalize()


if __name__ == "__main__":
    cf = ClassifierFitter(NaiveBayes, datafile='file.csv',
                          modeltype=NaiveBayes.GAUSSIAN,
                          id='1843')
    print(cf.functor)
    cf.start()
    while not cf.is_finished():
        pass
    cf.finalize()
