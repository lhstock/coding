//
var assert = require('assert');

describe('Array',function() {
	describe('#indexOf()',function() {
		var s = 'should return -1 when the value is not present';
		it(s,function() {
			assert.equal(-1,[1,2,3],indexOf(4));
		})
	})
})