# NumPortsProfile

The NumPortsProfile data object represents a subprofile for the number of ports for a virtual switch  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.num_ports_profile import NumPortsProfile

# TODO update the JSON string below
json = "{}"
# create an instance of NumPortsProfile from a JSON string
num_ports_profile_instance = NumPortsProfile.from_json(json)
# print the JSON string representation of the object
print NumPortsProfile.to_json()

# convert the object into a dict
num_ports_profile_dict = num_ports_profile_instance.to_dict()
# create an instance of NumPortsProfile from a dict
num_ports_profile_form_dict = num_ports_profile.from_dict(num_ports_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


