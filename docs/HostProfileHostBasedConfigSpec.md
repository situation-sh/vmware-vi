# HostProfileHostBasedConfigSpec

The *HostProfileHostBasedConfigSpec* data object specifies the host from which configuration data is to be extracted and the profile(s) to be created or updated.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**use_host_profile_engine** | **bool** | Flag indicating if the Profile Engine should use the profile plug-ins present on the host to create the profile.  If &lt;code&gt;true&lt;/code&gt;, the host Profile Engine uses the vSphere 5.0 (or later) profile plug-ins. The resulting profile is not compatible with legacy hosts (pre 5.0). If &lt;code&gt;false&lt;/code&gt; or not specified, the Profile Engine creates a legacy host profile.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.host_profile_host_based_config_spec import HostProfileHostBasedConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostProfileHostBasedConfigSpec from a JSON string
host_profile_host_based_config_spec_instance = HostProfileHostBasedConfigSpec.from_json(json)
# print the JSON string representation of the object
print HostProfileHostBasedConfigSpec.to_json()

# convert the object into a dict
host_profile_host_based_config_spec_dict = host_profile_host_based_config_spec_instance.to_dict()
# create an instance of HostProfileHostBasedConfigSpec from a dict
host_profile_host_based_config_spec_form_dict = host_profile_host_based_config_spec.from_dict(host_profile_host_based_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


