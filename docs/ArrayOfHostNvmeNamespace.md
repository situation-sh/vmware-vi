# ArrayOfHostNvmeNamespace

A boxed array of *HostNvmeNamespace*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNvmeNamespace]**](HostNvmeNamespace.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_nvme_namespace import ArrayOfHostNvmeNamespace

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNvmeNamespace from a JSON string
array_of_host_nvme_namespace_instance = ArrayOfHostNvmeNamespace.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNvmeNamespace.to_json()

# convert the object into a dict
array_of_host_nvme_namespace_dict = array_of_host_nvme_namespace_instance.to_dict()
# create an instance of ArrayOfHostNvmeNamespace from a dict
array_of_host_nvme_namespace_form_dict = array_of_host_nvme_namespace.from_dict(array_of_host_nvme_namespace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


