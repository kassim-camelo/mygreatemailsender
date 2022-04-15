import smtplib as s
import ssl as ss
#Formatação:
import email.message as em

mnsg = em.Message()

mnsg['From'] = input('Insira seu e-mail:\n')
password = input('Insira sua senha:\n')
mnsg['To'] = input('Insira o destinatário:\n')
mnsg.add_header('Content-Type', 'text/html')
mnsg['Subject'] = input('Insira o Assunto: (opcional)\n')
body = input('Insira a mensagem: (É aceito formatação em HTML)\n')
mnsg.set_payload(body)


context = ss.create_default_context()
with s.SMTP('smtp.gmail.com', 587) as conexao:
    print(conexao.ehlo())
    print(conexao.starttls(context=context))
    print(conexao.login(mnsg['From'], password))
    conexao.sendmail(mnsg['From'], mnsg['To'], mnsg.as_string().encode('utf-8'))
