# GuestMultipleMappings

A GuestMultipleMappings exception is thrown when an operation fails because the guest alias store mapping file contains multiple conflicting instances of the same certificate and username.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.guest_multiple_mappings import GuestMultipleMappings

# TODO update the JSON string below
json = "{}"
# create an instance of GuestMultipleMappings from a JSON string
guest_multiple_mappings_instance = GuestMultipleMappings.from_json(json)
# print the JSON string representation of the object
print GuestMultipleMappings.to_json()

# convert the object into a dict
guest_multiple_mappings_dict = guest_multiple_mappings_instance.to_dict()
# create an instance of GuestMultipleMappings from a dict
guest_multiple_mappings_form_dict = guest_multiple_mappings.from_dict(guest_multiple_mappings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


