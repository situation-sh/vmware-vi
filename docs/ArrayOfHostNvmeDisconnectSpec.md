# ArrayOfHostNvmeDisconnectSpec

A boxed array of *HostNvmeDisconnectSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNvmeDisconnectSpec]**](HostNvmeDisconnectSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_nvme_disconnect_spec import ArrayOfHostNvmeDisconnectSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNvmeDisconnectSpec from a JSON string
array_of_host_nvme_disconnect_spec_instance = ArrayOfHostNvmeDisconnectSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNvmeDisconnectSpec.to_json()

# convert the object into a dict
array_of_host_nvme_disconnect_spec_dict = array_of_host_nvme_disconnect_spec_instance.to_dict()
# create an instance of ArrayOfHostNvmeDisconnectSpec from a dict
array_of_host_nvme_disconnect_spec_form_dict = array_of_host_nvme_disconnect_spec.from_dict(array_of_host_nvme_disconnect_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


