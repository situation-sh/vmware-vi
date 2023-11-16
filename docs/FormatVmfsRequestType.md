# FormatVmfsRequestType

The parameters of *HostStorageSystem.FormatVmfs*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_spec** | [**HostVmfsSpec**](HostVmfsSpec.md) |  | 

## Example

```python
from vmware_vi.models.format_vmfs_request_type import FormatVmfsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of FormatVmfsRequestType from a JSON string
format_vmfs_request_type_instance = FormatVmfsRequestType.from_json(json)
# print the JSON string representation of the object
print FormatVmfsRequestType.to_json()

# convert the object into a dict
format_vmfs_request_type_dict = format_vmfs_request_type_instance.to_dict()
# create an instance of FormatVmfsRequestType from a dict
format_vmfs_request_type_form_dict = format_vmfs_request_type.from_dict(format_vmfs_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


