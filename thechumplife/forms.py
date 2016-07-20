from django import forms

class search_form(forms.Form):
    term = forms.CharField(label='Name of Game', required=True)



class gather_emailq(forms.Form):
    email = forms.CharField(label='', required=False, initial="Enter Email Address")


CATEGORIES = (
    (5, '5 miles'),
    (10, '10 miles'),
    (25, '25 miles'),
    (50, '50 miles'),
    (100, '100 miles'),

)

checkbox_list = (('blue', 'Breadboard, Wires, An Arduino, Soldering Iron'), )

checkbox_listb = (('1-mnth', '1-Month: $30'),

                ('3-mnth', '3-Months: $85 (6% discount)'),
                ('6-mnth', '6-Months: $165 (10% discount)'),
                ('9-mnth', '9-Months: $240 (14% discount)'),
                ('12-mnth', '12-Months: $300 (20% discount)'),
                )

# class account_form(forms.Form):
#     username = forms.CharField(label='Username', required=False)
#     password = forms.CharField(label='Password', required=False)
#     email = forms.CharField(label='Email Address', required=False)

class account_form(forms.Form):
	firstname = forms.CharField(label='First Name', required=False)
	lastname = forms.CharField(label='Last Name', required=False)
	address = forms.CharField(label='Address', required=False)
	zipcode = forms.CharField(label='Zipcode', required=False)
	City = forms.CharField(label='City', required=False)

class signin_form(forms.Form):
    username = forms.CharField(label='User Name', required=False)
    password = forms.CharField(label='Password', required=False)



class contact_us_form(forms.Form):
	firstname = forms.CharField(label='First Name', required=False)
	lastname = forms.CharField(label='Last Name', required=False)
	phone_number = forms.CharField(label='Phone Number', required=False)
	citya = forms.CharField(label='Order Number', required=False)
	city = forms.CharField(label='Email Address', required=False)
	message = forms.CharField(label='Message', required=False,widget=forms.Textarea(attrs={'cols':25, 'rows': 4}))
