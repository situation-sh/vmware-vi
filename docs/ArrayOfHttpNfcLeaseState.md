# ArrayOfHttpNfcLeaseState

A boxed array of *HttpNfcLeaseState_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HttpNfcLeaseStateEnum]**](HttpNfcLeaseStateEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_http_nfc_lease_state import ArrayOfHttpNfcLeaseState

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHttpNfcLeaseState from a JSON string
array_of_http_nfc_lease_state_instance = ArrayOfHttpNfcLeaseState.from_json(json)
# print the JSON string representation of the object
print ArrayOfHttpNfcLeaseState.to_json()

# convert the object into a dict
array_of_http_nfc_lease_state_dict = array_of_http_nfc_lease_state_instance.to_dict()
# create an instance of ArrayOfHttpNfcLeaseState from a dict
array_of_http_nfc_lease_state_form_dict = array_of_http_nfc_lease_state.from_dict(array_of_http_nfc_lease_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


