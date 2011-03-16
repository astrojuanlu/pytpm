# -*- coding: utf-8 -*-
# Test various interfaces defined in the pytpm_times.pxi file.
import unittest
from pytpm import tpm

class TestDMSStructure(unittest.TestCase):
    """Test if the methods in the DMS class work."""
    def testCreate(self):
        """Must be able to create an DMS object."""
        dms = tpm.DMS()
        self.assertEqual(type(dms), tpm.DMS)
        
    def testGetFields(self):
        """Must be able to retrieve default values of fields."""
        dms = tpm.DMS()
        self.assertAlmostEqual(dms.dd, 0.0)
        self.assertAlmostEqual(dms.mm, 0.0)
        self.assertAlmostEqual(dms.ss, 0.0)

    def testSetFieldValuesAtInit(self):
        """Must be able to set values to fields at creation."""
        dms = tpm.DMS(dms={'dd':1.0,'mm':1.0,'ss':1.34})
        self.assertAlmostEqual(dms.dd, 1.0)
        self.assertAlmostEqual(dms.mm, 1.0)
        self.assertAlmostEqual(dms.ss, 1.34)
        
    def testSetFieldValues(self):
        """Must be able to set values after creation."""
        dms = tpm.DMS()
        dms.dd = 1.0
        dms.mm = 1.0
        dms.ss = 1.34
        self.assertAlmostEqual(dms.dd, 1.0)
        self.assertAlmostEqual(dms.mm, 1.0)
        self.assertAlmostEqual(dms.ss, 1.34)
        
    def testAddition(self):
        """Must perform addition of two DMS values."""
        dms1 = tpm.DMS()
        dms2 = tpm.DMS()
        dms1.dd = 1.1
        dms1.mm = 1.2
        dms1.ss = 1.3
        dms2.dd = 2.4
        dms2.mm = 2.5
        dms2.ss = 2.6
        dms = dms1 + dms2
        self.assertAlmostEqual(dms.dd, dms1.dd+dms2.dd)
        self.assertAlmostEqual(dms.mm, dms1.mm+dms2.mm)
        self.assertAlmostEqual(dms.ss, dms1.ss+dms2.ss)

    def testAdditionNonHMS(self):
        """Must raise exception if addition involves non DMS value."""
        dms = tpm.DMS() # All zeros.
        def add_dms(dms,x):
            return dms + x
        self.assertRaises(TypeError,add_dms, dms, 1)

    def testSubtraction(self):
        """Must perform subtraction of two DMS values."""
        dms1 = tpm.DMS()
        dms2 = tpm.DMS()
        dms1.dd = 1.1
        dms1.mm = 1.2
        dms1.ss = 1.3
        dms2.dd = 2.4
        dms2.mm = 2.5
        dms2.ss = 2.6
        dms = dms1 - dms2
        self.assertAlmostEqual(dms.dd, dms1.dd-dms2.dd)
        self.assertAlmostEqual(dms.mm, dms1.mm-dms2.mm)
        self.assertAlmostEqual(dms.ss, dms1.ss-dms2.ss)

    def testSubtractionNonDMS(self):
        """Must raise exception if subtraction involves non DMS value."""
        dms = tpm.DMS() # All zeros.
        def sub_dms(dms,x):
            return dms - x
        self.assertRaises(TypeError,sub_dms, dms, 1)

    def testRepr(self):
        """The __repr__ method must give proper output."""
        dms = tpm.DMS()
        dms.dd = 1.1
        dms.mm = 1.2
        dms.ss = 1.3
        d = eval(repr(dms))
        self.assertAlmostEqual(d['dd'], dms.dd) 
        self.assertAlmostEqual(d['mm'], dms.mm) 
        self.assertAlmostEqual(d['ss'], dms.ss) 
        
    def testUnicodeAndStr(self):
        """Test string representation."""
        dms = tpm.DMS()
        dms.dd = 1.0
        dms.mm = 2.0
        dms.ss = 3.0
        self.assertEqual(str(dms),"+01\xc2\xb0 02' 03.000\"")
        self.assertEqual(dms.__unicode__(),u"+01\u00B0 02' 03.000\"")

        
