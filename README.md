# MITRE ATT&amp;CK Website

## Content Errors on the Website
If you find errors or typos on the site related to content, please let us know by sending an email to attack@mitre.org with the subject **Website Content Error**.

#### Please let us know the following:
1. The url where you found the error.
2. A short description of the error.

#### Examples of errors:
* Typos and syntax errors
* Improperly formatted web pages
* 404 errors when links are clicked

Thanks in advance for helping us improve the ATT&CK website!

#### Docker Container

```
$ docker run --rm -p 80:80 -d -v $(pwd):/usr/share/nginx/html nginx
OR 
$ docker run --rm -p 80:80 -d -v ~/WEB_SITE_FILES_LOCATION:/usr/share/nginx/html nginx
```