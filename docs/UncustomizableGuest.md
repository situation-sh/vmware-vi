# UncustomizableGuest

The specified guest operating system is not supported by the guest customization process. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uncustomizable_guest_os** | **str** | The guest OS ID for the uncustomizable guest.  | 

## Example

```python
from vmware_vi.models.uncustomizable_guest import UncustomizableGuest

# TODO update the JSON string below
json = "{}"
# create an instance of UncustomizableGuest from a JSON string
uncustomizable_guest_instance = UncustomizableGuest.from_json(json)
# print the JSON string representation of the object
print UncustomizableGuest.to_json()

# convert the object into a dict
uncustomizable_guest_dict = uncustomizable_guest_instance.to_dict()
# create an instance of UncustomizableGuest from a dict
uncustomizable_guest_form_dict = uncustomizable_guest.from_dict(uncustomizable_guest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


