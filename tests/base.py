import unittest
from weirdict import BaseNormalizedDict

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.empty = BaseNormalizedDict()
        self.d = BaseNormalizedDict(foo='bar')
    
    def test_init(self):
        BaseNormalizedDict()
        BaseNormalizedDict(foo='bar')
        BaseNormalizedDict({'foo': 'bar'})
        BaseNormalizedDict([('foo', 'bar')])
        BaseNormalizedDict({'foo': 'bar'}, bar='baz')
        BaseNormalizedDict({'foo': 'bar'}, bar='baz', baz='quux')
        BaseNormalizedDict([('foo', 'bar')], bar='baz')
        BaseNormalizedDict([('foo', 'bar')], bar='baz', baz='quux')
    
    def test_contains(self):
        self.assertIn('foo', self.d)
    
    def test_ncontains(self):
        self.assertNotIn('bar', self.d)
    
    def test_len(self):
        self.assertEqual(len(self.empty), 0)
        self.assertEqual(len(self.d), 1)
    
    def test_getitem(self):
        self.assertEqual(self.d['foo'], 'bar')
        with self.assertRaises(KeyError):
            self.d['bar']
    
    def test_setitem(self):
        self.d['foo'] = 'baz'
        self.d['bar'] = 'baz'
        self.assertEqual(self.d['foo'], 'baz')
        self.assertEqual(self.d['bar'], 'baz')
    
    def test_delitem(self):
        del self.d['foo']
        with self.assertRaises(KeyError):
            self.d['foo']
        with self.assertRaises(KeyError):
            del self.d['bar']
    
    def test_copy(self):
        copy = self.d.copy()
        self.assertEqual(copy['foo'], 'bar')
    
    def test_copy_changed(self):
        copy = self.d.copy()
        copy['foo'] = 'baz'
        self.assertEqual(self.d['foo'], 'bar')
        self.assertEqual(copy['foo'], 'baz')
    
    def test_get(self):
        self.assertEqual(self.d.get('foo'), 'bar')
        self.assertIsNone(self.d.get('bar'))
        self.assertEqual(self.d.get('bar', 'baz'), 'baz')
    
    def test_pop(self):
        self.assertEqual(self.d.pop('foo'), 'bar')
        self.assertRaises(KeyError, self.d.pop, ('foo',))
    
    def test_pop_default(self):
        self.assertRaises(KeyError, self.d.pop, ('bar',))
        self.assertEqual(self.d.pop('bar', 'baz'), 'baz')
