# ArrayOfHostNvmeTopologyInterface

A boxed array of *HostNvmeTopologyInterface*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNvmeTopologyInterface]**](HostNvmeTopologyInterface.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_nvme_topology_interface import ArrayOfHostNvmeTopologyInterface

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNvmeTopologyInterface from a JSON string
array_of_host_nvme_topology_interface_instance = ArrayOfHostNvmeTopologyInterface.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNvmeTopologyInterface.to_json()

# convert the object into a dict
array_of_host_nvme_topology_interface_dict = array_of_host_nvme_topology_interface_instance.to_dict()
# create an instance of ArrayOfHostNvmeTopologyInterface from a dict
array_of_host_nvme_topology_interface_form_dict = array_of_host_nvme_topology_interface.from_dict(array_of_host_nvme_topology_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


