# VASAStorageArrayDiscoveryFcTransport

Discovery service information of the array with FC transport. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_wwn** | **str** | Node-WWN (World Wide Name) represented in hexadecimal format.  | 
**port_wwn** | **str** | Port-WWN (World Wide Name) represented in hexadecimal format.  | 

## Example

```python
from vmware_vi.models.vasa_storage_array_discovery_fc_transport import VASAStorageArrayDiscoveryFcTransport

# TODO update the JSON string below
json = "{}"
# create an instance of VASAStorageArrayDiscoveryFcTransport from a JSON string
vasa_storage_array_discovery_fc_transport_instance = VASAStorageArrayDiscoveryFcTransport.from_json(json)
# print the JSON string representation of the object
print VASAStorageArrayDiscoveryFcTransport.to_json()

# convert the object into a dict
vasa_storage_array_discovery_fc_transport_dict = vasa_storage_array_discovery_fc_transport_instance.to_dict()
# create an instance of VASAStorageArrayDiscoveryFcTransport from a dict
vasa_storage_array_discovery_fc_transport_form_dict = vasa_storage_array_discovery_fc_transport.from_dict(vasa_storage_array_discovery_fc_transport_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


