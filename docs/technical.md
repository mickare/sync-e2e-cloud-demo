# Technical Documentation

Just a draft

## File handling

```

Server
+-----------------+     +---------------+     +-----------------------------+
+ History         +  &  | Cipher-Paths  |  &  | Storage Provider            |
+                 +     |               |     |   - get(uuid) -> File       |
+                 +     |               |     |   - delete(uuid) -> bool    |
+                 +     |               |     |   - put(uuid, File) -> bool |
+-----------------+     +---------------+     +-----------------------------+
         ||
         || Flatten
         \/
+-----------------+
+  Cipher Index   +
+-----------------+
         ||
~~~~~~~~ || ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
         ||
Client   \/
+-----------------+
+ Plaintext Index +
+-----------------+
         ||

```

### Scopes Table
#### Record:
- Scope-UUID (index)
- Scope-Key = SK

### Scope-Keys Table (NxU)
#### Record:
- User-UUID
- User-Scope-Key = USK

### File Table
#### Record:
- Scope-UUID (index)
- Cipher-File-UUID (index)
- Cipher-File-Size
- Cipher-File-Hash
- Current Timestamp
- Scope-File-Key = SK.sym_enc(FK)
- User-Signature

### File-Tags Table (NxM)
#### Record:
- Scope-UUID (index)
- Cipher-File-UUID (index)
- Tag-Name (index)
- Tag-Value

### File-Shares Table (NxM)
#### Record
- Scope-UUID (index)
- TOKEN (index)
- Cipher-File-UUID 
- implicit Encryption Key = XK.sym_enc(FK)


### History Table

The history is a flat record of changes to a file space. All basic file operations are
recorded and signed be the corresponding user. A record is final and it is not allowed to
change existing records.

##### Record:
- Scope-UUID (index)
- Cipher-Path-UUID (index)
- Unique Timestamp (index)
- Cipher-Path (Encrypted with Salt with Scope-Key)
- Server UUID
- User
- File-Action
    - PUT, DELETE, MOVE
- Cipher-File-UUID
- User-Signature for this record (Sign(record-values))

### File-Meta Table
##### Record Contents:
- Scope-UUID (index)
- Cipher-File-UUID
- Cipher-Algorithm
- Tags (Indexed for search)