class TestHMSStructure(unittest.TestCase):
    """Test if the methods in the HMS class work."""
    def testCreate(self):
        """Must be able to create an HMS object."""
        hms = tpm.HMS()
        self.assertEqual(type(hms), tpm.HMS)
        
    def testGetFields(self):
        """Must be able to retrieve default values of fields."""
        hms = tpm.HMS()
        self.assertAlmostEqual(hms.hh, 0.0)
        self.assertAlmostEqual(hms.mm, 0.0)
        self.assertAlmostEqual(hms.ss, 0.0)

    def testSetFieldValuesAtInit(self):
        """Must be able to set values to fields at creation."""
        hms = tpm.HMS(hms={'hh':1.0,'mm':1.0,'ss':1.34})
        self.assertAlmostEqual(hms.hh, 1.0)
        self.assertAlmostEqual(hms.mm, 1.0)
        self.assertAlmostEqual(hms.ss, 1.34)
        
    def testSetFieldValues(self):
        """Must be able to set values after creation."""
        hms = tpm.HMS()
        hms.hh = 1.0
        hms.mm = 1.0
        hms.ss = 1.34
        self.assertAlmostEqual(hms.hh, 1.0)
        self.assertAlmostEqual(hms.mm, 1.0)
        self.assertAlmostEqual(hms.ss, 1.34)
        
    def testAddition(self):
        """Must perform addition of two HMS values."""
        hms1 = tpm.HMS()
        hms2 = tpm.HMS()
        hms1.hh = 1.1
        hms1.mm = 1.2
        hms1.ss = 1.3
        hms2.hh = 2.4
        hms2.mm = 2.5
        hms2.ss = 2.6
        hms = hms1 + hms2
        self.assertAlmostEqual(hms.hh, hms1.hh+hms2.hh)
        self.assertAlmostEqual(hms.mm, hms1.mm+hms2.mm)
        self.assertAlmostEqual(hms.ss, hms1.ss+hms2.ss)
        
    def testAdditionNonHMS(self):
        """Must raise exception if addition involves non HMS value."""
        hms = tpm.HMS() # All zeros.
        def add_hms(hms,x):
            return hms + x
        self.assertRaises(TypeError, add_hms, hms, 1)

    def testSubtraction(self):
        """Must perform subtraction of two HMS values."""
        hms1 = tpm.HMS()
        hms2 = tpm.HMS()
        hms1.hh = 1.1
        hms1.mm = 1.2
        hms1.ss = 1.3
        hms2.hh = 2.4
        hms2.mm = 2.5
        hms2.ss = 2.6
        hms = hms1 - hms2
        self.assertAlmostEqual(hms.hh, hms1.hh-hms2.hh)
        self.assertAlmostEqual(hms.mm, hms1.mm-hms2.mm)
        self.assertAlmostEqual(hms.ss, hms1.ss-hms2.ss)

    def testSubtractNonHMS(self):
        """Must raise exception if subtraction involves non HMS value."""
        hms = tpm.HMS() # All zeros.
        def sub_hms(hms,x):
            return hms - x
        self.assertRaises(TypeError,sub_hms, hms, 1)

    def testRepr(self):
        """The __repr__ method must give proper output."""
        hms = tpm.HMS()
        hms.hh = 1.1
        hms.mm = 1.2
        hms.ss = 1.3
        h = eval(repr(hms))
        self.assertAlmostEqual(h['hh'], hms.hh) 
        self.assertAlmostEqual(h['mm'], hms.mm) 
        self.assertAlmostEqual(h['ss'], hms.ss) 
        
    def testUnicodeAndStr(self):
        """Test string representation."""
        hms = tpm.HMS()
        hms.hh = 1.0
        hms.mm = 2.0
        hms.ss = 3.0
        self.assertEqual(str(hms)," 01H 02M 03.000S")
        self.assertEqual(hms.__unicode__(),u" 01H 02M 03.000S")

        
