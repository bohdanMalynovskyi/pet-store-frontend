from djoser import email


class EmailReset(email.UsernameResetEmail):
    template_name = 'email/email_reset.html'


class PasswordReset(email.PasswordResetEmail):
    template_name = 'email/password_reset.html'


class EmailChangedConfirmation(email.UsernameChangedConfirmationEmail):
    template_name = 'email/email_changed_confirmation.html'
