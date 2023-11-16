# ArrayOfHttpNfcLeaseInfo

A boxed array of *HttpNfcLeaseInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HttpNfcLeaseInfo]**](HttpNfcLeaseInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_http_nfc_lease_info import ArrayOfHttpNfcLeaseInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHttpNfcLeaseInfo from a JSON string
array_of_http_nfc_lease_info_instance = ArrayOfHttpNfcLeaseInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHttpNfcLeaseInfo.to_json()

# convert the object into a dict
array_of_http_nfc_lease_info_dict = array_of_http_nfc_lease_info_instance.to_dict()
# create an instance of ArrayOfHttpNfcLeaseInfo from a dict
array_of_http_nfc_lease_info_form_dict = array_of_http_nfc_lease_info.from_dict(array_of_http_nfc_lease_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


