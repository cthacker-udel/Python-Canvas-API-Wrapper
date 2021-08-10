# Unofficial Python Canvas-LMS Wrapper
> Author : Cameron Thacker (cthacker@udel.edu)

> This wrapper centers around two files, CanvasClient and CanvasRestAPI, both which do most of the handling. Implementing the sub-classes that are implemented to store the variables and values used in requests differeing from POST to PUT to GET, allows for ease of integration if one method does not successfully complete, then instead of looking at a file of 1000 lines, you can examine a single file of 100 lines and discern which variable was incorrect or if the field was passed.


Each storage class (*classes besides CanvasClient and CanvasRestAPI*), implements two methods: 
1. **generate_queries(no args)** 
2. **clear_queries(no args)**

* **generate_queries(no args)** accesses all the class's attributes and constructs a dictionary object which can be passed as json or data via requests interface

* **clear_queries(no args)** clears all attributes (*setting them back to None*) to avoid having conflicts if making separate requests, or the attributes may simply be reset with the dot notation when directly accessing the class from its instantiated state

The following APIs are currently implemented :

* Account API
  * (*CanvasAccount.py*)
* Account Domain Lookup API
  * (*CanvasAccountDomainLookup.py*)
* Account Notifications API
  * (*CanvasAccountNotifications.py*)
* Account Report API
  * (*CanvasAccountReport.py*)
* Admin API
  * (*CanvasAdmin.py*)
* Analytics API
  * (*CanvasAnalytics.py*)
* Announcements API
  * (*CanvasAnnouncements.py*)
* Assignment Extensions API
  * (*CanvasAssignmentExtensions.py*)
* Assignment Groups API
  * (*CanvasAssignmentGroups.py*)
* Assignments API
  * (*CanvasAssignments.py*)
* External Feed API
  * (*CanvasExternalFeed.py*)
* Token Scopes API
  * (*CanvasTokenScopes.py*)


---

> Source : https://canvas.instructure.com/doc/api/
