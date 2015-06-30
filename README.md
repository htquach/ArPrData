Copyright (c) 2015 Hong Quach

This source file is licensed under the "MIT License."  Please see the LICENSE
in this distribution for license terms.

# ArPrData
Archive and Purge Data

The ArPrData is an application that will handle the data archival and purging
for a given database.

The objective of this application is that any data driven application that
need to have data archival and/or purging enforced simply configure this
application and let this application handles that.  The user only need to
provide a connection string and a set of policies.  This application will
carry out the action.