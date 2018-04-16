#!/usr/bin/env python3


import sys
import json
import os
import logging


sys.path += [os.getcwd()]


import swagger_server.controllers.feature_support as feature_support
from swagger_server.algorithms.classifier import *
from swagger_server.algorithms.cox_regression import *
from swagger_server.algorithms.kaplan_meier import *
from swagger_server.algorithms.csv_loader import *


NBG, NBM, NBB, RF, SVM, COX, KMF, KX = feature_support.jobs_list


def is_classifier(alg):
    return alg in [NBG, NBM, NBB, SVM, RF]


def get_classifier_type(alg):
    if alg in [NBG, NBM, NBB]:
        return NaiveBayes
    elif alg in [SVM]:
        return SupportVectorMachine
    elif alg in [RF]:
        return RandomForests
    else:
        raise Exception('cannot find classifier type for ' + str(alg))


def is_kcross(alg):
    return alg == KX


def is_cox(alg):
    return alg == COX


def is_kmf(alg):
    return alg == MKF


# https://stackoverflow.com/questions/1158076/implement-touch-using-python
def touch(fname, mode=0o666, dir_fd=None, **kwargs):
    flags = os.O_CREAT | os.O_APPEND
    with os.fdopen(os.open(fname, flags=flags, mode=mode, dir_fd=dir_fd)) as f:
        os.utime(f.fileno() if os.utime in os.supports_fd else fname,
            dir_fd=None if os.supports_fd else dir_fd, **kwargs)

def remove_file(fname):
    if os.path.exists(fname):
        os.remove(fname)


