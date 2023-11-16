# HostPlugStoreTopologyPath

This data object type is an association class that describes a Path and its associated Device.  A Path may be claimed by at most one Device.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The identifier for the Path.  ***Since:*** vSphere API 4.0  | 
**name** | **str** | Name of path.  Use this property to correlate this path object to other path objects.  The state of the Path can be retrieved from the data object (@link vim.host.MultipathStateInfo.Path} on the *HostMultipathStateInfo* data object.  Use this name to configure LogicalUnit multipathing policy using *HostStorageSystem.EnableMultipathPath* and *HostStorageSystem.DisableMultipathPath*.  ***Since:*** vSphere API 4.0  | 
**channel_number** | **int** | The channel number for a path if applicable.  ***Since:*** vSphere API 4.0  | [optional] 
**target_number** | **int** | The target number for a path if applicable.  The target number is not guaranteed to be consistent across reboots or rescans of the adapter.  ***Since:*** vSphere API 4.0  | [optional] 
**lun_number** | **int** | The LUN number for a path if applicable.  ***Since:*** vSphere API 4.0  | [optional] 
**adapter** | [**HostPlugStoreTopologyAdapter**](HostPlugStoreTopologyAdapter.md) |  | [optional] 
**target** | [**HostPlugStoreTopologyTarget**](HostPlugStoreTopologyTarget.md) |  | [optional] 
**device** | [**HostPlugStoreTopologyDevice**](HostPlugStoreTopologyDevice.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_plug_store_topology_path import HostPlugStoreTopologyPath

# TODO update the JSON string below
json = "{}"
# create an instance of HostPlugStoreTopologyPath from a JSON string
host_plug_store_topology_path_instance = HostPlugStoreTopologyPath.from_json(json)
# print the JSON string representation of the object
print HostPlugStoreTopologyPath.to_json()

# convert the object into a dict
host_plug_store_topology_path_dict = host_plug_store_topology_path_instance.to_dict()
# create an instance of HostPlugStoreTopologyPath from a dict
host_plug_store_topology_path_form_dict = host_plug_store_topology_path.from_dict(host_plug_store_topology_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


