
# Portal
## Master -> Portal
DELETE	/portal/api/v1/scope/<SID>/file/<CFID> ? MANAGER TOKEN
PUT		/portal/api/v1/scope/<SID>/upload/<token> ? MANAGER TOKEN + Upload slot + Hash

## Client -> Portal
GET 	/portal/api/v1/scope/<SID>/file/<CFID> ? CLIENT TOKEN
PUT 	/portal/api/v1/scope/<SID>/file/<CFID> ? CLIENT TOKEN + Signed History Record + Keys


# Server
## Portal -> Master
PUT 	/master/api/v1/scope/<SID>/upload/<token>/status ? GATEWAY TOKEN
PUT		/master/api/v1/scope/<SID>/upload/<token> 

## Client -> Master
GET 	/master/api/v1/scope
GET 	/master/api/v1/scope/<SID>
PUT 	/master/api/v1/scope/<SID>
DELETE 	/master/api/v1/scope/<SID>
GET 	/master/api/v1/scope/<SID>/index
GET 	/master/api/v1/scope/<SID>/index 			?since=<timestamp>&limit=<int:1000>
GET 	/master/api/v1/scope/<SID>/history 			?since=<timestamp>&limit=<int:1000>
GET 	/master/api/v1/scope/<SID>/Upload 			+ Size + Hash
GET 	/master/api/v1/scope/<SID>/upload/<CFID> 	+ Size + Hash
-> Upload Slot
	- Upload Token
	- Server UUID
	- Server Timestamp
	- Timeout
	- Storage Provider Upload URL
	- Cipher-File-UUID <CFID>



GET 	/master/api/v1/keys/<USER>

