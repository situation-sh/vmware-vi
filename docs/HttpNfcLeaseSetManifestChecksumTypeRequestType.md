# HttpNfcLeaseSetManifestChecksumTypeRequestType

The parameters of *HttpNfcLease.HttpNfcLeaseSetManifestChecksumType*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_urls_to_checksum_types** | [**List[KeyValue]**](KeyValue.md) | \\[in\\] Should contain key value pairs: where key is *HttpNfcLeaseDeviceUrl.key* returned in this lease info and value is desired algorithm from *HttpNfcLeaseManifestEntryChecksumType_enum*.  ***Since:*** VI API 2.5  | [optional] 

## Example

```python
from vmware_vi.models.http_nfc_lease_set_manifest_checksum_type_request_type import HttpNfcLeaseSetManifestChecksumTypeRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of HttpNfcLeaseSetManifestChecksumTypeRequestType from a JSON string
http_nfc_lease_set_manifest_checksum_type_request_type_instance = HttpNfcLeaseSetManifestChecksumTypeRequestType.from_json(json)
# print the JSON string representation of the object
print HttpNfcLeaseSetManifestChecksumTypeRequestType.to_json()

# convert the object into a dict
http_nfc_lease_set_manifest_checksum_type_request_type_dict = http_nfc_lease_set_manifest_checksum_type_request_type_instance.to_dict()
# create an instance of HttpNfcLeaseSetManifestChecksumTypeRequestType from a dict
http_nfc_lease_set_manifest_checksum_type_request_type_form_dict = http_nfc_lease_set_manifest_checksum_type_request_type.from_dict(http_nfc_lease_set_manifest_checksum_type_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


