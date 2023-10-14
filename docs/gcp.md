# note on gcp


Installing the gcloud sdk.  For some reason, I had problems with the install method on gcp page.  I recommend creating this entry
after attempting to do what is in the doc.  I blame github codespaces using azure and ubuntu.  I normally use debian, so you got me.


Create this as root
```
$ cd /etc/apt
/etc/apt $ cat sources.list.d/google-cloud-sdk.list 
deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main
```

Afterwords, you can do:

```
$ sudo apt-get update
$ sudo apt-get install google-cloud-cli
$ gcloud init
```



## CLI tips

Use this command to get info about current gcloud CLI account project name and email.

```
$ gcloud config list
```

## project notes

* project names need dashes and not underscores.

# URLS

* [cloud sdk install](https://cloud.google.com/sdk/docs/install)