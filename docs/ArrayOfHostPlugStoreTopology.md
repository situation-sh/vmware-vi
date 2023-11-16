# ArrayOfHostPlugStoreTopology

A boxed array of *HostPlugStoreTopology*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostPlugStoreTopology]**](HostPlugStoreTopology.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_plug_store_topology import ArrayOfHostPlugStoreTopology

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostPlugStoreTopology from a JSON string
array_of_host_plug_store_topology_instance = ArrayOfHostPlugStoreTopology.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostPlugStoreTopology.to_json()

# convert the object into a dict
array_of_host_plug_store_topology_dict = array_of_host_plug_store_topology_instance.to_dict()
# create an instance of ArrayOfHostPlugStoreTopology from a dict
array_of_host_plug_store_topology_form_dict = array_of_host_plug_store_topology.from_dict(array_of_host_plug_store_topology_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


