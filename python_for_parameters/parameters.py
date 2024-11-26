#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:36:58 2024

@author: russ
"""




# # --------------------
# if __name__ == "__main__":
#     #----- run the full app
#     import main

#     #main.main()
# # --------------------

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
            and if you wish add the plus_test_mode
            if you comment all out all modes you get the default mode which should
            run, perhaps not in the way you want
        """
        self.mode_new_user()
        #self.new_user_mode()
        #self.millhouse_1_mode()

        # two of my computers
        #self.mode_millhouse_mint()
        #self.mode_theprof_mint()
        #self.russ_1_mode()

        # --- add on for testing, use as desired edit mode for your needs
        #self.plus_test_mode()


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
        self.mode              = "default"
        self.parameter_1       = "i am the second parameter"

        # screen width for a qt application
        self.qt_width          = 1200


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
        Init for instance, usually not modified, except perhaps to debug
        may be down in listing because it should not be messed with.
        """
        self.mode_default()
        self.choose_mode()


# ---------------
#def create_if_needed( ):
global PARAMETERS
if not PARAMETERS:

     print( "creating global parameters.PARAMETERS")
     PARAMETERS    = Parameters()

# --------------------
#create_if_needed()
