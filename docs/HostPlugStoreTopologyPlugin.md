# HostPlugStoreTopologyPlugin

This data object type represents a Plugin in the plug store architecture.  A Plugin claims a set of paths and groups them into Devices.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The identifier of the plugin.  ***Since:*** vSphere API 4.0  | 
**name** | **str** | The name of the plugin.  ***Since:*** vSphere API 4.0  | 
**device** | [**List[HostPlugStoreTopologyDevice]**](HostPlugStoreTopologyDevice.md) | The set of devices formed by this plugin.  ***Since:*** vSphere API 4.0  | [optional] 
**claimed_path** | [**List[HostPlugStoreTopologyPath]**](HostPlugStoreTopologyPath.md) | The set of paths claimed by this plugin.  Not every claimed path will necessarily appear as part of a Device. Claimed paths will only appear under Devices if the device identifier of the path matches up with the device identifier exposed by the Device.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.host_plug_store_topology_plugin import HostPlugStoreTopologyPlugin

# TODO update the JSON string below
json = "{}"
# create an instance of HostPlugStoreTopologyPlugin from a JSON string
host_plug_store_topology_plugin_instance = HostPlugStoreTopologyPlugin.from_json(json)
# print the JSON string representation of the object
print HostPlugStoreTopologyPlugin.to_json()

# convert the object into a dict
host_plug_store_topology_plugin_dict = host_plug_store_topology_plugin_instance.to_dict()
# create an instance of HostPlugStoreTopologyPlugin from a dict
host_plug_store_topology_plugin_form_dict = host_plug_store_topology_plugin.from_dict(host_plug_store_topology_plugin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


