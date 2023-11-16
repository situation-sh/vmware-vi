# HttpNfcLeaseManifestEntry

Provides a manifest for downloaded (exported) files and disks.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key used to match this entry with the corresponding *HttpNfcLeaseDeviceUrl* entry in *HttpNfcLease.info*.  ***Since:*** vSphere API 4.1  | 
**sha1** | **str** | SHA-1 checksum of the data stream sent from the server.  This can be used to verify that the bytes received by the client match those sent by the HttpNfc server.  ***Since:*** vSphere API 4.1  | 
**checksum** | **str** | Checksum of the data stream sent/recieved by host.  See *HttpNfcLeaseManifestEntryChecksumType_enum* for used algoritm.  ***Since:*** vSphere API 6.7  | [optional] 
**checksum_type** | **str** | Algorithm used to produce checksum in respective property.  See *HttpNfcLeaseManifestEntryChecksumType_enum* for supported algorithms.  ***Since:*** vSphere API 6.7  | [optional] 
**size** | **int** | Size of the downloaded file.  ***Since:*** vSphere API 4.1  | 
**disk** | **bool** | True if the downloaded file is a virtual disk backing.  ***Since:*** vSphere API 4.1  | 
**capacity** | **int** | The capacity of the disk, if the file is a virtual disk backing.  ***Since:*** vSphere API 4.1  | [optional] 
**populated_size** | **int** | The populated size of the disk, if the file is a virtual disk backing.  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.http_nfc_lease_manifest_entry import HttpNfcLeaseManifestEntry

# TODO update the JSON string below
json = "{}"
# create an instance of HttpNfcLeaseManifestEntry from a JSON string
http_nfc_lease_manifest_entry_instance = HttpNfcLeaseManifestEntry.from_json(json)
# print the JSON string representation of the object
print HttpNfcLeaseManifestEntry.to_json()

# convert the object into a dict
http_nfc_lease_manifest_entry_dict = http_nfc_lease_manifest_entry_instance.to_dict()
# create an instance of HttpNfcLeaseManifestEntry from a dict
http_nfc_lease_manifest_entry_form_dict = http_nfc_lease_manifest_entry.from_dict(http_nfc_lease_manifest_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


