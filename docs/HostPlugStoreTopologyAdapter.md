# HostPlugStoreTopologyAdapter

This data object type is an association class that describes a host bus adapter and its associated storage Paths.  The set of Paths on all the host bus adapters is the complete set of Paths in the system.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The identifier for the host bus adapter.  ***Since:*** vSphere API 4.0  | 
**adapter** | [**HostHostBusAdapter**](HostHostBusAdapter.md) |  | 
**path** | [**List[HostPlugStoreTopologyPath]**](HostPlugStoreTopologyPath.md) | The list of paths to which the host bus adapter is associated.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.host_plug_store_topology_adapter import HostPlugStoreTopologyAdapter

# TODO update the JSON string below
json = "{}"
# create an instance of HostPlugStoreTopologyAdapter from a JSON string
host_plug_store_topology_adapter_instance = HostPlugStoreTopologyAdapter.from_json(json)
# print the JSON string representation of the object
print HostPlugStoreTopologyAdapter.to_json()

# convert the object into a dict
host_plug_store_topology_adapter_dict = host_plug_store_topology_adapter_instance.to_dict()
# create an instance of HostPlugStoreTopologyAdapter from a dict
host_plug_store_topology_adapter_form_dict = host_plug_store_topology_adapter.from_dict(host_plug_store_topology_adapter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


