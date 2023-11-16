# FormatVffsRequestType

The parameters of *HostStorageSystem.FormatVffs*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_spec** | [**HostVffsSpec**](HostVffsSpec.md) |  | 

## Example

```python
from vmware_vi.models.format_vffs_request_type import FormatVffsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of FormatVffsRequestType from a JSON string
format_vffs_request_type_instance = FormatVffsRequestType.from_json(json)
# print the JSON string representation of the object
print FormatVffsRequestType.to_json()

# convert the object into a dict
format_vffs_request_type_dict = format_vffs_request_type_instance.to_dict()
# create an instance of FormatVffsRequestType from a dict
format_vffs_request_type_form_dict = format_vffs_request_type.from_dict(format_vffs_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


