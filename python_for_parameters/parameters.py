#!/usr/bin/env python3
# -*- coding: utf-8 -*-


global PARAMETERS
PARAMETERS   = None

# ========================================
class Parameters( ):
    """
    manages parameter values: use it like an ini file but it is code
    """
    # -------
    def choose_mode( self ):
        """
        typically choose one mode
            if you comment all out all modes you get the default mode which should
            run, perhaps not in the way you want
            all modes are run on top of the drfaults so they need only include
            changes from the drfault
        """
        pass    # when all else ic commented out
        self.mode_new_user()
        #


    # ---- ---->> Methods:  one for each mode
    # -------
    def mode_new_user( self ):
        """
        a mode for the new user, pretty much empty,
        a new user may experiment here.
        """
        self.mode               = "mode_new_user"
        # but do they use the same units ?
        self.qt_width           = 1200


    # ------->> default mode, always call
    def mode_default( self ):
        """
        sets up prett        #rint( self ) # for debugging y much all settings
        documents the meaning of the modes
        call first, then override as necessary
        good chance these settings will at least let the app run
        """
        self.mode              = "mode_default" # I always name a moed like this.
        self.parameter_1       = "i am the second parameter"

        # screen width for a qt application
        self.qt_width          = 1200
        # then go on with as much as you want

    # -----------------------------------
    def __str__( self,   ):
        """
        sometimes it is hard to see where values have come out this may help if printed.
        not complete, add as needed -- compare across applications and code above
        """
        a_str   = ""
        a_str   = ">>>>>>>>>>* parameters *<<<<<<<<<<<<"
        a_str   = f"{a_str}\n    {self.mode = }"
        a_str   = f"{a_str}\n    {self.parameter_1 = }"
        a_str   = f"{a_str}\n    {self.qt_width = }"
        return a_str

    # -------
    def __init__( self, ):
        """
        Init for the instance, usually not modified, except perhaps to debug
        I keey way be down in listing because it should not be messed with.
        """
        self.mode_default()
        self.choose_mode()

# ---------------
def create_if_needed( ):
    global PARAMETERS
    if not PARAMETERS:

         print( "creating global parameters.PARAMETERS")
         PARAMETERS    = Parameters()

# --------------------
create_if_needed()
