# PhysicalNicProfile

The *PhysicalNicProfile* data object represents physical NIC configuration.  Use the *ApplyProfile.policy* list for access to configuration data for the physical NIC profile. Use the *ApplyProfile.property* list for access to subprofile configuration data, if any.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Linkable identifier.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.physical_nic_profile import PhysicalNicProfile

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalNicProfile from a JSON string
physical_nic_profile_instance = PhysicalNicProfile.from_json(json)
# print the JSON string representation of the object
print PhysicalNicProfile.to_json()

# convert the object into a dict
physical_nic_profile_dict = physical_nic_profile_instance.to_dict()
# create an instance of PhysicalNicProfile from a dict
physical_nic_profile_form_dict = physical_nic_profile.from_dict(physical_nic_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


