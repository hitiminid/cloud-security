import hashlib


def ID(x):
	x = x.encode('utf-8')
	return hashlib.sha1(x).hexdigest()
