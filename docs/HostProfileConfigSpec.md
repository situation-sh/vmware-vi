# HostProfileConfigSpec

*HostProfileConfigSpec* is the base data object for all *HostProfile* configuration specifications.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_profile_config_spec import HostProfileConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostProfileConfigSpec from a JSON string
host_profile_config_spec_instance = HostProfileConfigSpec.from_json(json)
# print the JSON string representation of the object
print HostProfileConfigSpec.to_json()

# convert the object into a dict
host_profile_config_spec_dict = host_profile_config_spec_instance.to_dict()
# create an instance of HostProfileConfigSpec from a dict
host_profile_config_spec_form_dict = host_profile_config_spec.from_dict(host_profile_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