class TestYMDStructure(unittest.TestCase):
    def testCreate(self):
        """Must be able to create a YMD object."""
        ymd = tpm.YMD()
        self.assertEqual(type(ymd), tpm.YMD)

    def testGetFields(self):
        """Must be able to retrieve field values."""
        ymd = tpm.YMD()
        self.assertAlmostEqual(ymd.y, 0)
        self.assertAlmostEqual(ymd.m, 0)
        self.assertAlmostEqual(ymd.dd, 0.0)
        self.assertAlmostEqual(ymd.hh, 0.0)
        self.assertAlmostEqual(ymd.mm, 0.0)
        self.assertAlmostEqual(ymd.ss, 0.0)

    def testSetFieldValuesAtInit(self):
        """Must be able to initialize field values."""
        t = dict(y=2000, m=10, dd=16.789, hh=15.654, mm=1.345, ss=9.45)
        ymd = tpm.YMD(ymd=t)
        self.assertAlmostEqual(ymd.y, t['y'])
        self.assertAlmostEqual(ymd.m, t['m'])
        self.assertAlmostEqual(ymd.dd, t['dd'])
        self.assertAlmostEqual(ymd.hh, t['hh'])
        self.assertAlmostEqual(ymd.mm, t['mm'])
        self.assertAlmostEqual(ymd.ss, t['ss'])

    def testSetFieldValues(self):
        """Must be able to set field values."""
        t = dict(y=2010, m=11, dd=19.34, hh=29.3, mm=1.345, ss=10.8)
        ymd = tpm.YMD()
        ymd.y = t['y']
        ymd.m = t['m']
        ymd.dd = t['dd']
        ymd.hh = t['hh']
        ymd.mm = t['mm']
        ymd.ss = t['ss']
        self.assertAlmostEqual(ymd.y, t['y'])
        self.assertAlmostEqual(ymd.m, t['m'])
        self.assertAlmostEqual(ymd.dd, t['dd'])
        self.assertAlmostEqual(ymd.hh, t['hh'])
        self.assertAlmostEqual(ymd.mm, t['mm'])
        self.assertAlmostEqual(ymd.ss, t['ss'])

    def testNonIntegerYearMonth(self):
        """Must raise exception for non-integer year and month."""
        ymd = tpm.YMD()
        def non_int(ymd,y,m):
            ymd.y = y
            ymd.m = m
        self.assertRaises(AssertionError, non_int, ymd, 1.0, 1.0)

    def testSubtract(self):
        """Must be able to subtract two YMD values."""
        t1 = dict(y=2000, m=10, dd=16.789, hh=15.654, mm=1.345, ss=9.45)
        t2 = dict(y=2010, m=11, dd=19.34, hh=29.3, mm=1.345, ss=10.8)
        ymd1 = tpm.YMD()
        ymd2 = tpm.YMD()
        ymd1.y = t1['y']
        ymd1.m = t1['m']
        ymd1.dd = t1['dd']
        ymd1.hh = t1['hh']
        ymd1.mm = t1['mm']
        ymd1.ss = t1['ss']
        ymd2.y = t2['y']
        ymd2.m = t2['m']
        ymd2.dd = t2['dd']
        ymd2.hh = t2['hh']
        ymd2.mm = t2['mm']
        ymd2.ss = t2['ss']
        ymd = ymd1 - ymd2
        self.assertAlmostEqual(ymd.y, t1['y'] - t2['y'])
        self.assertAlmostEqual(ymd.m, t1['m'] - t2['m'])
        self.assertAlmostEqual(ymd.dd, t1['dd'] - t2['dd'])
        self.assertAlmostEqual(ymd.hh, t1['hh'] - t2['hh'])
        self.assertAlmostEqual(ymd.mm, t1['mm'] - t2['mm'])
        self.assertAlmostEqual(ymd.ss, t1['ss'] - t2['ss'])

    def testSubtractNonYMD(self):
        """Must raise exception if subtraction involves non YMD value."""
        ymd = tpm.YMD() # All zeros.
        def sub_ymd(ymd,x):
            return ymd - x
        self.assertRaises(TypeError,sub_ymd, ymd, 1)
        
    def testUnicodeAndStr(self):
        """Must be able to get proper string represenations."""
        # The ouput strings were obtained from
        # pytpm/tests/c_tests/fmt_ymd_test.c
        t = dict(y=2010, m=10, dd=16.789, hh=15.654, mm=1.345, ss=9.45)
        t1 = dict(y=-1, m=10, dd=1.0, hh=23.9999, mm=54.0, ss=9.45)
        ymd = tpm.YMD()
        ymd.y = t['y']
        ymd.m = t['m']
        ymd.dd = t['dd']
        ymd.hh = t['hh']
        ymd.mm = t['mm']
        ymd.ss = t['ss']
        s = str(ymd)
        self.assertEqual(s, "Sun Oct 17 10:36:54.149 2010")
        s = unicode(ymd)
        self.assertEqual(s, u"Sun Oct 17 10:36:54.149 2010")
        ymd = tpm.YMD()
        ymd.y = t1['y']
        ymd.m = t1['m']
        ymd.dd = t1['dd']
        ymd.hh = t1['hh']
        ymd.mm = t1['mm']
        ymd.ss = t1['ss']
        s = str(ymd)
        self.assertEqual(s, "Sat Oct  2 00:54:09.090    2 BC")
        s = unicode(ymd)
        self.assertEqual(s, u"Sat Oct  2 00:54:09.090    2 BC")


