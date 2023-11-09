# Postmortem Report
  <img src="https://media.giphy.com/media/TqiwHbFBaZ4ti/giphy.gif" width="480" height="300" />
  
## **Issue Summary**

**Duration:** 40 minutes, from 00:00 PST to 00:40 PST on October 25, 2023

**Impact:** Users were unable to access our website due to a 504 error. Approximately 100% of users were affected.

**Root Cause:** A mistyped file name in the wp-settings.php file caused the Apache server to prematurely shut down.

### **Timeline**

-   **00:00 PST:** Users begin reporting a 504 error when trying to access the website.
-   **00:05 PST:** The engineering team is alerted to the issue.
-   **00:10 PST:** The engineering team investigates the issue and determines that it is being caused by a mistyped file name in the wp-settings.php file.
-   **00:12 PST:** The engineering team fixes the mistyped file name and restarts the Apache server.
-   **00:40 PST:** The issue is resolved and the website is back online.

**Misleading Investigation/Debugging Paths**

The engineering team initially investigated the issue by checking the server logs, but they did not find any useful information. They then tried restarting the Apache service, but that did not resolve the issue.

**Which Team/Individuals Was the Incident Escalated to**

The incident was escalated to the engineering manager and the on-call engineer.

**How the Incident Was Resolved**

The engineering team was able to resolve the issue by fixing the mistyped file name in the wp-settings.php file and restarting the Apache server.

## Root Cause and Resolution

<img src="https://media.giphy.com/media/26xBDPwbVGij9wIvu/giphy.gif" width="480" height="239"/>

**What Was Causing the Issue?**

A mistyped file name in the wp-settings.php file was causing the Apache server to prematurely shut down. This resulted in a 504 error for users who tried to access the website.

**How Was the Issue Fixed?**

The engineering team fixed the issue by correcting the mistyped file name in the wp-settings.php file and restarting the Apache server.

**Corrective and Preventative Measures**

**What Are the Things That Can Be Improved/Fixed (Broadly Speaking)?**

-   Improve documentation to ensure that file names are spelled correctly.
-   Implement automated tests to catch errors before code is deployed.
-   Improve monitoring to detect and alert on errors more quickly.

**A List of Tasks to Address the Issue (Be Very Specific, Like a TODO, Example: Patch Nginx Server, Add Monitoring on Server Memory)**

 - [x] Update wp-settings.php file to correct mistyped file name.

 - [x] Deploy changes to all servers.

 - [x] Implement automated tests to catch similar errors in the future.

 - [x] Improve monitoring to detect and alert on similar errors more
       quickly.

<img src="https://media.giphy.com/media/lD76yTC5zxZPG/giphy.gif" width="480" height="352">

I hope this postmortem report is attractive and informative. Please let me know if you have any other questions or feedback.