if __name__ == "__main__":
    # print('ARGS: ', sys.argv)
    # successfile, alg, datafile, output = sys.argv[1:5]
    # args = sys.argv[5:]
    # print(successfile, alg, datafile, output)
    # if is_classifier(alg):
    #     c = None
    #     clftype = get_classifier_type(alg)
    #     if clftype == NaiveBayes:
    #         mtype = None
    #         if alg == NBG:
    #             mtype = NaiveBayes.GAUSSIAN
    #         elif alg == NBM:
    #             mtype = NaiveBayes.MULTINOMIAL
    #         elif alg == NBB:
    #             mtype = NaiveBayes.BERNOULLI
    #         else:
    #             raise Exception('unknown nbtype of ' + str(mtype))
    #         c = Classifier(classifier=clftype, modeltype=mtype)
    #     else:
    #         c = Classifier(classifier=clftype)
    #     ycolumn = int(args[0])
    #     args = args[1:]
    #     data = load_csv_xy(datafile, [ycolumn], [int(x) for x in args] if len(args) else None)
    #     c.fit(data)
    #     c.save_model(output)
    # elif is_kcross(alg):
    #     pass
    # elif is_cox(alg):
    #     cox = CoxRegression()
    #     report_output, dur_col, event_col = args[:3]
    #     args = args[3:]
    #     ycolumn = int(args[0])
    #     args = args[1:]
    #     data = load_csv_xy(datafile, ycolumn, [int(x) for x in args] if len(args) else None)
    #     cox.fit(data, dur_col, event_col)
    #     pass  # dump output into output and report output
    # elif is_kmf(alg):
    #     report_output = args[0]
    #     args = args[1:]
    #     kmf = KaplanMeierFitter()
    #     args = args[1:]
    #     ycolumn = int(args[0])
    #     data = load_csv_xy(datafile, ycolumn, [int(x) for x in args] if len(args) else None)
    #     kmf.fit(data)
    #     pass  # dump plot/table into output and report output
    successfile, jsonfile = sys.argv[1:3]
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    try:
        with open(jsonfile) as fp:
            par = json.load(fp)
        opr = par['task_type'] # 'fit' or 'predict'
        if opr == 'fit':
            alg = par['algorithm'] # define the options above
            if is_classifier(alg):
                c = None
                clftype = get_classifier_type(alg)
                if clftype == NaiveBayes:
                    mtype = None
                    if alg == NBG:
                        mtype = NaiveBayes.GAUSSIAN
                    elif alg == NBM: # delete datafile
                        mtype = NaiveBayes.MULTINOMIAL
                    elif alg == NBB:
                        mtype = NaiveBayes.BERNOULLI
                    else:
                        raise Exception('unknown nbtype of ' + str(mtype))
                    c = Classifier(classifier=clftype, modeltype=mtype)
                else:
                    c = Classifier(classifier=clftype)
                datafile = par['datafile'] # e.g. file.csvs
                ycolumns = par['ycolumns'] # array(int)
                xcolumns = par['xcolumns'] # array(int)
                data = load_csv_xy(datafile, ycolumns, xcolumns)
                c.fit(data)
                output_file = par['model_out'] # model output
                report_file = par['report_out'] # report output
                c.save_model(output_file) # dumps the model into model file
                # generate report file
                # fill in the report
                report = make_report(
                    title='title',
                    desription='description',
                    created='created',
                    blocks=[
                    ])
                json.dump(report, report_file)
                remove_file(datafile)
            elif is_cox(alg):
                D = par['dur_column'] # duration column
                E = par['event_column'] # event column
                datafile = par['datafile']
                data = load_csv(datafile, [D, E])
                c = CoxRegression()
                c.fit(data, 0, 1)
                # generate a table
                report_file = par['report_out'] # report output
                # fill in the report
                report = make_report(
                    title='title',
                    desription='description',
                    created='created',
                    blocks=[
                    ])
                json.dump(report, report_file)
                # generate report file
                remove_file(datafile)
            elif is_kmf(alg):
                datafile = par['datafile']
                D = par['dur_column'] # duration column
                E = par['event_column'] # event column
                output_file = par['output_file']
                k = kaplan_meier()
                k.fit(load_csv(datafile, D), load_csv(datafile, E))
                output_file = par['table_out'] # csv output
                k.save_csv(output_file)
                report_file = par['report_out'] # report output
                report = make_report(
                    title='title',
                    desription='description',
                    created='created',
                    blocks=[
                        make_plot_block(title='title',
                                        sub_title='sub title',
                                        caption='Caption',
                                        plot_infos=[
                                            PlotInformation(type=PlotInformation.LINE,
                                                            x_col=D,
                                                            y_col=E,
                                                            file=FileRef(path=output_file))
                                        ])
                    ])
                json.dump(report, report_file)
                remove_file(datafile)
            elif is_kcross(alg):
                datafile = par['datafile']
                model_file = par['model_file'] # model file
                m = [] # load_model(model_file)
                cv = CrossValidation()
                cv.set(m)
                ycolumns = par['ycolumns'] # array(int)
                xcolumns = par['xcolumns'] # array(int)
                data = load_csv_xy(datafile, ycolumns, xcolumns)
                cv.score(data)
                # generate output
                report_file = par['report_out'] # report_output
                # fill in the report
                report = make_report(
                    title='title',
                    desription='description',
                    created='created',
                    blocks=[
                    ])
                json.dump(report, report_file)
                remove_file(model_file)
                remove_file(datafile)
            else:
                raise Exception('failed to identify fitter algorithm')
        elif opr == 'predict':
            raise Exception('prediction was moved to the server')
            # model_file = par['model_file'] # model file
            # m = [] # load_model(model_file)
            # datafile = par['datafile'] # csv filename
            # xcolumns = par['xcolumns'] # array(int)
            # X = load_csv(datafile, xcolumns)
            # y_pred = m.predict(X)
            # # dump y_pred into file
            # # generate report file
            # remove_file(model_file)
            # remove_file(datafile)
        else:
            raise Exception('failed to identify operation')
    except Exception as error:
        logger.exception(error)
    finally:
        # eval("%s(%s)" % (par['function_name'], 'jsonfile'))
        remove_file(jsonfile)
        touch(successfile)
