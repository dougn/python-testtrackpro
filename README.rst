TestTrack SOAP Python Interface
===================================

TestTrack Pro is the Issue Management software from Seapine Software

TestTrack is a registered trademark of Seapine Software.
http://www.seapine.com/testtrack.html

This library uses the suds library to talk to the TestTrack SDK SOAP API
and includes some helpful extensions for managing your client code and
interactions. There are a number of issues (and crashes) when talking to the
latest TestTrack SOAP API using suds, and this library addresses those.

While this module is named ``testtrackpro`` it will work with TestTrack RM
(Requirement Management) and TestTrack TCM (Test Case Management).

The TestTrack SOAP API uses a client cookie for managing login sessions.
This cookie must be supplied on (almost) every API call. This library
provides a client wrapper object which will manage the session cookie, and
even releasing the cookie (logging off) as part of a context exit.

The TestTrack SOAP API includes entity edit locking where a write lock is
implicit in every edit API call. The client must release the lock with either
a save or cancelSave API call. The lock will remain for 15 minuites, making
other attepts to edit fail on the entity.

Python contexts allow for dealing with safely releasing locks on success or
error. All objects returned form API calls which start with the string 'edit'
will return a context object that can be used with the 'with' statement.
At the end of the statement block the appropriate 'save' API call will be
made. If an exception occurs in the block, the appropriate 'cancelSave' API
call will be made. In either situation the lock will be released.

.. code:: python

    import testtrackpro
    with testtrackpro.TTP('http://hostname/', 'Project', 'username', 'password') as ttp:
        with ttp.editDefect(11, bDownloadAttachments=False) as defect:
            defect.priority = "Immediate"
        ## ttp.saveDefect(defect) is called, or ttp.cancelSave(defect.recordid) on exception.
    ## ttp.DatabaseLogoff() is called, even if an exception occured.


Additionally there is a new special edit context API extension when using
python contexts for ignoring the edit lock error, when someone else has the
edit lock on an entity. This is very useful when you do not want your script
or service to error out on a failed edit lock, but instead want to continue
processing.


.. code:: python

    import testtrackpro
    with testtrackpro.TTP('http://hostname/', 'Project', 'username', 'password') as ttp:
        with ttp.editDefect(11, bDownloadAttachments=False, ignoreEditLockError=True) as defect:
            defect.priority = "Immediate"
        ## ttp.saveDefect(defect) is called, or ttp.cancelSave(defect.recordid) on exception.
        
        assert not testtrackpro.have_edit_lock(defect)
        
        if testtrackpro.was_saved(defect):
            # The priority was changed
            pass
        elif testtrackpro.has_errored(defect):
            # It was not saved due to an error
            pass
            if testtrackpro.edit_lock_failed(defect):
                # because the edit lock failed
                pass
            else:
                # because of some other error
                # NOTE: unless there was other code to catch and ignore the
                #       error, this code is unreachable.
                pass
    ## ttp.DatabaseLogoff() is called, even if an exception occured.


References
----------

Project:

* `Documentation <http://pythonhosted.org/testtrackpro/>`_
* `PyPi <https://pypi.python.org/pypi/testtrackpro>`_
* `GitHub <https://github.com/dougn/python-testtrackpro>`_

External:

* `suds <https://fedorahosted.org/suds/>`_
* `Seapine Software <http://www.seapine.com/>`_
* `TestTrack <http://www.seapine.com/testtrack.html>`_
* `TestTrack Pro <http://www.seapine.com/ttpro.html>`_
* `TestTrack SOAP API <http://labs.seapine.com/TestTrackSDK.php>`_
* `TestTrack Python Tutorial <http://labs.seapine.com/wiki/index.php/TestTrack_SOAP_SDK_Tutorial_-_Python>`_
