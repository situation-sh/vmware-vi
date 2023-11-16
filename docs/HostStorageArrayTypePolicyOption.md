# HostStorageArrayTypePolicyOption

Description of options associated with a native multipathing storage array type plugin.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | [**ElementDescription**](ElementDescription.md) |  | 

## Example

```python
from vmware_vi.models.host_storage_array_type_policy_option import HostStorageArrayTypePolicyOption

# TODO update the JSON string below
json = "{}"
# create an instance of HostStorageArrayTypePolicyOption from a JSON string
host_storage_array_type_policy_option_instance = HostStorageArrayTypePolicyOption.from_json(json)
# print the JSON string representation of the object
print HostStorageArrayTypePolicyOption.to_json()

# convert the object into a dict
host_storage_array_type_policy_option_dict = host_storage_array_type_policy_option_instance.to_dict()
# create an instance of HostStorageArrayTypePolicyOption from a dict
host_storage_array_type_policy_option_form_dict = host_storage_array_type_policy_option.from_dict(host_storage_array_type_policy_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


