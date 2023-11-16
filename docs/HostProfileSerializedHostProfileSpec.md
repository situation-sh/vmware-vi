# HostProfileSerializedHostProfileSpec

The *HostProfileSerializedHostProfileSpec* data object contains a string representation of a host profile.  Use this object when you create a host profile from a file.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validator_host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**validating** | **bool** | If \&quot;false\&quot;, then the host profile will be saved without being validated.  The default if not specified is \&quot;true\&quot;. This option should be used with caution, since the resulting host profile will not be checked for errors.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.host_profile_serialized_host_profile_spec import HostProfileSerializedHostProfileSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostProfileSerializedHostProfileSpec from a JSON string
host_profile_serialized_host_profile_spec_instance = HostProfileSerializedHostProfileSpec.from_json(json)
# print the JSON string representation of the object
print HostProfileSerializedHostProfileSpec.to_json()

# convert the object into a dict
host_profile_serialized_host_profile_spec_dict = host_profile_serialized_host_profile_spec_instance.to_dict()
# create an instance of HostProfileSerializedHostProfileSpec from a dict
host_profile_serialized_host_profile_spec_form_dict = host_profile_serialized_host_profile_spec.from_dict(host_profile_serialized_host_profile_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


