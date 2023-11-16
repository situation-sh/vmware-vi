# UnsupportedGuest

The specified guest operating system is not supported on the host that is the target of the operation. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unsupported_guest_os** | **str** | The guest OS ID for the unsupported guest.  | 

## Example

```python
from vmware_vi.models.unsupported_guest import UnsupportedGuest

# TODO update the JSON string below
json = "{}"
# create an instance of UnsupportedGuest from a JSON string
unsupported_guest_instance = UnsupportedGuest.from_json(json)
# print the JSON string representation of the object
print UnsupportedGuest.to_json()

# convert the object into a dict
unsupported_guest_dict = unsupported_guest_instance.to_dict()
# create an instance of UnsupportedGuest from a dict
unsupported_guest_form_dict = unsupported_guest.from_dict(unsupported_guest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


