# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Name:         tracautosessionmail.py
# Purpose:      Automatically add the reporter email in the current user session, if anonymous.
#
# Author:       Richard Liao <richard.liao.i@gmail.com>
# Author:       Marko Mikulicic <marko.mikulicic@isti.cnr.it>
#
#----------------------------------------------------------------------------
from trac.config import BoolOption, IntOption, ListOption

from trac.core import *
from trac.ticket.api import ITicketManipulator
from trac.ticket.model import Ticket
from trac.util.html import html, Markup

import re

class TicketAutoSessionMail(Component):
    """ If an anonymous user creates a new ticket with a valid email address, put this address in the user's session
    """
    
    implements(ITicketChangeListener)

    # ITicketChangeListener methods
    def ticket_created(ticket):
        """Called when a ticket is created."""

        # is logged in?
        if req.authname == 'anonymous':
           isLoggedIn = False
        else:
           isLoggedIn = True
           
        # get author
        author = req.args.get("author")
        reporter = ticket.values.get("reporter")
        
        self.env.log.info("WOWOW")
                
    def _isValidateEmail(self, email):
        if not email:
            return False

        if len(email) > 7:
            if re.match("^[a-zA-Z0-9._%-]+@[a-zA-Z0-9._%-]+\.[a-zA-Z]{2,6}$", email) != None:
                return True
        return False

