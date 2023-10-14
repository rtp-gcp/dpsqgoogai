# set the default goal.
.DEFAULT_GOAL := list_docs
#.phony: list_docs gitupdate clean



list_docs:
	ls -l



gitupdate: clean
	git add .; git commit -m "update secrets/keys dir"; git push

clean:
	echo "docs: make clean"
	#-find . -name "*.backup" -print | xargs rm
	#-rm *.md
	-rm *.backup *.BACKUP *.swp *.key *.md *.json



encrypt:
	gpg --output keys.md.gpg --encrypt --recipient davisjf@gmail.com keys.md
	gpg --output application_default_credentials.json.gpg --encrypt --recipient davisjf@gmail.com application_default_credentials.json

