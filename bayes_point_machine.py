"""
Infer.Net Bayes Point Machine / Expectation Propagation demo

Adapted from C# tutorial code at http://goo.gl/k8R2AD

Matt Graham, December 2014
"""

from inferdotnet import *

def bayes_point_machine_model(x_data, y_data=None, w_dist=None, noise=0.1):
    """ Set up a Bayes Point machine classification model. """
    d_data = len(x_data[0])
    n_data = len(x_data)
    n_range = Models.Range(n_data)
    x = Variable.Array[Vector](n_range).Named("x")
    x.ObservedValue = Array[Vector]([Vector.FromArray(*x_i) for x_i in x_data])
    y = Variable.Array[bool](n_range).Named("y")
    if y_data is not None:
        assert len(x_data) == len(y_data)
        y.ObservedValue = Array[bool](y_data)
    if w_dist is None:
        w_dist = Distributions.VectorGaussian(
            Vector.Zero(d_data), 
            Maths.PositiveDefiniteMatrix.Identity(d_data)
        );
    w = Variable.Random(w_dist)
    y[n_range] = Variable.GaussianFromMeanAndVariance(
                     Variable.InnerProduct(w, x[n_range]), noise) > 0
    return x, y, w

def create_design_matrix(*features):
    """ Helper to construct design matrix from individual lists of features. """
    return [[float(val) for val in vals] + [1.] for vals in zip(*features)]

if __name__ == "__main__":
    incomes_train = [63,16,28,55,22,20]
    ages_train = [38,23,40,27,18,40]
    will_buy_train = [True, False, True, True, False, False]
    x_train = create_design_matrix(incomes_train, ages_train)
    x, y, w = bayes_point_machine_model(x_train, will_buy_train)
    engine = Infer.InferenceEngine(Infer.ExpectationPropagation())
    w_post = engine.Infer[Distributions.VectorGaussian](w)
    print('Posterior on weight parameters\n{0}'.format(w_post))
    incomes_test = [58, 18, 22]
    ages_test = [36, 24, 37]
    x_test = create_design_matrix(incomes_test, ages_test)
    x_test, y_test, w_test = bayes_point_machine_model(x_test, w_dist=w_post)
    y_pred = engine.Infer(y_test)
    print('Predictions on test inputs\n{0}'.format(y_pred))
    

