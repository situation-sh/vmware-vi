# VASAStorageArrayDiscoveryIpTransport

Discovery service information of the array with IP transport. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** | IP address (IPv4/v6) of the RDMA/TCP target port.  | 
**port_number** | **str** | Port number.  Defaults to port 8009 (TCP) and RoCEv2 port 4420 (UDP).  | [optional] 

## Example

```python
from vmware_vi.models.vasa_storage_array_discovery_ip_transport import VASAStorageArrayDiscoveryIpTransport

# TODO update the JSON string below
json = "{}"
# create an instance of VASAStorageArrayDiscoveryIpTransport from a JSON string
vasa_storage_array_discovery_ip_transport_instance = VASAStorageArrayDiscoveryIpTransport.from_json(json)
# print the JSON string representation of the object
print VASAStorageArrayDiscoveryIpTransport.to_json()

# convert the object into a dict
vasa_storage_array_discovery_ip_transport_dict = vasa_storage_array_discovery_ip_transport_instance.to_dict()
# create an instance of VASAStorageArrayDiscoveryIpTransport from a dict
vasa_storage_array_discovery_ip_transport_form_dict = vasa_storage_array_discovery_ip_transport.from_dict(vasa_storage_array_discovery_ip_transport_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


