<h2 class="content-heading">jqSolr v3</h2>
<h3 class="small-heading">A new data access layer</h3>
<p>A client has decided to switch the storage engine of their Django project from Postgres (a relational database) to Apache Solr (a full text search engine). Their code relied on Django ORM to perform many different kinds of analytical queries. They did not know how to make the switch such that the view codes need not be changed so much. Thing has gone wrong when bugs appeared from nowhere and the code looked like a plate of spaghetti.</p>

<p>I stepped in and took over from the previous programmer. I did a thorough code review. I wrote a complete test suite for the old system, wrote the new data access layer and a new Django manager such that all tests passed. I made the switch flawlessly and transparently for them. No view code is hurt in the process.</p>

<p align="center"><img src="images/folio/jqsolr-clip01m.jpg" width="600" alt="" /></p>
<p>This project was completed in one week within schedule.</p>

