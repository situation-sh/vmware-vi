# HttpNfcLeaseProgressRequestType

The parameters of *HttpNfcLease.HttpNfcLeaseProgress*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**percent** | **int** | \\[in\\] Completion status represented as an integer in the 0-100 range.  | 

## Example

```python
from vmware_vi.models.http_nfc_lease_progress_request_type import HttpNfcLeaseProgressRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of HttpNfcLeaseProgressRequestType from a JSON string
http_nfc_lease_progress_request_type_instance = HttpNfcLeaseProgressRequestType.from_json(json)
# print the JSON string representation of the object
print HttpNfcLeaseProgressRequestType.to_json()

# convert the object into a dict
http_nfc_lease_progress_request_type_dict = http_nfc_lease_progress_request_type_instance.to_dict()
# create an instance of HttpNfcLeaseProgressRequestType from a dict
http_nfc_lease_progress_request_type_form_dict = http_nfc_lease_progress_request_type.from_dict(http_nfc_lease_progress_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


