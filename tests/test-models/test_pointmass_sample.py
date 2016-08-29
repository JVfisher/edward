from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf

from edward.models import PointMass
from edward.util import get_dims


def _test(params, n):
  x = PointMass(params=params)
  val_est = get_dims(x.sample(n))
  val_true = n + get_dims(params)
  assert val_est == val_true


class test_pointmass_sample_class(tf.test.TestCase):

  def test_0d(self):
    with self.test_session():
      _test(0.5, [1])
      _test(np.array(0.5), [1])
      _test(tf.constant(0.5), [1])

  def test_1d(self):
    with self.test_session():
      _test(np.array([0.5]), [1])
      _test(np.array([0.5]), [5])
      _test(np.array([0.2, 0.8]), [1])
      _test(np.array([0.2, 0.8]), [10])
      _test(tf.constant([0.5]), [1])
      _test(tf.constant([0.5]), [5])
      _test(tf.constant([0.2, 0.8]), [1])
      _test(tf.constant([0.2, 0.8]), [10])
