<h2 class="content-heading">Contacts</h2>
<div class="status_message"> </div>
<form style="float:left;margin-right:40px;" action="#" method="post" id="contact_form">
  <p>
    <label>Your Name:<br />
      <input type="text" size="40" name="name" id="contact_name" />
    </label>
  </p>
  <p>
    <label>E-mail*:<br />
      <input type="text" size="40" name="email" id="contact_email" onkeyup="validateEmail()"/>
    </label>
  </p>
  <p>
    <label>Subject:<br />
      <input style="color:#777" type="text" size="40" id="contact_subject" value="Are you available to do some work for me?" name="subject" />
    </label>
  </p>
  <p>
    <label>Message*:<br />
      <textarea cols="40" rows="10" name="message" id="contact_message" onkeyup="validateMessage()"></textarea>
    </label>
  </p>
  <p>Fields marked with an asterisk(*) are required!</p>
  <input class="button" type="submit" name="submit" value="Send Message" />
</form>
<div>
  <div class="vcard">
    <h3 class="fn org small-heading">Wong Jiang Fung</h3>
    <div class="adr">
      <div class="street-address"></div>
      <span class="locality"></span><span class="postal-code"></span>
      <div class="country-name">Singapore</div>
    </div>
    <div class="tel"><span class="type"></span></div>
    <div class="tel"><span class="type"></span></div>
    <div>Email: <span class="email">kakarukeys [at]<br />gmail [dot] com</span><br /><br /></div>
    <div>Gtalk: <span class="email">kakarukeys [at]<br />gmail [dot] com</span><br /><br /></div>
    <div>Skype name: kakarukeys</div>
  </div>
</div>
