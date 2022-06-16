"""Creates classes dealing with the location of bodies in space.

Classes:
* ReferenceFrame -- set up a reference frame
* TestReferenceFrameMethods
  -- test all methods of the ReferenceFrame class
* Transformation
  -- set up a generalized transformation between reference frames
* Translation -- set up a translation between reference frames
* Rotation -- set up a rotation between reference frames
"""

import unittest


class ReferenceFrame:
    """Set up a reference frame.

    Instance variables:
    * mytype -- None, 'moving', or 'fixed' (defafult None)
    * myname -- a description (default None)
    """

    def settype(self, mytype):
        """Specify the type of the reference frame.

        Arguments:
        * mytype -- None, 'moving', or 'fixed'"
        """
        if not(mytype is None or mytype == "fixed" or mytype == "moving"):
            print("Error: mytype : None, 'moving', 'fixed'")
            self.mytype = None
        else:
            self.mytype = mytype

    def setname(self, myname):
        """Specify the name of the reference frame.

        Arguments:
        * myname -- a description
        """
        if not(myname is None or isinstance(myname, str)):
            print("Error: myname : None, <str>")
            self.myname = None
        else:
            self.myname = myname

    def __init__(self, mytype=None, myname=None):
        """Specify the type and name of a reference frame."""
        ReferenceFrame.settype(self, mytype)
        ReferenceFrame.setname(self, myname)

    def __repr__(self):
        return "ReferenceFrame(mytype=%r, myname=%r)" \
               % (self.mytype, self.myname)

    def __str__(self):
        if self.mytype is not None:
            if self.myname is not None:
                return "%s reference frame attached to %s" \
                       % (self.mytype, self.myname)
            return "%s reference frame" % self.mytype
        if self.myname is not None:
            return "fixed or moving reference frame attached to %s" \
                   % self.myname
        return "fixed or moving reference frame"


class TestReferenceFrameMethods(unittest.TestCase):
    """Test all methods of the ReferenceFrame class."""

    def setUp(self):
        self.frame = ReferenceFrame()

    def test_settype(self):
        """Test the settype method of the ReferenceFrame class."""
        with self.subTest(mytype="fixed"):
            self.frame.settype("fixed")
            self.assertEqual(self.frame.mytype, "fixed")
        with self.subTest(mytype=None):
            self.frame.settype(None)
            self.assertIsNone(self.frame.mytype)
        with self.subTest(mytype=1):
            self.frame.settype(1)
            self.assertIsNone(self.frame.mytype)

    def test_setname(self):
        """Test the setname method of the ReferenceFrame class."""
        with self.subTest(myname="<name>"):
            self.frame.setname("<name>")
            self.assertEqual(self.frame.myname, "<name>")
        with self.subTest(myname=None):
            self.frame.setname(None)
            self.assertIsNone(self.frame.myname)
        with self.subTest(myname=1):
            self.frame.setname(1)
            self.assertIsNone(self.frame.myname)

    def test__init__(self):
        """Test the __init__ method of the ReferenceFrame class."""
        with self.subTest(mytype="fixed"):
            self.assertEqual(ReferenceFrame(mytype="fixed").mytype, "fixed")
        with self.subTest(myname="<name>"):
            self.assertEqual(ReferenceFrame(myname="<name>").myname, "<name>")

    def test__repr__(self):
        """Test the ___repr__ method of the ReferenceFrame class."""
        with self.subTest(mytype="fixed", myname="<name>"):
            self.assertEqual(
                ReferenceFrame("fixed", "<name>").__repr__(),
                "ReferenceFrame(mytype='fixed', myname='<name>')")
        with self.subTest(mytype=None, myname=None):
            self.assertEqual(ReferenceFrame(None, None).__repr__(),
                             "ReferenceFrame(mytype=None, myname=None)")

    def test__str__(self):
        """Test the __str__ method of the ReferenceFrame class."""
        with self.subTest(mytype="fixed", myname="<name>"):
            self.assertEqual(ReferenceFrame("fixed", "<name>").__str__(),
                             "fixed reference frame attached to <name>")
        with self.subTest(mytype="fixed", myname=None):
            self.assertEqual(ReferenceFrame("fixed", None).__str__(),
                             "fixed reference frame")
        with self.subTest(mytype=None, myname="<name>"):
            self.assertEqual(
                ReferenceFrame(None, "<name>").__str__(),
                "fixed or moving reference frame attached to <name>")
        with self.subTest(mytype=None, myname=None):
            self.assertEqual(ReferenceFrame(None, None).__str__(),
                             "fixed or moving reference frame")


class Transformation:
    """Set up a generalized transformation between reference frames."""

    def __init__(self, source_frame=None, destination_frame=None):
        self.source_frame = source_frame
        self.destination_frame = destination_frame


class Translation(Transformation):
    """Set up a translation between reference frames."""

    def __init__(self, source_frame=None, destination_frame=None,
                 position_vector=None):
        super().__init__(source_frame, destination_frame)
        self.position_vector = position_vector


class Rotation(Transformation):
    """Set up a rotation between reference frames."""

    def __init__(self, source_frame=None, destination_frame=None,
                 orientation_matrix=None):
        super().__init__(source_frame, destination_frame)
        self.orientation_matrix = orientation_matrix


unittest.main()

A = ReferenceFrame(mytype='fixed')
B = ReferenceFrame(mytype='moving')
T = Transformation(source_frame=A, destination_frame=B)
P = Translation(source_frame=A, destination_frame=B)
