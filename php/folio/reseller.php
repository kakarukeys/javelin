<h2 class="content-heading">Reseller permission handling</h2>
<h3 class="small-heading">A classic problem</h3>

<p>A Saas company wanted to expand its business by selling resellership. They hired me to upgrade their django website to put in proper object-level permissions that segregate each reseller from others on the frontend as well as in the Django admin backend.</p>

<blockquote class="stylish">How can every user of every role be able to access the objects and only the objects he is allowed to access?</blockquote>

<p>The complexity of the project lies in the number of different levels the user hierarchy has. The company has many resellers. Each reseller may sell to different clients, each of them has his own group of users. Each level of the hierarchy has a staff and non-staff status. A staff at group level may only access objects belonging to the group, likewise for other levels. If there are two resellers, two groups for each, ten users for each, two types of credentials - all together 80 combinations I need to cover. If any combination is not covered, there will be a security breach.</p>

<p>The project was completed in 3 weeks with automated regresssion testing using Selenium. The company has registered many resellers. No security breach has been found.</p>

<p align="center"><a href="images/folio/reseller-clip01b.jpg" target="_blank"><img src="images/folio/reseller-clip01m.jpg" alt="" /></a></p>

