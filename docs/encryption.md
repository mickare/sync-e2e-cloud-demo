
n: Number files in scope s
u: Number users in scope s
x: Number of shares per file

# Each scope:
- implicit 1 Scope-Key [SK]
	- (Sym) (e.g. valid forever, used for 1 year)
- u * UK.encrypt(SK)			(stored in DB-Table `scope-keys`)

# Each file:
- implicit 1 FileKey [FK]
	- (Sym) (valid forever)
- 1 * SK.sym_enc(FK)			(stored in DB-Table `files`)
- x * XK.sym_enc(FK)			(stored in DB-Table `file-shares`)
	- XK transmitted via shared link (url?token#key)

# Each user:
- implicit 1 * User-Key-Encryption [UK]
	- (Asym + Certificate)
- Password Encrypted UK 		(stored in DB-Table `users`)

# User-Key Change:
- Update encrypted scope keys with the user's new key.
