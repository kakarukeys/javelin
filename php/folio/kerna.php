<h2 class="content-heading">Project Kerna</h2>
<h3 class="small-heading">A distributed realtime stream-processing backend</h3>
<p>As a startup grows bigger, its existing backend may not be able to sustain the ever increasing load. While I was working for <a href="http://jamiq.com" target="_blank">JamiQ Pte. Ltd.</a>, my boss realized that we were heading towards that situation. He planned for a new, scalable and more resilient backend and assigned me and another engineer to work on it.</p>

<p>We implemented the new backend in Clojure on top of <a href="http://storm-project.net/" target="_blank">Twitter Storm</a>. It has a few properties:</p>
<ol>
    <li>Fault-tolerance: if a node, worker or daemon dies, it is restarted and the operation is not affected.</li>
    <li>Easy migration: one can easily port the legacy components to the new architecture.</li>
    <li>Realtime processing: No intermediate storage, no offline processing is needed.</li>
    <li>Scalable: if the load increases, just add one more node, increase the parallelism to coup with it.</li>
</ol>

<h3 class="small-heading">Stream processing</h3>
<p>With an extensive test suite, I ensure that the data stream is processed correctly by the various existing algorithms and modules in a continuous manner. Click the diagram below to see an overview of the architecture.</p>
<p align="center"><a href="images/folio/kerna-clip01b.png" target="_blank"><img src="images/folio/kerna-clip01m.png" alt="" /></a></p>

<h3 class="small-heading">Project Kerna is powered by:</h3>
<ul>
  <li>Clojure</li>
  <li>Twitter Storm</li>
  <li>Redis</li>
  <li>Linux</li>
</ul>

<p>This is a major backend project I have ever worked on.</p>

