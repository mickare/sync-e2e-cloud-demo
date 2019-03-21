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


### File Space

### History Table

The history is a flat record of changes to a file space. All basic file operations are
recorded and signed be the corresponding user. A record is final and it is not allowed to
change existing records.

###### Record Contents:
- Unique Timestamp (of the Server)
- Server UUID
- User
- File-Action
    - PUT, DELETE, MOVE
- Cipher-File-UUID
- Cipher-File-Size
- Cipher-File-Hash
- Cipher-Path-UUID
- Cipher-Path (Encrypted with Salt with FileSpace-Key)
- User-Signature for this record (Sign(record-values))

### File-Meta Table

###### Record Contents:
- Cipher-File-UUID
- Cipher-Algorithm
- Encrypted Keys
  - User + AsymEnc(SymKey)
- Tags (Indexed for search)