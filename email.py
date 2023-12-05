import smtplib
from tkinter import Tk, Label, Entry, Text, Button, messagebox, ttk

############################ HERE ALL BUTTON FUNCTION ###########################
def send_email():
    sender_email = sender_email_entry.get()
    sender_password = sender_password_entry.get()
    receiver_email = receiver_email_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", "end-1c")
############################ LOGIN & LOGIC (connect & send) ######################################
    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        ############# Create the email message ##########
        email_message = f"Subject: {subject}\n\n{message}"

        ########### mail send ###################
        server.sendmail(sender_email, receiver_email, email_message)
        ################## show a dialog box popup #########
        messagebox.showinfo("Email Sent", "Email sent successfully!")
        server.quit()
        
    ################# EXCEPTION (error) ###############
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

######################## GUI HERE #####################################
root = Tk()
root.title("Email Sender😉")
root.geometry("445x400")   ## BOX SIZE ####
root.resizable(False, False)
############################## STYLISH GUI ########################################3
style = ttk.Style()
style.configure("TButton", padding=6, relief="flat", font=('Helvetica', 12))
style.configure("TEntry", padding=(5, 5, 5, 5), font=('Helvetica', 12))
style.configure("TText", font=('Helvetica', 12))

########################### ABOUT PART ###########################################################
made_by_label = ttk.Label(root, text="\t\t Made by Rajarshi🤗 \n  Send emails easily with a friendly and simple interface.😊", font=('Helvetica', 12), foreground="#f72a75")
made_by_label.grid(row=0, column=0, columnspan=2, pady=10)

############################## LABLES DEFINE (button size,font)######################################
Label(root, text="Sender Email:", font=('Helvetica', 12)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
Label(root, text="Sender Password:", font=('Helvetica', 12)).grid(row=2, column=0, padx=10, pady=5, sticky="e")
Label(root, text="Receiver Email:", font=('Helvetica', 12)).grid(row=3, column=0, padx=10, pady=5, sticky="e")
Label(root, text="Subject:", font=('Helvetica', 12)).grid(row=4, column=0, padx=10, pady=5, sticky="e")
Label(root, text="Message:", font=('Helvetica', 12)).grid(row=5, column=0, padx=10, pady=5, sticky="e")

###################################### Entry widgets (user I/P boxes) #################################
sender_email_entry = ttk.Entry(root, width=30)
sender_email_entry = ttk.Entry(root, width=25)
sender_password_entry = ttk.Entry(root, width=25, show="*")
receiver_email_entry = ttk.Entry(root, width=25)
subject_entry = ttk.Entry(root, width=25)
message_text = Text(root, width=29, height=5) 

##################### Position Entry widgets##########################
sender_email_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
sender_password_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")
receiver_email_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")
subject_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")
message_text.grid(row=5, column=1, padx=10, pady=5, sticky="w")

################################ Send Email Button ###########################
send_button = ttk.Button(root, text="Send Email", command=send_email)
send_button.grid(row=6, column=1, pady=10)

############ GUI RUN  ##########################
root.mainloop()
