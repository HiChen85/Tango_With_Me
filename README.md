# Tango_With_Me
Coursework Project



### How to use

#### For developers

- After clone the project from maste, you should make sure your virtual environment is activated

  We assume that all developers have the same virtual environments.

- Input `python manage.py migrate` to create databases and tables.

- If you haven't generated a superuser for your app admin interface, run `python manage.py createsuperuser` then fill out the information accordingly.

- If you want to test the third party auth function, you should have a third party OAuth2 Key that is given by its own organization. After getting the Key, you can open your admin interface, find the `Sites` and change the `example.com` domain to `127.0.0.1:8000`, and then clice `Social application` on the admin interface. If there is no application, add one.

- In the social application page, `Provider` can be the third-party you have added in your `settings.py`, add the Id and Key, then this function will be activated.

- Once you want to test if it is enabled, try `127.0.0.1:8000/accounts/logout`, then `127.0.0.1:8000/accounts/login`, you can find a simple page that requires you choose one of the login way. If success, you will be redirected to the default page that has been set in your django backend.