class TestJDStructure(unittest.TestCase):
    def testCreate(self):
        """Must be able to create a JD object."""
        jd = tpm.JD()
        self.assertEqual(type(jd), tpm.JD)

    def testGetFields(self):
        """Must be able to retrieve values of fields."""
        jd = tpm.JD()
        self.assertEqual(jd.dd, 0.0)
        self.assertEqual(jd.hh, 0.0)
        self.assertEqual(jd.mm, 0.0)
        self.assertEqual(jd.ss, 0.0)

    def testSetFieldValuesAtInit(self):
        """Must be able to set fields of JD at initialization."""
        j = dict(dd=2451445.0, hh=12.0, mm=0.0, ss=0.0)
        jd = tpm.JD(j)
        self.assertEqual(jd.dd, j['dd'])
        self.assertEqual(jd.hh, j['hh'])
        self.assertEqual(jd.mm, j['mm'])
        self.assertEqual(jd.ss, j['ss'])

    def testSetFieldValues(self):
        """Must be able to set fields of a JD object."""
        j = dict(dd=2451445.0, hh=12.0, mm=0.0, ss=0.0)
        jd = tpm.JD()
        jd.dd = j['dd']
        jd.hh = j['hh']
        jd.mm = j['mm']
        jd.ss = j['ss']
        self.assertEqual(jd.dd, j['dd'])
        self.assertEqual(jd.hh, j['hh'])
        self.assertEqual(jd.mm, j['mm'])
        self.assertEqual(jd.ss, j['ss'])

    def testAddition(self):
        """Must be able to add two JD values."""
        j1 = dict(dd=2451445.0, hh=12.0, mm=0.0, ss=0.0)
        j2 = dict(dd=1.0, hh=2.3, mm=23.4, ss=2.0)
        jd1 = tpm.JD()
        jd1.dd = j1['dd']
        jd1.hh = j1['hh']
        jd1.mm = j1['mm']
        jd1.ss = j1['ss']
        jd2 = tpm.JD()
        jd2.dd = j2['dd']
        jd2.hh = j2['hh']
        jd2.mm = j2['mm']
        jd2.ss = j2['ss']
        jd = jd1 + jd2
        self.assertEqual(jd.dd, jd1.dd + jd2.dd)
        self.assertEqual(jd.hh, jd1.hh + jd2.hh)
        self.assertEqual(jd.mm, jd1.mm + jd2.mm)
        self.assertEqual(jd.ss, jd1.ss + jd2.ss)

    def testAddNonJD(self):
        """Must raise exception if subtraction involves non JD value."""
        jd = tpm.JD() # All zeros.
        def add_jd(jd,x):
            return jd - x
        self.assertRaises(TypeError,add_jd, jd, 1)
                        
    def testSubtraction(self):
        """Must be able to subtract two JD values."""
        j1 = dict(dd=2451445.0, hh=12.0, mm=0.0, ss=0.0)
        j2 = dict(dd=1.0, hh=2.3, mm=23.4, ss=2.0)
        jd1 = tpm.JD()
        jd1.dd = j1['dd']
        jd1.hh = j1['hh']
        jd1.mm = j1['mm']
        jd1.ss = j1['ss']
        jd2 = tpm.JD()
        jd2.dd = j2['dd']
        jd2.hh = j2['hh']
        jd2.mm = j2['mm']
        jd2.ss = j2['ss']
        jd = jd1 - jd2
        self.assertEqual(jd.dd, jd1.dd - jd2.dd)
        self.assertEqual(jd.hh, jd1.hh - jd2.hh)
        self.assertEqual(jd.mm, jd1.mm - jd2.mm)
        self.assertEqual(jd.ss, jd1.ss - jd2.ss)

    def testSubtractNonJD(self):
        """Must raise exception if subtraction involves non JD value."""
        jd = tpm.JD() # All zeros.
        def sub_jd(jd,x):
            return jd - x
        self.assertRaises(TypeError,sub_jd, jd, 1)
    
    def testRepr(self):
        """Must give proper repr string."""
        j = dict(dd=2451445.0, hh=12.0, mm=0.0, ss=0.0)
        jd = tpm.JD()
        jd.dd = j['dd']
        jd.hh = j['hh']
        jd.mm = j['mm']
        jd.ss = j['ss']
        self.assertEqual(j, eval(repr(jd)))

    def testUnicodeAndStr(self):
        """Must give proper string representations."""
        # Output strings used as checks are from the file pytpm/tests
        # /c_tests/fmt_jd_test.c.
        s1 = " 2451545  12H 00M 00.000S"
        s2 = " 2456745  15H 06M 50.515S"
        j1 = dict(dd=2451545.0, hh=12.0, mm=0.0, ss=0.0)
        j2 = dict(dd=2456745.2456, hh=9.0, mm=12.3446, ss=49.99999)
        jd1 = tpm.JD()
        jd2 = tpm.JD()
        jd1.dd = j1['dd']
        jd1.hh = j1['hh']
        jd1.mm = j1['mm']
        jd1.ss = j1['ss']
        jd2.dd = j2['dd']
        jd2.hh = j2['hh']
        jd2.mm = j2['mm']
        jd2.ss = j2['ss']

        self.assertEqual(str(jd1), s1)
        self.assertEqual(unicode(jd1), unicode(s1))
        self.assertEqual(str(jd2), s2)
        self.assertEqual(unicode(jd2), unicode(s2))
        
if __name__ == '__main__':
    unittest.main()
