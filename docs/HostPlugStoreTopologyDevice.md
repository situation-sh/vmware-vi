# HostPlugStoreTopologyDevice

This data object type is an association class that describes a ScsiLun and its associated Path objects.  The ScsiLun is a Device that is formed from a set of Paths.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Linkable identifier.  ***Since:*** vSphere API 4.0  | 
**lun** | [**ScsiLun**](ScsiLun.md) |  | 
**path** | [**List[HostPlugStoreTopologyPath]**](HostPlugStoreTopologyPath.md) | The array of paths available to access this LogicalUnit.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.host_plug_store_topology_device import HostPlugStoreTopologyDevice

# TODO update the JSON string below
json = "{}"
# create an instance of HostPlugStoreTopologyDevice from a JSON string
host_plug_store_topology_device_instance = HostPlugStoreTopologyDevice.from_json(json)
# print the JSON string representation of the object
print HostPlugStoreTopologyDevice.to_json()

# convert the object into a dict
host_plug_store_topology_device_dict = host_plug_store_topology_device_instance.to_dict()
# create an instance of HostPlugStoreTopologyDevice from a dict
host_plug_store_topology_device_form_dict = host_plug_store_topology_device.from_dict(host_plug_store_topology_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


