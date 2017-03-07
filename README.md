![](https://cdn-images-1.medium.com/max/800/1*WZl4TRawuh-yZtji-SB7Fg.png)

***

# spring_exercise
consists django experimental codes for blog app

### Project TO-DO list 2017
- [x] Post
- [x] Post list
- [x] Account
- [x] Crispy_forms
- [x] markdown_deux
- [x] pagedown
- [x] comments
- [x] breadcrumb
- [x] footer
- [x] flatpages
- [x] heroku host
- [ ] taggit
- [ ] media files render and postgres
- [ ] feeds and recent notification
- [ ] user privilages and rules


# Cheatsheet Django
==================
1.django.apps

 class AppConfig:
	
		Configurable attributes:
			AppConfig.name
			AppConfig.label
			AppConfig.verbose_name
			AppConfig.path

		Read-only attributes:
			AppConfig.module
			AppConfig.models_module

		Methods:
			AppConfig.get_models()
			AppConfig.get_model(model_name)
			AppConfig.ready()

		Application registry:
			apps.ready
			apps.get_app_configs()
			apps.get_app_config(app_label)
			apps.is_installed(app_name)
			apps.get_model(app_label, model_name)

2.django.conf
	


3.django.contrib.auth

 class models.User

	fields:
		username
		first_name
		last_name
		email
		password
		groups
		user_permissions¶
		is_staff
		is_active
		is_superuser
		last_login
		date_joined

	Attributes:
		is_authenticated
		is_anonymous

	Methods:
		get_username()
		get_full_name()
		get_short_name()
		set_password(raw_password)
		check_password(raw_password)
		set_unusable_password()
		has_usable_password()
		get_group_permissions(obj=None)
		get_all_permissions(obj=None)
		has_perm(perm, obj=None)
		has_perms(perm_list, obj=None)
		has_module_perms(package_name)
		email_user(subject, message, from_email=None, **kwargs)

Manager Methods:
 
 class models.UserManager

	create_user(username, email=None, password=None, **extra_fields)
	create_superuser(username, email, password, **extra_fields)

AnonymousUser object:
	class models.AnonymousUser

Permission model:

	class models.Permission

		Fields:
			name 
			content_type 
			codename

		Validators:
			class validators.ASCIIUsernameValidator¶
			class validators.UnicodeUsernameValidator¶

		Login and logout signals:
			user_logged_in()
				sender
				request
				user
			user_logged_out()
				sender
				request
				user
			user_login_failed()
				sender
				credentials


