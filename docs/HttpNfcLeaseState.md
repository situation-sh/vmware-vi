# HttpNfcLeaseState

A boxed *HttpNfcLeaseState_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**HttpNfcLeaseStateEnum**](HttpNfcLeaseStateEnum.md) |  | 

## Example

```python
from vmware_vi.models.http_nfc_lease_state import HttpNfcLeaseState

# TODO update the JSON string below
json = "{}"
# create an instance of HttpNfcLeaseState from a JSON string
http_nfc_lease_state_instance = HttpNfcLeaseState.from_json(json)
# print the JSON string representation of the object
print HttpNfcLeaseState.to_json()

# convert the object into a dict
http_nfc_lease_state_dict = http_nfc_lease_state_instance.to_dict()
# create an instance of HttpNfcLeaseState from a dict
http_nfc_lease_state_form_dict = http_nfc_lease_state.from_dict(http_nfc_lease_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


