# HttpNfcLeaseAbortRequestType

The parameters of *HttpNfcLease.HttpNfcLeaseAbort*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fault** | [**MethodFault**](MethodFault.md) |  | [optional] 

## Example

```python
from vmware_vi.models.http_nfc_lease_abort_request_type import HttpNfcLeaseAbortRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of HttpNfcLeaseAbortRequestType from a JSON string
http_nfc_lease_abort_request_type_instance = HttpNfcLeaseAbortRequestType.from_json(json)
# print the JSON string representation of the object
print HttpNfcLeaseAbortRequestType.to_json()

# convert the object into a dict
http_nfc_lease_abort_request_type_dict = http_nfc_lease_abort_request_type_instance.to_dict()
# create an instance of HttpNfcLeaseAbortRequestType from a dict
http_nfc_lease_abort_request_type_form_dict = http_nfc_lease_abort_request_type.from_dict(http_nfc_lease_abort_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


