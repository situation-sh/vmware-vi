# DeleteNvdimmNamespaceRequestType

The parameters of *HostNvdimmSystem.DeleteNvdimmNamespace_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_spec** | [**NvdimmNamespaceDeleteSpec**](NvdimmNamespaceDeleteSpec.md) |  | 

## Example

```python
from vmware_vi.models.delete_nvdimm_namespace_request_type import DeleteNvdimmNamespaceRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteNvdimmNamespaceRequestType from a JSON string
delete_nvdimm_namespace_request_type_instance = DeleteNvdimmNamespaceRequestType.from_json(json)
# print the JSON string representation of the object
print DeleteNvdimmNamespaceRequestType.to_json()

# convert the object into a dict
delete_nvdimm_namespace_request_type_dict = delete_nvdimm_namespace_request_type_instance.to_dict()
# create an instance of DeleteNvdimmNamespaceRequestType from a dict
delete_nvdimm_namespace_request_type_form_dict = delete_nvdimm_namespace_request_type.from_dict(delete_nvdimm_namespace_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


