# --------------------------------------------------------------------
# This file is part of
# Weakly-supervised Pedestrian Attribute Localization Network.
#
# Weakly-supervised Pedestrian Attribute Localization Network
# is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Weakly-supervised Pedestrian Attribute Localization Network
# is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Weakly-supervised Pedestrian Attribute Localization Network.
# If not, see <http://www.gnu.org/licenses/>.
# --------------------------------------------------------------------

import numpy as np

def mA(attr, gt):
	num = attr.__len__()
	num_attrs = attr[0].__len__()

	for i in xrange(num_attrs):
		print '--------------------------------------------'
		print i
		print sum([attr[j][i] for j in xrange(num)]), \
			':', sum([attr[j][i] * gt[j][i] for j in xrange(num)]), \
			':', sum([gt[j][i] for j in xrange(num)])
		print sum([attr[j][i] * gt[j][i] for j in xrange(num)]) / sum([gt[j][i] for j in xrange(num)])
		print sum([(1 - attr[j][i]) for j in xrange(num)]), \
			':', sum([(1 - attr[j][i]) * (1 - gt[j][i]) for j in xrange(num)]), \
			':', sum([(1 - gt[j][i]) for j in xrange(num)])
		print sum([(1 - attr[j][i]) * (1 - gt[j][i]) for j in xrange(num)]) / sum([(1 - gt[j][i]) for j in xrange(num)])

	mA = (sum([(
		           sum([attr[j][i] * gt[j][i] for j in xrange(num)])
		           / sum([gt[j][i] for j in xrange(num)])
		           + sum([(1 - attr[j][i]) * (1 - gt[j][i]) for j in xrange(num)])
		           / sum([(1 - gt[j][i]) for j in xrange(num)])
	           ) for i in xrange(num_attrs)])) / (2 * num_attrs)
	return mA

def example_based(attr, gt):
	num = attr.__len__()
	num_attrs = attr[0].__len__()

	acc = 0
	prec = 0
	rec = 0
	f1 = 0

	attr = np.array(attr).astype(bool)
	gt = np.array(gt).astype(bool)
	
	for i in xrange(num):
		intersect = sum((attr[i] & gt[i]).astype(float))
		union = sum((attr[i] | gt[i]).astype(float))
		attr_sum = sum((attr[i]).astype(float))
		gt_sum = sum((gt[i]).astype(float))
		
		acc += intersect / union
		prec += intersect / attr_sum
		rec += intersect / gt_sum
	
	acc /= num
	prec /= num
	rec /= num
	f1 = 2 * prec * rec / (prec + rec)

	return acc, prec, rec, f1
