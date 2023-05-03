from win10toast import ToastNotifier

tn = ToastNotifier()  # The ToastNotifier class from the win10toast package is instantiated

tn.show_toast(  # To show the notification
    "Python Mini Project",  # The Title of the notification
    "Here is the notification body",  # the Text within the notification
    duration=10,  # The time for which the notification would pop up
    icon_path="logo.ico"  # It specifies the path to icon to be used for the notification
)
