# HostPlugStoreTopologyTarget

This data object represents target information.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The identifier of the target.  This will be a string representing the transport information of the target.  ***Since:*** vSphere API 4.0  | 
**transport** | [**HostTargetTransport**](HostTargetTransport.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_plug_store_topology_target import HostPlugStoreTopologyTarget

# TODO update the JSON string below
json = "{}"
# create an instance of HostPlugStoreTopologyTarget from a JSON string
host_plug_store_topology_target_instance = HostPlugStoreTopologyTarget.from_json(json)
# print the JSON string representation of the object
print HostPlugStoreTopologyTarget.to_json()

# convert the object into a dict
host_plug_store_topology_target_dict = host_plug_store_topology_target_instance.to_dict()
# create an instance of HostPlugStoreTopologyTarget from a dict
host_plug_store_topology_target_form_dict = host_plug_store_topology_target.from_dict(host_plug_store_topology_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


