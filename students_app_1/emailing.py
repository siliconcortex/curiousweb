import yagmail
import curiousweb

def send_email(student, temp_password):

    """yagmail is a library to manage google smtp in a more simpler manner,
    for more information, visit https://github.com/kootenpv/yagmail"""

    yag = yagmail.SMTP('cortexsilicon','jnzbhrbqcsavnlhu') #input the email username and app password

    domain = curiousweb.settings.DOMAIN
    conditional_statement = f"""<tr><td>Conditional Subject </td><td>{student.conditional_subject}</td></tr>"""
    #convert to blank for ee and tutorial
    review_status = f"""<tr><td>Review Status </td><td>{student.review_status}</td></tr>"""
    #convert to blank for tutorial

    contents = f"""
    <html>
    <body>
        <h1>Enrollment: CERTC Online Review</h1>
        <table>
          <ul>
            <tr><td>Name </td> <td>{student.last_name}, {student.first_name}, {student.middle_name}</td></tr>


            <tr><td>Course </td><td>ECE</td></tr>


            <tr><td>Username </td><td>{student.user.username}</td></tr>
            <tr><td>Password </td><td>{temp_password}</td></tr>
            <tr><td>School </td><td>{student.school}</td></tr>


            <tr><td>Date Graduated </td><td>{student.date_graduated}</td></tr>
            <tr><td>Honors </td><td>{student.honors}</td></tr>
            <tr><td>Officer Position </td><td>{student.officer_position}</td></tr>
            <tr><td>Scholarships </td><td>{student.scholarships}</td></tr>


            {review_status}
            {conditional_statement}
            <tr><td>Mobile Number </td><td>{student.mobile_number}</td></tr>
            <tr><td>Facebook Username </td><td>{student.facebook_username}</td></tr>
            <tr><td>ID picture</td><td><img src=" {domain}{student.id_picture.url}" alt="id picture" title="ID" style="display:block" width="200"/> </td></tr>
            <tr><td>Payment picture </td><td><img src=" {domain}{student.payment_picture.url}" alt="payment picture" title="Payment Proof" style="display:block" width="200"/> </td></tr>
          </ul>
        </table>
      </body>
    </html>"""

    #edit the course accordingly
    #remove the middle portion for tutorial

    yag.send(to = ['jmquiseo@gmail.com'], subject = 'CERTC CuriousWeb New Enrollment', contents = contents) #send the email
    yag.send(to = ['lesliecaminade@gmail.com', 'lesliecaminade@protonmail.com'], subject = 'CERTC CuriousWeb New Enrollment', contents = contents) #send the email
