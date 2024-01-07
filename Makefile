.PHONY: default push

default: push
ifndef $(m)
	@echo "please enter commit"
	exit 1
else
	commit = m
endif


clear:
	rm account/migrations/*.py
	touch account/migrations/__init__.py
	rm home/migrations/*.py
	touch home/migrations/__init__.py
	rm product/migrations/*.py
	touch product/migrations/__init__.py
	rm payment/migrations/*.py
	touch payment/migrations/__init__.py
	rm db.sqlite3

migrate:
	./manage.py makemigrations
	./manage.py migrate
	./manage.py createsuperuser --username admin --password 2004 --noinput --email 'ahikmatullayev024@gmail.com'

push:
	git add .
	git commit -m $(commit)
	git push
