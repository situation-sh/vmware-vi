# HostProfileManagerHostToConfigSpecMap

Data class for <code>HostSystem</code>-<code>AnswerFileCreateSpec</code> mapping.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**config_spec** | [**AnswerFileCreateSpec**](AnswerFileCreateSpec.md) |  | 

## Example

```python
from vmware_vi.models.host_profile_manager_host_to_config_spec_map import HostProfileManagerHostToConfigSpecMap

# TODO update the JSON string below
json = "{}"
# create an instance of HostProfileManagerHostToConfigSpecMap from a JSON string
host_profile_manager_host_to_config_spec_map_instance = HostProfileManagerHostToConfigSpecMap.from_json(json)
# print the JSON string representation of the object
print HostProfileManagerHostToConfigSpecMap.to_json()

# convert the object into a dict
host_profile_manager_host_to_config_spec_map_dict = host_profile_manager_host_to_config_spec_map_instance.to_dict()
# create an instance of HostProfileManagerHostToConfigSpecMap from a dict
host_profile_manager_host_to_config_spec_map_form_dict = host_profile_manager_host_to_config_spec_map.from_dict(host_profile_manager_host_to_config_spec_map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


