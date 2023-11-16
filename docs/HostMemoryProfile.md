# HostMemoryProfile

The *HostMemoryProfile* data object represents memory configuration for the host.  This may not be valid all versions of the host.  Use the *ApplyProfile.policy* list for access to configuration data for the host memory profile. Use the *ApplyProfile.property* list for access to subprofile configuration data, if any.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_memory_profile import HostMemoryProfile

# TODO update the JSON string below
json = "{}"
# create an instance of HostMemoryProfile from a JSON string
host_memory_profile_instance = HostMemoryProfile.from_json(json)
# print the JSON string representation of the object
print HostMemoryProfile.to_json()

# convert the object into a dict
host_memory_profile_dict = host_memory_profile_instance.to_dict()
# create an instance of HostMemoryProfile from a dict
host_memory_profile_form_dict = host_memory_profile.from_dict(host_memory_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


