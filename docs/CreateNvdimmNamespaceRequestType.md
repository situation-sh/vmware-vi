# CreateNvdimmNamespaceRequestType

The parameters of *HostNvdimmSystem.CreateNvdimmNamespace_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_spec** | [**NvdimmNamespaceCreateSpec**](NvdimmNamespaceCreateSpec.md) |  | 

## Example

```python
from vmware_vi.models.create_nvdimm_namespace_request_type import CreateNvdimmNamespaceRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNvdimmNamespaceRequestType from a JSON string
create_nvdimm_namespace_request_type_instance = CreateNvdimmNamespaceRequestType.from_json(json)
# print the JSON string representation of the object
print CreateNvdimmNamespaceRequestType.to_json()

# convert the object into a dict
create_nvdimm_namespace_request_type_dict = create_nvdimm_namespace_request_type_instance.to_dict()
# create an instance of CreateNvdimmNamespaceRequestType from a dict
create_nvdimm_namespace_request_type_form_dict = create_nvdimm_namespace_request_type.from_dict(create_nvdimm_namespace_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


