import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication



html_body = f"""<!DOCTYPE html>
<!--Code By Webdevtrick ( https://webdevtrick.com )-->
<html lang="en">

<head>
  <meta charset="UTF-8">
  <title>HTML Email Template | Webdevtrick.com</title>
<!--The following script tag downloads a font from the Adobe Edge Web Fonts server for use within the web page. We recommend that you do not modify it.--><script>var __adobewebfontsappname__="dreamweaver"</script><script src="http://use.edgefonts.net/annie-use-your-telescope:n4:default;averia-sans-libre:n4:default.js" type="text/javascript"></script>
</head>

<body>

  <table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">

<!--HEADER -->

		<tbody><tr>
			<td align="center">
				<table class="col-600" width="600" border="0" align="center" cellpadding="0" cellspacing="0">
					<tbody><tr>
						<td align="center" valign="top" background="https://g.foolcdn.com/image/?url=https%3A//g.foolcdn.com/editorial/images/593788/bear-wearing-a-mask-stock-market-crash.jpg&w=2000&op=resize" bgcolor="#66809b" style="background-size:cover; background-position:top;height=" 400""="">
							<table class="col-600" width="600" height="400" border="0" align="center" cellpadding="0" cellspacing="0">

								<tbody><tr>
									<td height="40"></td>
								</tr>


								<tr>
									<td align="center" style="line-height: 0px;">
										<img style="display:block; line-height:0px; font-size:0px; border:0px;" src="https://png.pngtree.com/png-clipart/20211009/original/pngtree-alien-logo-hip-pop-style-green-png-image_6841197.png" width="109" height="115" alt="logo">
									</td>
								</tr>



								<tr>
									<td align="center" style="font-family: 'Raleway', sans-serif; font-size:37px; color:#ffffff; line-height:24px; font-weight: bold; letter-spacing: 5px;">
										 <span style="font-family: 'Raleway', sans-serif; font-size: 35px; color: #ffffff; line-height: 39px; font-weight: bolder; letter-spacing: 5px;">STOCK ALERT NEWS&nbsp;</span>
									</td>
								</tr>





								<tr>
								  <td align="center" style="font-family: 'Lato', sans-serif; font-size:15px; color:#ffffff; line-height:24px; font-weight: 300;">&nbsp;
								   </td>
								</tr>


								<tr>
									<td height="50"></td>
								</tr>
							</tbody></table>
						</td>
					</tr>
				</tbody></table>
			</td>
		</tr>


<!-- END HEADERR -->


<!-- START SHOWCASE -->

		<tr>
			<td align="center">
				<table class="col-600" width="600" border="0" align="center" cellpadding="0" cellspacing="0" style="margin-left:20px; margin-right:20px; border-left: 1px solid #dbd9d9; border-right: 1px solid #dbd9d9;">
					<tbody><tr>
						<td height="10"></td>
					</tr>

					<tr>
						<td align="center" style="font-family: 'Raleway', sans-serif; font-size:22px; font-weight: bold; color:#333;">RECENT NEWS&nbsp;</td>
						<br>
					
					</tr>
						<br>
						<td align="center">
				<table class="col-600" width="600" border="0" align="center" cellpadding="0" cellspacing="0">
					<tbody><tr>
						<td align="center" valign="top" background={IMAGE_1} bgcolor="#66809b" style="background-size:cover; background-position:top;height=" 400""="">
							<table class="col-500" width="500" height="300" border="0" align="center" cellpadding="0" cellspacing="0">

					<tr>
						<td height="10"></td>
					</tr>


					

				</tbody></table>
						
			</td>
							<tr>
						<td align="center" style="font-family: 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', 'DejaVu Sans', Verdana, sans-serif; font-size: 20px; color: #0C0B0B; line-height: 24px; font-weight: bold; font-style: oblique;">
						
							<br> <a href={LINK_1}>{LINK_TEXT_1}</a>
						</td>
					</tr>
							<br>
							
							<td align="center">
				<table class="col-600" width="600" border="0" align="center" cellpadding="0" cellspacing="0">
					<tbody><tr>
						<td align="center" valign="top" background={IMAGE_2} bgcolor="#66809b" style="background-size:cover; background-position:top;height=" 400""="">
							<table class="col-500" width="500" height="300" border="0" align="center" cellpadding="0" cellspacing="0">

					<tr>
						<td height="10"></td>
					</tr>



				</tbody></table>
						
			</td>
							<tr>
						<td align="center" style="font-family: 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', 'DejaVu Sans', Verdana, sans-serif; font-size: 20px; color: #0C0B0B; line-height: 24px; font-weight: bold; font-style: oblique;">
						
							<br> <a href={LINK_2}>{LINK_TEXT_2}</a>
						</td>
					</tr>
					
							
		</tr>
			

		

		

<!-- END SHOWCASE -->


<!-- START TITLE -->



<!-- END TITLE -->


<!--ABOUT -->

	
<!-- END FOOTER -->
	
				</tbody></table>
  
</body>
</html>"""

class MailAlert:
    def __init__(self, mail, password) -> None:
        self.mail=mail
        self.password=password
        self.msg = MIMEMultipart('alternative')
        self.msg['Subject'] = "Stock Alert "
        self.msg['From'] = self.mail
        self.msg['To'] = self.mail


        
    def price_mail_alert(self,symbol,alert_price):
        print("fun2")
        self.connection = smtplib.SMTP("smtp.gmail.com")
        print("smtp")
        self.connection.starttls()
        print("tls")
        self.connection.login(user=self.mail,password=self.password)
        self.connection.sendmail(from_addr=self.mail,to_addrs=self.mail,msg=f"Subject:{symbol} price Alert\n\n{symbol} : {alert_price}")
        self.connection.close()


    def attach_file_to_email(self,email_message, filename, extra_headers=None):
        with open(filename, "rb") as f:
            self.file_attachment = MIMEApplication(f.read())
        self.file_attachment.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )
        if extra_headers is not None:
            for name, value in extra_headers.items():
                self.file_attachment.add_header(name, value)
        email_message.attach(self.file_attachment)


    def send_mail(self,image):
        self.connection = smtplib.SMTP("smtp.gmail.com")
        self.connection.starttls()
        self.part2=MIMEText(html_body, 'html')    
        self.msg.attach(self.part2)
        self.attach_file_to_email(self.msg, f'{image}.png', {'Content-ID': '<myimageid>'})
        self.connection.login(user=self.mail,password=self.password)
        self.connection.sendmail(from_addr=self.mail,to_addrs=self.mail,msg=self.msg.as_string())
        self.connection.close()
    

