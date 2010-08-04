This is a trac plugin which automatically adds the anonymous reporter email into the user's session.

This is useful when you want to make a helpdesk trac instance, open to anonymous users. They will put their email in the "reporter" field, pass a captcha test, and
submit tickets. The problem is that, whenever they want to comment or make another ticket, they are required to type their email over and over again, unless they 
go to 'preferences' and set their session's email address, which is unlikely to happen for 'normal' users.

This plugin simply adds the reporter email address into the session email field, when an anonymous user creates a ticket, and it doesn't already have a session email address.

Tested with trac 0.11

Based on the TracTicketValidator plugin by Richard Liao <richard.liao.i@gmail.com>
